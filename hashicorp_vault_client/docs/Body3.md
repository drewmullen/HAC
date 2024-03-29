# Body3

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowed_redirect_uris** | **list[str]** | Comma-separated list of allowed values for redirect_uri | [optional] 
**bound_audiences** | **list[str]** | Comma-separated list of &#x27;aud&#x27; claims that are valid for login; any match is sufficient | [optional] 
**bound_cidrs** | **list[str]** | Use \&quot;token_bound_cidrs\&quot; instead. If this and \&quot;token_bound_cidrs\&quot; are both specified, only \&quot;token_bound_cidrs\&quot; will be used. | [optional] 
**bound_claims** | **object** | Map of claims/values which must match for login | [optional] 
**bound_subject** | **str** | The &#x27;sub&#x27; claim that is valid for login. Optional. | [optional] 
**claim_mappings** | **object** | Mappings of claims (key) that will be copied to a metadata field (value) | [optional] 
**clock_skew_leeway** | **int** | Duration in seconds of leeway when validating all claims to account for clock skew. Defaults to 60 (1 minute) if set to 0 and can be disabled if set to -1. | [optional] 
**expiration_leeway** | **int** | Duration in seconds of leeway when validating expiration of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional] [default to 150]
**groups_claim** | **str** | The claim to use for the Identity group alias names | [optional] 
**max_ttl** | **int** | Use \&quot;token_max_ttl\&quot; instead. If this and \&quot;token_max_ttl\&quot; are both specified, only \&quot;token_max_ttl\&quot; will be used. | [optional] 
**not_before_leeway** | **int** | Duration in seconds of leeway when validating not before values of a token to account for clock skew. Defaults to 150 (2.5 minutes) if set to 0 and can be disabled if set to -1. | [optional] [default to 150]
**num_uses** | **int** | Use \&quot;token_num_uses\&quot; instead. If this and \&quot;token_num_uses\&quot; are both specified, only \&quot;token_num_uses\&quot; will be used. | [optional] 
**oidc_scopes** | **list[str]** | Comma-separated list of OIDC scopes | [optional] 
**period** | **int** | Use \&quot;token_period\&quot; instead. If this and \&quot;token_period\&quot; are both specified, only \&quot;token_period\&quot; will be used. | [optional] 
**policies** | **list[str]** | Use \&quot;token_policies\&quot; instead. If this and \&quot;token_policies\&quot; are both specified, only \&quot;token_policies\&quot; will be used. | [optional] 
**role_type** | **str** | Type of the role, either &#x27;jwt&#x27; or &#x27;oidc&#x27;. | [optional] 
**token_bound_cidrs** | **list[str]** | Comma separated string or JSON list of CIDR blocks. If set, specifies the blocks of IP addresses which are allowed to use the generated token. | [optional] 
**token_explicit_max_ttl** | **int** | If set, tokens created via this role carry an explicit maximum TTL. During renewal, the current maximum TTL values of the role and the mount are not checked for changes, and any updates to these values will have no effect on the token being renewed. | [optional] 
**token_max_ttl** | **int** | The maximum lifetime of the generated token | [optional] 
**token_no_default_policy** | **bool** | If true, the &#x27;default&#x27; policy will not automatically be added to generated tokens | [optional] 
**token_num_uses** | **int** | The maximum number of times a token may be used, a value of zero means unlimited | [optional] 
**token_period** | **int** | If set, tokens created via this role will have no max lifetime; instead, their renewal period will be fixed to this value. This takes an integer number of seconds, or a string duration (e.g. \&quot;24h\&quot;). | [optional] 
**token_policies** | **list[str]** | Comma-separated list of policies | [optional] 
**token_ttl** | **int** | The initial ttl of the token to generate | [optional] 
**token_type** | **str** | The type of token to generate, service or batch | [optional] [default to 'default-service']
**ttl** | **int** | Use \&quot;token_ttl\&quot; instead. If this and \&quot;token_ttl\&quot; are both specified, only \&quot;token_ttl\&quot; will be used. | [optional] 
**user_claim** | **str** | The claim to use for the Identity entity alias name | [optional] 
**verbose_oidc_logging** | **bool** | Log received OIDC tokens and claims when debug-level logging is active. Not recommended in production since sensitive information may be present in OIDC responses. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

