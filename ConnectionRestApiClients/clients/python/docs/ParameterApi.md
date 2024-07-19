# connection_restapi_client_poc.ParameterApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_evaluate_expression_post**](ParameterApi.md#api1_projects_project_id_connections_connection_id_evaluate_expression_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/evaluate-expression | 
[**api1_projects_project_id_connections_connection_id_parameters_get**](ParameterApi.md#api1_projects_project_id_connections_connection_id_parameters_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/parameters | 
[**api1_projects_project_id_connections_connection_id_parameters_put**](ParameterApi.md#api1_projects_project_id_connections_connection_id_parameters_put) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/parameters | 


# **api1_projects_project_id_connections_connection_id_evaluate_expression_post**
> str api1_projects_project_id_connections_connection_id_evaluate_expression_post(project_id, connection_id, body=body)



### Example


```python
import connection_restapi_client_poc
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
    api_instance = connection_restapi_client_poc.ParameterApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    body = 'body_example' # str |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_evaluate_expression_post(project_id, connection_id, body=body)
        print("The response of ParameterApi->api1_projects_project_id_connections_connection_id_evaluate_expression_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterApi->api1_projects_project_id_connections_connection_id_evaluate_expression_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **body** | **str**|  | [optional] 

### Return type

**str**

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

# **api1_projects_project_id_connections_connection_id_parameters_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_parameters_get(project_id, connection_id, include_hidden=include_hidden)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ParameterApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    include_hidden = False # bool |  (optional) (default to False)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_parameters_get(project_id, connection_id, include_hidden=include_hidden)
        print("The response of ParameterApi->api1_projects_project_id_connections_connection_id_parameters_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterApi->api1_projects_project_id_connections_connection_id_parameters_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **include_hidden** | **bool**|  | [optional] [default to False]

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_parameters_put**
> List[IdeaRSCommonParametersParameterDataCIBasicTypes] api1_projects_project_id_connections_connection_id_parameters_put(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rs_common_parameters_parameter_data_ci_basic_types import IdeaRSCommonParametersParameterDataCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ParameterApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin = [connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin()] # List[IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin] |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_parameters_put(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin)
        print("The response of ParameterApi->api1_projects_project_id_connections_connection_id_parameters_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ParameterApi->api1_projects_project_id_connections_connection_id_parameters_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_parameter_idea_parameter_update_idea_stati_ca_plugin** | [**List[IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelParameterIdeaParameterUpdateIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**List[IdeaRSCommonParametersParameterDataCIBasicTypes]**](IdeaRSCommonParametersParameterDataCIBasicTypes.md)

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

