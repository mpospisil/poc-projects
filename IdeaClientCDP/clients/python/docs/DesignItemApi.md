# idea_cdp_client_poc.DesignItemApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_design_items_design_item_id_delete**](DesignItemApi.md#api1_design_items_design_item_id_delete) | **DELETE** /api/1/design-items/{designItemId} | 
[**api1_design_items_design_item_id_get**](DesignItemApi.md#api1_design_items_design_item_id_get) | **GET** /api/1/design-items/{designItemId} | 
[**api1_design_items_design_item_id_picture_get**](DesignItemApi.md#api1_design_items_design_item_id_picture_get) | **GET** /api/1/design-items/{designItemId}/picture | 
[**api1_design_items_design_item_id_publish_post**](DesignItemApi.md#api1_design_items_design_item_id_publish_post) | **POST** /api/1/design-items/{designItemId}/publish | 
[**api1_design_items_post**](DesignItemApi.md#api1_design_items_post) | **POST** /api/1/design-items | 
[**api1_design_items_put**](DesignItemApi.md#api1_design_items_put) | **PUT** /api/1/design-items | 


# **api1_design_items_design_item_id_delete**
> api1_design_items_design_item_id_delete(design_item_id)



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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    design_item_id = 'design_item_id_example' # str | 

    try:
        api_instance.api1_design_items_design_item_id_delete(design_item_id)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_design_item_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_item_id** | **str**|  | 

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

# **api1_design_items_design_item_id_get**
> IConDesignItem api1_design_items_design_item_id_get(design_item_id)



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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    design_item_id = 'design_item_id_example' # str | 

    try:
        api_response = api_instance.api1_design_items_design_item_id_get(design_item_id)
        print("The response of DesignItemApi->api1_design_items_design_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_design_item_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_item_id** | **str**|  | 

### Return type

[**IConDesignItem**](IConDesignItem.md)

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

# **api1_design_items_design_item_id_picture_get**
> api1_design_items_design_item_id_picture_get(design_item_id)



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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    design_item_id = 'design_item_id_example' # str | 

    try:
        api_instance.api1_design_items_design_item_id_picture_get(design_item_id)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_design_item_id_picture_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_item_id** | **str**|  | 

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

# **api1_design_items_design_item_id_publish_post**
> IConDesignItem api1_design_items_design_item_id_publish_post(design_item_id, picture=picture)



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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    design_item_id = 'design_item_id_example' # str | 
    picture = None # bytearray |  (optional)

    try:
        api_response = api_instance.api1_design_items_design_item_id_publish_post(design_item_id, picture=picture)
        print("The response of DesignItemApi->api1_design_items_design_item_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_design_item_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_item_id** | **str**|  | 
 **picture** | **bytearray**|  | [optional] 

### Return type

[**IConDesignItem**](IConDesignItem.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_design_items_post**
> str api1_design_items_post(con_design_item=con_design_item)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_item import ConDesignItem
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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    con_design_item = idea_cdp_client_poc.ConDesignItem() # ConDesignItem |  (optional)

    try:
        api_response = api_instance.api1_design_items_post(con_design_item=con_design_item)
        print("The response of DesignItemApi->api1_design_items_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **con_design_item** | [**ConDesignItem**](ConDesignItem.md)|  | [optional] 

### Return type

**str**

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

# **api1_design_items_put**
> api1_design_items_put(con_design_item=con_design_item)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.con_design_item import ConDesignItem
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
    api_instance = idea_cdp_client_poc.DesignItemApi(api_client)
    con_design_item = idea_cdp_client_poc.ConDesignItem() # ConDesignItem |  (optional)

    try:
        api_instance.api1_design_items_put(con_design_item=con_design_item)
    except Exception as e:
        print("Exception when calling DesignItemApi->api1_design_items_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **con_design_item** | [**ConDesignItem**](ConDesignItem.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

