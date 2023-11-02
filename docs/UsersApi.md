# onelogin.UsersApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_user_roles**](UsersApi.md#add_user_roles) | **PUT** /1/users/{id}/add_roles | Assign Role to User
[**create_user**](UsersApi.md#create_user) | **POST** /1/users | Create a User
[**create_user_temp_mfa_token**](UsersApi.md#create_user_temp_mfa_token) | **POST** /1/users/{id}/mfa_token | Generate Temp MFA Token
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /1/users/{id} | Delete a user account
[**get_custom_attributes**](UsersApi.md#get_custom_attributes) | **GET** /1/users/custom_attributes | Get Custom Attributes
[**get_user**](UsersApi.md#get_user) | **GET** /1/users/{id} | Get a User
[**get_user_apps**](UsersApi.md#get_user_apps) | **GET** /1/users/{id}/apps | Get User Apps
[**get_user_roles**](UsersApi.md#get_user_roles) | **GET** /1/users/{id}/roles | Get User Roles
[**get_users**](UsersApi.md#get_users) | **GET** /1/users | Get Users
[**lock_user**](UsersApi.md#lock_user) | **PUT** /1/users/{id}/lock_user | Lock a user account
[**logout_user**](UsersApi.md#logout_user) | **PUT** /1/users/{id}/logout | Log a user out of any and all sessions
[**remove_user_roles**](UsersApi.md#remove_user_roles) | **PUT** /1/users/{id}/remove_roles | Remove Roles from User
[**update_user**](UsersApi.md#update_user) | **PUT** /1/users/{id} | Update a User
[**update_user_custom_attributes**](UsersApi.md#update_user_custom_attributes) | **PUT** /1/users/{id}/set_custom_attributes | Set a custom attribute
[**update_user_password**](UsersApi.md#update_user_password) | **PUT** /1/users/set_password_clear_text/{id} | Set a the password for a user
[**update_user_password_salted**](UsersApi.md#update_user_password_salted) | **PUT** /1/users/set_password_using_salt/{id} | Set a pre salted password for a user
[**update_user_state**](UsersApi.md#update_user_state) | **PUT** /1/users/{id}/set_state | Set the State for a user.


# **add_user_roles**
> Status add_user_roles(id, add_user_roles_request=add_user_roles_request)

Assign Role to User

Assign one or more existing roles to a user.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
add_user_roles_request = [onelogin.list[int]()] # list[int] | The roles to assign (optional)

try:
    # Assign Role to User
    api_response = api_instance.add_user_roles(id, add_user_roles_request=add_user_roles_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->add_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **add_user_roles_request** | **list[int]**| The roles to assign | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> CreateUserResponse create_user(create_user_request=create_user_request)

Create a User

Creates a new user account in OneLogin

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
create_user_request = onelogin.User() # User | The user to create (optional)

try:
    # Create a User
    api_response = api_instance.create_user(create_user_request=create_user_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**User**](User.md)| The user to create | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_temp_mfa_token**
> GenerateMfaTokenResponse create_user_temp_mfa_token(id, generate_mfa_token_request=generate_mfa_token_request)

Generate Temp MFA Token

Use to generate a temporary MFA token that can be used in place of other MFA tokens for a set time period. For example, use this token for account recovery.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
generate_mfa_token_request = onelogin.GenerateMfaTokenRequest() # GenerateMfaTokenRequest |  (optional)

try:
    # Generate Temp MFA Token
    api_response = api_instance.create_user_temp_mfa_token(id, generate_mfa_token_request=generate_mfa_token_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->create_user_temp_mfa_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **generate_mfa_token_request** | [**GenerateMfaTokenRequest**](GenerateMfaTokenRequest.md)|  | [optional] 

### Return type

[**GenerateMfaTokenResponse**](GenerateMfaTokenResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> Status delete_user(id)

Delete a user account

Use this call to delete a user by ID.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Delete a user account
    api_response = api_instance.delete_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_custom_attributes**
> CustomAttributesResponse get_custom_attributes()

Get Custom Attributes

Returns a list of all custom attribute fields (also known as custom user fields) that have been defined for your account.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))

try:
    # Get Custom Attributes
    api_response = api_instance.get_custom_attributes()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_custom_attributes: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CustomAttributesResponse**](CustomAttributesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> CreateUserResponse get_user(id)

Get a User

Returns a single user

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Get a User
    api_response = api_instance.get_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_apps**
> UserAppsResponse get_user_apps(id)

Get User Apps

Get a list of apps accessible by a user, not including personal apps.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Get User Apps
    api_response = api_instance.get_user_apps(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_apps: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserAppsResponse**](UserAppsResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_roles**
> UserRolesResponse get_user_roles(id)

Get User Roles

Get a list of role IDs that have been assigned to a user.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Get User Roles
    api_response = api_instance.get_user_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**UserRolesResponse**](UserRolesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_users**
> UsersResponse get_users(directory_id=directory_id, email=email, external_id=external_id, firstname=firstname, id=id, manager_ad_id=manager_ad_id, role_id=role_id, samaccountname=samaccountname, since=since, until=until, username=username, userprincipalname=userprincipalname)

Get Users

Returns a list of users. Supports filtering and paging.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
directory_id = 56 # int |  (optional)
email = 'email_example' # str |  (optional)
external_id = 'external_id_example' # str |  (optional)
firstname = 'firstname_example' # str |  (optional)
id = 56 # int |  (optional)
manager_ad_id = 56 # int |  (optional)
role_id = 56 # int |  (optional)
samaccountname = 'samaccountname_example' # str |  (optional)
since = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
until = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
username = 'username_example' # str |  (optional)
userprincipalname = 'userprincipalname_example' # str |  (optional)

try:
    # Get Users
    api_response = api_instance.get_users(directory_id=directory_id, email=email, external_id=external_id, firstname=firstname, id=id, manager_ad_id=manager_ad_id, role_id=role_id, samaccountname=samaccountname, since=since, until=until, username=username, userprincipalname=userprincipalname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **directory_id** | **int**|  | [optional] 
 **email** | **str**|  | [optional] 
 **external_id** | **str**|  | [optional] 
 **firstname** | **str**|  | [optional] 
 **id** | **int**|  | [optional] 
 **manager_ad_id** | **int**|  | [optional] 
 **role_id** | **int**|  | [optional] 
 **samaccountname** | **str**|  | [optional] 
 **since** | **datetime**|  | [optional] 
 **until** | **datetime**|  | [optional] 
 **username** | **str**|  | [optional] 
 **userprincipalname** | **str**|  | [optional] 

### Return type

[**UsersResponse**](UsersResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lock_user**
> Status lock_user(id, lock_user_request=lock_user_request)

Lock a user account

Use this call to lock a user’s account based on the policy assigned to the user, for a specific time you define in the request, or until you unlock it.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
lock_user_request = onelogin.LockUserRequest() # LockUserRequest |  (optional)

try:
    # Lock a user account
    api_response = api_instance.lock_user(id, lock_user_request=lock_user_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->lock_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **lock_user_request** | [**LockUserRequest**](LockUserRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_user**
> Status logout_user(id)

Log a user out of any and all sessions

Log a user out of any and all sessions.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID

try:
    # Log a user out of any and all sessions
    api_response = api_instance.logout_user(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->logout_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_user_roles**
> Status remove_user_roles(id, remove_user_roles_request=remove_user_roles_request)

Remove Roles from User

Remove one or more existing roles to a user.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
remove_user_roles_request = [onelogin.list[int]()] # list[int] | The roles to remove (optional)

try:
    # Remove Roles from User
    api_response = api_instance.remove_user_roles(id, remove_user_roles_request=remove_user_roles_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->remove_user_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **remove_user_roles_request** | **list[int]**| The roles to remove | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> CreateUserResponse update_user(id, update_user_request=update_user_request)

Update a User

Use to update a user by ID

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
update_user_request = onelogin.User() # User | The user to update (optional)

try:
    # Update a User
    api_response = api_instance.update_user(id, update_user_request=update_user_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **update_user_request** | [**User**](User.md)| The user to update | [optional] 

### Return type

[**CreateUserResponse**](CreateUserResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_custom_attributes**
> Status update_user_custom_attributes(id, set_user_custom_attributes_request=set_user_custom_attributes_request)

Set a custom attribute

Set a custom attribute field (also known as a custom user field) value for a user.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
set_user_custom_attributes_request = onelogin.SetUserCustomAttributesRequest() # SetUserCustomAttributesRequest |  (optional)

try:
    # Set a custom attribute
    api_response = api_instance.update_user_custom_attributes(id, set_user_custom_attributes_request=set_user_custom_attributes_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_custom_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **set_user_custom_attributes_request** | [**SetUserCustomAttributesRequest**](SetUserCustomAttributesRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password**
> Status update_user_password(id, new_cleartext_password_request=new_cleartext_password_request)

Set a the password for a user

Set a the password for a user

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
new_cleartext_password_request = onelogin.NewCleartextPasswordRequest() # NewCleartextPasswordRequest |  (optional)

try:
    # Set a the password for a user
    api_response = api_instance.update_user_password(id, new_cleartext_password_request=new_cleartext_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **new_cleartext_password_request** | [**NewCleartextPasswordRequest**](NewCleartextPasswordRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_password_salted**
> Status update_user_password_salted(id, new_salted_password_request=new_salted_password_request)

Set a pre salted password for a user

Set a pre salted password for a user

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
new_salted_password_request = onelogin.NewSaltedPasswordRequest() # NewSaltedPasswordRequest |  (optional)

try:
    # Set a pre salted password for a user
    api_response = api_instance.update_user_password_salted(id, new_salted_password_request=new_salted_password_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_password_salted: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **new_salted_password_request** | [**NewSaltedPasswordRequest**](NewSaltedPasswordRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_state**
> Status update_user_state(id, set_user_state_request=set_user_state_request)

Set the State for a user.

States describe a stage in a process (such as user account approval). User state determines the possible statuses a user account can be in.

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
api_instance = onelogin.UsersApi(onelogin.ApiClient(configuration))
id = 56 # int | User ID
set_user_state_request = onelogin.SetUserStateRequest() # SetUserStateRequest |  (optional)

try:
    # Set the State for a user.
    api_response = api_instance.update_user_state(id, set_user_state_request=set_user_state_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UsersApi->update_user_state: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| User ID | 
 **set_user_state_request** | [**SetUserStateRequest**](SetUserStateRequest.md)|  | [optional] 

### Return type

[**Status**](Status.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

