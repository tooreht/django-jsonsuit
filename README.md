# django-jsonsuit

![image][1] ![image][2] ![image][3]

Django goodies to dress JSON data in a suit.

## Documentation

The full documentation is at <https://tooreht.github.io/django-jsonsuit>.

## Features

- Editable and readonly widget
- Change JSON syntax highlighter themes
- Set custom widget media (JS & CSS) files
- Use custom HTML templates

## Quickstart

Install django-jsonsuit:

    pip install django-jsonsuit

Add it to your `INSTALLED_APPS`:

``` sourceCode
INSTALLED_APPS = (
    ...
    'jsonsuit.apps.JSONSuitConfig',
    ...
)
```

## Usage

### Widgets

django-jsonsuit currently provides two widgets to dress your JSON data:

1. `JSONSuit`: Widget that displays JSON data with indentation and syntax highlighting as default, but allows to toggle between the standard django `Textarea` for editing.
2. `ReadonlyJSONSuit`: Widget that simply displays JSON data with indentation and syntax highlighting. It is useful for JSON fields that contain readonly data.

**Note**: Because a widget in django is only responsible for displaying fields, it has no direct access to its field properties. Thus there is no easy way to check if the field is readonly. The readonly behaviour is even handled differently among django forms, model forms and admin. This is why the `ReadonlyJSONSuit` was introduced.

#### JSONSuit

In a form or model admin, enable a JSON suit for a particular field:

```python
from jsonsuit.widgets import JSONSuit

class JSONForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = '__all__'
    widgets = {
      'myjsonfield': JSONSuit(),
    }

class JSONAdmin(admin.ModelAdmin):
  form = JSONForm
```

Enable JSON suit for every JSONField of a model:

```python
from django.contrib.postgres.fields import JSONField

class JSONAdmin(admin.ModelAdmin):
  formfield_overrides = {
    JSONField: {'widget': JSONSuit }
  }
```

#### ReadonlyJSONSuit

In a form or model admin, enable a readonly JSON suit for a particular field:

```python
from jsonsuit.widgets import ReadonlyJSONSuit

class ReadonlyJSONForm(forms.ModelForm):
  class Meta:
    model = Test
    fields = '__all__'
    widgets = {
      'myjsonfield': ReadonlyJSONSuit(),
    }

class ReadonlyJSONAdmin(admin.ModelAdmin):
  form = ReadonlyJSONForm
```

Enable readonly JSON suit for every JSONField of a model:

```python
from django.contrib.postgres.fields import JSONField

class ReadonlyJSONAdmin(admin.ModelAdmin):
  formfield_overrides = {
    JSONField: {'widget': ReadonlyJSONSuit }
  }
```

### Template Tags

Use the jsonsuit template tag to display serializable objects in templates. Note that in order to use the `jsonsuit`, `jsonsuit_css` and `jsonsuit_js` tags, they must be loaded using `{% load jsonsuit %}`. 

```html
{% extends "ui/base.html" %}
{% load jsonsuit %}

{% block title %}{% trans "JSONSuit Template Tag" %}{% endblock %}

{% block styles %}
    {{ block.super }}
    {% jsonsuit_css %} <!-- include jsonsuit css files -->
{% endblock %}

{% block content %}
<div class="row">
  <div class="col-md-4">
      <h2>Unnamed Suit</h2>
      {% jsonsuit data %} <!-- with no parameter supplied,
                               a uuid css class name is generated
                               to identify each individual suit -->
  </div>
  <div class="col-md-8">
      <h2>Named Suit</h2>
      {% jsonsuit data 'suit_name' %} <!-- for each suit,
                                           a css class name
                                           can be supplied -->
  </div>
</div>
{% endblock %}

{% block scripts %}
    {{ block.super }}
    {% jsonsuit_js %} <!-- include jsonsuit js files -->
{% endblock %}
```

### Theme

Set JSON syntax highlighter theme in settings:

```python
JSONSUIT_WIDGET_THEME = 'twilight'
```

Available themes: `coy`, `dark`, `default`, `funky`, `okaidia`, `solarizedlight`, `twilight`. Defaults to the `default` theme.

### Custom Widget Media

Set custom widget media (JS & CSS) files:

```python
JSONSUIT_WIDGET_MEDIA_JS = (
    'jsonsuit/js/mysyntaxhighlighter.js', 'jsonsuit/js/myscripts.js'
)

JSONSUIT_WIDGET_MEDIA_CSS = {
    'all': ('jsonsuit/css/mytheme.css', 'jsonsuit/css/mystyles.css')
}

JSONSUIT_READONLY_WIDGET_MEDIA_JS = (
    'jsonsuit/js/mysyntaxhighlighter.js', 'jsonsuit/js/myreadonlyscripts.js'
)

JSONSUIT_READONLY_WIDGET_MEDIA_CSS = {
    'all': ('jsonsuit/css/mytheme.css', 'jsonsuit/css/myreadonlystyles.css')
}
```

To only replace the syntax highlighter assets for all widgets, simply change:

```python
JSONSUIT_SYNTAX_HIGHLIGHTER_JS = ('jsonsuit/js/mysyntaxhighlighter.js',)
JSONSUIT_SYNTAX_HIGHLIGHTER_CSS = ('jsonsuit/css/mytheme.css',)
```

### Custom HTML template

Override `jsonsuit/widget.html` or `jsonsuit/readonly_widget.html` template:

```bash
jsonsuit/templates
└── jsonsuit
    └── widget.html
    └── readonly_widget.html
```

## Running Tests

Does the code actually work?

    source <YOURVIRTUALENV>/bin/activate
    (myenv) $ pip install tox
    (myenv) $ tox

## Credits

Project dependencies:

- [prism](http://prismjs.com/)
- [vanilla-js](http://vanilla-js.com/)

Project documentation:

- [MkDocs](http://www.mkdocs.org/)

Tools used in rendering this package:

- [Cookiecutter]
- [cookiecutter-djangopackage]

  [1]: https://badge.fury.io/py/django-jsonsuit.svg
  [2]: https://travis-ci.org/tooreht/django-jsonsuit.svg?branch=master
  [3]: https://codecov.io/gh/tooreht/django-jsonsuit/branch/master/graph/badge.svg
  [Cookiecutter]: https://github.com/audreyr/cookiecutter
  [cookiecutter-djangopackage]: https://github.com/pydanny/cookiecutter-djangopackage
