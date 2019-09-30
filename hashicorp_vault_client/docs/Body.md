# Body

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bound_issuer** | **str** | The value against which to match the &#x27;iss&#x27; claim in a JWT. Optional. | [optional] 
**default_role** | **str** | The default role to use if none is provided during login. If not set, a role is required during login. | [optional] 
**jwks_ca_pem** | **str** | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the JWKS URL. If not set, system certificates are used. | [optional] 
**jwks_url** | **str** | JWKS URL to use to authenticate signatures. Cannot be used with \&quot;oidc_discovery_url\&quot; or \&quot;jwt_validation_pubkeys\&quot;. | [optional] 
**jwt_supported_algs** | **list[str]** | A list of supported signing algorithms. Defaults to RS256. | [optional] 
**jwt_validation_pubkeys** | **list[str]** | A list of PEM-encoded public keys to use to authenticate signatures locally. Cannot be used with \&quot;jwks_url\&quot; or \&quot;oidc_discovery_url\&quot;. | [optional] 
**oidc_client_id** | **str** | The OAuth Client ID configured with your OIDC provider. | [optional] 
**oidc_client_secret** | **str** | The OAuth Client Secret configured with your OIDC provider. | [optional] 
**oidc_discovery_ca_pem** | **str** | The CA certificate or chain of certificates, in PEM format, to use to validate connections to the OIDC Discovery URL. If not set, system certificates are used. | [optional] 
**oidc_discovery_url** | **str** | OIDC Discovery URL, without any .well-known component (base path). Cannot be used with \&quot;jwks_url\&quot; or \&quot;jwt_validation_pubkeys\&quot;. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

