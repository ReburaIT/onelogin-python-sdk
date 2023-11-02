# onelogin.ConnectorsApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_connectors**](ConnectorsApi.md#get_connectors) | **GET** /2/connectors | Get Connectors


# **get_connectors**
> list[Connector] get_connectors(name=name, auth_method=auth_method)

Get Connectors

Returns a list of connectors

### Example
```python
from __future__ import print_function
import time
import onelogin
from onelogin.rest import ApiException
from pprint import pprint

# Configure OAuth2 access token for authorization: application
configuration = onelogin.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = onelogin.ConnectorsApi(onelogin.ApiClient(configuration))
name = 'name_example' # str |  (optional)
auth_method = 56 # int |  (optional)

try:
    # Get Connectors
    api_response = api_instance.get_connectors(name=name, auth_method=auth_method)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ConnectorsApi->get_connectors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **auth_method** | **int**|  | [optional] 

### Return type

[**list[Connector]**](Connector.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

