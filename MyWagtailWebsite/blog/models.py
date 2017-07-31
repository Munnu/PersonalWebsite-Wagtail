from __future__ import unicode_literals

from django import forms
from django.db import models

from modelcluster.tags import ClusterTaggableManager

from taggit.models import TaggedItemBase
from wagtail.wagtailcore.models import Page, Orderable

from modelcluster.fields import ParentalKey, ParentalManyToManyField
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailcore.fields import StreamField

from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel,
                                                MultiFieldPanel,
                                                PageChooserPanel,
                                                StreamFieldPanel,
                                                )
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail_embed_videos.edit_handlers import EmbedVideoChooserPanel

from wagtail.wagtailsearch import index
from wagtail.wagtailsnippets.models import register_snippet

from code_markdown_blocks import CodeBlock, MarkDownBlock


@register_snippet
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ForeignKey(
        'wagtailimages.Image', null=True, blank=True,
        on_delete=models.SET_NULL, related_name='+'
    )

    panels = [
        FieldPanel('name'),
        ImageChooserPanel('icon'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'blog categories'


class BlogIndexPage(Page):
    intro = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('intro', classname="full")
    ]

    def get_context(self, request):
        # Filter by tag
        tag = request.GET.get('tag')
        blogpages = BlogPage.objects.filter(tags__name=tag)

        # Update context to include only published posts, ordered by reverse-chron
        context = super(BlogIndexPage, self).get_context(request)

        # basically, I didn't want my BlogTagIndexPage type to show up on my BlogIndexPage
        # so I'm filtering my BlogIndexPage to only show BlogPage types
        blogpages = self.get_children().live().order_by('-first_published_at').type(BlogPage)
        context['blogpages'] = blogpages
        return context


class BlogTagIndexPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        if tag is None:
            # if tags endpoint param isn't filled out, get all
            # pages on our current website
            blogpages = BlogPage.objects.in_site(request.site)
        else:
            # if tags?=<whatever_tag_here> then get our current website
            # and filter on specific tag provided
            blogpages = BlogPage.objects.in_site(request.site).filter(tags__name=tag)

        # Update template context
        context = super(BlogTagIndexPage, self).get_context(request)
        context['blogpages'] = blogpages
        return context


class LinkFields(models.Model):
    link_external = models.URLField("External link", blank=True)
    link_page = models.ForeignKey(
        'wagtailcore.Page',
        null=True,
        blank=True,
        related_name='+'
    )

    @property
    def link(self):
        if self.link_page:
            return self.link_page.url
        else:
            return self.link_external

    panels = [
        FieldPanel('link_external'),
        PageChooserPanel('link_page'),
    ]

    class Meta:
        abstract = True


class RelatedLink(LinkFields):
    title = models.CharField(max_length=255, help_text="Link title")

    panels = [
        FieldPanel('title'),
        MultiFieldPanel(LinkFields.panels, "Link"),
    ]

    class Meta:
        abstract = True


class BlogPageTag(TaggedItemBase):
    content_object = ParentalKey('BlogPage', related_name='tagged_items')


class BlogPage(Page):
    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    tags = ClusterTaggableManager(through=BlogPageTag, blank=True)
    categories = ParentalManyToManyField('blog.BlogCategory', blank=True)
    code_md_block = StreamField([
        ('code_block', CodeBlock()),
        ('md_block', MarkDownBlock()),
    ])
    # media = models.ForeignKey(
    #     'wagtailmedia.Media',
    #     null=True,
    #     blank=True,
    #     on_delete=models.SET_NULL,
    #     related_name='+'
    # )
    video = models.ForeignKey(
        'wagtail_embed_videos.EmbedVideo',
        verbose_name="Video",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('tags'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
        ], heading="Blog information"),
        FieldPanel('intro'),
        FieldPanel('body', classname="full"),
        StreamFieldPanel('code_md_block'),
        # MediaChooserPanel('media'),  # this breaks the WYSIWYG, so I'm not using it anymore
        EmbedVideoChooserPanel('video'),
    InlinePanel('gallery_images', label="Gallery images"),
    ]


class BlogPageGalleryImage(Orderable):
    page = ParentalKey(BlogPage, related_name="gallery_images")
    image = models.ForeignKey(
        'wagtailimages.Image',
        on_delete=models.CASCADE, related_name="+"
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


class BlogIndexRelatedLink(Orderable, RelatedLink):
    page = ParentalKey('BlogIndexPage', related_name='related_links')

