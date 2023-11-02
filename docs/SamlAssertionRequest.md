# SamlAssertionRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username_or_email** | **str** | Set to the username or email of the user that you want to log in. | 
**password** | **str** | Set to the password of the user that you want to log in. | 
**subdomain** | **str** | Set to the subdomain of the user that you want to log in. | 
**app_id** | **int** | App ID of the app for which you want to generate a SAML token. This is the app ID in OneLogin. | 
**ip_address** | **str** | If you are using this API in a scenario in which MFA is required and you’ll need to be able to honor IP address whitelisting defined in MFA policies, provide this parameter and set its value to the whitelisted IP address that needs to be bypassed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


