# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django.conf.urls import url, include

from jsonsuit.urls import urlpatterns as jsonsuit_urls

urlpatterns = [
    url(r'^', include(jsonsuit_urls, namespace='jsonsuit')),
]
