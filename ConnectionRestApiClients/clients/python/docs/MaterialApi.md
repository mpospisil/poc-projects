# connection_restapi_client_poc.MaterialApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies | 
[**api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies | 
[**api1_projects_project_id_connections_connection_id_materials_cross_sections_get**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_cross_sections_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections | 
[**api1_projects_project_id_connections_connection_id_materials_cross_sections_post**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_cross_sections_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections | 
[**api1_projects_project_id_connections_connection_id_materials_get**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials | 
[**api1_projects_project_id_connections_connection_id_materials_pins_get**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_pins_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/pins | 
[**api1_projects_project_id_connections_connection_id_materials_pins_post**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_pins_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/pins | 
[**api1_projects_project_id_connections_connection_id_materials_post**](MaterialApi.md#api1_projects_project_id_connections_connection_id_materials_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials | 


# **api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get**
> List[IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get(project_id, connection_id)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post**
> IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_proj_bolt_assembly_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_cross_sections_get**
> List[IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_materials_cross_sections_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_cross_sections_get(project_id, connection_id)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_cross_sections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_cross_sections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_cross_sections_post**
> IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi api1_projects_project_id_connections_connection_id_materials_cross_sections_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_cross_sections_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_cross_sections_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_cross_sections_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_proj_cross_section_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_get**
> List[IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_materials_get(project_id, connection_id, type=type)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_material_type_ci_basic_types import IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    type = connection_restapi_client_poc.IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes() # IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_get(project_id, connection_id, type=type)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **type** | [**IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes**](.md)|  | [optional] 

### Return type

[**List[IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_pins_get**
> List[IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_materials_pins_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_pin_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_pins_get(project_id, connection_id)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_pins_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_pins_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_pins_post**
> IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi api1_projects_project_id_connections_connection_id_materials_pins_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_pin_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_pins_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_pins_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_pins_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi.md)

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

# **api1_projects_project_id_connections_connection_id_materials_post**
> IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi api1_projects_project_id_connections_connection_id_materials_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api import IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_post(project_id, connection_id, idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api=idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api)
        print("The response of MaterialApi->api1_projects_project_id_connections_connection_id_materials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MaterialApi->api1_projects_project_id_connections_connection_id_materials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_api_connection_model_proj_material_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)

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

