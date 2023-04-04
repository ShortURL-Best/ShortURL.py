from setuptools import setup, find_packages

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setup(
    name = "shorturl.best",
    version = "p0.0.2",
    author = "6A-Realm",
    author_email = "6arealm@gmail.com",
    description = "A Python wrapper for the ShortURL API",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ShortURL-Best/shorturl.py",
    project_urls = {
        "Documentation": 'https://shorturlpy.readthedocs.io/en/latest/',
        "Bug Tracker": "https://github.com/ShortURL-Best/shorturl.py/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "shorturl"},
    packages = find_packages(where="shorturl"),
    python_requires = ">=3.8"
)
