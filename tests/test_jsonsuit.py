#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-jsonsuit
------------

Tests for `django-jsonsuit` models module.
"""

from django.test import TestCase

from tests.forms import TestForm


class TestJSONSuitWidget(TestCase):

    def setUp(self):
        self.form = TestForm(data={'stats': {'rookies': 10, 'newbies': 50, 'experts': 2}})

    def test_widget_html(self):
        self.assertTrue(self.form.is_valid())
        html = self.form.as_table()
        self.assertIn('<div class="jsonsuit" data-jsonsuit="stats">', html)
        self.assertIn('<button class="toggle button" data-raw="Raw" data-suit="Neat">Raw</button>', html)
        self.assertIn('<textarea ', html)
        self.assertIn('<div class="suit">\n    <pre><code class="language-json"></code></pre>\n  </div>', html)

    def tearDown(self):
        pass
