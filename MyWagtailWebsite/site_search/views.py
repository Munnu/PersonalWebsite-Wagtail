from __future__ import absolute_import, unicode_literals

from django.shortcuts import render

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query
from wagtail.wagtailimages.models import Image

from about.models import AboutPage
from blog.models import BlogPage
from contact.models import FormPage
from home.models import HomePage
from portfolio.models import PortfolioItemPage
from resume.models import ResumePage


def site_search(request, template=None, results_per_page=10, path=None):
    # Search
    search_query = str(request.GET.get('query', None))
    search_results = []
    if search_query:
        # Search for pages and also images, in the future maybe more options will be in place

        # find out if certain page subsets exist, and if so, search on their fields
        # this code might be a little crude if there is a better way to do this part than to
        # manually import each page type and/or make multiple conditional statements
        if Page.objects.type(BlogPage):
            search_results.extend(BlogPage.objects.live().search(search_query,
                                                                 fields=['title', 'intro', 'body'],
                                                                 order_by_relevance=True))

        if Page.objects.type(PortfolioItemPage):
            search_results.extend(PortfolioItemPage.objects.live().search(search_query,
                                                                          fields=['title', 'intro', 'body'],
                                                                          order_by_relevance=True))

        if Page.objects.type(AboutPage):
            search_results.extend(AboutPage.objects.live().search(search_query,
                                                                  fields=['title', 'body'],
                                                                  order_by_relevance=True))

        if Page.objects.type(ResumePage):
            search_results.extend(ResumePage.objects.live().search(search_query,
                                                                   fields=['title', 'body'],
                                                                   order_by_relevance=True))

        if Page.objects.type(FormPage):
            search_results.extend(Page.objects.live().type(FormPage).in_site(request.site)
                                  .search(search_query, order_by_relevance=True))

        if Page.objects.type(HomePage):
            search_results.extend(Page.objects.live().type(HomePage).in_site(request.site)
                                  .search(search_query, order_by_relevance=True))

        image_results = Image.objects.search(search_query)

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()
        image_results = Image.objects.none()

    # Render template
    return render(request, 'site_search/search.html', {
        'search_query': search_query,
        'search_results': search_results,
        'image_results': image_results,
    })
