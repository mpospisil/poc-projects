# connection_restapi_client_poc.CalculationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_calculate_post**](CalculationApi.md#api1_projects_project_id_calculate_post) | **POST** /api/1/projects/{projectId}/calculate | 
[**api1_projects_project_id_rawresults_post**](CalculationApi.md#api1_projects_project_id_rawresults_post) | **POST** /api/1/projects/{projectId}/rawresults | Get raw CBFEM results (an instance of CheckResultsData)
[**api1_projects_project_id_rawresults_text_post**](CalculationApi.md#api1_projects_project_id_rawresults_text_post) | **POST** /api/1/projects/{projectId}/rawresults-text | Get json string which represents raw CBFEM results (an instance of CheckResultsData)
[**api1_projects_project_id_results_post**](CalculationApi.md#api1_projects_project_id_results_post) | **POST** /api/1/projects/{projectId}/results | 


# **api1_projects_project_id_calculate_post**
> List[IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi] api1_projects_project_id_calculate_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_result_summary_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_calculate_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->api1_projects_project_id_calculate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_calculate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**List[IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi.md)

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
> CheckResultsDataIdeaStatiCaConnectionChecks api1_projects_project_id_rawresults_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)

Get raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.check_results_data_idea_stati_ca_connection_checks import CheckResultsDataIdeaStatiCaConnectionChecks
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi | Type of requested analysis and connection to calculate (optional)

    try:
        # Get raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_projects_project_id_rawresults_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->api1_projects_project_id_rawresults_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_rawresults_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened connection in the ConnectionReastApi service | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)| Type of requested analysis and connection to calculate | [optional] 

### Return type

[**CheckResultsDataIdeaStatiCaConnectionChecks**](CheckResultsDataIdeaStatiCaConnectionChecks.md)

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
> str api1_projects_project_id_rawresults_text_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)

Get json string which represents raw CBFEM results (an instance of CheckResultsData)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionReastApi service
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi | Type of requested analysis and connection to calculate (optional)

    try:
        # Get json string which represents raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.api1_projects_project_id_rawresults_text_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->api1_projects_project_id_rawresults_text_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_rawresults_text_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened connection in the ConnectionReastApi service | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)| Type of requested analysis and connection to calculate | [optional] 

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
> List[ConnectionConnectionCheckResIdeaRSOpenModel] api1_projects_project_id_results_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.connection_connection_check_res_idea_rs_open_model import ConnectionConnectionCheckResIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.CalculationApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_results_post(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->api1_projects_project_id_results_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->api1_projects_project_id_results_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**List[ConnectionConnectionCheckResIdeaRSOpenModel]**](ConnectionConnectionCheckResIdeaRSOpenModel.md)

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

