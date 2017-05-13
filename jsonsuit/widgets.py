from django.forms import widgets
from django.template.loader import render_to_string

from .app_settings import WIDGET_MEDIA_JS, WIDGET_MEDIA_CSS


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
