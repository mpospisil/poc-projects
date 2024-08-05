# connection_restapi_client_poc.ConnectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_get**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId} | 
[**api1_projects_project_id_connections_connection_id_missing_welds_get**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_missing_welds_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/missing-welds | 
[**api1_projects_project_id_connections_connection_id_operations_delete**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_operations_delete) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/operations | 
[**api1_projects_project_id_connections_connection_id_operations_get**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_operations_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/operations | 
[**api1_projects_project_id_connections_connection_id_production_cost_get**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_production_cost_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/production-cost | 
[**api1_projects_project_id_connections_connection_id_put**](ConnectionApi.md#api1_projects_project_id_connections_connection_id_put) | **PUT** /api/1/projects/{projectId}/connections/{connectionId} | 
[**api1_projects_project_id_connections_get**](ConnectionApi.md#api1_projects_project_id_connections_get) | **GET** /api/1/projects/{projectId}/connections | 


# **api1_projects_project_id_connections_connection_id_get**
> IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi api1_projects_project_id_connections_connection_id_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_get(project_id, connection_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_missing_welds_get**
> List[IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_missing_welds_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_missing_weld_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_missing_welds_get(project_id, connection_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_missing_welds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_missing_welds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_operations_delete**
> MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore api1_projects_project_id_connections_connection_id_operations_delete(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.microsoft_asp_net_core_mvc_ok_object_result_microsoft_asp_net_core_mvc_core import MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_operations_delete(project_id, connection_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_operations_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_operations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore**](MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore.md)

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

# **api1_projects_project_id_connections_connection_id_operations_get**
> List[IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_operations_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_operation_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_operations_get(project_id, connection_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_operations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_operations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_production_cost_get**
> IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi api1_projects_project_id_connections_connection_id_production_cost_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_production_cost_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_production_cost_get(project_id, connection_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_production_cost_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_production_cost_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_connection_id_put**
> IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi api1_projects_project_id_connections_connection_id_put(project_id, connection_id, idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_put(project_id, connection_id, idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api)
        print("The response of ConnectionApi->api1_projects_project_id_connections_connection_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_connection_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/*+xml, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_connections_get**
> List[IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi] api1_projects_project_id_connections_get(project_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_get(project_id)
        print("The response of ConnectionApi->api1_projects_project_id_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->api1_projects_project_id_connections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

