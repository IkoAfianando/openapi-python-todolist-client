# swagger_client.TodolistApi

All URIs are relative to *https://{environment}.programmingwithiko.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**todolist_get**](TodolistApi.md#todolist_get) | **GET** /todolist | Get All Todolist
[**todolist_post**](TodolistApi.md#todolist_post) | **POST** /todolist | Create New Todolist
[**todollist_todolist_id_delete**](TodolistApi.md#todollist_todolist_id_delete) | **DELETE** /todollist/{todolistId} | Delete existing Todolist
[**todollist_todolist_id_put**](TodolistApi.md#todollist_todolist_id_put) | **PUT** /todollist/{todolistId} | Update existing Todolist

# **todolist_get**
> ArrayTodolist todolist_get(include_done=include_done, name=name)

Get All Todolist

Get all todolist by default

### Example
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
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **include_done** | **bool**| Include done todolist in the result | [optional] [default to false]
 **name** | **str**| Filter todolist by name | [optional] 

### Return type

[**ArrayTodolist**](ArrayTodolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todolist_post**
> Todolist todolist_post(body)

Create New Todolist

Create new todolist to database

### Example
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
body = swagger_client.CreateOrUpdateTodolist() # CreateOrUpdateTodolist | 

try:
    # Create New Todolist
    api_response = api_instance.todolist_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todolist_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todollist_todolist_id_delete**
> InlineResponse200 todollist_todolist_id_delete(todolist_id)

Delete existing Todolist

Delete existing todolist in database

### Example
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
todolist_id = 'todolist_id_example' # str | Todolist id for updated

try:
    # Delete existing Todolist
    api_response = api_instance.todollist_todolist_id_delete(todolist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todollist_todolist_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **todolist_id** | **str**| Todolist id for updated | 

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **todollist_todolist_id_put**
> Todolist todollist_todolist_id_put(body, todolist_id)

Update existing Todolist

Update existing todolist in database

### Example
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
body = swagger_client.CreateOrUpdateTodolist() # CreateOrUpdateTodolist | 
todolist_id = 'todolist_id_example' # str | Todolist id for updated

try:
    # Update existing Todolist
    api_response = api_instance.todollist_todolist_id_put(body, todolist_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TodolistApi->todollist_todolist_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrUpdateTodolist**](CreateOrUpdateTodolist.md)|  | 
 **todolist_id** | **str**| Todolist id for updated | 

### Return type

[**Todolist**](Todolist.md)

### Authorization

[TodolistAuth](../README.md#TodolistAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

