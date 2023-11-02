# onelogin.SamlApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_saml_assertion**](SamlApi.md#create_saml_assertion) | **POST** /1/saml_assertion | Generate SAML assertion
[**verify_saml_assertion_mfa_token**](SamlApi.md#verify_saml_assertion_mfa_token) | **POST** /1/saml_assertion/verify_factor | Verify an MFA token


# **create_saml_assertion**
> SamlAssertionResponse create_saml_assertion(saml_assertion_request=saml_assertion_request)

Generate SAML assertion

Use this API to generate a SAML assertion.

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
api_instance = onelogin.SamlApi(onelogin.ApiClient(configuration))
saml_assertion_request = onelogin.SamlAssertionRequest() # SamlAssertionRequest |  (optional)

try:
    # Generate SAML assertion
    api_response = api_instance.create_saml_assertion(saml_assertion_request=saml_assertion_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamlApi->create_saml_assertion: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_assertion_request** | [**SamlAssertionRequest**](SamlAssertionRequest.md)|  | [optional] 

### Return type

[**SamlAssertionResponse**](SamlAssertionResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **verify_saml_assertion_mfa_token**
> SamlAssertionResponse verify_saml_assertion_mfa_token(saml_verify_mfa_request=saml_verify_mfa_request)

Verify an MFA token

Verify a one-time password (OTP) value, provided for a second factor, when multi-factor authentication (MFA) is required for SAML authentication.

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
api_instance = onelogin.SamlApi(onelogin.ApiClient(configuration))
saml_verify_mfa_request = onelogin.SamlVerifyMfaRequest() # SamlVerifyMfaRequest |  (optional)

try:
    # Verify an MFA token
    api_response = api_instance.verify_saml_assertion_mfa_token(saml_verify_mfa_request=saml_verify_mfa_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SamlApi->verify_saml_assertion_mfa_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saml_verify_mfa_request** | [**SamlVerifyMfaRequest**](SamlVerifyMfaRequest.md)|  | [optional] 

### Return type

[**SamlAssertionResponse**](SamlAssertionResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

