# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField
from modelcluster.tags import ClusterTaggableManager

from wagtail.wagtailcore.models import Page, Orderable
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsearch import index

from wagtail.wagtailadmin.edit_handlers import (FieldPanel,
                                                InlinePanel,
                                                MultiFieldPanel
                                                )
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet
from taggit.models import TaggedItemBase

# # Create your models here.
class PortfolioPageTag(TaggedItemBase):
    content_object = ParentalKey('PortfolioItemPage', related_name='tagged_items')

class PortfolioPage(Page):

    def get_context(self, request):

        # Filter by tag
        tag = request.GET.get('tag')
        if tag:
            portfolio_item_pages = PortfolioItemPage.objects.filter(tags__name=tag).live().order_by('-first_published_at')
        else:
            portfolio_item_pages = PortfolioItemPage.objects.live().order_by('-first_published_at')

        # Update template context
        context = super(PortfolioPage, self).get_context(request)
        context['portfolio_item_pages'] = portfolio_item_pages
        return context


class PortfolioItemPage(Page):
    date = models.DateField("Post date")
    intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    categories = ParentalManyToManyField('portfolio.PortfolioCategory', blank=True)
    tags = ClusterTaggableManager(through=PortfolioPageTag, blank=True)

    def main_image(self):
        gallery_item = self.gallery_images.first()
        if gallery_item:
            return gallery_item.image
        else:
            return None

    search_fields = Page.search_fields + [
        index.SearchField('intro'),
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            FieldPanel('date'),
            FieldPanel('categories', widget=forms.CheckboxSelectMultiple),
            FieldPanel('tags'),
        ], heading="Portfolio item full description"),
        FieldPanel('intro'),
        FieldPanel('body'),
        InlinePanel('gallery_images', label="Gallery images"),
    ]

class PortfolioItemPageGalleryImage(Orderable):
    page = ParentalKey(PortfolioItemPage, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]


@register_snippet
class PortfolioCategory(models.Model):
    name = models.CharField(max_length=255)

    panels = [
        FieldPanel('name'),
    ]

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'portfolio categories'