#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

"""
test_django-jsonsuit
------------

Tests for `django-jsonsuit`.
"""

from django.test import TestCase
from django.template import Context, Template

from jsonsuit.app_settings import (
    WIDGET_MEDIA_JS, WIDGET_MEDIA_CSS,
    READONLY_WIDGET_MEDIA_JS, READONLY_WIDGET_MEDIA_CSS
)
from tests.forms import TestForm, ReadonlyTestForm

import django
import re


class TestJSONSuitWidget(TestCase):

    def setUp(self):
        self.form = TestForm(data={'stats': {'rookies': 10, 'newbies': 50, 'experts': 2}})

    def test_widget_html(self):
        self.assertTrue(self.form.is_valid())
        self.assertTrue(self.form.fields.get('stats').widget.media['js'], list(WIDGET_MEDIA_JS))
        self.assertTrue(self.form.fields.get('stats').widget.media['css'], list(WIDGET_MEDIA_CSS))
        html = self.form.as_table()
        self.assertIn('<div class="jsonsuit editable" data-jsonsuit="stats">', html)
        self.assertIn('<button type="button" class="toggle button" data-raw="Raw" data-suit="Suit">Raw</button>', html)
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
        self.assertIn('<div class="jsonsuit readonly" data-jsonsuit="stats">', html)
        self.assertNotIn('<button type="button" class="toggle button" data-raw="Raw" data-suit="Suit">Raw</button>', html)  # noqa
        self.assertNotIn('<textarea ', html)
        self.assertIn('<div class="suit">\n    <pre><code class="language-json" data-raw="', html)

    def tearDown(self):
        pass


class TestJSONSuitTemplateTag(TestCase):
    def test_jsonsuit_tag_dict(self):
        "The jsonsuit template tag retrieves a dict to render as JSON with the name 'dict_test'."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit data 'dict_test' %}"
        ).render(Context({'data': {'stats': ['rookies', 'newbies', 'experts']}}))
        self.assertEqual(out,
"""<div class="jsonsuit readonly" data-jsonsuit="dict_test">
  <div class="suit">
    <pre><code class="language-json" data-raw="{&quot;stats&quot;: [&quot;rookies&quot;, &quot;newbies&quot;, &quot;experts&quot;]}"></code></pre>
  </div>
</div>
""")  # noqa

    def test_jsonsuit_tag_string(self):
        "The jsonsuit template tag retrieves a string to render as JSON with the name 'string_test'."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit data 'string_test' %}"
        ).render(Context({'data': '{"stats": ["rookies", "newbies", "experts"]}'}))
        self.assertEqual(out,
"""<div class="jsonsuit readonly" data-jsonsuit="string_test">
  <div class="suit">
    <pre><code class="language-json" data-raw="{&quot;stats&quot;: [&quot;rookies&quot;, &quot;newbies&quot;, &quot;experts&quot;]}"></code></pre>
  </div>
</div>
""")  # noqa

    def test_jsonsuit_tag_empty_string(self):
        "The jsonsuit template tag retrieves an empty string to render as JSON with the name 'empty_string_test'."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit data 'empty_string_test' %}"
        ).render(Context({'data': '""'}))
        self.assertEqual(out,
"""<div class="jsonsuit readonly" data-jsonsuit="empty_string_test">
  <div class="suit">
    <pre><code class="language-json" data-raw="&quot;&quot;"></code></pre>
  </div>
</div>
""")  # noqa

    def test_jsonsuit_tag_uuid(self):
        "The jsonsuit template tag retrieves a dict to render as JSON without a name and should therefore use a uuid."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit data %}"
        ).render(Context({'data': {'stats': ["rookies", "newbies", "experts"]}}))
        pattern = re.compile(r'data-jsonsuit="[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}')  # noqa
        self.assertTrue(pattern.search(out))

    def test_jsonsuit_tag_js(self):
        "The jsonsuit template tag js default includes."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit_js %}"
        ).render(Context())
        if django.get_version().startswith('3.2'):
            self.assertEqual(out, '<script type="text/javascript" src="/static/jsonsuit/js/prism.js"></script>\n'
                                  '<script type="text/javascript" src="/static/jsonsuit/js/readonly-jsonsuit.js"></script>')  # noqa
        else:
            self.assertEqual(out, '<script src="/static/jsonsuit/js/prism.js"></script>\n'
                                  '<script src="/static/jsonsuit/js/readonly-jsonsuit.js"></script>')

    def test_jsonsuit_tag_css(self):
        "The jsonsuit template tag css default includes."
        out = Template(
            "{% load jsonsuit %}"
            "{% jsonsuit_css %}"
        ).render(Context())
        if django.get_version().startswith('3.2'):
            self.assertEqual(out, '<link href="/static/jsonsuit/css/prism-default.css" type="text/css" media="all" rel="stylesheet" />\n'  # noqa
                                  '<link href="/static/jsonsuit/css/jsonsuit.css" type="text/css" media="all" rel="stylesheet" />')  # noqa
        else:
            self.assertEqual(out, '<link href="/static/jsonsuit/css/prism-default.css" media="all" rel="stylesheet">\n'  # noqa
                                  '<link href="/static/jsonsuit/css/jsonsuit.css" media="all" rel="stylesheet">')  # noqa
