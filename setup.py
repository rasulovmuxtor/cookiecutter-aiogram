#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "0.1.0"

with open("README.rst") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-aiogram",
    version=version,
    description=(
        "A Cookiecutter template for creating production-ready "
        "Aiogram projects quickly."
    ),
    long_description=long_description,
    author="Mukhtor Rasulov",
    author_email="rasulovoff@gmail.com",
    packages=[],
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Aiogram :: 2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, Python, projects, project templates, aiogram, "
        "skeleton, scaffolding, project directory, setup.py"
    ),
)
