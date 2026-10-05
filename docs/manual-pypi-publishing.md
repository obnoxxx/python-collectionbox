# Manual PyPI publishing

GitHub Actions and PyPI trusted publishing are the preferred way to release
this project. Use this procedure only when a manual upload is necessary.

## Prepare the release

1. Update `project.version` in `pyproject.toml` to a version that has not
   already been published. PyPI does not allow replacing an existing release.
2. Run the project's tests before building the release.
3. Build the source distribution and wheel in an isolated virtual environment:

   ```bash
   python -m venv .venv
   source .venv/bin/activate
   python -m pip install --upgrade build twine
   rm -rf dist
   python -m build
   python -m twine check dist/*
   ```

## Test on TestPyPI

Create a TestPyPI API token, then upload the artifacts. Do not put the token
directly in a command that will be saved in shell history.

```bash
export TWINE_USERNAME=__token__

read -r -s -p 'API token: ' TWINE_PASSWORD
printf '\n'
export TWINE_PASSWORD
export TWINE_PASSWORD='pypi-...'



read -r -s -p 'API token: ' TWINE_PASSWORD
printf '\n'
export TWINE_PASSWORD
python -m twine upload --repository testpypi dist/*
unset TWINE_PASSWORD
```

Install the exact version from TestPyPI to verify it:

```bash
python -m pip install --index-url https://test.pypi.org/simple/ \
  --extra-index-url https://pypi.org/simple/ collectionbox==<new-version>
```

## Publish to PyPI

Create a PyPI API token scoped to the `collectionbox` project, then upload the
same checked artifacts:

```bash
export TWINE_USERNAME=__token__

read -r -s -p 'API token: ' TWINE_PASSWORD
printf '\n'
export TWINE_PASSWORD
export TWINE_PASSWORD='pypi-...'
read -r -s -p 'API token: ' TWINE_PASSWORD
printf '\n'
export TWINE_PASSWORD
python -m twine upload dist/*
unset TWINE_PASSWORD
```

If PyPI reports that the version already exists, choose a new version, rebuild
from a clean `dist/` directory, and upload the new artifacts. Do not use
`--skip-existing` to treat an incomplete upload as a successful release.
