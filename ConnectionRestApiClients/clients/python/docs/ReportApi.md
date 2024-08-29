# connection_restapi_client_poc.ReportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**generate_pdf**](ReportApi.md#generate_pdf) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/pdf | Generates report for projectId and connectionId
[**generate_word**](ReportApi.md#generate_word) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/word | Generates report for projectId and connectionId


# **generate_pdf**
> MemoryStream generate_pdf(project_id, connection_id)

Generates report for projectId and connectionId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.memory_stream import MemoryStream
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection_restapi_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_restapi_client_poc.ReportApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        # Generates report for projectId and connectionId
        api_response = api_instance.generate_pdf(project_id, connection_id)
        print("The response of ReportApi->generate_pdf:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->generate_pdf: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**MemoryStream**](MemoryStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_word**
> MemoryStream generate_word(project_id, connection_id)

Generates report for projectId and connectionId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.memory_stream import MemoryStream
from connection_restapi_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection_restapi_client_poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection_restapi_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection_restapi_client_poc.ReportApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        # Generates report for projectId and connectionId
        api_response = api_instance.generate_word(project_id, connection_id)
        print("The response of ReportApi->generate_word:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->generate_word: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**MemoryStream**](MemoryStream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

