# onelogin.EventsApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_event**](EventsApi.md#get_event) | **GET** /1/events/{id} | Get Event by ID
[**get_event_types**](EventsApi.md#get_event_types) | **GET** /1/events/types | Get Event Types
[**get_events**](EventsApi.md#get_events) | **GET** /1/events | Get Events


# **get_event**
> EventResponse get_event(id)

Get Event by ID

Returns a single event

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
api_instance = onelogin.EventsApi(onelogin.ApiClient(configuration))
id = 56 # int | Event ID

try:
    # Get Event by ID
    api_response = api_instance.get_event(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Event ID | 

### Return type

[**EventResponse**](EventResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_event_types**
> EventTypesResponse get_event_types()

Get Event Types

Returns a list of event types

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
api_instance = onelogin.EventsApi(onelogin.ApiClient(configuration))

try:
    # Get Event Types
    api_response = api_instance.get_event_types()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_event_types: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**EventTypesResponse**](EventTypesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_events**
> EventsResponse get_events(client_id=client_id, created_at=created_at, directory_id=directory_id, event_type_id=event_type_id, id=id, resolution=resolution, since=since, until=until, user_id=user_id)

Get Events

Returns a list of events. Supports filtering and paging.

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
api_instance = onelogin.EventsApi(onelogin.ApiClient(configuration))
client_id = 'client_id_example' # str |  (optional)
created_at = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
directory_id = 56 # int |  (optional)
event_type_id = 56 # int |  (optional)
id = 56 # int |  (optional)
resolution = 'resolution_example' # str |  (optional)
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
user_id = 56 # int |  (optional)

try:
    # Get Events
    api_response = api_instance.get_events(client_id=client_id, created_at=created_at, directory_id=directory_id, event_type_id=event_type_id, id=id, resolution=resolution, since=since, until=until, user_id=user_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EventsApi->get_events: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_id** | **str**|  | [optional] 
 **created_at** | **datetime**|  | [optional] 
 **directory_id** | **int**|  | [optional] 
 **event_type_id** | **int**|  | [optional] 
 **id** | **int**|  | [optional] 
 **resolution** | **str**|  | [optional] 
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 
 **user_id** | **int**|  | [optional] 

### Return type

[**EventsResponse**](EventsResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

