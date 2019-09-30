# Body66

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_token** | **str** | Okta API key. | [optional] 
**base_url** | **str** | The base domain to use for the Okta API. When not specified in the configuration, \&quot;okta.com\&quot; is used. | [optional] 
**mount_accessor** | **str** | The mount to tie this method to for use in automatic mappings. The mapping will use the Name field of Aliases associated with this mount as the username in the mapping. | [optional] 
**org_name** | **str** | Name of the organization to be used in the Okta API. | [optional] 
**primary_email** | **bool** | If true, the username will only match the primary email for the account. Defaults to false. | [optional] 
**production** | **bool** | (DEPRECATED) Use base_url instead. | [optional] 
**username_format** | **str** | A format string for mapping Identity names to MFA method names. Values to subtitute should be placed in {{}}. For example, \&quot;{{alias.name}}@example.com\&quot;. Currently-supported mappings: alias.name: The name returned by the mount configured via the mount_accessor parameter If blank, the Alias&#x27;s name field will be used as-is. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

