# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Use poetry for packaging and dependency management
- Use nox for test automation

### Changed

- Renamed HISTORY.md to CHANGELOG.md and reworked it

## [0.5.0] - 2023-01-20

### Added

- Update jsonsuit on toggle
- Support for multiple mixed forms

### Changed

- Modernize tooling
- Support python 3.9, 3.10, 3.11
- Support django 3.2, 4.1
- Update PrismJS to version 1.29.0
- Simplify DOM ready for modern browsers

## [0.4.4] - 2018-01-31

### Changed

- Update django doc links
- Remove unused load of i18n template tag
- Update prism assets

## [0.4.3] - 2018-01-19

### Changed

- Update test requirements
- Add renderer kwarg to the widget render fn

### Fixed

- Fix toggling of JSON field instead of submitting
- Fix test for jsonsuit template tag
- Fix tox and travis config

## [0.4.2] - 2017-07-03

### Fixed

- Fix test for jsonsuit template tag
- Fix jsonsuit template tag for empty strings and add test case

## [0.4.1] - 2017-06-19

### Changed

- Simplify tests to work with multiple python versions

### Fixed

- Fix docs about template tags

## [0.4.0] - 2017-06-18

### Added

- Add jsonsuit template tags

## [0.3.0] - 2017-06-02

### Added

- Add ReadonlyJSONSuit widget

### Changed

- Make app settings more modular
- Make JS code more generic (mostly using classes in selectors)
- Use Prism's "default" theme as default

## [0.2.0] - 2017-05-14

### Added

- Set custom widget media (JS & CSS) files
- Use custom HTML template

### Changed

- Change JSON syntax highlighter themes

## [0.1.0] - 2017-05-13

### Added

- First release on PyPI.
