# connection_restapi_client_poc.TemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**apply_template**](TemplateApi.md#apply_template) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/apply-template | Apply the connection template applyTemplateParam on the connection connectionId in the project projectId
[**get_default_template_mapping**](TemplateApi.md#get_default_template_mapping) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/get-template-mapping | Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId


# **apply_template**
> object apply_template(project_id, connection_id, idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api)

Apply the connection template applyTemplateParam on the connection connectionId in the project projectId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.TemplateApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection where to apply the template
    idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi | Template to apply (optional)

    try:
        # Apply the connection template applyTemplateParam on the connection connectionId in the project projectId
        api_response = api_instance.apply_template(project_id, connection_id, idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api)
        print("The response of TemplateApi->apply_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->apply_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection where to apply the template | 
 **idea_stati_ca_api_connection_model_con_template_apply_param_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConTemplateApplyParamIdeaStatiCaApi.md)| Template to apply | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_default_template_mapping**
> IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi get_default_template_mapping(project_id, connection_id, idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api)

Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId

The result IdeaStatiCa.Api.Connection.Model.TemplateConversionsDefault mapping to apply the passed template.  It can be modified by a user and used for the application of a template M:IdeaStatiCa.ConnectionRestApi.Controllers.TemplateController.ApplyConnectionTemplateAsync(System.Guid,System.Int32,IdeaStatiCa.Api.Connection.Model.ConTemplateApplyParam) method.

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_template_conversions_idea_stati_ca_api import IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.TemplateApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get default mapping
    idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi | Data of the template to get default mapping (optional)

    try:
        # Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId
        api_response = api_instance.get_default_template_mapping(project_id, connection_id, idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api)
        print("The response of TemplateApi->get_default_template_mapping:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TemplateApi->get_default_template_mapping: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get default mapping | 
 **idea_stati_ca_api_connection_model_con_template_mapping_get_param_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConTemplateMappingGetParamIdeaStatiCaApi.md)| Data of the template to get default mapping | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelTemplateConversionsIdeaStatiCaApi.md)

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

