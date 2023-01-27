import json

import nox
import nox_poetry

PYTHON_VERSIONS = {
    "py-3.9": "3.9",
    "py-3.10": "3.10",
    "py-3.11": "3.11",
}

DJANGO_VERSIONS = {
    "dj-32": "django==3.2",
    "dj-41": "django==4.1",
    "dj-master": "https://api.github.com/repos/django/django/tarball/master",
}


@nox.session(python=False)
def py_versions(session):
    print(
        json.dumps(
            dict(
                keys=list(PYTHON_VERSIONS.keys()),
                values=list(PYTHON_VERSIONS.values()),
                object=PYTHON_VERSIONS,
            )
        )
    )


@nox.session(python=False)
def dj_versions(session):
    print(
        json.dumps(
            dict(
                keys=list(DJANGO_VERSIONS.keys()),
                values=list(DJANGO_VERSIONS.values()),
                object=DJANGO_VERSIONS,
            )
        )
    )


@nox.session(python=False)
def gha_matrix_exclude(session):
    print(
        json.dumps(
            [
                dict(
                    py=PYTHON_VERSIONS["py-3.9"],
                    dj="dj-master",
                )
            ]
        )
    )


@nox.session(tags=["style"])
def black(session):
    session.install("black")
    session.run("black", "--check", ".")


@nox.session(tags=["style"])
def isort(session):
    session.install("isort")
    session.run("isort", "--check", ".")


@nox.session(tags=["style"])
def flake8(session):
    session.install("flake8")
    session.run("flake8", ".")


@nox_poetry.session(tags=["test"])
@nox.parametrize(
    "python, django",
    [
        (nox.param(python, django, id=f"{py_id}-{dj_id}"))
        for py_id, python in PYTHON_VERSIONS.items()
        for dj_id, django in DJANGO_VERSIONS.items()
        if (python, django) != (PYTHON_VERSIONS["py-3.9"], DJANGO_VERSIONS["dj-master"])
    ],
)
def test(session, django):
    session.install("pytest")
    session.install("pytest-cov")
    session.install("pytest-django")
    session.poetry.installroot()
    session.run("pip", "install", django)
    session.run("pytest", "--cov=./jsonsuit", "--cov-report=xml")
