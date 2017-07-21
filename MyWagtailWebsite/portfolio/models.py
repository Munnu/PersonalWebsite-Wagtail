# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from modelcluster.fields import ParentalKey, ParentalManyToManyField


from wagtail.wagtailcore.models import Page
from wagtail.wagtailcore.fields import RichTextField
from wagtail.wagtailsearch import index

from wagtail.wagtailadmin.edit_handlers import FieldPanel
from wagtail.wagtailimages.edit_handlers import ImageChooserPanel
from wagtail.wagtailsnippets.models import register_snippet

# # Create your models here.
# class PortfolioPage(Page):
#     intro = RichTextField(blank=True)
#
#     content_panels = Page.content_panels + [
#         FieldPanel('intro', classname="full")
#     ]

class PortfolioItemPage(Page):
    # date = models.DateField("Post date")
    # intro = models.CharField(max_length=250)
    body = RichTextField(blank=True)
    # categories = ParentalManyToManyField('blog.BlogCategory', blank=True)

    search_fields = Page.search_fields + [
        index.SearchField('body'),
    ]

    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]