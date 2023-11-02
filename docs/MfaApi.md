# onelogin.MfaApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_user_mfa_device**](MfaApi.md#activate_user_mfa_device) | **POST** /1/users/{id}/otp_devices/{device_id}/trigger | Activate an authentication factor
[**delete_user_mfa_device**](MfaApi.md#delete_user_mfa_device) | **DELETE** /1/users/{id}/otp_devices/{device_id} | Remove an authentication device
[**enroll_user_mfa_device**](MfaApi.md#enroll_user_mfa_device) | **POST** /1/users/{id}/otp_devices | Enroll a user with a given authentication factor.
[**get_user_available_mfa_factors**](MfaApi.md#get_user_available_mfa_factors) | **GET** /1/users/{id}/auth_factors | Get a list of MFA factors available to user
[**get_user_enrolled_mfa_devices**](MfaApi.md#get_user_enrolled_mfa_devices) | **GET** /1/users/{id}/otp_devices | Get enrolled authentication devices
[**verify_user_mfa_device**](MfaApi.md#verify_user_mfa_device) | **POST** /1/users/{id}/otp_devices/{device_id}/verify | Verify an authentication device


# **activate_user_mfa_device**
> EnrollMfaDeviceResponse activate_user_mfa_device(id, device_id)

Activate an authentication factor

Use this API to trigger an SMS or Push notification containing a One-Time Password (OTP) that can be used to authenticate a user with the Verify Factor call.

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
device_id = 56 # int | Device ID

try:
    # Activate an authentication factor
    api_response = api_instance.activate_user_mfa_device(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->activate_user_mfa_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **device_id** | **int**| Device ID | 

### Return type

[**EnrollMfaDeviceResponse**](EnrollMfaDeviceResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_mfa_device**
> object delete_user_mfa_device(id, device_id)

Remove an authentication device

Use this API to remove an enrolled factor from a user.

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
device_id = 56 # int | Device ID

try:
    # Remove an authentication device
    api_response = api_instance.delete_user_mfa_device(id, device_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->delete_user_mfa_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **device_id** | **int**| Device ID | 

### Return type

**object**

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enroll_user_mfa_device**
> EnrollMfaDeviceResponse enroll_user_mfa_device(id, enroll_mfa_device_request=enroll_mfa_device_request)

Enroll a user with a given authentication factor.

If the authentication factor requires confirmation to complete, then the device will have an active state of false otherwise it will have an active state of true (corresponding to devices that are either pending confirmation or not)

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
enroll_mfa_device_request = onelogin.EnrollMfaDeviceRequest() # EnrollMfaDeviceRequest |  (optional)

try:
    # Enroll a user with a given authentication factor.
    api_response = api_instance.enroll_user_mfa_device(id, enroll_mfa_device_request=enroll_mfa_device_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->enroll_user_mfa_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **enroll_mfa_device_request** | [**EnrollMfaDeviceRequest**](EnrollMfaDeviceRequest.md)|  | [optional] 

### Return type

[**EnrollMfaDeviceResponse**](EnrollMfaDeviceResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_available_mfa_factors**
> UserMfaFactorsResponse get_user_available_mfa_factors(id)

Get a list of MFA factors available to user

Use this API to return a list of authentication factors that are available for user enrollment via API

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Get a list of MFA factors available to user
    api_response = api_instance.get_user_available_mfa_factors(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->get_user_available_mfa_factors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserMfaFactorsResponse**](UserMfaFactorsResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_enrolled_mfa_devices**
> EnrolledMfaDevicesResponse get_user_enrolled_mfa_devices(id)

Get enrolled authentication devices

Use this API to return a list of authentication factors registered to a particular user for multifactor authentication (MFA).

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Get enrolled authentication devices
    api_response = api_instance.get_user_enrolled_mfa_devices(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->get_user_enrolled_mfa_devices: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**EnrolledMfaDevicesResponse**](EnrolledMfaDevicesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_user_mfa_device**
> Status verify_user_mfa_device(id, device_id, verify_mfa_device_request=verify_mfa_device_request)

Verify an authentication device

Use this API to authenticate a one-time password (OTP) code provided by a multifactor authentication (MFA) device.

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
api_instance = onelogin.MfaApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
device_id = 56 # int | Device ID
verify_mfa_device_request = onelogin.VerifyMfaDeviceRequest() # VerifyMfaDeviceRequest |  (optional)

try:
    # Verify an authentication device
    api_response = api_instance.verify_user_mfa_device(id, device_id, verify_mfa_device_request=verify_mfa_device_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MfaApi->verify_user_mfa_device: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **device_id** | **int**| Device ID | 
 **verify_mfa_device_request** | [**VerifyMfaDeviceRequest**](VerifyMfaDeviceRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

