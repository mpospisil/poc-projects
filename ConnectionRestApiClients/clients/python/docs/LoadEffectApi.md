# connection_restapi_client_poc.LoadEffectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_load_effects_get**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_delete) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | 
[**api1_projects_project_id_connections_connection_id_load_effects_post**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | 
[**api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post**](LoadEffectApi.md#api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/set-equilibrium | 


# **api1_projects_project_id_connections_connection_id_load_effects_get**
> List[IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi] api1_projects_project_id_connections_connection_id_load_effects_get(project_id, connection_id, is_percentage=is_percentage)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
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

[**List[IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
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
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_get(project_id, connection_id, load_effect_id, is_percentage=is_percentage)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
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

[**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put(project_id, connection_id, load_effect_id, idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi
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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    load_effect_id = 56 # int | 
    idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_load_effect_id_put(project_id, connection_id, load_effect_id, idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api)
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
 **idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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
> LoadEffectDataIdeaStatiCaConnectionChecks api1_projects_project_id_connections_connection_id_load_effects_post(project_id, connection_id, idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi
from connection_restapi_client_poc.models.load_effect_data_idea_stati_ca_connection_checks import LoadEffectDataIdeaStatiCaConnectionChecks
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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api = connection_restapi_client_poc.IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi() # IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_post(project_id, connection_id, idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api=idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api)
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
 **idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api** | [**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)|  | [optional] 

### Return type

[**LoadEffectDataIdeaStatiCaConnectionChecks**](LoadEffectDataIdeaStatiCaConnectionChecks.md)

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

# **api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post**
> bool api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post(project_id, connection_id, loads_in_equilibrium=loads_in_equilibrium)



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
    api_instance = connection_restapi_client_poc.LoadEffectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    loads_in_equilibrium = True # bool |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post(project_id, connection_id, loads_in_equilibrium=loads_in_equilibrium)
        print("The response of LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->api1_projects_project_id_connections_connection_id_load_effects_set_equilibrium_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **loads_in_equilibrium** | **bool**|  | [optional] 

### Return type

**bool**

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

