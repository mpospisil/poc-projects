# connection_restapi_client_poc.ReportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_reports_connection_id_pdf_get**](ReportApi.md#api1_projects_project_id_reports_connection_id_pdf_get) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/pdf | Generates report for projectId and connectionId
[**api1_projects_project_id_reports_connection_id_word_get**](ReportApi.md#api1_projects_project_id_reports_connection_id_word_get) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/word | Generates report for projectId and connectionId


# **api1_projects_project_id_reports_connection_id_pdf_get**
> Stream api1_projects_project_id_reports_connection_id_pdf_get(project_id, connection_id, body=body)

Generates report for projectId and connectionId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.stream import Stream
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
    body = None # object |  (optional)

    try:
        # Generates report for projectId and connectionId
        api_response = api_instance.api1_projects_project_id_reports_connection_id_pdf_get(project_id, connection_id, body=body)
        print("The response of ReportApi->api1_projects_project_id_reports_connection_id_pdf_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->api1_projects_project_id_reports_connection_id_pdf_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**Stream**](Stream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_reports_connection_id_word_get**
> Stream api1_projects_project_id_reports_connection_id_word_get(project_id, connection_id, body=body)

Generates report for projectId and connectionId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.stream import Stream
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
    body = None # object |  (optional)

    try:
        # Generates report for projectId and connectionId
        api_response = api_instance.api1_projects_project_id_reports_connection_id_word_get(project_id, connection_id, body=body)
        print("The response of ReportApi->api1_projects_project_id_reports_connection_id_word_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReportApi->api1_projects_project_id_reports_connection_id_word_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **body** | **object**|  | [optional] 

### Return type

[**Stream**](Stream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

