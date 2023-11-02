# onelogin.InvitesApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_invite_link**](InvitesApi.md#create_invite_link) | **POST** /1/invites/get_invite_link | Generate Invite Link
[**send_invite_link**](InvitesApi.md#send_invite_link) | **POST** /1/invites/send_invite_link | Send Invite Link


# **create_invite_link**
> CustomAttributesResponse create_invite_link(generate_invite_link_request=generate_invite_link_request)

Generate Invite Link

Generate an invite link for a user already created in your OneLogin account.

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
api_instance = onelogin.InvitesApi(onelogin.ApiClient(configuration))
generate_invite_link_request = onelogin.GenerateInviteLinkRequest() # GenerateInviteLinkRequest |  (optional)

try:
    # Generate Invite Link
    api_response = api_instance.create_invite_link(generate_invite_link_request=generate_invite_link_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitesApi->create_invite_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **generate_invite_link_request** | [**GenerateInviteLinkRequest**](GenerateInviteLinkRequest.md)|  | [optional] 

### Return type

[**CustomAttributesResponse**](CustomAttributesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_invite_link**
> Status send_invite_link(send_invite_link_request=send_invite_link_request)

Send Invite Link

Send an invite link to an existing user in your OneLogin account.

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
api_instance = onelogin.InvitesApi(onelogin.ApiClient(configuration))
send_invite_link_request = onelogin.SendInviteLinkRequest() # SendInviteLinkRequest |  (optional)

try:
    # Send Invite Link
    api_response = api_instance.send_invite_link(send_invite_link_request=send_invite_link_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvitesApi->send_invite_link: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_invite_link_request** | [**SendInviteLinkRequest**](SendInviteLinkRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

