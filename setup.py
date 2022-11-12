# -*- coding: utf-8 -*-
"""
Setup script for MaYom.
https://github.com/PyThaiNLP/MaYom
"""
from setuptools import find_packages, setup

with open("README.md", "r", encoding="utf-8-sig") as f:
    readme = f.read()

with open("requirements.txt", "r", encoding="utf-8-sig") as f:
    requirements = f.read()

setup(
    name="MaYom",
    version="0.0.4dev0",
    description="Thai Natural Language Processing library",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Wannaphong Phatthiyaphaibun",
    author_email="wannaphong@yahoo.com",
    url="https://github.com/PyThaiNLP/pythainlp",
    packages=find_packages(exclude=["tests", "tests.*"]),
    test_suite="tests",
    python_requires=">=3.7",
    package_data={
        "mayom": [
            "corpus/*",
        ],
    },
    include_package_data=True,
    install_requires=requirements,
    extras_require=extras,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords=[
        "pythainlp",
        "NLP",
        "natural language processing",
        "text analytics",
        "text processing",
        "localization",
        "computational linguistics",
        "ThaiNLP",
        "Thai NLP",
        "Thai language",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: Thai",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Text Processing",
        "Topic :: Text Processing :: General",
        "Topic :: Text Processing :: Linguistic",
    ],
    project_urls={
        "Source Code": "https://github.com/PyThaiNLP/MaYom",
        "Bug Tracker": "https://github.com/PyThaiNLP/MaYom/issues",
    },
)
