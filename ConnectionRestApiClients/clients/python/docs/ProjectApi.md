# connection_restapi_client_poc.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_project**](ProjectApi.md#close_project) | **GET** /api/1/projects/{projectId}/close | Close the project. Needed for releasing resources in the service.
[**connect_client**](ProjectApi.md#connect_client) | **GET** /api/1/connect-client | Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.
[**download_project**](ProjectApi.md#download_project) | **GET** /api/1/projects/{projectId}/download | Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
[**get_active_projects**](ProjectApi.md#get_active_projects) | **GET** /api/1/projects | Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient
[**get_project_data**](ProjectApi.md#get_project_data) | **GET** /api/1/projects/{projectId}/project-data | Get data of the project.
[**get_setup**](ProjectApi.md#get_setup) | **GET** /api/1/projects/{projectId}/connection-setup | Get setup from project
[**import_iom**](ProjectApi.md#import_iom) | **POST** /api/1/projects/import-iom-file | Creates an IDEA Connection project. IOM is passed in the body of the request.
[**import_iom_container**](ProjectApi.md#import_iom_container) | **POST** /api/1/projects/import-iom | Creates an IDEA Connection project from model (model and results)
[**open_project**](ProjectApi.md#open_project) | **POST** /api/1/projects/open | Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method
[**update_from_iom**](ProjectApi.md#update_from_iom) | **POST** /api/1/projects/{projectId}/update-iom-file | Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.
[**update_from_iom_container**](ProjectApi.md#update_from_iom_container) | **POST** /api/1/projects/{projectId}/update-iom | Update an IDEA Connection project by model (model and results)
[**update_setup**](ProjectApi.md#update_setup) | **PUT** /api/1/projects/{projectId}/connection-setup | Update setup of the project


# **close_project**
> str close_project(project_id)

Close the project. Needed for releasing resources in the service.

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
    project_id = 'project_id_example' # str | The unique identifier of the project to be closed

    try:
        # Close the project. Needed for releasing resources in the service.
        api_response = api_instance.close_project(project_id)
        print("The response of ProjectApi->close_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->close_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the project to be closed | 

### Return type

**str**

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

# **connect_client**
> str connect_client()

Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.

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
        # Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.
        api_response = api_instance.connect_client()
        print("The response of ProjectApi->connect_client:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->connect_client: %s\n" % e)
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

# **download_project**
> SystemIOMemoryStreamSystemPrivateCoreLib download_project(project_id)

Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.

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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service

    try:
        # Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
        api_response = api_instance.download_project(project_id)
        print("The response of ProjectApi->download_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->download_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 

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

# **get_active_projects**
> List[IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi] get_active_projects()

Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi
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
        # Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient
        api_response = api_instance.get_active_projects()
        print("The response of ProjectApi->get_active_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_active_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

# **get_project_data**
> IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi get_project_data(project_id)

Get data of the project.

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_data_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi
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
    project_id = 'project_id_example' # str | The unique identifier of the requested project

    try:
        # Get data of the project.
        api_response = api_instance.get_project_data(project_id)
        print("The response of ProjectApi->get_project_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_project_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the requested project | 

### Return type

[**IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi.md)

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

# **get_setup**
> ConnectionSetupIdeaRSOpenModel get_setup(project_id)

Get setup from project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.connection_setup_idea_rs_open_model import ConnectionSetupIdeaRSOpenModel
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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to get setup

    try:
        # Get setup from project
        api_response = api_instance.get_setup(project_id)
        print("The response of ProjectApi->get_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to get setup | 

### Return type

[**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md)

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

# **import_iom**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi import_iom(connections_to_create=connections_to_create)

Creates an IDEA Connection project. IOM is passed in the body of the request.

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi
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
        # Creates an IDEA Connection project. IOM is passed in the body of the request.
        api_response = api_instance.import_iom(connections_to_create=connections_to_create)
        print("The response of ProjectApi->import_iom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->import_iom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_to_create** | [**List[int]**](int.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

# **import_iom_container**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi import_iom_container(connections_to_create=connections_to_create, open_model_container_idea_rs_open_model=open_model_container_idea_rs_open_model)

Creates an IDEA Connection project from model (model and results)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi
from connection_restapi_client_poc.models.open_model_container_idea_rs_open_model import OpenModelContainerIdeaRSOpenModel
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
    open_model_container_idea_rs_open_model = connection_restapi_client_poc.OpenModelContainerIdeaRSOpenModel() # OpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Creates an IDEA Connection project from model (model and results)
        api_response = api_instance.import_iom_container(connections_to_create=connections_to_create, open_model_container_idea_rs_open_model=open_model_container_idea_rs_open_model)
        print("The response of ProjectApi->import_iom_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->import_iom_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_to_create** | [**List[int]**](int.md)|  | [optional] 
 **open_model_container_idea_rs_open_model** | [**OpenModelContainerIdeaRSOpenModel**](OpenModelContainerIdeaRSOpenModel.md)|  | [optional] 

### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

# **open_project**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi open_project()

Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi
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
        # Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method
        api_response = api_instance.open_project()
        print("The response of ProjectApi->open_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->open_project: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

# **update_from_iom**
> bool update_from_iom(project_id)

Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.

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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to be updated

    try:
        # Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.
        api_response = api_instance.update_from_iom(project_id)
        print("The response of ProjectApi->update_from_iom:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_from_iom: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to be updated | 

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

# **update_from_iom_container**
> bool update_from_iom_container(project_id, open_model_container_idea_rs_open_model=open_model_container_idea_rs_open_model)

Update an IDEA Connection project by model (model and results)

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.open_model_container_idea_rs_open_model import OpenModelContainerIdeaRSOpenModel
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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to be updated
    open_model_container_idea_rs_open_model = connection_restapi_client_poc.OpenModelContainerIdeaRSOpenModel() # OpenModelContainerIdeaRSOpenModel |  (optional)

    try:
        # Update an IDEA Connection project by model (model and results)
        api_response = api_instance.update_from_iom_container(project_id, open_model_container_idea_rs_open_model=open_model_container_idea_rs_open_model)
        print("The response of ProjectApi->update_from_iom_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_from_iom_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to be updated | 
 **open_model_container_idea_rs_open_model** | [**OpenModelContainerIdeaRSOpenModel**](OpenModelContainerIdeaRSOpenModel.md)|  | [optional] 

### Return type

**bool**

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

# **update_setup**
> ConnectionSetupIdeaRSOpenModel update_setup(project_id, connection_setup_idea_rs_open_model=connection_setup_idea_rs_open_model)

Update setup of the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.connection_setup_idea_rs_open_model import ConnectionSetupIdeaRSOpenModel
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
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to update project setup
    connection_setup_idea_rs_open_model = connection_restapi_client_poc.ConnectionSetupIdeaRSOpenModel() # ConnectionSetupIdeaRSOpenModel |  (optional)

    try:
        # Update setup of the project
        api_response = api_instance.update_setup(project_id, connection_setup_idea_rs_open_model=connection_setup_idea_rs_open_model)
        print("The response of ProjectApi->update_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to update project setup | 
 **connection_setup_idea_rs_open_model** | [**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md)|  | [optional] 

### Return type

[**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md)

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

