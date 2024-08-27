# connection_restapi_client_poc.LoadEffectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_load_effect**](LoadEffectApi.md#add_load_effect) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | Add new load effect to the connection
[**delete_load_effect**](LoadEffectApi.md#delete_load_effect) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Delete load effect loadEffectId
[**get_load_effect**](LoadEffectApi.md#get_load_effect) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Get load impulses from loadEffectId
[**get_load_effects**](LoadEffectApi.md#get_load_effects) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | Get all load effects which are defined in connectionId
[**set_loads_in_equilibrium**](LoadEffectApi.md#set_loads_in_equilibrium) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/set-equilibrium | Update the option &#39;LoadsInEquilibrium&#39; for connectionId
[**update_load_effect**](LoadEffectApi.md#update_load_effect) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Update load impulses in loadEffectId


# **add_load_effect**
> LoadEffectData add_load_effect(project_id, connection_id, con_load_effect=con_load_effect)

Add new load effect to the connection

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_load_effect import ConLoadEffect
from connection_restapi_client_poc.models.load_effect_data import LoadEffectData
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
    con_load_effect = connection_restapi_client_poc.ConLoadEffect() # ConLoadEffect |  (optional)

    try:
        # Add new load effect to the connection
        api_response = api_instance.add_load_effect(project_id, connection_id, con_load_effect=con_load_effect)
        print("The response of LoadEffectApi->add_load_effect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->add_load_effect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **con_load_effect** | [**ConLoadEffect**](ConLoadEffect.md)|  | [optional] 

### Return type

[**LoadEffectData**](LoadEffectData.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_load_effect**
> int delete_load_effect(project_id, connection_id, load_effect_id)

Delete load effect loadEffectId

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
        # Delete load effect loadEffectId
        api_response = api_instance.delete_load_effect(project_id, connection_id, load_effect_id)
        print("The response of LoadEffectApi->delete_load_effect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->delete_load_effect: %s\n" % e)
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

# **get_load_effect**
> ConLoadEffect get_load_effect(project_id, connection_id, load_effect_id, is_percentage=is_percentage)

Get load impulses from loadEffectId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_load_effect import ConLoadEffect
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
        # Get load impulses from loadEffectId
        api_response = api_instance.get_load_effect(project_id, connection_id, load_effect_id, is_percentage=is_percentage)
        print("The response of LoadEffectApi->get_load_effect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->get_load_effect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **load_effect_id** | **int**|  | 
 **is_percentage** | **bool**|  | [optional] 

### Return type

[**ConLoadEffect**](ConLoadEffect.md)

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

# **get_load_effects**
> List[ConLoadEffect] get_load_effects(project_id, connection_id, is_percentage=is_percentage)

Get all load effects which are defined in connectionId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_load_effect import ConLoadEffect
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
        # Get all load effects which are defined in connectionId
        api_response = api_instance.get_load_effects(project_id, connection_id, is_percentage=is_percentage)
        print("The response of LoadEffectApi->get_load_effects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->get_load_effects: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **is_percentage** | **bool**|  | [optional] 

### Return type

[**List[ConLoadEffect]**](ConLoadEffect.md)

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

# **set_loads_in_equilibrium**
> bool set_loads_in_equilibrium(project_id, connection_id, loads_in_equilibrium=loads_in_equilibrium)

Update the option 'LoadsInEquilibrium' for connectionId

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
    loads_in_equilibrium = True # bool | Value to be set (optional)

    try:
        # Update the option 'LoadsInEquilibrium' for connectionId
        api_response = api_instance.set_loads_in_equilibrium(project_id, connection_id, loads_in_equilibrium=loads_in_equilibrium)
        print("The response of LoadEffectApi->set_loads_in_equilibrium:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->set_loads_in_equilibrium: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **loads_in_equilibrium** | **bool**| Value to be set | [optional] 

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

# **update_load_effect**
> ConLoadEffect update_load_effect(project_id, connection_id, load_effect_id, con_load_effect=con_load_effect)

Update load impulses in loadEffectId

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_load_effect import ConLoadEffect
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
    con_load_effect = connection_restapi_client_poc.ConLoadEffect() # ConLoadEffect |  (optional)

    try:
        # Update load impulses in loadEffectId
        api_response = api_instance.update_load_effect(project_id, connection_id, load_effect_id, con_load_effect=con_load_effect)
        print("The response of LoadEffectApi->update_load_effect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoadEffectApi->update_load_effect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **load_effect_id** | **int**|  | 
 **con_load_effect** | [**ConLoadEffect**](ConLoadEffect.md)|  | [optional] 

### Return type

[**ConLoadEffect**](ConLoadEffect.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

