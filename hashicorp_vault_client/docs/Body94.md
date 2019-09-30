# Body94

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ca_file** | **str** | A path to a file containing a PEM-encoded CA certificate to verify the call against the primary&#x27;s API address | [optional] 
**ca_path** | **str** | A path to a directory containing PEM-encoded CA certificates to verify the call against the primary&#x27;s API address | [optional] 
**client_cert_pem** | **str** | The client certificate to use for authentication, in PEM format. Note: client authentication for this operation will always use TLS 1.2 or higher. | [optional] 
**client_key_pem** | **str** | The client key to use for authentication, in PEM format. | [optional] 
**dr_operation_token** | **str** | DR operation token used to authorize this request. | [optional] 
**primary_api_addr** | **str** | The API address of the primary. If not set, the value the primary supplies in the token will be used, which is the primary&#x27;s redirect address. | [optional] 
**token** | **str** | The token given by the primary to activate secondary status for this cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

