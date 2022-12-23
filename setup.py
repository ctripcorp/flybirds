#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
tool setup
"""
from setuptools import setup, find_packages
import sys


def parse_requirements(filename):
    """
    get requirements list from config file
    """
    line_iter = (line.strip() for line in open(filename))
    reqs = [line for line in line_iter if line and not line.startswith("#")]
    if sys.platform == "win32":
        reqs.remove("paddleocr>=2.5.0")
        reqs.remove("paddlepaddle>=2.3.0")
        reqs.remove("protobuf==3.20.1")
    return reqs


req = parse_requirements("requirements.txt")

setup(
    name="flybirds",
    version="0.5.2",
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
    python_requires=">=3.7, <3.10",
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
