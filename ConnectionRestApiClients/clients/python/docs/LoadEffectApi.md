# openapi_client.LoadEffectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_load_effects_get**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_post**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | 


# **api1_projects_project_id_connections_connection_id_load_effects_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_load_effects_get(project_id, connection_id, is_percentage=is_percentage)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin
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
    api_instance = openapi_client.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    is_percentage = True # bool |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_get(project_id, connection_id, is_percentage=is_percentage)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **is_percentage** | **bool**|  | [optional] 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete**
> int api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete(project_id, connection_id, load_effect_id)



### Example


```python
import openapi_client
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
    api_instance = openapi_client.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    load_effect_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete(project_id, connection_id, load_effect_id)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **load_effect_id** | **int**|  | 

### Return type

**int**

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

# **api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get(project_id, connection_id, load_effect_id, is_percentage=is_percentage)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin
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
    api_instance = openapi_client.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    load_effect_id = 56 # int | 
    is_percentage = True # bool |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get(project_id, connection_id, load_effect_id, is_percentage=is_percentage)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **load_effect_id** | **int**|  | 
 **is_percentage** | **bool**|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put(project_id, connection_id, load_effect_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin
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
    api_instance = openapi_client.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    load_effect_id = 56 # int | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put(project_id, connection_id, load_effect_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **load_effect_id** | **int**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_load_effects_post**
> ConModelerConnectionPlugInLoadEffectDataIdeaStatiCaConnectionChecks api1_projects_project_id_connections_connection_id_load_effects_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin)



### Example


```python
import openapi_client
from openapi_client.models.con_modeler_connection_plug_in_load_effect_data_idea_stati_ca_connection_checks import ConModelerConnectionPlugInLoadEffectDataIdeaStatiCaConnectionChecks
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin
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
    api_instance = openapi_client.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_post(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_load_effect_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConLoadEffectIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**ConModelerConnectionPlugInLoadEffectDataIdeaStatiCaConnectionChecks**](ConModelerConnectionPlugInLoadEffectDataIdeaStatiCaConnectionChecks.md)

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

