# hashicorp_vault_client.IdentityApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_identity_alias_id_id**](IdentityApi.md#delete_identity_alias_id_id) | **DELETE** /identity/alias/id/{id} | Update, read or delete an alias ID.
[**delete_identity_entity_alias_id_id**](IdentityApi.md#delete_identity_entity_alias_id_id) | **DELETE** /identity/entity-alias/id/{id} | Update, read or delete an alias ID.
[**delete_identity_entity_id_id**](IdentityApi.md#delete_identity_entity_id_id) | **DELETE** /identity/entity/id/{id} | Update, read or delete an entity using entity ID
[**delete_identity_entity_name_name**](IdentityApi.md#delete_identity_entity_name_name) | **DELETE** /identity/entity/name/{name} | Update, read or delete an entity using entity name
[**delete_identity_group_alias_id_id**](IdentityApi.md#delete_identity_group_alias_id_id) | **DELETE** /identity/group-alias/id/{id} | 
[**delete_identity_group_id_id**](IdentityApi.md#delete_identity_group_id_id) | **DELETE** /identity/group/id/{id} | Update or delete an existing group using its ID.
[**delete_identity_group_name_name**](IdentityApi.md#delete_identity_group_name_name) | **DELETE** /identity/group/name/{name} | 
[**delete_identity_oidc_key_name**](IdentityApi.md#delete_identity_oidc_key_name) | **DELETE** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**delete_identity_oidc_role_name**](IdentityApi.md#delete_identity_oidc_role_name) | **DELETE** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**delete_identity_persona_id_id**](IdentityApi.md#delete_identity_persona_id_id) | **DELETE** /identity/persona/id/{id} | Update, read or delete an alias ID.
[**get_identity_alias_id**](IdentityApi.md#get_identity_alias_id) | **GET** /identity/alias/id | List all the alias IDs.
[**get_identity_alias_id_id**](IdentityApi.md#get_identity_alias_id_id) | **GET** /identity/alias/id/{id} | Update, read or delete an alias ID.
[**get_identity_entity_alias_id**](IdentityApi.md#get_identity_entity_alias_id) | **GET** /identity/entity-alias/id | List all the alias IDs.
[**get_identity_entity_alias_id_id**](IdentityApi.md#get_identity_entity_alias_id_id) | **GET** /identity/entity-alias/id/{id} | Update, read or delete an alias ID.
[**get_identity_entity_id**](IdentityApi.md#get_identity_entity_id) | **GET** /identity/entity/id | List all the entity IDs
[**get_identity_entity_id_id**](IdentityApi.md#get_identity_entity_id_id) | **GET** /identity/entity/id/{id} | Update, read or delete an entity using entity ID
[**get_identity_entity_name**](IdentityApi.md#get_identity_entity_name) | **GET** /identity/entity/name | List all the entity names
[**get_identity_entity_name_name**](IdentityApi.md#get_identity_entity_name_name) | **GET** /identity/entity/name/{name} | Update, read or delete an entity using entity name
[**get_identity_group_alias_id**](IdentityApi.md#get_identity_group_alias_id) | **GET** /identity/group-alias/id | List all the group alias IDs.
[**get_identity_group_alias_id_id**](IdentityApi.md#get_identity_group_alias_id_id) | **GET** /identity/group-alias/id/{id} | 
[**get_identity_group_id**](IdentityApi.md#get_identity_group_id) | **GET** /identity/group/id | List all the group IDs.
[**get_identity_group_id_id**](IdentityApi.md#get_identity_group_id_id) | **GET** /identity/group/id/{id} | Update or delete an existing group using its ID.
[**get_identity_group_name**](IdentityApi.md#get_identity_group_name) | **GET** /identity/group/name | 
[**get_identity_group_name_name**](IdentityApi.md#get_identity_group_name_name) | **GET** /identity/group/name/{name} | 
[**get_identity_oidc_config**](IdentityApi.md#get_identity_oidc_config) | **GET** /identity/oidc/config | OIDC configuration
[**get_identity_oidc_key**](IdentityApi.md#get_identity_oidc_key) | **GET** /identity/oidc/key | List OIDC keys
[**get_identity_oidc_key_name**](IdentityApi.md#get_identity_oidc_key_name) | **GET** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**get_identity_oidc_role**](IdentityApi.md#get_identity_oidc_role) | **GET** /identity/oidc/role | List configured OIDC roles
[**get_identity_oidc_role_name**](IdentityApi.md#get_identity_oidc_role_name) | **GET** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**get_identity_oidc_token_name**](IdentityApi.md#get_identity_oidc_token_name) | **GET** /identity/oidc/token/{name} | Generate an OIDC token
[**get_identity_oidc_well_known_keys**](IdentityApi.md#get_identity_oidc_well_known_keys) | **GET** /identity/oidc/.well-known/keys | Retrieve public keys
[**get_identity_oidc_well_known_openid_configuration**](IdentityApi.md#get_identity_oidc_well_known_openid_configuration) | **GET** /identity/oidc/.well-known/openid-configuration | Query OIDC configurations
[**get_identity_persona_id**](IdentityApi.md#get_identity_persona_id) | **GET** /identity/persona/id | List all the alias IDs.
[**get_identity_persona_id_id**](IdentityApi.md#get_identity_persona_id_id) | **GET** /identity/persona/id/{id} | Update, read or delete an alias ID.
[**post_identity_alias**](IdentityApi.md#post_identity_alias) | **POST** /identity/alias | Create a new alias.
[**post_identity_alias_id_id**](IdentityApi.md#post_identity_alias_id_id) | **POST** /identity/alias/id/{id} | Update, read or delete an alias ID.
[**post_identity_entity**](IdentityApi.md#post_identity_entity) | **POST** /identity/entity | Create a new entity
[**post_identity_entity_alias**](IdentityApi.md#post_identity_entity_alias) | **POST** /identity/entity-alias | Create a new alias.
[**post_identity_entity_alias_id_id**](IdentityApi.md#post_identity_entity_alias_id_id) | **POST** /identity/entity-alias/id/{id} | Update, read or delete an alias ID.
[**post_identity_entity_id_id**](IdentityApi.md#post_identity_entity_id_id) | **POST** /identity/entity/id/{id} | Update, read or delete an entity using entity ID
[**post_identity_entity_merge**](IdentityApi.md#post_identity_entity_merge) | **POST** /identity/entity/merge | Merge two or more entities together
[**post_identity_entity_name_name**](IdentityApi.md#post_identity_entity_name_name) | **POST** /identity/entity/name/{name} | Update, read or delete an entity using entity name
[**post_identity_group**](IdentityApi.md#post_identity_group) | **POST** /identity/group | Create a new group.
[**post_identity_group_alias**](IdentityApi.md#post_identity_group_alias) | **POST** /identity/group-alias | Creates a new group alias, or updates an existing one.
[**post_identity_group_alias_id_id**](IdentityApi.md#post_identity_group_alias_id_id) | **POST** /identity/group-alias/id/{id} | 
[**post_identity_group_id_id**](IdentityApi.md#post_identity_group_id_id) | **POST** /identity/group/id/{id} | Update or delete an existing group using its ID.
[**post_identity_group_name_name**](IdentityApi.md#post_identity_group_name_name) | **POST** /identity/group/name/{name} | 
[**post_identity_lookup_entity**](IdentityApi.md#post_identity_lookup_entity) | **POST** /identity/lookup/entity | Query entities based on various properties.
[**post_identity_lookup_group**](IdentityApi.md#post_identity_lookup_group) | **POST** /identity/lookup/group | Query groups based on various properties.
[**post_identity_oidc_config**](IdentityApi.md#post_identity_oidc_config) | **POST** /identity/oidc/config | OIDC configuration
[**post_identity_oidc_introspect**](IdentityApi.md#post_identity_oidc_introspect) | **POST** /identity/oidc/introspect | Verify the authenticity of an OIDC token
[**post_identity_oidc_key_name**](IdentityApi.md#post_identity_oidc_key_name) | **POST** /identity/oidc/key/{name} | CRUD operations for OIDC keys.
[**post_identity_oidc_key_name_rotate**](IdentityApi.md#post_identity_oidc_key_name_rotate) | **POST** /identity/oidc/key/{name}/rotate | Rotate a named OIDC key.
[**post_identity_oidc_role_name**](IdentityApi.md#post_identity_oidc_role_name) | **POST** /identity/oidc/role/{name} | CRUD operations on OIDC Roles
[**post_identity_persona**](IdentityApi.md#post_identity_persona) | **POST** /identity/persona | Create a new alias.
[**post_identity_persona_id_id**](IdentityApi.md#post_identity_persona_id_id) | **POST** /identity/persona/id/{id} | Update, read or delete an alias ID.

# **delete_identity_alias_id_id**
> delete_identity_alias_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias

try:
    # Update, read or delete an alias ID.
    api_instance.delete_identity_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_entity_alias_id_id**
> delete_identity_entity_alias_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias

try:
    # Update, read or delete an alias ID.
    api_instance.delete_identity_entity_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_entity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_entity_id_id**
> delete_identity_entity_id_id(id)

Update, read or delete an entity using entity ID

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.

try:
    # Update, read or delete an entity using entity ID
    api_instance.delete_identity_entity_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_entity_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_entity_name_name**
> delete_identity_entity_name_name(name)

Update, read or delete an entity using entity name

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the entity

try:
    # Update, read or delete an entity using entity name
    api_instance.delete_identity_entity_name_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_entity_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_group_alias_id_id**
> delete_identity_group_alias_id_id(id)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group alias.

try:
    api_instance.delete_identity_group_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_group_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_group_id_id**
> delete_identity_group_id_id(id)

Update or delete an existing group using its ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.

try:
    # Update or delete an existing group using its ID.
    api_instance.delete_identity_group_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_group_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_group_name_name**
> delete_identity_group_name_name(name)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the group.

try:
    api_instance.delete_identity_group_name_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_group_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_oidc_key_name**
> delete_identity_oidc_key_name(name)

CRUD operations for OIDC keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the key

try:
    # CRUD operations for OIDC keys.
    api_instance.delete_identity_oidc_key_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_oidc_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_oidc_role_name**
> delete_identity_oidc_role_name(name)

CRUD operations on OIDC Roles

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the role

try:
    # CRUD operations on OIDC Roles
    api_instance.delete_identity_oidc_role_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_identity_persona_id_id**
> delete_identity_persona_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the persona

try:
    # Update, read or delete an alias ID.
    api_instance.delete_identity_persona_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->delete_identity_persona_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_alias_id**
> get_identity_alias_id(list=list)

List all the alias IDs.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the alias IDs.
    api_instance.get_identity_alias_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_alias_id: %s\n" % e)
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

# **get_identity_alias_id_id**
> get_identity_alias_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias

try:
    # Update, read or delete an alias ID.
    api_instance.get_identity_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_entity_alias_id**
> get_identity_entity_alias_id(list=list)

List all the alias IDs.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the alias IDs.
    api_instance.get_identity_entity_alias_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_alias_id: %s\n" % e)
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

# **get_identity_entity_alias_id_id**
> get_identity_entity_alias_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias

try:
    # Update, read or delete an alias ID.
    api_instance.get_identity_entity_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_entity_id**
> get_identity_entity_id(list=list)

List all the entity IDs

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the entity IDs
    api_instance.get_identity_entity_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_id: %s\n" % e)
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

# **get_identity_entity_id_id**
> get_identity_entity_id_id(id)

Update, read or delete an entity using entity ID

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.

try:
    # Update, read or delete an entity using entity ID
    api_instance.get_identity_entity_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_entity_name**
> get_identity_entity_name(list=list)

List all the entity names

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the entity names
    api_instance.get_identity_entity_name(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_name: %s\n" % e)
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

# **get_identity_entity_name_name**
> get_identity_entity_name_name(name)

Update, read or delete an entity using entity name

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the entity

try:
    # Update, read or delete an entity using entity name
    api_instance.get_identity_entity_name_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_entity_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_group_alias_id**
> get_identity_group_alias_id(list=list)

List all the group alias IDs.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the group alias IDs.
    api_instance.get_identity_group_alias_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_alias_id: %s\n" % e)
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

# **get_identity_group_alias_id_id**
> get_identity_group_alias_id_id(id)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group alias.

try:
    api_instance.get_identity_group_alias_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_group_id**
> get_identity_group_id(list=list)

List all the group IDs.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the group IDs.
    api_instance.get_identity_group_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_id: %s\n" % e)
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

# **get_identity_group_id_id**
> get_identity_group_id_id(id)

Update or delete an existing group using its ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.

try:
    # Update or delete an existing group using its ID.
    api_instance.get_identity_group_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_group_name**
> get_identity_group_name(list=list)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    api_instance.get_identity_group_name(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_name: %s\n" % e)
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

# **get_identity_group_name_name**
> get_identity_group_name_name(name)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the group.

try:
    api_instance.get_identity_group_name_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_group_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_oidc_config**
> get_identity_oidc_config()

OIDC configuration

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()

try:
    # OIDC configuration
    api_instance.get_identity_oidc_config()
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_config: %s\n" % e)
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

# **get_identity_oidc_key**
> get_identity_oidc_key(list=list)

List OIDC keys

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List OIDC keys
    api_instance.get_identity_oidc_key(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_key: %s\n" % e)
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

# **get_identity_oidc_key_name**
> get_identity_oidc_key_name(name)

CRUD operations for OIDC keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the key

try:
    # CRUD operations for OIDC keys.
    api_instance.get_identity_oidc_key_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_oidc_role**
> get_identity_oidc_role(list=list)

List configured OIDC roles

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List configured OIDC roles
    api_instance.get_identity_oidc_role(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_role: %s\n" % e)
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

# **get_identity_oidc_role_name**
> get_identity_oidc_role_name(name)

CRUD operations on OIDC Roles

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the role

try:
    # CRUD operations on OIDC Roles
    api_instance.get_identity_oidc_role_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_oidc_token_name**
> get_identity_oidc_token_name(name)

Generate an OIDC token

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the role

try:
    # Generate an OIDC token
    api_instance.get_identity_oidc_token_name(name)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_token_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_identity_oidc_well_known_keys**
> get_identity_oidc_well_known_keys()

Retrieve public keys

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()

try:
    # Retrieve public keys
    api_instance.get_identity_oidc_well_known_keys()
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_well_known_keys: %s\n" % e)
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

# **get_identity_oidc_well_known_openid_configuration**
> get_identity_oidc_well_known_openid_configuration()

Query OIDC configurations

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()

try:
    # Query OIDC configurations
    api_instance.get_identity_oidc_well_known_openid_configuration()
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_oidc_well_known_openid_configuration: %s\n" % e)
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

# **get_identity_persona_id**
> get_identity_persona_id(list=list)

List all the alias IDs.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # List all the alias IDs.
    api_instance.get_identity_persona_id(list=list)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_persona_id: %s\n" % e)
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

# **get_identity_persona_id_id**
> get_identity_persona_id_id(id)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the persona

try:
    # Update, read or delete an alias ID.
    api_instance.get_identity_persona_id_id(id)
except ApiException as e:
    print("Exception when calling IdentityApi->get_identity_persona_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_alias**
> post_identity_alias(body=body)

Create a new alias.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body13() # Body13 |  (optional)

try:
    # Create a new alias.
    api_instance.post_identity_alias(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body13**](Body13.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_alias_id_id**
> post_identity_alias_id_id(id, body=body)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias
body = hashicorp_vault_client.Body14() # Body14 |  (optional)

try:
    # Update, read or delete an alias ID.
    api_instance.post_identity_alias_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 
 **body** | [**Body14**](Body14.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity**
> post_identity_entity(body=body)

Create a new entity

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body15() # Body15 |  (optional)

try:
    # Create a new entity
    api_instance.post_identity_entity(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body15**](Body15.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity_alias**
> post_identity_entity_alias(body=body)

Create a new alias.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body16() # Body16 |  (optional)

try:
    # Create a new alias.
    api_instance.post_identity_entity_alias(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body16**](Body16.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity_alias_id_id**
> post_identity_entity_alias_id_id(id, body=body)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the alias
body = hashicorp_vault_client.Body17() # Body17 |  (optional)

try:
    # Update, read or delete an alias ID.
    api_instance.post_identity_entity_alias_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the alias | 
 **body** | [**Body17**](Body17.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity_id_id**
> post_identity_entity_id_id(id, body=body)

Update, read or delete an entity using entity ID

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the entity. If set, updates the corresponding existing entity.
body = hashicorp_vault_client.Body18() # Body18 |  (optional)

try:
    # Update, read or delete an entity using entity ID
    api_instance.post_identity_entity_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the entity. If set, updates the corresponding existing entity. | 
 **body** | [**Body18**](Body18.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity_merge**
> post_identity_entity_merge(body=body)

Merge two or more entities together

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body19() # Body19 |  (optional)

try:
    # Merge two or more entities together
    api_instance.post_identity_entity_merge(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity_merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body19**](Body19.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_entity_name_name**
> post_identity_entity_name_name(name, body=body)

Update, read or delete an entity using entity name

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the entity
body = hashicorp_vault_client.Body20() # Body20 |  (optional)

try:
    # Update, read or delete an entity using entity name
    api_instance.post_identity_entity_name_name(name, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_entity_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the entity | 
 **body** | [**Body20**](Body20.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_group**
> post_identity_group(body=body)

Create a new group.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body21() # Body21 |  (optional)

try:
    # Create a new group.
    api_instance.post_identity_group(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body21**](Body21.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_group_alias**
> post_identity_group_alias(body=body)

Creates a new group alias, or updates an existing one.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body22() # Body22 |  (optional)

try:
    # Creates a new group alias, or updates an existing one.
    api_instance.post_identity_group_alias(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_group_alias: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body22**](Body22.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_group_alias_id_id**
> post_identity_group_alias_id_id(id, body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group alias.
body = hashicorp_vault_client.Body23() # Body23 |  (optional)

try:
    api_instance.post_identity_group_alias_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_group_alias_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group alias. | 
 **body** | [**Body23**](Body23.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_group_id_id**
> post_identity_group_id_id(id, body=body)

Update or delete an existing group using its ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the group. If set, updates the corresponding existing group.
body = hashicorp_vault_client.Body24() # Body24 |  (optional)

try:
    # Update or delete an existing group using its ID.
    api_instance.post_identity_group_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_group_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the group. If set, updates the corresponding existing group. | 
 **body** | [**Body24**](Body24.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_group_name_name**
> post_identity_group_name_name(name, body=body)



### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the group.
body = hashicorp_vault_client.Body25() # Body25 |  (optional)

try:
    api_instance.post_identity_group_name_name(name, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_group_name_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the group. | 
 **body** | [**Body25**](Body25.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_lookup_entity**
> post_identity_lookup_entity(body=body)

Query entities based on various properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body26() # Body26 |  (optional)

try:
    # Query entities based on various properties.
    api_instance.post_identity_lookup_entity(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_lookup_entity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body26**](Body26.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_lookup_group**
> post_identity_lookup_group(body=body)

Query groups based on various properties.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body27() # Body27 |  (optional)

try:
    # Query groups based on various properties.
    api_instance.post_identity_lookup_group(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_lookup_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body27**](Body27.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_oidc_config**
> post_identity_oidc_config(body=body)

OIDC configuration

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body28() # Body28 |  (optional)

try:
    # OIDC configuration
    api_instance.post_identity_oidc_config(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_oidc_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body28**](Body28.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_oidc_introspect**
> post_identity_oidc_introspect(body=body)

Verify the authenticity of an OIDC token

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body29() # Body29 |  (optional)

try:
    # Verify the authenticity of an OIDC token
    api_instance.post_identity_oidc_introspect(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_oidc_introspect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body29**](Body29.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_oidc_key_name**
> post_identity_oidc_key_name(name, body=body)

CRUD operations for OIDC keys.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the key
body = hashicorp_vault_client.Body30() # Body30 |  (optional)

try:
    # CRUD operations for OIDC keys.
    api_instance.post_identity_oidc_key_name(name, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_oidc_key_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **body** | [**Body30**](Body30.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_oidc_key_name_rotate**
> post_identity_oidc_key_name_rotate(name, body=body)

Rotate a named OIDC key.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the key
body = hashicorp_vault_client.Body31() # Body31 |  (optional)

try:
    # Rotate a named OIDC key.
    api_instance.post_identity_oidc_key_name_rotate(name, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_oidc_key_name_rotate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the key | 
 **body** | [**Body31**](Body31.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_oidc_role_name**
> post_identity_oidc_role_name(name, body=body)

CRUD operations on OIDC Roles

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
name = 'name_example' # str | Name of the role
body = hashicorp_vault_client.Body32() # Body32 |  (optional)

try:
    # CRUD operations on OIDC Roles
    api_instance.post_identity_oidc_role_name(name, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_oidc_role_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| Name of the role | 
 **body** | [**Body32**](Body32.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_persona**
> post_identity_persona(body=body)

Create a new alias.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
body = hashicorp_vault_client.Body33() # Body33 |  (optional)

try:
    # Create a new alias.
    api_instance.post_identity_persona(body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_persona: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body33**](Body33.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_identity_persona_id_id**
> post_identity_persona_id_id(id, body=body)

Update, read or delete an alias ID.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.IdentityApi()
id = 'id_example' # str | ID of the persona
body = hashicorp_vault_client.Body34() # Body34 |  (optional)

try:
    # Update, read or delete an alias ID.
    api_instance.post_identity_persona_id_id(id, body=body)
except ApiException as e:
    print("Exception when calling IdentityApi->post_identity_persona_id_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the persona | 
 **body** | [**Body34**](Body34.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

