# swagger-client
OpenAPI for Todolist RESTful API

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1
- Package version: 1.0.0
- Build package: io.swagger.codegen.v3.generators.python.PythonClientCodegen
For more information, please visit [https://github.com/IkoAfianando](https://github.com/IkoAfianando)

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import swagger_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import swagger_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: TodolistAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TodolistApi(swagger_client.ApiClient(configuration))
include_done = false # bool | Include done todolist in the result (optional) (default to false)
name = 'name_example' # str | Filter todolist by name (optional)

try:
    # Get All Todolist
    api_response = api_instance.todolist_get(include_done=include_done, name=name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todolist_get: %s\n" % e)

# Configure API key authorization: TodolistAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TodolistApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateOrUpdateTodolist() # CreateOrUpdateTodolist | 

try:
    # Create New Todolist
    api_response = api_instance.todolist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todolist_post: %s\n" % e)

# Configure API key authorization: TodolistAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TodolistApi(swagger_client.ApiClient(configuration))
todolist_id = 'todolist_id_example' # str | Todolist id for updated

try:
    # Delete existing Todolist
    api_response = api_instance.todollist_todolist_id_delete(todolist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todollist_todolist_id_delete: %s\n" % e)

# Configure API key authorization: TodolistAuth
configuration = swagger_client.Configuration()
configuration.api_key['X-API-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-API-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.TodolistApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateOrUpdateTodolist() # CreateOrUpdateTodolist | 
todolist_id = 'todolist_id_example' # str | Todolist id for updated

try:
    # Update existing Todolist
    api_response = api_instance.todollist_todolist_id_put(body, todolist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todollist_todolist_id_put: %s\n" % e)
```

## Documentation for API Endpoints

All URIs are relative to *https://{environment}.programmingwithiko.com/api/v1*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*TodolistApi* | [**todolist_get**](docs/TodolistApi.md#todolist_get) | **GET** /todolist | Get All Todolist
*TodolistApi* | [**todolist_post**](docs/TodolistApi.md#todolist_post) | **POST** /todolist | Create New Todolist
*TodolistApi* | [**todollist_todolist_id_delete**](docs/TodolistApi.md#todollist_todolist_id_delete) | **DELETE** /todollist/{todolistId} | Delete existing Todolist
*TodolistApi* | [**todollist_todolist_id_put**](docs/TodolistApi.md#todollist_todolist_id_put) | **PUT** /todollist/{todolistId} | Update existing Todolist

## Documentation For Models

 - [ArrayTodolist](docs/ArrayTodolist.md)
 - [CreateOrUpdateTodolist](docs/CreateOrUpdateTodolist.md)
 - [InlineResponse200](docs/InlineResponse200.md)
 - [Todolist](docs/Todolist.md)

## Documentation For Authorization


## TodolistAuth

- **Type**: API key
- **API key parameter name**: X-API-Key
- **Location**: HTTP header


## Author

ikoafianando123@gmail.com
