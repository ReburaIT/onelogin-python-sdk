# onelogin.LoginApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**authenticate_user**](LoginApi.md#authenticate_user) | **POST** /1/login/auth | Authenticate a user
[**verify_login_mfa_token**](LoginApi.md#verify_login_mfa_token) | **POST** /1/login/verify_factor | Verify an MFA token


# **authenticate_user**
> UserLoginResponse authenticate_user(custom_allowed_origin_header_1=custom_allowed_origin_header_1, user_login_request=user_login_request)

Authenticate a user

Use this API to generate a session login token in scenarios in which MFA may or may not be required. Both scenarios are supported. A session login token expires two minutes after creation.

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
api_instance = onelogin.LoginApi(onelogin.ApiClient(configuration))
custom_allowed_origin_header_1 = 'custom_allowed_origin_header_1_example' # str | Required for CORS requests only. Set to the Origin URI from which you are allowed to send a request using CORS. (optional)
user_login_request = onelogin.UserLoginRequest() # UserLoginRequest |  (optional)

try:
    # Authenticate a user
    api_response = api_instance.authenticate_user(custom_allowed_origin_header_1=custom_allowed_origin_header_1, user_login_request=user_login_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->authenticate_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_allowed_origin_header_1** | **str**| Required for CORS requests only. Set to the Origin URI from which you are allowed to send a request using CORS. | [optional] 
 **user_login_request** | [**UserLoginRequest**](UserLoginRequest.md)|  | [optional] 

### Return type

[**UserLoginResponse**](UserLoginResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_login_mfa_token**
> LoginVerifyMfaResponse verify_login_mfa_token(custom_allowed_origin_header_1=custom_allowed_origin_header_1, login_verify_mfa_request=login_verify_mfa_request)

Verify an MFA token

Verify a one-time password (OTP) value, provided for a second factor, when multi-factor authentication (MFA) is required.

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
api_instance = onelogin.LoginApi(onelogin.ApiClient(configuration))
custom_allowed_origin_header_1 = 'custom_allowed_origin_header_1_example' # str | Required for CORS requests only. Set to the Origin URI from which you are allowed to send a request using CORS. (optional)
login_verify_mfa_request = onelogin.LoginVerifyMfaRequest() # LoginVerifyMfaRequest |  (optional)

try:
    # Verify an MFA token
    api_response = api_instance.verify_login_mfa_token(custom_allowed_origin_header_1=custom_allowed_origin_header_1, login_verify_mfa_request=login_verify_mfa_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LoginApi->verify_login_mfa_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_allowed_origin_header_1** | **str**| Required for CORS requests only. Set to the Origin URI from which you are allowed to send a request using CORS. | [optional] 
 **login_verify_mfa_request** | [**LoginVerifyMfaRequest**](LoginVerifyMfaRequest.md)|  | [optional] 

### Return type

[**LoginVerifyMfaResponse**](LoginVerifyMfaResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

