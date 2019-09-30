# hashicorp_vault_client.SecretsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_cubbyhole_path**](SecretsApi.md#delete_cubbyhole_path) | **DELETE** /cubbyhole/{path} | Deletes the secret at the specified location.
[**delete_kv_data_path**](SecretsApi.md#delete_kv_data_path) | **DELETE** /kv/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**delete_kv_metadata_path**](SecretsApi.md#delete_kv_metadata_path) | **DELETE** /kv/metadata/{path} | Configures settings for the KV store
[**get_cubbyhole_path**](SecretsApi.md#get_cubbyhole_path) | **GET** /cubbyhole/{path} | Retrieve the secret at the specified location.
[**get_kv_config**](SecretsApi.md#get_kv_config) | **GET** /kv/config | Read the backend level settings.
[**get_kv_data_path**](SecretsApi.md#get_kv_data_path) | **GET** /kv/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**get_kv_metadata_path**](SecretsApi.md#get_kv_metadata_path) | **GET** /kv/metadata/{path} | Configures settings for the KV store
[**post_cubbyhole_path**](SecretsApi.md#post_cubbyhole_path) | **POST** /cubbyhole/{path} | Store a secret at the specified location.
[**post_kv_config**](SecretsApi.md#post_kv_config) | **POST** /kv/config | Configure backend level settings that are applied to every key in the key-value store.
[**post_kv_data_path**](SecretsApi.md#post_kv_data_path) | **POST** /kv/data/{path} | Write, Read, and Delete data in the Key-Value Store.
[**post_kv_delete_path**](SecretsApi.md#post_kv_delete_path) | **POST** /kv/delete/{path} | Marks one or more versions as deleted in the KV store.
[**post_kv_destroy_path**](SecretsApi.md#post_kv_destroy_path) | **POST** /kv/destroy/{path} | Permanently removes one or more versions in the KV store
[**post_kv_metadata_path**](SecretsApi.md#post_kv_metadata_path) | **POST** /kv/metadata/{path} | Configures settings for the KV store
[**post_kv_undelete_path**](SecretsApi.md#post_kv_undelete_path) | **POST** /kv/undelete/{path} | Undeletes one or more versions from the KV store.

# **delete_cubbyhole_path**
> delete_cubbyhole_path(path)

Deletes the secret at the specified location.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Specifies the path of the secret.

try:
    # Deletes the secret at the specified location.
    api_instance.delete_cubbyhole_path(path)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_cubbyhole_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kv_data_path**
> delete_kv_data_path(path)

Write, Read, and Delete data in the Key-Value Store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.

try:
    # Write, Read, and Delete data in the Key-Value Store.
    api_instance.delete_kv_data_path(path)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_kv_data_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kv_metadata_path**
> delete_kv_metadata_path(path)

Configures settings for the KV store

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.

try:
    # Configures settings for the KV store
    api_instance.delete_kv_metadata_path(path)
except ApiException as e:
    print("Exception when calling SecretsApi->delete_kv_metadata_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_cubbyhole_path**
> get_cubbyhole_path(path, list=list)

Retrieve the secret at the specified location.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Specifies the path of the secret.
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Retrieve the secret at the specified location.
    api_instance.get_cubbyhole_path(path, list=list)
except ApiException as e:
    print("Exception when calling SecretsApi->get_cubbyhole_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kv_config**
> get_kv_config()

Read the backend level settings.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()

try:
    # Read the backend level settings.
    api_instance.get_kv_config()
except ApiException as e:
    print("Exception when calling SecretsApi->get_kv_config: %s\n" % e)
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

# **get_kv_data_path**
> get_kv_data_path(path)

Write, Read, and Delete data in the Key-Value Store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.

try:
    # Write, Read, and Delete data in the Key-Value Store.
    api_instance.get_kv_data_path(path)
except ApiException as e:
    print("Exception when calling SecretsApi->get_kv_data_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kv_metadata_path**
> get_kv_metadata_path(path, list=list)

Configures settings for the KV store

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
list = 'list_example' # str | Return a list if `true` (optional)

try:
    # Configures settings for the KV store
    api_instance.get_kv_metadata_path(path, list=list)
except ApiException as e:
    print("Exception when calling SecretsApi->get_kv_metadata_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **list** | **str**| Return a list if &#x60;true&#x60; | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_cubbyhole_path**
> post_cubbyhole_path(path)

Store a secret at the specified location.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Specifies the path of the secret.

try:
    # Store a secret at the specified location.
    api_instance.post_cubbyhole_path(path)
except ApiException as e:
    print("Exception when calling SecretsApi->post_cubbyhole_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Specifies the path of the secret. | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_config**
> post_kv_config(body=body)

Configure backend level settings that are applied to every key in the key-value store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
body = hashicorp_vault_client.Body35() # Body35 |  (optional)

try:
    # Configure backend level settings that are applied to every key in the key-value store.
    api_instance.post_kv_config(body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_config: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Body35**](Body35.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_data_path**
> post_kv_data_path(path, body=body)

Write, Read, and Delete data in the Key-Value Store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
body = hashicorp_vault_client.Body36() # Body36 |  (optional)

try:
    # Write, Read, and Delete data in the Key-Value Store.
    api_instance.post_kv_data_path(path, body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_data_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **body** | [**Body36**](Body36.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_delete_path**
> post_kv_delete_path(path, body=body)

Marks one or more versions as deleted in the KV store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
body = hashicorp_vault_client.Body37() # Body37 |  (optional)

try:
    # Marks one or more versions as deleted in the KV store.
    api_instance.post_kv_delete_path(path, body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_delete_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **body** | [**Body37**](Body37.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_destroy_path**
> post_kv_destroy_path(path, body=body)

Permanently removes one or more versions in the KV store

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
body = hashicorp_vault_client.Body38() # Body38 |  (optional)

try:
    # Permanently removes one or more versions in the KV store
    api_instance.post_kv_destroy_path(path, body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_destroy_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **body** | [**Body38**](Body38.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_metadata_path**
> post_kv_metadata_path(path, body=body)

Configures settings for the KV store

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
body = hashicorp_vault_client.Body39() # Body39 |  (optional)

try:
    # Configures settings for the KV store
    api_instance.post_kv_metadata_path(path, body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_metadata_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **body** | [**Body39**](Body39.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_kv_undelete_path**
> post_kv_undelete_path(path, body=body)

Undeletes one or more versions from the KV store.

### Example
```python
from __future__ import print_function
import time
import hashicorp_vault_client
from hashicorp_vault_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = hashicorp_vault_client.SecretsApi()
path = 'path_example' # str | Location of the secret.
body = hashicorp_vault_client.Body40() # Body40 |  (optional)

try:
    # Undeletes one or more versions from the KV store.
    api_instance.post_kv_undelete_path(path, body=body)
except ApiException as e:
    print("Exception when calling SecretsApi->post_kv_undelete_path: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **path** | **str**| Location of the secret. | 
 **body** | [**Body40**](Body40.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

