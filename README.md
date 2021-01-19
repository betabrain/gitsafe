# gitsafe

A tool to keep copies (aka backups) of git repositories.

## Usage
```shell
gitsafe add https://github.com/tammann/gitsafe.git
gitsafe add /local/repository
gitsafe update
gitsafe stats
```

## Development
```shell
black .
rm -rv dist/
python setup.py sdist bdist_wheel
twine upload dist/*
```
