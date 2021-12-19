# coding: utf-8

"""
    Todolist RESTful API

    OpenAPI for Todolist RESTful API  # noqa: E501

    OpenAPI spec version: 1
    Contact: ikoafianando123@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from setuptools import setup, find_packages  # noqa: H301

NAME = "swagger-client"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Todolist RESTful API",
    author_email="ikoafianando123@gmail.com",
    url="",
    keywords=["Swagger", "Todolist RESTful API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    OpenAPI for Todolist RESTful API  # noqa: E501
    """
)
