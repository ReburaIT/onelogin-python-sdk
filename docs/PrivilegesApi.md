# onelogin.PrivilegesApi

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_privilege_roles**](PrivilegesApi.md#add_privilege_roles) | **POST** /1/privileges/{id}/roles | Assign roles
[**add_privilege_users**](PrivilegesApi.md#add_privilege_users) | **POST** /1/privileges/{id}/users | Assign users
[**create_privilege**](PrivilegesApi.md#create_privilege) | **POST** /1/privileges | Creates privilege
[**delete_privilege**](PrivilegesApi.md#delete_privilege) | **DELETE** /1/privileges/{id} | Delete privilege
[**get_privilege**](PrivilegesApi.md#get_privilege) | **GET** /1/privileges/{id} | Get privilege
[**get_privilege_roles**](PrivilegesApi.md#get_privilege_roles) | **GET** /1/privileges/{id}/roles | Get roles
[**get_privilege_users**](PrivilegesApi.md#get_privilege_users) | **GET** /1/privileges/{id}/users | Get privilege users
[**get_privileges**](PrivilegesApi.md#get_privileges) | **GET** /1/privileges | Get Privileges
[**remove_privilege_role**](PrivilegesApi.md#remove_privilege_role) | **DELETE** /1/privileges/{id}/roles/{role_id} | Remove a role
[**remove_privlege_user**](PrivilegesApi.md#remove_privlege_user) | **DELETE** /1/privileges/{id}/users/{user_id} | Remove a user
[**update_privilege**](PrivilegesApi.md#update_privilege) | **PUT** /1/privileges/{id} | Update privilege


# **add_privilege_roles**
> AssignPrivilegeRolesResponse add_privilege_roles(id, assign_privilege_roles_request)

Assign roles

Use this API to assign a privilege to one or more roles.

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID
assign_privilege_roles_request = onelogin.AssignPrivilegeRolesRequest() # AssignPrivilegeRolesRequest | Roles

try:
    # Assign roles
    api_response = api_instance.add_privilege_roles(id, assign_privilege_roles_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->add_privilege_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 
 **assign_privilege_roles_request** | [**AssignPrivilegeRolesRequest**](AssignPrivilegeRolesRequest.md)| Roles | 

### Return type

[**AssignPrivilegeRolesResponse**](AssignPrivilegeRolesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **add_privilege_users**
> AssignPrivilegeRolesResponse add_privilege_users(id, assign_privilege_users_request)

Assign users

Use this API to assign a privilege to one or more users.

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID
assign_privilege_users_request = onelogin.AssignPrivilegeUsersRequest() # AssignPrivilegeUsersRequest | Users

try:
    # Assign users
    api_response = api_instance.add_privilege_users(id, assign_privilege_users_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->add_privilege_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 
 **assign_privilege_users_request** | [**AssignPrivilegeUsersRequest**](AssignPrivilegeUsersRequest.md)| Users | 

### Return type

[**AssignPrivilegeRolesResponse**](AssignPrivilegeRolesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_privilege**
> CreatePrivilegeResponse create_privilege(privilege=privilege)

Creates privilege

Creates a privilege    

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
privilege = onelogin.Privilege() # Privilege |  (optional)

try:
    # Creates privilege
    api_response = api_instance.create_privilege(privilege=privilege)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->create_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **privilege** | [**Privilege**](Privilege.md)|  | [optional] 

### Return type

[**CreatePrivilegeResponse**](CreatePrivilegeResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_privilege**
> delete_privilege(id)

Delete privilege

Delete a privilege    

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID

try:
    # Delete privilege
    api_instance.delete_privilege(id)
except ApiException as e:
    print("Exception when calling PrivilegesApi->delete_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege**
> get_privilege(id)

Get privilege

Get a privilege    

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID

try:
    # Get privilege
    api_instance.get_privilege(id)
except ApiException as e:
    print("Exception when calling PrivilegesApi->get_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege_roles**
> PrivilegeRolesResponse get_privilege_roles(id)

Get roles

Get roles assigned to a privilege  

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID

try:
    # Get roles
    api_response = api_instance.get_privilege_roles(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->get_privilege_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 

### Return type

[**PrivilegeRolesResponse**](PrivilegeRolesResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privilege_users**
> PrivilegeUsersResponse get_privilege_users(id)

Get privilege users

Get users assigned to a privilege  

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID

try:
    # Get privilege users
    api_response = api_instance.get_privilege_users(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->get_privilege_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 

### Return type

[**PrivilegeUsersResponse**](PrivilegeUsersResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_privileges**
> list[Privilege] get_privileges()

Get Privileges

Use this API to list the Privileges created in an account.

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))

try:
    # Get Privileges
    api_response = api_instance.get_privileges()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->get_privileges: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Privilege]**](Privilege.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_privilege_role**
> remove_privilege_role(id, role_id)

Remove a role

Use this API to remove a single role from a privilege.

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID
role_id = 56 # int | Role ID

try:
    # Remove a role
    api_instance.remove_privilege_role(id, role_id)
except ApiException as e:
    print("Exception when calling PrivilegesApi->remove_privilege_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 
 **role_id** | **int**| Role ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **remove_privlege_user**
> remove_privlege_user(id, user_id)

Remove a user

Use this API to remove a single user from a privilege.

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID
user_id = 56 # int | User ID

try:
    # Remove a user
    api_instance.remove_privlege_user(id, user_id)
except ApiException as e:
    print("Exception when calling PrivilegesApi->remove_privlege_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 
 **user_id** | **int**| User ID | 

### Return type

void (empty response body)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_privilege**
> CreatePrivilegeResponse update_privilege(id, update_privilege_request=update_privilege_request)

Update privilege

Update a privilege    

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
api_instance = onelogin.PrivilegesApi(onelogin.ApiClient(configuration))
id = 'id_example' # str | Privilege ID
update_privilege_request = onelogin.Privilege() # Privilege |  (optional)

try:
    # Update privilege
    api_response = api_instance.update_privilege(id, update_privilege_request=update_privilege_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PrivilegesApi->update_privilege: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| Privilege ID | 
 **update_privilege_request** | [**Privilege**](Privilege.md)|  | [optional] 

### Return type

[**CreatePrivilegeResponse**](CreatePrivilegeResponse.md)

### Authorization

[application](../README.md#application)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

