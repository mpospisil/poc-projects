# idea_cdp_client_poc.DesignSetApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_design_sets_delete**](DesignSetApi.md#api1_design_sets_delete) | **DELETE** /api/1/design-sets | 
[**api1_design_sets_design_set_id_design_items_get**](DesignSetApi.md#api1_design_sets_design_set_id_design_items_get) | **GET** /api/1/design-sets/{designSetId}/design-items | 
[**api1_design_sets_design_set_id_get**](DesignSetApi.md#api1_design_sets_design_set_id_get) | **GET** /api/1/design-sets/{designSetId} | 
[**api1_design_sets_get**](DesignSetApi.md#api1_design_sets_get) | **GET** /api/1/design-sets | 
[**api1_design_sets_post**](DesignSetApi.md#api1_design_sets_post) | **POST** /api/1/design-sets | 


# **api1_design_sets_delete**
> api1_design_sets_delete(design_set_id=design_set_id)



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
        api_instance.api1_design_sets_delete(design_set_id=design_set_id)
    except Exception as e:
        print("Exception when calling DesignSetApi->api1_design_sets_delete: %s\n" % e)
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

# **api1_design_sets_design_set_id_design_items_get**
> List[IConDesignItem] api1_design_sets_design_set_id_design_items_get(design_set_id, version=version)



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
    version = 1 # int |  (optional) (default to 1)

    try:
        api_response = api_instance.api1_design_sets_design_set_id_design_items_get(design_set_id, version=version)
        print("The response of DesignSetApi->api1_design_sets_design_set_id_design_items_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api1_design_sets_design_set_id_design_items_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | 
 **version** | **int**|  | [optional] [default to 1]

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

# **api1_design_sets_design_set_id_get**
> IConDesignSet api1_design_sets_design_set_id_get(design_set_id)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
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
    design_set_id = 'design_set_id_example' # str | 

    try:
        api_response = api_instance.api1_design_sets_design_set_id_get(design_set_id)
        print("The response of DesignSetApi->api1_design_sets_design_set_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api1_design_sets_design_set_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_set_id** | **str**|  | 

### Return type

[**IConDesignSet**](IConDesignSet.md)

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

# **api1_design_sets_get**
> List[IConDesignSet] api1_design_sets_get()



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
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

    try:
        api_response = api_instance.api1_design_sets_get()
        print("The response of DesignSetApi->api1_design_sets_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api1_design_sets_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IConDesignSet]**](IConDesignSet.md)

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

# **api1_design_sets_post**
> IConDesignSet api1_design_sets_post(create_con_design_set=create_con_design_set)



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
        api_response = api_instance.api1_design_sets_post(create_con_design_set=create_con_design_set)
        print("The response of DesignSetApi->api1_design_sets_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignSetApi->api1_design_sets_post: %s\n" % e)
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

