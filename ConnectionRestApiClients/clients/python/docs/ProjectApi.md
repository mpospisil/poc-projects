# ideastatica_connection_api.ProjectApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close_project**](ProjectApi.md#close_project) | **GET** /api/1/projects/{projectId}/close | Close the project. Needed for releasing resources in the service.
[**download_project**](ProjectApi.md#download_project) | **GET** /api/1/projects/{projectId}/download | Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
[**get_active_projects**](ProjectApi.md#get_active_projects) | **GET** /api/1/projects | Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ClientController.ConnectClient
[**get_project_data**](ProjectApi.md#get_project_data) | **GET** /api/1/projects/{projectId} | Get data of the project.
[**get_setup**](ProjectApi.md#get_setup) | **GET** /api/1/projects/{projectId}/connection-setup | Get setup from project
[**import_iom**](ProjectApi.md#import_iom) | **POST** /api/1/projects/import-iom-file | Creates an IDEA Connection project. IOM is passed in the body of the request.
[**import_iom_container**](ProjectApi.md#import_iom_container) | **POST** /api/1/projects/import-iom | Creates an IDEA Connection project from model (model and results)
[**open_project**](ProjectApi.md#open_project) | **POST** /api/1/projects/open | Open ideacon project from ideaConFile
[**update_from_iom**](ProjectApi.md#update_from_iom) | **POST** /api/1/projects/{projectId}/update-iom-file | Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.
[**update_from_iom_container**](ProjectApi.md#update_from_iom_container) | **POST** /api/1/projects/{projectId}/update-iom | Update an IDEA Connection project by model (model and results)
[**update_project_data**](ProjectApi.md#update_project_data) | **PUT** /api/1/projects/{projectId} | Updates ConProjectData of project
[**update_setup**](ProjectApi.md#update_setup) | **PUT** /api/1/projects/{projectId}/connection-setup | Update setup of the project


# **close_project**
> str close_project(project_id)

Close the project. Needed for releasing resources in the service.

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
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

# **download_project**
> download_project(project_id)

Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service

    try:
        # Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
        api_instance.download_project(project_id)
    except Exception as e:
        print("Exception when calling ProjectApi->download_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 

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

# **get_active_projects**
> List[ConProject] get_active_projects()

Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ClientController.ConnectClient

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)

    try:
        # Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ClientController.ConnectClient
        api_response = api_instance.get_active_projects()
        print("The response of ProjectApi->get_active_projects:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->get_active_projects: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[ConProject]**](ConProject.md)

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
> ConProject get_project_data(project_id)

Get data of the project.

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
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

[**ConProject**](ConProject.md)

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
> ConnectionSetup get_setup(project_id)

Get setup from project

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.connection_setup import ConnectionSetup
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
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

[**ConnectionSetup**](ConnectionSetup.md)

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
> ConProject import_iom(connections_to_create=connections_to_create)

Creates an IDEA Connection project. IOM is passed in the body of the request.

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
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

[**ConProject**](ConProject.md)

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
> ConProject import_iom_container(connections_to_create=connections_to_create, open_model_container=open_model_container)

Creates an IDEA Connection project from model (model and results)

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.models.open_model_container import OpenModelContainer
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    connections_to_create = [56] # List[int] |  (optional)
    open_model_container = ideastatica_connection_api.OpenModelContainer() # OpenModelContainer |  (optional)

    try:
        # Creates an IDEA Connection project from model (model and results)
        api_response = api_instance.import_iom_container(connections_to_create=connections_to_create, open_model_container=open_model_container)
        print("The response of ProjectApi->import_iom_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->import_iom_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connections_to_create** | [**List[int]**](int.md)|  | [optional] 
 **open_model_container** | [**OpenModelContainer**](OpenModelContainer.md)|  | [optional] 

### Return type

[**ConProject**](ConProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **open_project**
> ConProject open_project(idea_con_file=idea_con_file)

Open ideacon project from ideaConFile

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    idea_con_file = None # bytearray |  (optional)

    try:
        # Open ideacon project from ideaConFile
        api_response = api_instance.open_project(idea_con_file=idea_con_file)
        print("The response of ProjectApi->open_project:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->open_project: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **idea_con_file** | **bytearray**|  | [optional] 

### Return type

[**ConProject**](ConProject.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
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
import ideastatica_connection_api
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
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
> bool update_from_iom_container(project_id, open_model_container=open_model_container)

Update an IDEA Connection project by model (model and results)

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.open_model_container import OpenModelContainer
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to be updated
    open_model_container = ideastatica_connection_api.OpenModelContainer() # OpenModelContainer |  (optional)

    try:
        # Update an IDEA Connection project by model (model and results)
        api_response = api_instance.update_from_iom_container(project_id, open_model_container=open_model_container)
        print("The response of ProjectApi->update_from_iom_container:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_from_iom_container: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to be updated | 
 **open_model_container** | [**OpenModelContainer**](OpenModelContainer.md)|  | [optional] 

### Return type

**bool**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_project_data**
> ConProject update_project_data(project_id, con_project_data=con_project_data)

Updates ConProjectData of project

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.con_project import ConProject
from ideastatica_connection_api.models.con_project_data import ConProjectData
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    project_id = 'project_id_example' # str | 
    con_project_data = ideastatica_connection_api.ConProjectData() # ConProjectData |  (optional)

    try:
        # Updates ConProjectData of project
        api_response = api_instance.update_project_data(project_id, con_project_data=con_project_data)
        print("The response of ProjectApi->update_project_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_project_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **con_project_data** | [**ConProjectData**](ConProjectData.md)|  | [optional] 

### Return type

[**ConProject**](ConProject.md)

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

# **update_setup**
> ConnectionSetup update_setup(project_id, connection_setup=connection_setup)

Update setup of the project

### Example


```python
import ideastatica_connection_api
from ideastatica_connection_api.models.connection_setup import ConnectionSetup
from ideastatica_connection_api.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ideastatica_connection_api.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ideastatica_connection_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ideastatica_connection_api.ProjectApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service to update project setup
    connection_setup = ideastatica_connection_api.ConnectionSetup() # ConnectionSetup |  (optional)

    try:
        # Update setup of the project
        api_response = api_instance.update_setup(project_id, connection_setup=connection_setup)
        print("The response of ProjectApi->update_setup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProjectApi->update_setup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service to update project setup | 
 **connection_setup** | [**ConnectionSetup**](ConnectionSetup.md)|  | [optional] 

### Return type

[**ConnectionSetup**](ConnectionSetup.md)

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

