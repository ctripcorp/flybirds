#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tool setup
"""
from setuptools import setup, find_packages


def parse_requirements(filename):
    """
    get requirements list from config file
    """
    line_iter = (line.strip() for line in open(filename))
    return [line for line in line_iter if line and not line.startswith("#")]


req = parse_requirements("requirements.txt")

setup(
    name="flybirds",
    version="0.1.4",
    author="trip_flight",
    author_email="flybirds_support@trip.com",
    description="BDD-driven natural language automated testing framework",
    long_description="BDD-driven natural language automated testing "
                     "framework, present by Trip Flight",
    keywords=[
        "automation",
        "automated-test",
        "bdd",
        "framework",
        "android",
        "ios",
        "behave",
    ],
    license="MIT license",
    packages=find_packages(exclude=["dist", "build", "tests", "docs"]),
    include_package_data=True,
    install_requires=req,
    entry_points="""
    [console_scripts]
    flybirds = flybirds.launcher:main
    """,
    url="https://github.com/ctripcorp/flybirds",
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
