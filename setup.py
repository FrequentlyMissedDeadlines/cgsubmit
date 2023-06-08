from setuptools import setup, find_namespace_packages
from os.path import abspath, dirname, join

# Fetches the content from README.md
# This will be used for the "long_description" field.
README_MD = open(join(dirname(abspath(__file__)), "README.md")).read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name="cgsubmit",
    version="1.0.6",
    packages=find_namespace_packages(include=['cgsubmit', 'cgsubmit.*'], exclude=['*.tests*']),
    description="Analyse your submit in codingame competitions.",
    long_description=README_MD,
    long_description_content_type="text/markdown",
    url="https://github.com/FrequentlyMissedDeadlines/cgsubmit",
    author="FrequentlyMissedDeadlines",
    author_email="FrequentlyMissedDeadlines+cgsubmit@gmail.com",

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: End Users/Desktop",
        "Natural Language :: English",
        "Topic :: Software Development",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    install_requires=required,
    project_urls={
        'Bug Reports': 'https://github.com/FrequentlyMissedDeadlines/cgsubmit/issues',
        'Source': 'https://github.com/FrequentlyMissedDeadlines/cgsubmit',
    }
)