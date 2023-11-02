# VerifyMfaDeviceRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**otp_token** | **int** | OTP code provided by the device or SMS message sent to user. | [optional] 
**state_token** | **str** | The state_token is returned after a successful request to Enroll a Factor or Activate a Factor. The state_token MUST be provided if the needs_trigger attribute from the proceeding calls is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


