#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-jsonsuit
------------

Tests for `django-jsonsuit` models module.
"""

from django.test import TestCase

from jsonsuit.app_settings import (
    WIDGET_MEDIA_JS, WIDGET_MEDIA_CSS,
    READONLY_WIDGET_MEDIA_JS, READONLY_WIDGET_MEDIA_CSS
)
from tests.forms import TestForm, ReadonlyTestForm


class TestJSONSuitWidget(TestCase):

    def setUp(self):
        self.form = TestForm(data={'stats': {'rookies': 10, 'newbies': 50, 'experts': 2}})

    def test_widget_html(self):
        self.assertTrue(self.form.is_valid())
        self.assertTrue(self.form.fields.get('stats').widget.media['js'], list(WIDGET_MEDIA_JS))
        self.assertTrue(self.form.fields.get('stats').widget.media['css'], list(WIDGET_MEDIA_CSS))
        html = self.form.as_table()
        self.assertIn('<div class="jsonsuit" data-jsonsuit="stats">', html)
        self.assertIn('<button class="toggle button" data-raw="Raw" data-suit="Suit">Raw</button>', html)
        self.assertIn('<textarea ', html)
        self.assertIn('<div class="suit">\n    <pre><code class="language-json" data-raw="', html)

    def tearDown(self):
        pass


class TestReadonlyJSONSuitWidget(TestCase):

    def setUp(self):
        self.form = ReadonlyTestForm(data={'stats': {'rookies': 10, 'newbies': 50, 'experts': 2}})

    def test_widget_html(self):
        self.assertTrue(self.form.is_valid())
        self.assertTrue(self.form.fields.get('stats').widget.media['js'], list(READONLY_WIDGET_MEDIA_JS))
        self.assertTrue(self.form.fields.get('stats').widget.media['css'], list(READONLY_WIDGET_MEDIA_CSS))
        html = self.form.as_table()
        self.assertIn('<div class="jsonsuit" data-jsonsuit="stats">', html)
        self.assertNotIn('<button class="toggle button" data-raw="Raw" data-suit="Suit">Raw</button>', html)
        self.assertNotIn('<textarea ', html)
        self.assertIn('<div class="suit">\n    <pre><code class="language-json" data-raw="', html)

    def tearDown(self):
        pass
