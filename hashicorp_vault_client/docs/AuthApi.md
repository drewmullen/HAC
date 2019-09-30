# hashicorp_vault_client.AuthApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_auth_oidc_role_name**](AuthApi.md#delete_auth_oidc_role_name) | **DELETE** /auth/oidc/role/{name} | Delete an existing role.
[**delete_auth_token_roles_role_name**](AuthApi.md#delete_auth_token_roles_role_name) | **DELETE** /auth/token/roles/{role_name} | 
[**get_auth_oidc_config**](AuthApi.md#get_auth_oidc_config) | **GET** /auth/oidc/config | Read the current JWT authentication backend configuration.
[**get_auth_oidc_oidc_callback**](AuthApi.md#get_auth_oidc_oidc_callback) | **GET** /auth/oidc/oidc/callback | Callback endpoint to complete an OIDC login.
[**get_auth_oidc_role**](AuthApi.md#get_auth_oidc_role) | **GET** /auth/oidc/role | Lists all the roles registered with the backend.
[**get_auth_oidc_role_name**](AuthApi.md#get_auth_oidc_role_name) | **GET** /auth/oidc/role/{name} | Read an existing role.
[**get_auth_token_accessors**](AuthApi.md#get_auth_token_accessors) | **GET** /auth/token/accessors/ | List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires &#x27;sudo&#x27; capability in addition to &#x27;list&#x27;.
[**get_auth_token_lookup**](AuthApi.md#get_auth_token_lookup) | **GET** /auth/token/lookup | This endpoint will lookup a token and its properties.
[**get_auth_token_lookup_self**](AuthApi.md#get_auth_token_lookup_self) | **GET** /auth/token/lookup-self | This endpoint will lookup a token and its properties.
[**get_auth_token_roles**](AuthApi.md#get_auth_token_roles) | **GET** /auth/token/roles | This endpoint lists configured roles.
[**get_auth_token_roles_role_name**](AuthApi.md#get_auth_token_roles_role_name) | **GET** /auth/token/roles/{role_name} | 
[**post_auth_oidc_config**](AuthApi.md#post_auth_oidc_config) | **POST** /auth/oidc/config | Configure the JWT authentication backend.
[**post_auth_oidc_login**](AuthApi.md#post_auth_oidc_login) | **POST** /auth/oidc/login | Authenticates to Vault using a JWT (or OIDC) token.
[**post_auth_oidc_oidc_auth_url**](AuthApi.md#post_auth_oidc_oidc_auth_url) | **POST** /auth/oidc/oidc/auth_url | Request an authorization URL to start an OIDC login flow.
[**post_auth_oidc_role_name**](AuthApi.md#post_auth_oidc_role_name) | **POST** /auth/oidc/role/{name} | Register an role with the backend.
[**post_auth_token_create**](AuthApi.md#post_auth_token_create) | **POST** /auth/token/create | The token create path is used to create new tokens.
[**post_auth_token_create_orphan**](AuthApi.md#post_auth_token_create_orphan) | **POST** /auth/token/create-orphan | The token create path is used to create new orphan tokens.
[**post_auth_token_create_role_name**](AuthApi.md#post_auth_token_create_role_name) | **POST** /auth/token/create/{role_name} | This token create path is used to create new tokens adhering to the given role.
[**post_auth_token_lookup**](AuthApi.md#post_auth_token_lookup) | **POST** /auth/token/lookup | This endpoint will lookup a token and its properties.
[**post_auth_token_lookup_accessor**](AuthApi.md#post_auth_token_lookup_accessor) | **POST** /auth/token/lookup-accessor | This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.
[**post_auth_token_lookup_self**](AuthApi.md#post_auth_token_lookup_self) | **POST** /auth/token/lookup-self | This endpoint will lookup a token and its properties.
[**post_auth_token_renew**](AuthApi.md#post_auth_token_renew) | **POST** /auth/token/renew | This endpoint will renew the given token and prevent expiration.
[**post_auth_token_renew_self**](AuthApi.md#post_auth_token_renew_self) | **POST** /auth/token/renew-self | This endpoint will renew the token used to call it and prevent expiration.
[**post_auth_token_revoke**](AuthApi.md#post_auth_token_revoke) | **POST** /auth/token/revoke | This endpoint will delete the given token and all of its child tokens.
[**post_auth_token_revoke_accessor**](AuthApi.md#post_auth_token_revoke_accessor) | **POST** /auth/token/revoke-accessor | This endpoint will delete the token associated with the accessor and all of its child tokens.
[**post_auth_token_revoke_orphan**](AuthApi.md#post_auth_token_revoke_orphan) | **POST** /auth/token/revoke-orphan | This endpoint will delete the token and orphan its child tokens.
[**post_auth_token_revoke_self**](AuthApi.md#post_auth_token_revoke_self) | **POST** /auth/token/revoke-self | This endpoint will delete the token used to call it and all of its child tokens.
[**post_auth_token_roles_role_name**](AuthApi.md#post_auth_token_roles_role_name) | **POST** /auth/token/roles/{role_name} | 
[**post_auth_token_tidy**](AuthApi.md#post_auth_token_tidy) | **POST** /auth/token/tidy | This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.

# **delete_auth_oidc_role_name**
> delete_auth_oidc_role_name(name)

Delete an existing role.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
name = 'name_example' # str | Name of the role.

try:
    # Delete an existing role.
    api_instance.delete_auth_oidc_role_name(name)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_auth_token_roles_role_name**
> delete_auth_token_roles_role_name(role_name)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
role_name = 'role_name_example' # str | Name of the role

try:
    api_instance.delete_auth_token_roles_role_name(role_name)
except ApiException as e:
    print("Exception when calling AuthApi->delete_auth_token_roles_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_oidc_config**
> get_auth_oidc_config()

Read the current JWT authentication backend configuration.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # Read the current JWT authentication backend configuration.
    api_instance.get_auth_oidc_config()
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_oidc_config: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_oidc_oidc_callback**
> get_auth_oidc_oidc_callback()

Callback endpoint to complete an OIDC login.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # Callback endpoint to complete an OIDC login.
    api_instance.get_auth_oidc_oidc_callback()
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_oidc_oidc_callback: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_oidc_role**
> get_auth_oidc_role(list=list)

Lists all the roles registered with the backend.

The list will contain the names of the roles.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Lists all the roles registered with the backend.
    api_instance.get_auth_oidc_role(list=list)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_oidc_role: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_oidc_role_name**
> get_auth_oidc_role_name(name)

Read an existing role.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
name = 'name_example' # str | Name of the role.

try:
    # Read an existing role.
    api_instance.get_auth_oidc_role_name(name)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_token_accessors**
> get_auth_token_accessors(list=list)

List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List token accessors, which can then be be used to iterate and discover their properties or revoke them. Because this can be used to cause a denial of service, this endpoint requires 'sudo' capability in addition to 'list'.
    api_instance.get_auth_token_accessors(list=list)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_token_accessors: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_token_lookup**
> get_auth_token_lookup()

This endpoint will lookup a token and its properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # This endpoint will lookup a token and its properties.
    api_instance.get_auth_token_lookup()
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_token_lookup: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_token_lookup_self**
> get_auth_token_lookup_self()

This endpoint will lookup a token and its properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # This endpoint will lookup a token and its properties.
    api_instance.get_auth_token_lookup_self()
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_token_lookup_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_token_roles**
> get_auth_token_roles(list=list)

This endpoint lists configured roles.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # This endpoint lists configured roles.
    api_instance.get_auth_token_roles(list=list)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_token_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_token_roles_role_name**
> get_auth_token_roles_role_name(role_name)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
role_name = 'role_name_example' # str | Name of the role

try:
    api_instance.get_auth_token_roles_role_name(role_name)
except ApiException as e:
    print("Exception when calling AuthApi->get_auth_token_roles_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_oidc_config**
> post_auth_oidc_config(body=body)

Configure the JWT authentication backend.

The JWT authentication backend validates JWTs (or OIDC) using the configured credentials. If using OIDC Discovery, the URL must be provided, along with (optionally) the CA cert to use for the connection. If performing JWT validation locally, a set of public keys must be provided.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body() # Body |  (optional)

try:
    # Configure the JWT authentication backend.
    api_instance.post_auth_oidc_config(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_oidc_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body**](Body.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_oidc_login**
> post_auth_oidc_login(body=body)

Authenticates to Vault using a JWT (or OIDC) token.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body1() # Body1 |  (optional)

try:
    # Authenticates to Vault using a JWT (or OIDC) token.
    api_instance.post_auth_oidc_login(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_oidc_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body1**](Body1.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_oidc_oidc_auth_url**
> post_auth_oidc_oidc_auth_url(body=body)

Request an authorization URL to start an OIDC login flow.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body2() # Body2 |  (optional)

try:
    # Request an authorization URL to start an OIDC login flow.
    api_instance.post_auth_oidc_oidc_auth_url(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_oidc_oidc_auth_url: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body2**](Body2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_oidc_role_name**
> post_auth_oidc_role_name(name, body=body)

Register an role with the backend.

A role is required to authenticate with this backend. The role binds   JWT token information with token policies and settings.   The bindings, token polices and token settings can all be configured   using this endpoint

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
name = 'name_example' # str | Name of the role.
body = hashicorp_vault_client.Body3() # Body3 |  (optional)

try:
    # Register an role with the backend.
    api_instance.post_auth_oidc_role_name(name, body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role. | 
 **body** | [**Body3**](Body3.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_create**
> post_auth_token_create()

The token create path is used to create new tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # The token create path is used to create new tokens.
    api_instance.post_auth_token_create()
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_create: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_create_orphan**
> post_auth_token_create_orphan()

The token create path is used to create new orphan tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # The token create path is used to create new orphan tokens.
    api_instance.post_auth_token_create_orphan()
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_create_orphan: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_create_role_name**
> post_auth_token_create_role_name(role_name)

This token create path is used to create new tokens adhering to the given role.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
role_name = 'role_name_example' # str | Name of the role

try:
    # This token create path is used to create new tokens adhering to the given role.
    api_instance.post_auth_token_create_role_name(role_name)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_create_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_lookup**
> post_auth_token_lookup(body=body)

This endpoint will lookup a token and its properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body4() # Body4 |  (optional)

try:
    # This endpoint will lookup a token and its properties.
    api_instance.post_auth_token_lookup(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body4**](Body4.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_lookup_accessor**
> post_auth_token_lookup_accessor(body=body)

This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body5() # Body5 |  (optional)

try:
    # This endpoint will lookup a token associated with the given accessor and its properties. Response will not contain the token ID.
    api_instance.post_auth_token_lookup_accessor(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_lookup_accessor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body5**](Body5.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_lookup_self**
> post_auth_token_lookup_self(body=body)

This endpoint will lookup a token and its properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body6() # Body6 |  (optional)

try:
    # This endpoint will lookup a token and its properties.
    api_instance.post_auth_token_lookup_self(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_lookup_self: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body6**](Body6.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_renew**
> post_auth_token_renew(body=body)

This endpoint will renew the given token and prevent expiration.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body7() # Body7 |  (optional)

try:
    # This endpoint will renew the given token and prevent expiration.
    api_instance.post_auth_token_renew(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_renew: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body7**](Body7.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_renew_self**
> post_auth_token_renew_self(body=body)

This endpoint will renew the token used to call it and prevent expiration.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body8() # Body8 |  (optional)

try:
    # This endpoint will renew the token used to call it and prevent expiration.
    api_instance.post_auth_token_renew_self(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_renew_self: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body8**](Body8.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_revoke**
> post_auth_token_revoke(body=body)

This endpoint will delete the given token and all of its child tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body9() # Body9 |  (optional)

try:
    # This endpoint will delete the given token and all of its child tokens.
    api_instance.post_auth_token_revoke(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_revoke: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body9**](Body9.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_revoke_accessor**
> post_auth_token_revoke_accessor(body=body)

This endpoint will delete the token associated with the accessor and all of its child tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body10() # Body10 |  (optional)

try:
    # This endpoint will delete the token associated with the accessor and all of its child tokens.
    api_instance.post_auth_token_revoke_accessor(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_revoke_accessor: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body10**](Body10.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_revoke_orphan**
> post_auth_token_revoke_orphan(body=body)

This endpoint will delete the token and orphan its child tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
body = hashicorp_vault_client.Body11() # Body11 |  (optional)

try:
    # This endpoint will delete the token and orphan its child tokens.
    api_instance.post_auth_token_revoke_orphan(body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_revoke_orphan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body11**](Body11.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_revoke_self**
> post_auth_token_revoke_self()

This endpoint will delete the token used to call it and all of its child tokens.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # This endpoint will delete the token used to call it and all of its child tokens.
    api_instance.post_auth_token_revoke_self()
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_revoke_self: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_roles_role_name**
> post_auth_token_roles_role_name(role_name, body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()
role_name = 'role_name_example' # str | Name of the role
body = hashicorp_vault_client.Body12() # Body12 |  (optional)

try:
    api_instance.post_auth_token_roles_role_name(role_name, body=body)
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_roles_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **role_name** | **str**| Name of the role | 
 **body** | [**Body12**](Body12.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_auth_token_tidy**
> post_auth_token_tidy()

This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.AuthApi()

try:
    # This endpoint performs cleanup tasks that can be run if certain error conditions have occurred.
    api_instance.post_auth_token_tidy()
except ApiException as e:
    print("Exception when calling AuthApi->post_auth_token_tidy: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

