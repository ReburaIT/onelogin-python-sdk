# onelogin.RolesApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_role**](RolesApi.md#get_role) | **GET** /1/roles/{id} | Get Role by ID
[**get_roles**](RolesApi.md#get_roles) | **GET** /1/roles | Get Roles


# **get_role**
> RoleReponse get_role(id)

Get Role by ID

Use this call to get a role by ID.

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
api_instance = onelogin.RolesApi(onelogin.ApiClient(configuration))
id = 56 # int | Role ID

try:
    # Get Role by ID
    api_response = api_instance.get_role(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Role ID | 

### Return type

[**RoleReponse**](RoleReponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_roles**
> RolesResponse get_roles(id=id, name=name, limit=limit, sort=sort, fields=fields)

Get Roles

Returns a list of roles. Supports filtering and paging.

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
api_instance = onelogin.RolesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str |  (optional)
name = 'name_example' # str |  (optional)
limit = 56 # int |  (optional)
sort = 'sort_example' # str |  (optional)
fields = 'fields_example' # str |  (optional)

try:
    # Get Roles
    api_response = api_instance.get_roles(id=id, name=name, limit=limit, sort=sort, fields=fields)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RolesApi->get_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | [optional] 
 **name** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] 
 **sort** | **str**|  | [optional] 
 **fields** | **str**|  | [optional] 

### Return type

[**RolesResponse**](RolesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

