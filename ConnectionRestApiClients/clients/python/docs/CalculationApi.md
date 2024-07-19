# connection-restapi-client-poc.CalculationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_calculate_post**](CalculationApi.md#api1_projects_project_id_calculate_post) | **POST** /api/1/projects/{projectId}/calculate | 
[**api1_projects_project_id_rawresults_post**](CalculationApi.md#api1_projects_project_id_rawresults_post) | **POST** /api/1/projects/{projectId}/rawresults | Get raw CBFEM results (an instance of CheckResultsData)
[**api1_projects_project_id_rawresults_text_post**](CalculationApi.md#api1_projects_project_id_rawresults_text_post) | **POST** /api/1/projects/{projectId}/rawresults-text | Get json string which represents raw CBFEM results (an instance of CheckResultsData)
[**api1_projects_project_id_results_post**](CalculationApi.md#api1_projects_project_id_results_post) | **POST** /api/1/projects/{projectId}/results | 


# **api1_projects_project_id_calculate_post**
> List[IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin] api1_projects_project_id_calculate_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)



### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_result_con_result_summary_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = connection-restapi-client-poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_calculate_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of CalculationApi->api1_projects_project_id_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_rawresults_post**
> ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks api1_projects_project_id_rawresults_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)

Get raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.con_modeler_connection_plug_in_check_results_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = connection-restapi-client-poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin | Type of requested analysis and connection to calculate (optional)

    try:
        # Get raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_projects_project_id_rawresults_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of CalculationApi->api1_projects_project_id_rawresults_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_rawresults_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened connection in the ConnectionReastApi service | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin.md)| Type of requested analysis and connection to calculate | [optional] 

### Return type

[**ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks**](ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks.md)

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

# **api1_projects_project_id_rawresults_text_post**
> str api1_projects_project_id_rawresults_text_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)

Get json string which represents raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = connection-restapi-client-poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin | Type of requested analysis and connection to calculate (optional)

    try:
        # Get json string which represents raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_projects_project_id_rawresults_text_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of CalculationApi->api1_projects_project_id_rawresults_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_rawresults_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened connection in the ConnectionReastApi service | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin.md)| Type of requested analysis and connection to calculate | [optional] 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/*+xml, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_projects_project_id_results_post**
> List[IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel] api1_projects_project_id_results_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)



### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_rs_open_model_connection_connection_check_res_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = connection-restapi-client-poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_results_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of CalculationApi->api1_projects_project_id_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**List[IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel]**](IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel.md)

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

