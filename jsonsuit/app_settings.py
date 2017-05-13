from django.conf import settings
from django.core.exceptions import ImproperlyConfigured


def check_theme(name):
    if name in AVAILABLE_THEMES:
        return name
    else:
        raise ImproperlyConfigured(
            'JSONSUIT_WIDGET_THEME must be one of {}'.format(
                ', '.join(AVAILABLE_THEMES)))

AVAILABLE_THEMES = getattr(settings, 'JSONSUIT_AVAILABLE_THEMES', ['coy',
                                                                   'dark',
                                                                   'default',
                                                                   'funky',
                                                                   'okaidia',
                                                                   'solarizedlight',
                                                                   'twilight'])

WIDGET_THEME = getattr(settings, 'JSONSUIT_WIDGET_THEME', 'twilight')

WIDGET_MEDIA_JS = getattr(settings, 'JSONSUIT_WIDGET_MEDIA_JS', (
    'jsonsuit/js/prism.js', 'jsonsuit/js/jsonsuit.js')
)

WIDGET_MEDIA_CSS = getattr(settings, 'JSONSUIT_WIDGET_MEDIA_CSS', {
    'all': ('jsonsuit/css/prism-{}.css'.format(check_theme(WIDGET_THEME)), 'jsonsuit/css/jsonsuit.css')
})
