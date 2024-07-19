# connection_restapi_client_poc.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_connect_client_get**](ProjectApi.md#api1_connect_client_get) | **GET** /api/1/connect-client | 
[**api1_projects_get**](ProjectApi.md#api1_projects_get) | **GET** /api/1/projects | 
[**api1_projects_import_iom_file_post**](ProjectApi.md#api1_projects_import_iom_file_post) | **POST** /api/1/projects/import-iom-file | Creates an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_projects_import_iom_post**](ProjectApi.md#api1_projects_import_iom_post) | **POST** /api/1/projects/import-iom | Creates an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_projects_open_post**](ProjectApi.md#api1_projects_open_post) | **POST** /api/1/projects/open | 
[**api1_projects_project_id_close_get**](ProjectApi.md#api1_projects_project_id_close_get) | **GET** /api/1/projects/{projectId}/close | 
[**api1_projects_project_id_connection_setup_get**](ProjectApi.md#api1_projects_project_id_connection_setup_get) | **GET** /api/1/projects/{projectId}/connection-setup | 
[**api1_projects_project_id_connection_setup_put**](ProjectApi.md#api1_projects_project_id_connection_setup_put) | **PUT** /api/1/projects/{projectId}/connection-setup | 
[**api1_projects_project_id_download_get**](ProjectApi.md#api1_projects_project_id_download_get) | **GET** /api/1/projects/{projectId}/download | 
[**api1_projects_project_id_project_data_get**](ProjectApi.md#api1_projects_project_id_project_data_get) | **GET** /api/1/projects/{projectId}/project-data | 
[**api1_projects_project_id_update_iom_file_post**](ProjectApi.md#api1_projects_project_id_update_iom_file_post) | **POST** /api/1/projects/{projectId}/update-iom-file | Update an IDEA Connection project based on OpenModelContainer (model and results)
[**api1_projects_project_id_update_iom_post**](ProjectApi.md#api1_projects_project_id_update_iom_post) | **POST** /api/1/projects/{projectId}/update-iom | Update an IDEA Connection project based on OpenModelContainer (model and results)


# **api1_connect_client_get**
> str api1_connect_client_get()



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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)

    try:
        api_response = api_instance.api1_connect_client_get()
        print("The response of ProjectApi->api1_connect_client_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_connect_client_get: %s\n" % e)
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

# **api1_projects_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin] api1_projects_get()



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)

    try:
        api_response = api_instance.api1_projects_get()
        print("The response of ProjectApi->api1_projects_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_get: %s\n" % e)
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

# **api1_projects_import_iom_file_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_projects_import_iom_file_post(connections_to_create=connections_to_create)

Creates an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    connections_to_create = [56] # List[int] |  (optional)

    try:
        # Creates an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_projects_import_iom_file_post(connections_to_create=connections_to_create)
        print("The response of ProjectApi->api1_projects_import_iom_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_import_iom_file_post: %s\n" % e)
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

# **api1_projects_import_iom_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_projects_import_iom_post(connections_to_create=connections_to_create, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)

Creates an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rs_open_model_open_model_container_idea_rs_open_model import IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    connections_to_create = [56] # List[int] |  (optional)
    idea_rs_open_model_open_model_container_idea_rs_open_model = connection_restapi_client_poc.IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel() # IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Creates an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_projects_import_iom_post(connections_to_create=connections_to_create, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)
        print("The response of ProjectApi->api1_projects_import_iom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_import_iom_post: %s\n" % e)
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

# **api1_projects_open_post**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin api1_projects_open_post()



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)

    try:
        api_response = api_instance.api1_projects_open_post()
        print("The response of ProjectApi->api1_projects_open_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_open_post: %s\n" % e)
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

# **api1_projects_project_id_close_get**
> str api1_projects_project_id_close_get(project_id)



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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # 
        api_response = api_instance.api1_projects_project_id_close_get(project_id)
        print("The response of ProjectApi->api1_projects_project_id_close_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_close_get: %s\n" % e)
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

# **api1_projects_project_id_connection_setup_get**
> IdeaRSOpenModelConnectionSetupIdeaRSOpenModel api1_projects_project_id_connection_setup_get(project_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_projects_project_id_connection_setup_get(project_id)
        print("The response of ProjectApi->api1_projects_project_id_connection_setup_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_connection_setup_get: %s\n" % e)
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

# **api1_projects_project_id_connection_setup_put**
> IdeaRSOpenModelConnectionSetupIdeaRSOpenModel api1_projects_project_id_connection_setup_put(project_id, idea_rs_open_model_connection_setup_idea_rs_open_model=idea_rs_open_model_connection_setup_idea_rs_open_model)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rs_open_model_connection_setup_idea_rs_open_model import IdeaRSOpenModelConnectionSetupIdeaRSOpenModel
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_rs_open_model_connection_setup_idea_rs_open_model = connection_restapi_client_poc.IdeaRSOpenModelConnectionSetupIdeaRSOpenModel() # IdeaRSOpenModelConnectionSetupIdeaRSOpenModel |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connection_setup_put(project_id, idea_rs_open_model_connection_setup_idea_rs_open_model=idea_rs_open_model_connection_setup_idea_rs_open_model)
        print("The response of ProjectApi->api1_projects_project_id_connection_setup_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_connection_setup_put: %s\n" % e)
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

# **api1_projects_project_id_download_get**
> SystemIOMemoryStreamSystemPrivateCoreLib api1_projects_project_id_download_get(project_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_projects_project_id_download_get(project_id)
        print("The response of ProjectApi->api1_projects_project_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_download_get: %s\n" % e)
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

# **api1_projects_project_id_project_data_get**
> IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin api1_projects_project_id_project_data_get(project_id)



### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_project_con_project_data_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelProjectConProjectDataIdeaStatiCaPlugin
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        api_response = api_instance.api1_projects_project_id_project_data_get(project_id)
        print("The response of ProjectApi->api1_projects_project_id_project_data_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_project_data_get: %s\n" % e)
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

# **api1_projects_project_id_update_iom_file_post**
> bool api1_projects_project_id_update_iom_file_post(project_id)

Update an IDEA Connection project based on OpenModelContainer (model and results)

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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Update an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_projects_project_id_update_iom_file_post(project_id)
        print("The response of ProjectApi->api1_projects_project_id_update_iom_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_update_iom_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

# **api1_projects_project_id_update_iom_post**
> bool api1_projects_project_id_update_iom_post(project_id, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)

Update an IDEA Connection project based on OpenModelContainer (model and results)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_rs_open_model_open_model_container_idea_rs_open_model import IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel
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
    api_instance = connection_restapi_client_poc.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 
    idea_rs_open_model_open_model_container_idea_rs_open_model = connection_restapi_client_poc.IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel() # IdeaRSOpenModelOpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Update an IDEA Connection project based on OpenModelContainer (model and results)
        api_response = api_instance.api1_projects_project_id_update_iom_post(project_id, idea_rs_open_model_open_model_container_idea_rs_open_model=idea_rs_open_model_open_model_container_idea_rs_open_model)
        print("The response of ProjectApi->api1_projects_project_id_update_iom_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->api1_projects_project_id_update_iom_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
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

