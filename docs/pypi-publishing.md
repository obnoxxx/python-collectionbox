# Publishing to PyPI

Publishing is automated with GitHub Actions. Creating a published GitHub
release, including the releases created automatically when a `v*` tag is
pushed, builds the package from that tag and publishes it to PyPI using
trusted publishing. Tag-triggered CI publishes directly from `ci.yml` after
it creates the release, because releases created with `GITHUB_TOKEN` do not
emit a `release` event for other workflows. Releases published outside that
tag-triggered path are published by `publish-pypi.yml`.

Before the first automated publication, configure a
[PyPI trusted publisher](https://docs.pypi.org/trusted-publishers/) for each
workflow that can publish this repository:

- Owner: `obnoxxx`
- Repository: `python-collectionbox`
- Environment: `pypi`
- Workflow: `ci.yml` for tag-triggered releases
- Workflow: `publish-pypi.yml` for other published GitHub releases
