# django-jsonsuit

![image][1] ![image][2] ![image][3]

Django goodies to dress JSON data in a suit.

## Documentation

The full documentation is at <https://tooreht.github.io/django-jsonsuit>.

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

## Features

-   TODO

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
