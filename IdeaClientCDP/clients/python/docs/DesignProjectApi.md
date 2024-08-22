# idea_cdp_client_poc.DesignProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_design_project_design_item_id_get**](DesignProjectApi.md#api1_design_project_design_item_id_get) | **GET** /api/1/design-project/{designItemId} | 
[**api1_design_project_get**](DesignProjectApi.md#api1_design_project_get) | **GET** /api/1/design-project | 


# **api1_design_project_design_item_id_get**
> str api1_design_project_design_item_id_get(design_item_id)



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
    api_instance = idea_cdp_client_poc.DesignProjectApi(api_client)
    design_item_id = 'design_item_id_example' # str | 

    try:
        api_response = api_instance.api1_design_project_design_item_id_get(design_item_id)
        print("The response of DesignProjectApi->api1_design_project_design_item_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignProjectApi->api1_design_project_design_item_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **design_item_id** | **str**|  | 

### Return type

**str**

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

# **api1_design_project_get**
> str api1_design_project_get()



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
    api_instance = idea_cdp_client_poc.DesignProjectApi(api_client)

    try:
        api_response = api_instance.api1_design_project_get()
        print("The response of DesignProjectApi->api1_design_project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DesignProjectApi->api1_design_project_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

