# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

from django import forms

from jsonsuit.widgets import JSONSuit, ReadonlyJSONSuit


class TestForm(forms.Form):
    stats = forms.CharField(widget=JSONSuit)


class ReadonlyTestForm(forms.Form):
    stats = forms.CharField(widget=ReadonlyJSONSuit)
