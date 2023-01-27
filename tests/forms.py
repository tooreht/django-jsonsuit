# -*- coding: utf-8
from __future__ import absolute_import, unicode_literals

from django import forms

from jsonsuit.widgets import JSONSuit, ReadonlyJSONSuit


class EditableTestForm(forms.Form):
    stats = forms.CharField(widget=JSONSuit)


class ReadonlyTestForm(forms.Form):
    stats = forms.CharField(widget=ReadonlyJSONSuit)
