# Body30

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**algorithm** | **str** | Signing algorithm to use. This will default to RS256. | [optional] [default to 'RS256']
**allowed_client_ids** | **list[str]** | Comma separated string or array of role client ids allowed to use this key for signing. If empty no roles are allowed. If \&quot;*\&quot; all roles are allowed. | [optional] 
**rotation_period** | **int** | How often to generate a new keypair. | [optional] 
**verification_ttl** | **int** | Controls how long the public portion of a key will be available for verification after being rotated. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

