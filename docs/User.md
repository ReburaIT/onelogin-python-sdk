# User

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | User’s unique ID in OneLogin | [optional] 
**email** | **str** | User’s email address, which he also uses to log in to OneLogin | 
**username** | **str** | If the user’s directory is set to authenticate using a user name value, this is the value used to sign in | 
**firstname** | **str** | User’s first name | 
**lastname** | **str** | User’s last name | 
**group_id** | **int** | Group to which the user belongs | [optional] 
**invalid_login_attempts** | **int** | Number of sequential invalid login attempts the user has made that is less than or equal to the Maximum invalid login attempts value defined on the Session page in OneLogin. When this number reaches this value, the user account will be locked for the amount of time defined by the Lock effective period field on the Session page and this value will be reset to 0. | [optional] 
**activated_at** | **datetime** | Date and time at which the user’s status was set to 1 (active)       | [optional] 
**created_at** | **datetime** | Date and time at which the user was created  | [optional] 
**updated_at** | **datetime** | Date and time at which the user’s information was last updated | [optional] 
**invitation_sent_at** | **datetime** | Date and time at which an invitation to OneLogin was sent to the user  | [optional] 
**password_changed_at** | **datetime** | Date and time at which the user’s password was last changed | [optional] 
**last_login** | **datetime** | Date and time of the user’s last login  | [optional] 
**locked_until** | **datetime** | Date and time at which the user’s account will be unlocked  | [optional] 
**notes** | **str** |  | [optional] 
**openid_name** | **str** | OpenID URL that can be configured in other applications that accept OpenID for sign-in | [optional] 
**locale_code** | **str** | Represents a geographical, political, or cultural region. Some features may use the locale value to tailor the display of information, such as numbers, for the user based on locale-specific customs and conventions | [optional] 
**phone** | **str** | User’s phone number | [optional] 
**status** | **int** | Determines the user’s ability to log in to OneLogin    Possible values      0 - Unactivated   1 - Active Only users assigned this status can log in to OneLogin.   2 - Suspended   3 - Locked   4 - Password expired   5 - Awaiting password reset | [optional] 
**state** | **int** | Represents the user’s stage in a process (such as user account approval). User state determines the possible statuses a user account can be in. States include 0 - Unapproved 1 - Approved 2 - Rejected 3 - Unlicensed | [optional] 
**distinguished_name** | **str** | Synchronized from Active Directory | [optional] 
**external_id** | **str** | External ID that can be used to uniquely identify the user in another system | [optional] 
**directory_id** | **int** | ID of the directory (Active Directory, LDAP, for example) from which the user was created | [optional] 
**member_of** | **str** | Synchronized from Active Directory | [optional] 
**samaccountname** | **str** | Synchronized from Active Directory | [optional] 
**userprincipalname** | **str** | Synchronized from Active Directory | [optional] 
**manager_ad_id** | **str** | ID of the user’s manager in Active Directory | [optional] 
**role_id** | **list[int]** | Role IDs to which the user is assigned | [optional] 
**custom_attributes** | **dict(str, str)** | Provides a list of custom attribute fields (also known as custom user fields) that are available for your account. The values returned correspond to the values you provided in the Shortname field when you defined the custom user field | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


