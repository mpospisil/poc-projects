# openapi_client.ExportApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_export_ifc_get**](ExportApi.md#api1_projects_project_id_connections_connection_id_export_ifc_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-ifc | 
[**api1_projects_project_id_connections_connection_id_export_iom_connection_data_get**](ExportApi.md#api1_projects_project_id_connections_connection_id_export_iom_connection_data_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-iom-connection-data | 
[**api1_projects_project_id_connections_connection_id_export_iom_get**](ExportApi.md#api1_projects_project_id_connections_connection_id_export_iom_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-iom | 


# **api1_projects_project_id_connections_connection_id_export_ifc_get**
> SystemIOMemoryStreamSystemPrivateCoreLib api1_projects_project_id_connections_connection_id_export_ifc_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_export_ifc_get(project_id, connection_id)
        print("The response of ExportApi->api1_projects_project_id_connections_connection_id_export_ifc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->api1_projects_project_id_connections_connection_id_export_ifc_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**SystemIOMemoryStreamSystemPrivateCoreLib**](SystemIOMemoryStreamSystemPrivateCoreLib.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/xml, text/xml, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_export_iom_connection_data_get**
> IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel api1_projects_project_id_connections_connection_id_export_iom_connection_data_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_connection_connection_data_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_export_iom_connection_data_get(project_id, connection_id)
        print("The response of ExportApi->api1_projects_project_id_connections_connection_id_export_iom_connection_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ExportApi->api1_projects_project_id_connections_connection_id_export_iom_connection_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel**](IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_export_iom_get**
> api1_projects_project_id_connections_connection_id_export_iom_get(project_id, connection_id, version=version)



### Example


```python
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ExportApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    version = 'version_example' # str |  (optional)

    try:
        api_instance.api1_projects_project_id_connections_connection_id_export_iom_get(project_id, connection_id, version=version)
    except Exception as e:
        print("Exception when calling ExportApi->api1_projects_project_id_connections_connection_id_export_iom_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

