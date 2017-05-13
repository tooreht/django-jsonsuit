from django.forms import widgets
from django.template.loader import render_to_string


class JSONSuit(widgets.Textarea):
    def render(self, name, value, attrs={}):
        attrs.update({'class': 'hidden'})
        textarea = super(JSONSuit, self).render(name, value, attrs)
        return render_to_string('jsonsuit/widget.html', {
            'name': name, 'value': value, 'textarea': textarea})

    class Media:
        js = ('jsonsuit/js/prism.js', 'jsonsuit/js/jsonsuit.js', )
        # https://docs.djangoproject.com/en/1.9/topics/forms/media/#css
        css = {
            'all': ('jsonsuit/css/prism.css', 'jsonsuit/css/jsonsuit.css', )
        }
