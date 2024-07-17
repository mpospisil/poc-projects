# openapi_client.ConProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_con_project_connect_client_get**](ConProjectApi.md#api1_con_project_connect_client_get) | **GET** /api/1/ConProject/ConnectClient | 
[**api1_con_project_create_project_from_iom_file_post**](ConProjectApi.md#api1_con_project_create_project_from_iom_file_post) | **POST** /api/1/ConProject/CreateProjectFromIOMFile | Creates an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_con_project_create_project_from_iom_post**](ConProjectApi.md#api1_con_project_create_project_from_iom_post) | **POST** /api/1/ConProject/CreateProjectFromIOM | Creates an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_con_project_project_get**](ConProjectApi.md#api1_con_project_project_get) | **GET** /api/1/ConProject/Project | 
[**api1_con_project_project_id_close_get**](ConProjectApi.md#api1_con_project_project_id_close_get) | **GET** /api/1/ConProject/{projectId}/Close | 
[**api1_con_project_project_id_connection_id_ifc_get**](ConProjectApi.md#api1_con_project_project_id_connection_id_ifc_get) | **GET** /api/1/ConProject/{projectId}/{connectionId}/Ifc | 
[**api1_con_project_project_id_connection_setup_get**](ConProjectApi.md#api1_con_project_project_id_connection_setup_get) | **GET** /api/1/ConProject/{projectId}/ConnectionSetup | 
[**api1_con_project_project_id_connection_setup_put**](ConProjectApi.md#api1_con_project_project_id_connection_setup_put) | **PUT** /api/1/ConProject/{projectId}/ConnectionSetup | 
[**api1_con_project_project_id_download_get**](ConProjectApi.md#api1_con_project_project_id_download_get) | **GET** /api/1/ConProject/{projectId}/Download | 
[**api1_con_project_project_id_project_data_get**](ConProjectApi.md#api1_con_project_project_id_project_data_get) | **GET** /api/1/ConProject/{projectId}/ProjectData | 
[**api1_con_project_project_post**](ConProjectApi.md#api1_con_project_project_post) | **POST** /api/1/ConProject/Project | 


# **api1_con_project_connect_client_get**
> str api1_con_project_connect_client_get()



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
    api_instance = openapi_client.ConProjectApi(api_client)

    try:
        api_response = api_instance.api1_con_project_connect_client_get()
        print("The response of ConProjectApi->api1_con_project_connect_client_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_connect_client_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**str**

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

# **api1_con_project_create_project_from_iom_file_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_con_project_create_project_from_iom_file_post(connections_to_create=connections_to_create)

Creates an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConProjectApi(api_client)
    connections_to_create = [56] # List[int] |  (optional)

    try:
        # Creates an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_con_project_create_project_from_iom_file_post(connections_to_create=connections_to_create)
        print("The response of ConProjectApi->api1_con_project_create_project_from_iom_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_create_project_from_iom_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_to_create** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin.md)

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

# **api1_con_project_create_project_from_iom_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_con_project_create_project_from_iom_post(connections_to_create=connections_to_create, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)

Creates an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_open_model_container_idea_rs_open_model import IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConProjectApi(api_client)
    connections_to_create = [56] # List[int] |  (optional)
    idea_rs_open_model_open_model_container_idea_rs_open_model = openapi_client.IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel() # IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Creates an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_con_project_create_project_from_iom_post(connections_to_create=connections_to_create, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)
        print("The response of ConProjectApi->api1_con_project_create_project_from_iom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_create_project_from_iom_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_to_create** | [**List[int]**](int.md)|  | [optional] 
 **idea_rs_open_model_open_model_container_idea_rs_open_model** | [**IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel**](IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin.md)

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

# **api1_con_project_project_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin] api1_con_project_project_get()



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConProjectApi(api_client)

    try:
        api_response = api_instance.api1_con_project_project_get()
        print("The response of ConProjectApi->api1_con_project_project_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin.md)

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

# **api1_con_project_project_id_close_get**
> str api1_con_project_project_id_close_get(project_id)



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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # 
        api_response = api_instance.api1_con_project_project_id_close_get(project_id)
        print("The response of ConProjectApi->api1_con_project_project_id_close_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_close_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

**str**

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

# **api1_con_project_project_id_connection_id_ifc_get**
> SystemIOMemoryStreamSystemPrivateCoreLib api1_con_project_project_id_connection_id_ifc_get(project_id, connection_id)



### Example


```python
import openapi_client
from openapi_client.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_con_project_project_id_connection_id_ifc_get(project_id, connection_id)
        print("The response of ConProjectApi->api1_con_project_project_id_connection_id_ifc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_connection_id_ifc_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**SystemIOMemoryStreamSystemPrivateCoreLib**](SystemIOMemoryStreamSystemPrivateCoreLib.md)

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

# **api1_con_project_project_id_connection_setup_get**
> IdeaRSOpenModelConnectionSetupIdeaRSOpenModel api1_con_project_project_id_connection_setup_get(project_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_con_project_project_id_connection_setup_get(project_id)
        print("The response of ConProjectApi->api1_con_project_project_id_connection_setup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_connection_setup_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**IdeaRSOpenModelConnectionSetupIdeaRSOpenModel**](IdeaRSOpenModelConnectionSetupIdeaRSOpenModel.md)

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

# **api1_con_project_project_id_connection_setup_put**
> IdeaRSOpenModelConnectionSetupIdeaRSOpenModel api1_con_project_project_id_connection_setup_put(project_id, idea_rs_open_model_connection_setup_idea_rs_open_model=idea_rs_open_model_connection_setup_idea_rs_open_model)



### Example


```python
import openapi_client
from openapi_client.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_rs_open_model_connection_setup_idea_rs_open_model = openapi_client.IdeaRSOpenModelConnectionSetupIdeaRSOpenModel() # IdeaRSOpenModelConnectionSetupIdeaRSOpenModel |  (optional)

    try:
        api_response = api_instance.api1_con_project_project_id_connection_setup_put(project_id, idea_rs_open_model_connection_setup_idea_rs_open_model=idea_rs_open_model_connection_setup_idea_rs_open_model)
        print("The response of ConProjectApi->api1_con_project_project_id_connection_setup_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_connection_setup_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **idea_rs_open_model_connection_setup_idea_rs_open_model** | [**IdeaRSOpenModelConnectionSetupIdeaRSOpenModel**](IdeaRSOpenModelConnectionSetupIdeaRSOpenModel.md)|  | [optional] 

### Return type

[**IdeaRSOpenModelConnectionSetupIdeaRSOpenModel**](IdeaRSOpenModelConnectionSetupIdeaRSOpenModel.md)

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

# **api1_con_project_project_id_download_get**
> SystemIOMemoryStreamSystemPrivateCoreLib api1_con_project_project_id_download_get(project_id)



### Example


```python
import openapi_client
from openapi_client.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_con_project_project_id_download_get(project_id)
        print("The response of ConProjectApi->api1_con_project_project_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**SystemIOMemoryStreamSystemPrivateCoreLib**](SystemIOMemoryStreamSystemPrivateCoreLib.md)

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

# **api1_con_project_project_id_project_data_get**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin api1_con_project_project_id_project_data_get(project_id)



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_data_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_con_project_project_id_project_data_get(project_id)
        print("The response of ConProjectApi->api1_con_project_project_id_project_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_id_project_data_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin.md)

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

# **api1_con_project_project_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_con_project_project_post()



### Example


```python
import openapi_client
from openapi_client.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = openapi_client.ConProjectApi(api_client)

    try:
        api_response = api_instance.api1_con_project_project_post()
        print("The response of ConProjectApi->api1_con_project_project_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConProjectApi->api1_con_project_project_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin.md)

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

