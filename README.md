# onelogin
This is an administrative API for OneLogin customers

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 1.1.0
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com//.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com//.git`)

Then import the package:
```python
import onelogin 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import onelogin
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/OneLogin-Auth/onelogin-api/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AppsApi* | [**create_app**](docs/AppsApi.md#create_app) | **POST** /2/apps | Create an App
*AppsApi* | [**delete_app**](docs/AppsApi.md#delete_app) | **DELETE** /2/apps/{id} | Delete an app
*AppsApi* | [**delete_app_parameter**](docs/AppsApi.md#delete_app_parameter) | **DELETE** /2/apps/{id}/parameters/{parameter_id} | Delete an app parameter
*AppsApi* | [**get_app**](docs/AppsApi.md#get_app) | **GET** /2/apps/{id} | Get an App
*AppsApi* | [**get_apps**](docs/AppsApi.md#get_apps) | **GET** /2/apps | Get Apps
*AppsApi* | [**update_app**](docs/AppsApi.md#update_app) | **PUT** /2/apps/{id} | Update an App
*ConnectorsApi* | [**get_connectors**](docs/ConnectorsApi.md#get_connectors) | **GET** /2/connectors | Get Connectors
*EventsApi* | [**get_event**](docs/EventsApi.md#get_event) | **GET** /1/events/{id} | Get Event by ID
*EventsApi* | [**get_event_types**](docs/EventsApi.md#get_event_types) | **GET** /1/events/types | Get Event Types
*EventsApi* | [**get_events**](docs/EventsApi.md#get_events) | **GET** /1/events | Get Events
*GroupsApi* | [**get_group**](docs/GroupsApi.md#get_group) | **GET** /1/groups/{id} | Get Group by ID
*GroupsApi* | [**get_groups**](docs/GroupsApi.md#get_groups) | **GET** /1/groups | Get Groups
*InvitesApi* | [**create_invite_link**](docs/InvitesApi.md#create_invite_link) | **POST** /1/invites/get_invite_link | Generate Invite Link
*InvitesApi* | [**send_invite_link**](docs/InvitesApi.md#send_invite_link) | **POST** /1/invites/send_invite_link | Send Invite Link
*LoginApi* | [**authenticate_user**](docs/LoginApi.md#authenticate_user) | **POST** /1/login/auth | Authenticate a user
*LoginApi* | [**verify_login_mfa_token**](docs/LoginApi.md#verify_login_mfa_token) | **POST** /1/login/verify_factor | Verify an MFA token
*MfaApi* | [**activate_user_mfa_device**](docs/MfaApi.md#activate_user_mfa_device) | **POST** /1/users/{id}/otp_devices/{device_id}/trigger | Activate an authentication factor
*MfaApi* | [**delete_user_mfa_device**](docs/MfaApi.md#delete_user_mfa_device) | **DELETE** /1/users/{id}/otp_devices/{device_id} | Remove an authentication device
*MfaApi* | [**enroll_user_mfa_device**](docs/MfaApi.md#enroll_user_mfa_device) | **POST** /1/users/{id}/otp_devices | Enroll a user with a given authentication factor.
*MfaApi* | [**get_user_available_mfa_factors**](docs/MfaApi.md#get_user_available_mfa_factors) | **GET** /1/users/{id}/auth_factors | Get a list of MFA factors available to user
*MfaApi* | [**get_user_enrolled_mfa_devices**](docs/MfaApi.md#get_user_enrolled_mfa_devices) | **GET** /1/users/{id}/otp_devices | Get enrolled authentication devices
*MfaApi* | [**verify_user_mfa_device**](docs/MfaApi.md#verify_user_mfa_device) | **POST** /1/users/{id}/otp_devices/{device_id}/verify | Verify an authentication device
*PrivilegesApi* | [**add_privilege_roles**](docs/PrivilegesApi.md#add_privilege_roles) | **POST** /1/privileges/{id}/roles | Assign roles
*PrivilegesApi* | [**add_privilege_users**](docs/PrivilegesApi.md#add_privilege_users) | **POST** /1/privileges/{id}/users | Assign users
*PrivilegesApi* | [**create_privilege**](docs/PrivilegesApi.md#create_privilege) | **POST** /1/privileges | Creates privilege
*PrivilegesApi* | [**delete_privilege**](docs/PrivilegesApi.md#delete_privilege) | **DELETE** /1/privileges/{id} | Delete privilege
*PrivilegesApi* | [**get_privilege**](docs/PrivilegesApi.md#get_privilege) | **GET** /1/privileges/{id} | Get privilege
*PrivilegesApi* | [**get_privilege_roles**](docs/PrivilegesApi.md#get_privilege_roles) | **GET** /1/privileges/{id}/roles | Get roles
*PrivilegesApi* | [**get_privilege_users**](docs/PrivilegesApi.md#get_privilege_users) | **GET** /1/privileges/{id}/users | Get privilege users
*PrivilegesApi* | [**get_privileges**](docs/PrivilegesApi.md#get_privileges) | **GET** /1/privileges | Get Privileges
*PrivilegesApi* | [**remove_privilege_role**](docs/PrivilegesApi.md#remove_privilege_role) | **DELETE** /1/privileges/{id}/roles/{role_id} | Remove a role
*PrivilegesApi* | [**remove_privlege_user**](docs/PrivilegesApi.md#remove_privlege_user) | **DELETE** /1/privileges/{id}/users/{user_id} | Remove a user
*PrivilegesApi* | [**update_privilege**](docs/PrivilegesApi.md#update_privilege) | **PUT** /1/privileges/{id} | Update privilege
*RolesApi* | [**get_role**](docs/RolesApi.md#get_role) | **GET** /1/roles/{id} | Get Role by ID
*RolesApi* | [**get_roles**](docs/RolesApi.md#get_roles) | **GET** /1/roles | Get Roles
*SamlApi* | [**create_saml_assertion**](docs/SamlApi.md#create_saml_assertion) | **POST** /1/saml_assertion | Generate SAML assertion
*SamlApi* | [**verify_saml_assertion_mfa_token**](docs/SamlApi.md#verify_saml_assertion_mfa_token) | **POST** /1/saml_assertion/verify_factor | Verify an MFA token
*UsersApi* | [**add_user_roles**](docs/UsersApi.md#add_user_roles) | **PUT** /1/users/{id}/add_roles | Assign Role to User
*UsersApi* | [**create_user**](docs/UsersApi.md#create_user) | **POST** /1/users | Create a User
*UsersApi* | [**create_user_temp_mfa_token**](docs/UsersApi.md#create_user_temp_mfa_token) | **POST** /1/users/{id}/mfa_token | Generate Temp MFA Token
*UsersApi* | [**delete_user**](docs/UsersApi.md#delete_user) | **DELETE** /1/users/{id} | Delete a user account
*UsersApi* | [**get_custom_attributes**](docs/UsersApi.md#get_custom_attributes) | **GET** /1/users/custom_attributes | Get Custom Attributes
*UsersApi* | [**get_user**](docs/UsersApi.md#get_user) | **GET** /1/users/{id} | Get a User
*UsersApi* | [**get_user_apps**](docs/UsersApi.md#get_user_apps) | **GET** /1/users/{id}/apps | Get User Apps
*UsersApi* | [**get_user_roles**](docs/UsersApi.md#get_user_roles) | **GET** /1/users/{id}/roles | Get User Roles
*UsersApi* | [**get_users**](docs/UsersApi.md#get_users) | **GET** /1/users | Get Users
*UsersApi* | [**lock_user**](docs/UsersApi.md#lock_user) | **PUT** /1/users/{id}/lock_user | Lock a user account
*UsersApi* | [**logout_user**](docs/UsersApi.md#logout_user) | **PUT** /1/users/{id}/logout | Log a user out of any and all sessions
*UsersApi* | [**remove_user_roles**](docs/UsersApi.md#remove_user_roles) | **PUT** /1/users/{id}/remove_roles | Remove Roles from User
*UsersApi* | [**update_user**](docs/UsersApi.md#update_user) | **PUT** /1/users/{id} | Update a User
*UsersApi* | [**update_user_custom_attributes**](docs/UsersApi.md#update_user_custom_attributes) | **PUT** /1/users/{id}/set_custom_attributes | Set a custom attribute
*UsersApi* | [**update_user_password**](docs/UsersApi.md#update_user_password) | **PUT** /1/users/set_password_clear_text/{id} | Set a the password for a user
*UsersApi* | [**update_user_password_salted**](docs/UsersApi.md#update_user_password_salted) | **PUT** /1/users/set_password_using_salt/{id} | Set a pre salted password for a user
*UsersApi* | [**update_user_state**](docs/UsersApi.md#update_user_state) | **PUT** /1/users/{id}/set_state | Set the State for a user.


## Documentation For Models

 - [Action](docs/Action.md)
 - [App](docs/App.md)
 - [AppConfiguration](docs/AppConfiguration.md)
 - [AppInfo](docs/AppInfo.md)
 - [AppParameters](docs/AppParameters.md)
 - [AppProvisioning](docs/AppProvisioning.md)
 - [AppSso](docs/AppSso.md)
 - [AppSsoCertificate](docs/AppSsoCertificate.md)
 - [AssignPrivilegeRolesRequest](docs/AssignPrivilegeRolesRequest.md)
 - [AssignPrivilegeRolesResponse](docs/AssignPrivilegeRolesResponse.md)
 - [AssignPrivilegeUsersRequest](docs/AssignPrivilegeUsersRequest.md)
 - [Connector](docs/Connector.md)
 - [CreatePrivilegeResponse](docs/CreatePrivilegeResponse.md)
 - [CreateUserResponse](docs/CreateUserResponse.md)
 - [CustomAttributesResponse](docs/CustomAttributesResponse.md)
 - [EnrollMfaDeviceRequest](docs/EnrollMfaDeviceRequest.md)
 - [EnrollMfaDeviceResponse](docs/EnrollMfaDeviceResponse.md)
 - [EnrolledMfaDevicesResponse](docs/EnrolledMfaDevicesResponse.md)
 - [EnrolledMfaDevicesResponseData](docs/EnrolledMfaDevicesResponseData.md)
 - [Event](docs/Event.md)
 - [EventResponse](docs/EventResponse.md)
 - [EventType](docs/EventType.md)
 - [EventTypesResponse](docs/EventTypesResponse.md)
 - [EventsResponse](docs/EventsResponse.md)
 - [GenerateInviteLinkRequest](docs/GenerateInviteLinkRequest.md)
 - [GenerateMfaTokenRequest](docs/GenerateMfaTokenRequest.md)
 - [GenerateMfaTokenResponse](docs/GenerateMfaTokenResponse.md)
 - [Group](docs/Group.md)
 - [GroupResponse](docs/GroupResponse.md)
 - [GroupsResponse](docs/GroupsResponse.md)
 - [InlineResponse400](docs/InlineResponse400.md)
 - [LockUserRequest](docs/LockUserRequest.md)
 - [LoginVerifyMfaRequest](docs/LoginVerifyMfaRequest.md)
 - [LoginVerifyMfaResponse](docs/LoginVerifyMfaResponse.md)
 - [LoginVerifyMfaResponseData](docs/LoginVerifyMfaResponseData.md)
 - [MfaDevice](docs/MfaDevice.md)
 - [NewCleartextPasswordRequest](docs/NewCleartextPasswordRequest.md)
 - [NewSaltedPasswordRequest](docs/NewSaltedPasswordRequest.md)
 - [Pagination](docs/Pagination.md)
 - [Privilege](docs/Privilege.md)
 - [PrivilegePrivilege](docs/PrivilegePrivilege.md)
 - [PrivilegeRolesResponse](docs/PrivilegeRolesResponse.md)
 - [PrivilegeUsersResponse](docs/PrivilegeUsersResponse.md)
 - [Response](docs/Response.md)
 - [ResponseDevices](docs/ResponseDevices.md)
 - [ResponseUser](docs/ResponseUser.md)
 - [Role](docs/Role.md)
 - [RoleReponse](docs/RoleReponse.md)
 - [RolesResponse](docs/RolesResponse.md)
 - [SamlAssertionRequest](docs/SamlAssertionRequest.md)
 - [SamlAssertionResponse](docs/SamlAssertionResponse.md)
 - [SamlVerifyMfaRequest](docs/SamlVerifyMfaRequest.md)
 - [Scope](docs/Scope.md)
 - [SendInviteLinkRequest](docs/SendInviteLinkRequest.md)
 - [SetUserCustomAttributesRequest](docs/SetUserCustomAttributesRequest.md)
 - [SetUserStateRequest](docs/SetUserStateRequest.md)
 - [Statement](docs/Statement.md)
 - [Status](docs/Status.md)
 - [User](docs/User.md)
 - [UserApp](docs/UserApp.md)
 - [UserAppsResponse](docs/UserAppsResponse.md)
 - [UserLoginRequest](docs/UserLoginRequest.md)
 - [UserLoginResponse](docs/UserLoginResponse.md)
 - [UserMfaFactorsResponse](docs/UserMfaFactorsResponse.md)
 - [UserMfaFactorsResponseData](docs/UserMfaFactorsResponseData.md)
 - [UserMfaFactorsResponseDataAuthFactors](docs/UserMfaFactorsResponseDataAuthFactors.md)
 - [UserRolesResponse](docs/UserRolesResponse.md)
 - [UsersResponse](docs/UsersResponse.md)
 - [VerifyMfaDeviceRequest](docs/VerifyMfaDeviceRequest.md)


## Documentation For Authorization


## application

- **Type**: OAuth
- **Flow**: application
- **Authorization URL**: 
- **Scopes**: N/A


## Author



