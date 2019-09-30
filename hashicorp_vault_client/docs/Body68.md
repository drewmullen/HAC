# Body68

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | The hashing algorithm used to generate the TOTP token. Options include SHA1, SHA256 and SHA512. | [optional] [default to 'SHA1']
**digits** | **int** | The number of digits in the generated TOTP token. This value can either be 6 or 8. | [optional] [default to 6]
**issuer** | **str** | The name of the key&#x27;s issuing organization. | [optional] 
**key_size** | **int** | Determines the size in bytes of the generated key. | [optional] [default to 20]
**period** | **int** | The length of time used to generate a counter for the TOTP token calculation. | [optional] [default to 30]
**qr_size** | **int** | The pixel size of the generated square QR code. | [optional] [default to 200]
**skew** | **int** | The number of delay periods that are allowed when validating a TOTP token. This value can either be 0 or 1. | [optional] [default to 1]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

