# LoginVerifyMfaRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_id** | **int** | Provide the MFA device_id you are submitting for verification. | 
**state_token** | **str** | Provide the state_token associated with the MFA device_id you are submitting for verification. | 
**otp_token** | **str** | Provide the OTP value for the MFA factor you are submitting for verification. | [optional] 
**do_not_notify** | **bool** | When verifying MFA via Protect Push, set this to true to stop additional push notifications being sent to the OneLogin Protect device. | [optional] [default to False]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


