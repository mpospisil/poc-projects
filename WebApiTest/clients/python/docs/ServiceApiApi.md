# webserviceapi_client.ServiceApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_service_api_get**](ServiceApiApi.md#api_service_api_get) | **GET** /api/ServiceApi | 
[**api_service_api_upload_post**](ServiceApiApi.md#api_service_api_upload_post) | **POST** /api/ServiceApi/upload | 


# **api_service_api_get**
> List[str] api_service_api_get()



### Example


```python
import webserviceapi_client
from webserviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webserviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webserviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webserviceapi_client.ServiceApiApi(api_client)

    try:
        api_response = api_instance.api_service_api_get()
        print("The response of ServiceApiApi->api_service_api_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApiApi->api_service_api_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_service_api_upload_post**
> api_service_api_upload_post(file=file)



### Example


```python
import webserviceapi_client
from webserviceapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = webserviceapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with webserviceapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = webserviceapi_client.ServiceApiApi(api_client)
    file = None # bytearray |  (optional)

    try:
        api_instance.api_service_api_upload_post(file=file)
    except Exception as e:
        print("Exception when calling ServiceApiApi->api_service_api_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

