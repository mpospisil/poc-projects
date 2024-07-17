# openapi_client.ConConnectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_con_connection_project_id_connection_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_get) | **GET** /api/1/ConConnection/{projectId}/Connection | 
[**api1_con_connection_project_id_connection_id_connection_put**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_connection_put) | **PUT** /api/1/ConConnection/{projectId}/{connectionId}/Connection | 
[**api1_con_connection_project_id_connection_id_export_iom_connection_data_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_export_iom_connection_data_get) | **GET** /api/1/ConConnection/{projectId}/{connectionId}/ExportIOMConnectionData | 
[**api1_con_connection_project_id_connection_id_export_iom_model_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_export_iom_model_get) | **GET** /api/1/ConConnection/{projectId}/{connectionId}/ExportIOMModel | 
[**api1_con_connection_project_id_connection_id_missing_welds_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_missing_welds_get) | **GET** /api/1/ConConnection/{projectId}/{connectionId}/MissingWelds | 
[**api1_con_connection_project_id_connection_id_operations_delete**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_operations_delete) | **DELETE** /api/1/ConConnection/{projectId}/{connectionId}/Operations | 
[**api1_con_connection_project_id_connection_id_operations_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_operations_get) | **GET** /api/1/ConConnection/{projectId}/{connectionId}/Operations | 
[**api1_con_connection_project_id_connection_id_production_cost_get**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_production_cost_get) | **GET** /api/1/ConConnection/{projectId}/{connectionId}/production-cost | 
[**api1_con_connection_project_id_connection_id_update_project_from_iom_file_post**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_update_project_from_iom_file_post) | **POST** /api/1/ConConnection/{projectId}/{connectionId}/UpdateProjectFromIOMFile | Update an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_con_connection_project_id_connection_id_update_project_from_iom_post**](ConConnectionApi.md#api1_con_connection_project_id_connection_id_update_project_from_iom_post) | **POST** /api/1/ConConnection/{projectId}/{connectionId}/UpdateProjectFromIOM | Update an IDEA Connection project based on OpenModelContainer (model and results)


# **api1_con_connection_project_id_connection_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin] api1_con_connection_project_id_connection_get(project_id, connection_id=connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int |  (optional)

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_get(project_id, connection_id=connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | [optional] 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.md)

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

# **api1_con_connection_project_id_connection_id_connection_put**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin api1_con_connection_project_id_connection_id_connection_put(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin = openapi_client.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_connection_put(project_id, connection_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_connection_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_connection_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.md)

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

# **api1_con_connection_project_id_connection_id_export_iom_connection_data_get**
> IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel api1_con_connection_project_id_connection_id_export_iom_connection_data_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_connection_connection_data_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_export_iom_connection_data_get(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_export_iom_connection_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_export_iom_connection_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel**](IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_con_connection_project_id_connection_id_export_iom_model_get**
> api1_con_connection_project_id_connection_id_export_iom_model_get(project_id, connection_id, version=version)



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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    version = 'version_example' # str |  (optional)

    try:
        api_instance.api1_con_connection_project_id_connection_id_export_iom_model_get(project_id, connection_id, version=version)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_export_iom_model_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **version** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_con_connection_project_id_connection_id_missing_welds_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin] api1_con_connection_project_id_connection_id_missing_welds_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_missing_weld_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_missing_welds_get(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_missing_welds_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_missing_welds_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMissingWeldIdeaStatiCaPlugin.md)

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

# **api1_con_connection_project_id_connection_id_operations_delete**
> MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore api1_con_connection_project_id_connection_id_operations_delete(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.microsoft_asp_net_core_mvc_ok_object_result_microsoft_asp_net_core_mvc_core import MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_operations_delete(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_operations_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_operations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore**](MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_con_connection_project_id_connection_id_operations_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConOperationIdeaStatiCaPlugin] api1_con_connection_project_id_connection_id_operations_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_operation_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConOperationIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_operations_get(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_operations_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_operations_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConOperationIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConOperationIdeaStatiCaPlugin.md)

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

# **api1_con_connection_project_id_connection_id_production_cost_get**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConProductionCostIdeaStatiCaPlugin api1_con_connection_project_id_connection_id_production_cost_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_production_cost_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConProductionCostIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_connection_project_id_connection_id_production_cost_get(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_production_cost_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_production_cost_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConProductionCostIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConProductionCostIdeaStatiCaPlugin.md)

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

# **api1_con_connection_project_id_connection_id_update_project_from_iom_file_post**
> bool api1_con_connection_project_id_connection_id_update_project_from_iom_file_post(project_id, connection_id)

Update an IDEA Connection project based on OpenModelContainer (model and results)

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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        # Update an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_con_connection_project_id_connection_id_update_project_from_iom_file_post(project_id, connection_id)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_update_project_from_iom_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_update_project_from_iom_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/xml, text/xml, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api1_con_connection_project_id_connection_id_update_project_from_iom_post**
> bool api1_con_connection_project_id_connection_id_update_project_from_iom_post(project_id, connection_id, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)

Update an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_open_model_container_idea_rs_open_model import IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel
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
    api_instance = openapi_client.ConConnectionApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    idea_rs_open_model_open_model_container_idea_rs_open_model = openapi_client.IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel() # IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Update an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_con_connection_project_id_connection_id_update_project_from_iom_post(project_id, connection_id, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)
        print("The response of ConConnectionApi->api1_con_connection_project_id_connection_id_update_project_from_iom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConConnectionApi->api1_con_connection_project_id_connection_id_update_project_from_iom_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **idea_rs_open_model_open_model_container_idea_rs_open_model** | [**IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel**](IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel.md)|  | [optional] 

### Return type

**bool**

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

