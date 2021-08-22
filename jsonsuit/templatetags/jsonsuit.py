# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import unicode_literals

import json
import uuid

from django.template import Library
from django.utils.safestring import mark_safe

from ..widgets import ReadonlyJSONSuit


register = Library()


@register.simple_tag
def jsonsuit_css():
    widget = ReadonlyJSONSuit()
    return widget.media['css']


@register.simple_tag
def jsonsuit_js():
    widget = ReadonlyJSONSuit()
    return widget.media['js']


@register.simple_tag
def jsonsuit(obj, name=None):
    if name is None:
        name = uuid.uuid4()
    if isinstance(obj, str) and obj:
        obj = json.loads(obj)
    widget = ReadonlyJSONSuit()
    return mark_safe(widget.render(
        name=name,
        value=json.dumps(obj, ensure_ascii=False)))
