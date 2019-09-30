# Body71

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **object** | Configuration for this mount, such as default_lease_ttl and max_lease_ttl. | [optional] 
**description** | **str** | User-friendly description for this mount. | [optional] 
**local** | **bool** | Mark the mount as a local mount, which is not replicated and is unaffected by replication. | [optional] [default to False]
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**plugin_name** | **str** | Name of the plugin to mount based from the name registered in the plugin catalog. | [optional] 
**seal_wrap** | **bool** | Whether to turn on seal wrapping for the mount. | [optional] [default to False]
**type** | **str** | The type of the backend. Example: \&quot;passthrough\&quot; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

