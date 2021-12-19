# coding: utf-8

"""
    Todolist RESTful API

    OpenAPI for Todolist RESTful API  # noqa: E501

    OpenAPI spec version: 1
    Contact: ikoafianando123@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.todolist_api import TodolistApi  # noqa: E501
from swagger_client.rest import ApiException


class TestTodolistApi(unittest.TestCase):
    """TodolistApi unit test stubs"""

    def setUp(self):
        self.api = TodolistApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_todolist_get(self):
        """Test case for todolist_get

        Get All Todolist  # noqa: E501
        """
        pass

    def test_todolist_post(self):
        """Test case for todolist_post

        Create New Todolist  # noqa: E501
        """
        pass

    def test_todollist_todolist_id_delete(self):
        """Test case for todollist_todolist_id_delete

        Delete existing Todolist  # noqa: E501
        """
        pass

    def test_todollist_todolist_id_put(self):
        """Test case for todollist_todolist_id_put

        Update existing Todolist  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
