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
                                                                   'twilight',
                                                                   'tomorrow'])
WIDGET_THEME = getattr(settings, 'JSONSUIT_WIDGET_THEME', 'default')

SYNTAX_HIGHLIGHTER_JS = getattr(settings, 'JSONSUIT_SYNTAX_HIGHLIGHTER_JS', ('jsonsuit/js/prism.js',))
SYNTAX_HIGHLIGHTER_CSS = getattr(settings, 'JSONSUIT_SYNTAX_HIGHLIGHTER_CSS', (
    'jsonsuit/css/prism-{}.css'.format(check_theme(WIDGET_THEME)),)
)

WIDGET_MEDIA_JS = getattr(settings, 'JSONSUIT_WIDGET_MEDIA_JS', SYNTAX_HIGHLIGHTER_JS + (
    'jsonsuit/js/jsonsuit.js',)
)
WIDGET_MEDIA_CSS = getattr(settings, 'JSONSUIT_WIDGET_MEDIA_CSS', {
    'all': SYNTAX_HIGHLIGHTER_CSS + ('jsonsuit/css/jsonsuit.css',)
})

READONLY_WIDGET_MEDIA_JS = getattr(settings, 'JSONSUIT_READONLY_WIDGET_MEDIA_JS', SYNTAX_HIGHLIGHTER_JS + (
    'jsonsuit/js/readonly-jsonsuit.js',)
)
READONLY_WIDGET_MEDIA_CSS = getattr(settings, 'JSONSUIT_READONLY_WIDGET_MEDIA_CSS', {
    'all': SYNTAX_HIGHLIGHTER_CSS + ('jsonsuit/css/jsonsuit.css',)
})
