from django.forms import widgets
from django.template.loader import render_to_string

from .app_settings import (
    WIDGET_MEDIA_JS, WIDGET_MEDIA_CSS,
    READONLY_WIDGET_MEDIA_JS, READONLY_WIDGET_MEDIA_CSS
)


class JSONSuit(widgets.Textarea):
    def render(self, name, value, attrs={}):
        attrs.update({'class': 'hidden'})
        textarea = super(JSONSuit, self).render(name, value, attrs)
        return render_to_string('jsonsuit/widget.html', {
            'name': name, 'value': value, 'textarea': textarea})

    class Media:
        js = WIDGET_MEDIA_JS
        # https://docs.djangoproject.com/en/1.9/topics/forms/media/#css
        css = WIDGET_MEDIA_CSS


class ReadonlyJSONSuit(widgets.Widget):
    def render(self, name, value, attrs=None):
        return render_to_string('jsonsuit/readonly_widget.html', {
            'name': name, 'value': value, 'attrs': attrs})

    class Media:
        js = READONLY_WIDGET_MEDIA_JS
        # https://docs.djangoproject.com/en/1.9/topics/forms/media/#css
        css = READONLY_WIDGET_MEDIA_CSS
