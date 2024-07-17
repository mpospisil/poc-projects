# openapi_client.ConCalculationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_con_calculation_project_id_calculate_post**](ConCalculationApi.md#api1_con_calculation_project_id_calculate_post) | **POST** /api/1/ConCalculation/{projectId}/calculate | 
[**api1_con_calculation_project_id_rawresults_post**](ConCalculationApi.md#api1_con_calculation_project_id_rawresults_post) | **POST** /api/1/ConCalculation/{projectId}/rawresults | Get raw CBFEM results (an instance of CheckResultsData)
[**api1_con_calculation_project_id_rawresults_text_post**](ConCalculationApi.md#api1_con_calculation_project_id_rawresults_text_post) | **POST** /api/1/ConCalculation/{projectId}/rawresults-text | Get json string which represents raw CBFEM results (an instance of CheckResultsData)
[**api1_con_calculation_project_id_results_post**](ConCalculationApi.md#api1_con_calculation_project_id_results_post) | **POST** /api/1/ConCalculation/{projectId}/results | 


# **api1_con_calculation_project_id_calculate_post**
> List[IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin] api1_con_calculation_project_id_calculate_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_result_con_result_summary_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelResultConResultSummaryIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConCalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_con_calculation_project_id_calculate_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of ConCalculationApi->api1_con_calculation_project_id_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConCalculationApi->api1_con_calculation_project_id_calculate_post: %s\n" % e)
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
 - **Accept**: text/plain, application/xml, text/xml, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_con_calculation_project_id_rawresults_post**
> ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks api1_con_calculation_project_id_rawresults_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)

Get raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import openapi_client
from openapi_client.models.con_modeler_connection_plug_in_check_results_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInCheckResultsDataIdeaStatiCaConnectionChecks
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConCalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin | Type of requested analysis and connection to calculate (optional)

    try:
        # Get raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_con_calculation_project_id_rawresults_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of ConCalculationApi->api1_con_calculation_project_id_rawresults_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConCalculationApi->api1_con_calculation_project_id_rawresults_post: %s\n" % e)
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

# **api1_con_calculation_project_id_rawresults_text_post**
> str api1_con_calculation_project_id_rawresults_text_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)

Get json string which represents raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConCalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin | Type of requested analysis and connection to calculate (optional)

    try:
        # Get json string which represents raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_con_calculation_project_id_rawresults_text_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of ConCalculationApi->api1_con_calculation_project_id_rawresults_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConCalculationApi->api1_con_calculation_project_id_rawresults_text_post: %s\n" % e)
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

# **api1_con_calculation_project_id_results_post**
> List[IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel] api1_con_calculation_project_id_results_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)



### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_connection_connection_check_res_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConCalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConCalculationParameterIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_con_calculation_project_id_results_post(project_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_calculation_parameter_idea_stati_ca_plugin)
        print("The response of ConCalculationApi->api1_con_calculation_project_id_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConCalculationApi->api1_con_calculation_project_id_results_post: %s\n" % e)
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
 - **Accept**: text/plain, application/xml, text/xml, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

