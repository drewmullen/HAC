# Body65

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_hostname** | **str** | API host name for Duo. | [optional] 
**integration_key** | **str** | Integration key for Duo. | [optional] 
**mount_accessor** | **str** | The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping. | [optional] 
**push_info** | **str** | Push information for Duo. | [optional] 
**secret_key** | **str** | Secret key for Duo. | [optional] 
**username_format** | **str** | A format string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \&quot;{{alias.name}}@example.com\&quot;. Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias&#x27;s name field will be used as-is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

