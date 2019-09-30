# Body39

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cas_required** | **bool** | If true the key will require the cas parameter to be set on all write requests. If false, the backend’s configuration will be used. | [optional] 
**delete_version_after** | **int** | The length of time before a version is deleted. If not set, the backend&#x27;s configured delete_version_after is used. Cannot be greater than the backend&#x27;s delete_version_after. A zero duration clears the current setting. A negative duration will cause an error. | [optional] 
**max_versions** | **int** | The number of versions to keep. If not set, the backend’s configured max version is used. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

