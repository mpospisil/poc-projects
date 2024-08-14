# connection_restapi_client_poc.CalculationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**calculate**](CalculationApi.md#calculate) | **POST** /api/1/projects/{projectId}/calculate | Run CBFEM caluclation and return the summary of the results
[**get_raw_json_results**](CalculationApi.md#get_raw_json_results) | **POST** /api/1/projects/{projectId}/rawresults-text | Get json string which represents raw CBFEM results (an instance of CheckResultsData)
[**get_results**](CalculationApi.md#get_results) | **POST** /api/1/projects/{projectId}/results | Get detailed results of the CBFEM analysis


# **calculate**
> List[IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi] calculate(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)

Run CBFEM caluclation and return the summary of the results

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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi | List of connections to calculate and a type of CBFEM analysis (optional)

    try:
        # Run CBFEM caluclation and return the summary of the results
        api_response = api_instance.calculate(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->calculate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->calculate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)| List of connections to calculate and a type of CBFEM analysis | [optional] 

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

# **get_raw_json_results**
> str get_raw_json_results(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)

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
    project_id = 'project_id_example' # str | The unique identifier of the opened connection in the ConnectionRestApi service
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi | Type of requested analysis and connection to calculate (optional)

    try:
        # Get json string which represents raw CBFEM results (an instance of CheckResultsData)
        api_response = api_instance.get_raw_json_results(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->get_raw_json_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->get_raw_json_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened connection in the ConnectionRestApi service | 
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

# **get_results**
> List[ConnectionConnectionCheckResIdeaRSOpenModel] get_results(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)

Get detailed results of the CBFEM analysis

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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi | List of connections to calculate and a type of CBFEM analysis (optional)

    try:
        # Get detailed results of the CBFEM analysis
        api_response = api_instance.get_results(project_id, idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api)
        print("The response of CalculationApi->get_results:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CalculationApi->get_results: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **idea_stati_ca_api_connection_model_con_calculation_parameter_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi.md)| List of connections to calculate and a type of CBFEM analysis | [optional] 

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

