# idea_cdp_client_poc.DesignSetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api9_design_sets_delete**](DesignSetApi.md#api9_design_sets_delete) | **DELETE** /api/9/design-sets | 
[**api9_design_sets_design_items_filter_get**](DesignSetApi.md#api9_design_sets_design_items_filter_get) | **GET** /api/9/design-sets/design-items/filter | 
[**api9_design_sets_design_set_id_design_items_filter_get**](DesignSetApi.md#api9_design_sets_design_set_id_design_items_filter_get) | **GET** /api/9/design-sets/{designSetId}/design-items/filter | 
[**api9_design_sets_design_set_id_design_items_get**](DesignSetApi.md#api9_design_sets_design_set_id_design_items_get) | **GET** /api/9/design-sets/{designSetId}/design-items | 
[**api9_design_sets_design_set_id_get**](DesignSetApi.md#api9_design_sets_design_set_id_get) | **GET** /api/9/design-sets/{designSetId} | 
[**api9_design_sets_get**](DesignSetApi.md#api9_design_sets_get) | **GET** /api/9/design-sets | 
[**api9_design_sets_post**](DesignSetApi.md#api9_design_sets_post) | **POST** /api/9/design-sets | 


# **api9_design_sets_delete**
> api9_design_sets_delete(design_set_id=design_set_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    design_set_id = 'design_set_id_example' # str |  (optional)

    try:
        api_instance.api9_design_sets_delete(design_set_id=design_set_id)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_design_items_filter_get**
> ConDesignItemLitePaginatedConDesignItems api9_design_sets_design_items_filter_get(var_from=var_from, search_query_filter=search_query_filter, version=version)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_item_lite_paginated_con_design_items import ConDesignItemLitePaginatedConDesignItems
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    var_from = 56 # int |  (optional)
    search_query_filter = 'search_query_filter_example' # str |  (optional)
    version = 56 # int |  (optional)

    try:
        api_response = api_instance.api9_design_sets_design_items_filter_get(var_from=var_from, search_query_filter=search_query_filter, version=version)
        print("The response of DesignSetApi->api9_design_sets_design_items_filter_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_design_items_filter_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **var_from** | **int**|  | [optional] 
 **search_query_filter** | **str**|  | [optional] 
 **version** | **int**|  | [optional] 

### Return type

[**ConDesignItemLitePaginatedConDesignItems**](ConDesignItemLitePaginatedConDesignItems.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_design_set_id_design_items_filter_get**
> ConDesignItemLitePaginatedConDesignItems api9_design_sets_design_set_id_design_items_filter_get(design_set_id, var_from=var_from, search_query_filter=search_query_filter, version=version)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_item_lite_paginated_con_design_items import ConDesignItemLitePaginatedConDesignItems
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    design_set_id = 'design_set_id_example' # str | 
    var_from = 56 # int |  (optional)
    search_query_filter = 'search_query_filter_example' # str |  (optional)
    version = 56 # int |  (optional)

    try:
        api_response = api_instance.api9_design_sets_design_set_id_design_items_filter_get(design_set_id, var_from=var_from, search_query_filter=search_query_filter, version=version)
        print("The response of DesignSetApi->api9_design_sets_design_set_id_design_items_filter_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_design_set_id_design_items_filter_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | 
 **var_from** | **int**|  | [optional] 
 **search_query_filter** | **str**|  | [optional] 
 **version** | **int**|  | [optional] 

### Return type

[**ConDesignItemLitePaginatedConDesignItems**](ConDesignItemLitePaginatedConDesignItems.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_design_set_id_design_items_get**
> List[IConDesignItem] api9_design_sets_design_set_id_design_items_get(design_set_id, version=version)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.i_con_design_item import IConDesignItem
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    design_set_id = 'design_set_id_example' # str | 
    version = 56 # int |  (optional)

    try:
        api_response = api_instance.api9_design_sets_design_set_id_design_items_get(design_set_id, version=version)
        print("The response of DesignSetApi->api9_design_sets_design_set_id_design_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_design_set_id_design_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | 
 **version** | **int**|  | [optional] 

### Return type

[**List[IConDesignItem]**](IConDesignItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_design_set_id_get**
> ConDesignSetDto api9_design_sets_design_set_id_get(design_set_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_set_dto import ConDesignSetDto
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    design_set_id = 'design_set_id_example' # str | 

    try:
        api_response = api_instance.api9_design_sets_design_set_id_get(design_set_id)
        print("The response of DesignSetApi->api9_design_sets_design_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_design_set_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | 

### Return type

[**ConDesignSetDto**](ConDesignSetDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_get**
> List[ConDesignSetDto] api9_design_sets_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_set_dto import ConDesignSetDto
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)

    try:
        api_response = api_instance.api9_design_sets_get()
        print("The response of DesignSetApi->api9_design_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConDesignSetDto]**](ConDesignSetDto.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api9_design_sets_post**
> IConDesignSet api9_design_sets_post(create_con_design_set=create_con_design_set)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.create_con_design_set import CreateConDesignSet
from idea_cdp_client_poc.models.i_con_design_set import IConDesignSet
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.DesignSetApi(api_client)
    create_con_design_set = idea_cdp_client_poc.CreateConDesignSet() # CreateConDesignSet |  (optional)

    try:
        api_response = api_instance.api9_design_sets_post(create_con_design_set=create_con_design_set)
        print("The response of DesignSetApi->api9_design_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api9_design_sets_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_con_design_set** | [**CreateConDesignSet**](CreateConDesignSet.md)|  | [optional] 

### Return type

[**IConDesignSet**](IConDesignSet.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

