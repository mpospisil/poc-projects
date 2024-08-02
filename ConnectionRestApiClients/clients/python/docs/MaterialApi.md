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
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin
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

[**List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin.md)

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
> IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin
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
    idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_bolt_assemblies_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin)
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
 **idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_bolt_assembly_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjBoltAssemblyIdeaStatiCaPlugin.md)

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
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_materials_cross_sections_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin
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

[**List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin.md)

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
> IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_materials_cross_sections_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin
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
    idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_cross_sections_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin)
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
 **idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_cross_section_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjCrossSectionIdeaStatiCaPlugin.md)

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
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_materials_get(project_id, connection_id, type=type)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rsws_lib_css_service_material_type_ci_basic_types import IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin
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

[**List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin.md)

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
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_materials_pins_get(project_id, connection_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_pin_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin
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

[**List[IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin.md)

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
> IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_materials_pins_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_pin_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin
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
    idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_pins_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin)
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
 **idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjPinIdeaStatiCaPlugin.md)

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
> IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_materials_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin
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
    idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin = connection_restapi_client_poc.IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_materials_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin)
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
 **idea_stati_ca_plugin_api_connection_rest_model_model_project_proj_material_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectProjMaterialIdeaStatiCaPlugin.md)

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

