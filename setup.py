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
    need_remove_list = []
    if "win" in sys.platform:
        for req in reqs:
            if req is not None:
                if "paddleocr>" in req and req.index("paddleocr>") == 0:
                    need_remove_list.append(req)
                if "paddleocr<" in req and req.index("paddleocr<") == 0:
                    need_remove_list.append(req)
                if "paddleocr=" in req and req.index("paddleocr=") == 0:
                    need_remove_list.append(req)
                if "paddlepaddle>" in req and req.index("paddlepaddle>") == 0:
                    need_remove_list.append(req)
                if "paddlepaddle=" in req and req.index("paddlepaddle=") == 0:
                    need_remove_list.append(req)
                if "paddlepaddle<" in req and req.index("paddlepaddle<") == 0:
                    need_remove_list.append(req)
                if "protobuf=" in req and req.index("protobuf=") == 0:
                    need_remove_list.append(req)
                if "protobuf>" in req and req.index("protobuf>") == 0:
                    need_remove_list.append(req)
                if "protobuf<" in req and req.index("protobuf<") == 0:
                    need_remove_list.append(req)
        need_remove_list = []
        if len(need_remove_list) > 0:
            for rem in need_remove_list:
                reqs.remove(rem)
    return reqs


req = parse_requirements("requirements.txt")

setup(
    name="flybirds",
    version="0.6.17",
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
    python_requires=">=3.8, <3.11",
    packages=find_packages(exclude=["dist", "build", "tests", "docs"]),
    include_package_data=True,
    install_requires=req,
    entry_points="""
    [console_scripts]
    flybirds = flybirds.launcher:main
    """,
    url="https://github.com/ctripcorp/flybirds",
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)
