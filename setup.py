#!/usr/bin/env python
from setuptools import setup

with open("package_readme.md") as readme_file:
    readme = readme_file.read()

with open("requirements.txt") as requirements_file:
    requirements = requirements_file.read().splitlines()


setup(
    name="neural-ninjas",
    version="0.0.1",
    description="A CLI and library for interacting with the Neural ninjas API.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="Neural ninjas",
    author_email="support@neural-ninjas.ai",
    url="https://github.com/Neural-Ninjas/neural-ninjas-python",
    packages=["neural_ninjas"],
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    python_requires=">=3.6",
)