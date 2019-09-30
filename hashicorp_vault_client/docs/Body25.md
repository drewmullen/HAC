# Body25

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | ID of the group. If set, updates the corresponding existing group. | [optional] 
**member_entity_ids** | **list[str]** | Entity IDs to be assigned as group members. | [optional] 
**member_group_ids** | **list[str]** | Group IDs to be assigned as group members. | [optional] 
**metadata** | **object** | Metadata to be associated with the group. In CLI, this parameter can be repeated multiple times, and it all gets merged together. For example: vault &lt;command&gt; &lt;path&gt; metadata&#x3D;key1&#x3D;value1 metadata&#x3D;key2&#x3D;value2 | [optional] 
**policies** | **list[str]** | Policies to be tied to the group. | [optional] 
**type** | **str** | Type of the group, &#x27;internal&#x27; or &#x27;external&#x27;. Defaults to &#x27;internal&#x27; | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

