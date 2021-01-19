from os import path
from subprocess import run

from setuptools import setup


def git_describe():
    output = run(
        "git describe --tags --dirty --broken",
        capture_output=True,
        check=True,
        text=True,
    ).stdout
    parts = output.strip()[1:].split("-")
    return f"{parts[0]}.post{parts[1]}+{'.'.join(parts[2:])}"


def readme():
    this_directory = path.abspath(path.dirname(__file__))
    with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
        return f.read()


setup(
    name="gitsafe",
    version=git_describe(),
    description="A tool to keep copies (aka backups) of git repositories.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/tammann/gitsafe",
    author="Tobias Ammann",
    author_email="tammann@ergonomics.ch",
    license="MIT",
    py_modules=["gitsafe"],
    install_requires=["SQLObject", "tabulate"],
    extras_require={
        "dev": [
            "black",
        ]
    },
    entry_points={
        "console_scripts": ["gitsafe=gitsafe:main"],
    },
    zip_safe=False,
)