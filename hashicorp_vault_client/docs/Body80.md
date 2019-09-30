# Body80

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **bool** | Specifies if using PGP-encrypted keys, whether Vault should also store a plaintext backup of the PGP-encrypted keys. | [optional] 
**pgp_keys** | **list[str]** | Specifies an array of PGP public keys used to encrypt the output unseal keys. Ordering is preserved. The keys must be base64-encoded from their original binary representation. The size of this array must be the same as secret_shares. | [optional] 
**require_verification** | **bool** | Turns on verification functionality | [optional] 
**secret_shares** | **int** | Specifies the number of shares to split the master key into. | [optional] 
**secret_threshold** | **int** | Specifies the number of shares required to reconstruct the master key. This must be less than or equal secret_shares. If using Vault HSM with auto-unsealing, this value must be the same as secret_shares. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

