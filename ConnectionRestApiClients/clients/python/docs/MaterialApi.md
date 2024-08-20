# connection_restapi_client_poc.MaterialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_bolt_assembly**](MaterialApi.md#add_bolt_assembly) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies | Add bolt assembly to the project
[**add_cross_section**](MaterialApi.md#add_cross_section) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections | Add cross section to the project
[**add_material_bolt_grade**](MaterialApi.md#add_material_bolt_grade) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-grade | Add material to the project
[**add_material_concrete**](MaterialApi.md#add_material_concrete) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/concrete | Add material to the project
[**add_material_steel**](MaterialApi.md#add_material_steel) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/steel | Add material to the project
[**add_material_weld**](MaterialApi.md#add_material_weld) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/welding | Add material to the project
[**get_all_materials**](MaterialApi.md#get_all_materials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials | Get materials which are used in the connectionId
[**get_blot_grade_materials**](MaterialApi.md#get_blot_grade_materials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-grade | Get materials which are used in the connectionId
[**get_bolt_assemblies**](MaterialApi.md#get_bolt_assemblies) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/bolt-assemblies | Get bolt assemblies which are used in the connectionId
[**get_concrete_materials**](MaterialApi.md#get_concrete_materials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/concrete | Get materials which are used in the connectionId
[**get_cross_sections**](MaterialApi.md#get_cross_sections) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/cross-sections | Get cross sections which are used in the connectionId
[**get_steel_materials**](MaterialApi.md#get_steel_materials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/steel | Get materials which are used in the connectionId
[**get_welding_materials**](MaterialApi.md#get_welding_materials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/welding | Get materials which are used in the connectionId


# **add_bolt_assembly**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi add_bolt_assembly(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)

Add bolt assembly to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi | Definition of a new bolt assemby to be added to the project (optional)

    try:
        # Add bolt assembly to the project
        api_response = api_instance.add_bolt_assembly(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)
        print("The response of MaterialApi->add_bolt_assembly:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_bolt_assembly: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)| Definition of a new bolt assemby to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

# **add_cross_section**
> IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi add_cross_section(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api)

Add cross section to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi | Definition of a new cross-section to be added to the project (optional)

    try:
        # Add cross section to the project
        api_response = api_instance.add_cross_section(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api)
        print("The response of MaterialApi->add_cross_section:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_cross_section: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_cross_section_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi.md)| Definition of a new cross-section to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi.md)

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

# **add_material_bolt_grade**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi add_material_bolt_grade(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)

Add material to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi | Definition of a new material to be added to the project (optional)

    try:
        # Add material to the project
        api_response = api_instance.add_material_bolt_grade(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)
        print("The response of MaterialApi->add_material_bolt_grade:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_material_bolt_grade: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)| Definition of a new material to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

# **add_material_concrete**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi add_material_concrete(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)

Add material to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi | Definition of a new material to be added to the project (optional)

    try:
        # Add material to the project
        api_response = api_instance.add_material_concrete(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)
        print("The response of MaterialApi->add_material_concrete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_material_concrete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)| Definition of a new material to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

# **add_material_steel**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi add_material_steel(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)

Add material to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi | Definition of a new material to be added to the project (optional)

    try:
        # Add material to the project
        api_response = api_instance.add_material_steel(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)
        print("The response of MaterialApi->add_material_steel:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_material_steel: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)| Definition of a new material to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

# **add_material_weld**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi add_material_weld(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)

Add material to the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api import IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi | Definition of a new material to be added to the project (optional)

    try:
        # Add material to the project
        api_response = api_instance.add_material_weld(project_id, connection_id, idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api=idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api)
        print("The response of MaterialApi->add_material_weld:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->add_material_weld: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_material_con_mprl_element_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)| Definition of a new material to be added to the project | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

# **get_all_materials**
> List[object] get_all_materials(project_id, connection_id)

Get materials which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its materials

    try:
        # Get materials which are used in the connectionId
        api_response = api_instance.get_all_materials(project_id, connection_id)
        print("The response of MaterialApi->get_all_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_all_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its materials | 

### Return type

**List[object]**

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

# **get_blot_grade_materials**
> List[object] get_blot_grade_materials(project_id, connection_id)

Get materials which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its materials

    try:
        # Get materials which are used in the connectionId
        api_response = api_instance.get_blot_grade_materials(project_id, connection_id)
        print("The response of MaterialApi->get_blot_grade_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_blot_grade_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its materials | 

### Return type

**List[object]**

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

# **get_bolt_assemblies**
> List[object] get_bolt_assemblies(project_id, connection_id)

Get bolt assemblies which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its bolt assemblies

    try:
        # Get bolt assemblies which are used in the connectionId
        api_response = api_instance.get_bolt_assemblies(project_id, connection_id)
        print("The response of MaterialApi->get_bolt_assemblies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_bolt_assemblies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its bolt assemblies | 

### Return type

**List[object]**

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

# **get_concrete_materials**
> List[object] get_concrete_materials(project_id, connection_id)

Get materials which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its materials

    try:
        # Get materials which are used in the connectionId
        api_response = api_instance.get_concrete_materials(project_id, connection_id)
        print("The response of MaterialApi->get_concrete_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_concrete_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its materials | 

### Return type

**List[object]**

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

# **get_cross_sections**
> List[object] get_cross_sections(project_id, connection_id)

Get cross sections which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its cross-sections

    try:
        # Get cross sections which are used in the connectionId
        api_response = api_instance.get_cross_sections(project_id, connection_id)
        print("The response of MaterialApi->get_cross_sections:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_cross_sections: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its cross-sections | 

### Return type

**List[object]**

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

# **get_steel_materials**
> List[object] get_steel_materials(project_id, connection_id)

Get materials which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its materials

    try:
        # Get materials which are used in the connectionId
        api_response = api_instance.get_steel_materials(project_id, connection_id)
        print("The response of MaterialApi->get_steel_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_steel_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its materials | 

### Return type

**List[object]**

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

# **get_welding_materials**
> List[object] get_welding_materials(project_id, connection_id)

Get materials which are used in the connectionId

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
    api_instance = connection_restapi_client_poc.MaterialApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to get its materials

    try:
        # Get materials which are used in the connectionId
        api_response = api_instance.get_welding_materials(project_id, connection_id)
        print("The response of MaterialApi->get_welding_materials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->get_welding_materials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to get its materials | 

### Return type

**List[object]**

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

