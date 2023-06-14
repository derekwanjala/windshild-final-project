from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):

    priority = 0.
    changefreq = 'daily'

    def items(self):
        return [
            'home:home',
            'windshild',
            'portfolio',
            'contact',
        ]

    def location(self, item):
        return reverse(item)