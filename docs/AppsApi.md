# onelogin.AppsApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_app**](AppsApi.md#create_app) | **POST** /2/apps | Create an App
[**delete_app**](AppsApi.md#delete_app) | **DELETE** /2/apps/{id} | Delete an app
[**delete_app_parameter**](AppsApi.md#delete_app_parameter) | **DELETE** /2/apps/{id}/parameters/{parameter_id} | Delete an app parameter
[**get_app**](AppsApi.md#get_app) | **GET** /2/apps/{id} | Get an App
[**get_apps**](AppsApi.md#get_apps) | **GET** /2/apps | Get Apps
[**update_app**](AppsApi.md#update_app) | **PUT** /2/apps/{id} | Update an App


# **create_app**
> App create_app(create_app_request=create_app_request)

Create an App

Creates a new app in OneLogin

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
create_app_request = onelogin.App() # App | The app to create (optional)

try:
    # Create an App
    api_response = api_instance.create_app(create_app_request=create_app_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->create_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_app_request** | [**App**](App.md)| The app to create | [optional] 

### Return type

[**App**](App.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app**
> delete_app(id)

Delete an app

Use this call to delete a app by ID.

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
id = 56 # int | App ID

try:
    # Delete an app
    api_instance.delete_app(id)
except ApiException as e:
    print("Exception when calling AppsApi->delete_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| App ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_parameter**
> delete_app_parameter(id, parameter_id)

Delete an app parameter

Use this call to delete a app by ID.

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
id = 56 # int | App ID
parameter_id = 56 # int | Parameter ID

try:
    # Delete an app parameter
    api_instance.delete_app_parameter(id, parameter_id)
except ApiException as e:
    print("Exception when calling AppsApi->delete_app_parameter: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| App ID | 
 **parameter_id** | **int**| Parameter ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app**
> App get_app(id)

Get an App

Get an app in OneLogin

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
id = 56 # int | App ID

try:
    # Get an App
    api_response = api_instance.get_app(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| App ID | 

### Return type

[**App**](App.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_apps**
> list[AppInfo] get_apps(name=name, auth_method=auth_method, connector_id=connector_id)

Get Apps

Returns a list of apps

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
name = 'name_example' # str |  (optional)
auth_method = 56 # int |  (optional)
connector_id = 56 # int |  (optional)

try:
    # Get Apps
    api_response = api_instance.get_apps(name=name, auth_method=auth_method, connector_id=connector_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 
 **auth_method** | **int**|  | [optional] 
 **connector_id** | **int**|  | [optional] 

### Return type

[**list[AppInfo]**](AppInfo.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app**
> App update_app(id, update_app_request=update_app_request)

Update an App

Update an app in OneLogin

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
api_instance = onelogin.AppsApi(onelogin.ApiClient(configuration))
id = 56 # int | App ID
update_app_request = onelogin.App() # App | The app to update (optional)

try:
    # Update an App
    api_response = api_instance.update_app(id, update_app_request=update_app_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_app: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| App ID | 
 **update_app_request** | [**App**](App.md)| The app to update | [optional] 

### Return type

[**App**](App.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

