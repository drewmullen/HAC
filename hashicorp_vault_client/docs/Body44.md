# Body44

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_response_headers** | **list[str]** | A list of headers to whitelist and allow a plugin to set on responses. | [optional] 
**audit_non_hmac_request_keys** | **list[str]** | The list of keys in the request data object that will not be HMAC&#x27;ed by audit devices. | [optional] 
**audit_non_hmac_response_keys** | **list[str]** | The list of keys in the response data object that will not be HMAC&#x27;ed by audit devices. | [optional] 
**default_lease_ttl** | **str** | The default lease TTL for this mount. | [optional] 
**description** | **str** | User-friendly description for this credential backend. | [optional] 
**listing_visibility** | **str** | Determines the visibility of the mount in the UI-specific listing endpoint. Accepted value are &#x27;unauth&#x27; and &#x27;&#x27;. | [optional] 
**max_lease_ttl** | **str** | The max lease TTL for this mount. | [optional] 
**options** | **object** | The options to pass into the backend. Should be a json object with string keys and values. | [optional] 
**passthrough_request_headers** | **list[str]** | A list of headers to whitelist and pass from the request to the plugin. | [optional] 
**token_type** | **str** | The type of token to issue (service or batch). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

