from __future__ import absolute_import, unicode_literals

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.shortcuts import render

from wagtail.wagtailadmin.forms import SearchForm

from wagtail.wagtailcore.models import Page
from wagtail.wagtailsearch.models import Query
from wagtail.wagtailsearch.views import search

# from wagtail.wagtailsearch.views import wagtail_search_views

# from wagtail repo wagtail/wagtail/project_template/site_search/views.py

def site_search(request):
    # Search
    search_query = str(request.GET.get('query', None))
    if search_query:
        # print "Dir", dir( search_results = Page.objects.live().site_search())
        search_results = Page.objects.live().search("test")

        # Log the query so Wagtail can suggest promoted results
        Query.get(search_query).add_hit()
    else:
        search_results = Page.objects.none()

    # Render template
    return render(request, 'site_search/site_search.html', {
        'search_query': search_query,
        'search_results': search_results,
    })
