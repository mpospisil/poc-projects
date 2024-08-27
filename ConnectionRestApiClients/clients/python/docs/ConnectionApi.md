# connection_restapi_client_poc.ConnectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_operations**](ConnectionApi.md#delete_operations) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/operations | Delete all operations for the connection
[**get_all_connections_data**](ConnectionApi.md#get_all_connections_data) | **GET** /api/1/projects/{projectId}/connections | Get data about all connections in the project
[**get_connection_data**](ConnectionApi.md#get_connection_data) | **GET** /api/1/projects/{projectId}/connections/{connectionId} | Get data about a specific connection in the project
[**get_missing_welds**](ConnectionApi.md#get_missing_welds) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/missing-welds | Get missing welds in the connection
[**get_operations**](ConnectionApi.md#get_operations) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/operations | Get the list of operations for the connection
[**get_production_cost**](ConnectionApi.md#get_production_cost) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/production-cost | Get production cost of the connection
[**update_connection_data**](ConnectionApi.md#update_connection_data) | **PUT** /api/1/projects/{projectId}/connections/{connectionId} | Update data of a specific connection in the project


# **delete_operations**
> OkObjectResult delete_operations(project_id, connection_id)

Delete all operations for the connection

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.ok_object_result import OkObjectResult
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to be modified

    try:
        # Delete all operations for the connection
        api_response = api_instance.delete_operations(project_id, connection_id)
        print("The response of ConnectionApi->delete_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->delete_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to be modified | 

### Return type

[**OkObjectResult**](OkObjectResult.md)

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

# **get_all_connections_data**
> List[ConConnection] get_all_connections_data(project_id)

Get data about all connections in the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_connection import ConConnection
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service

    try:
        # Get data about all connections in the project
        api_response = api_instance.get_all_connections_data(project_id)
        print("The response of ConnectionApi->get_all_connections_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->get_all_connections_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 

### Return type

[**List[ConConnection]**](ConConnection.md)

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

# **get_connection_data**
> ConConnection get_connection_data(project_id, connection_id)

Get data about a specific connection in the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_connection import ConConnection
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | The id of the requested connection

    try:
        # Get data about a specific connection in the project
        api_response = api_instance.get_connection_data(project_id, connection_id)
        print("The response of ConnectionApi->get_connection_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->get_connection_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| The id of the requested connection | 

### Return type

[**ConConnection**](ConConnection.md)

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

# **get_missing_welds**
> List[ConMissingWeld] get_missing_welds(project_id, connection_id)

Get missing welds in the connection

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_missing_weld import ConMissingWeld
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the requested connection in the project

    try:
        # Get missing welds in the connection
        api_response = api_instance.get_missing_welds(project_id, connection_id)
        print("The response of ConnectionApi->get_missing_welds:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->get_missing_welds: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the requested connection in the project | 

### Return type

[**List[ConMissingWeld]**](ConMissingWeld.md)

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

# **get_operations**
> List[ConOperation] get_operations(project_id, connection_id)

Get the list of operations for the connection

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_operation import ConOperation
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the requested connection

    try:
        # Get the list of operations for the connection
        api_response = api_instance.get_operations(project_id, connection_id)
        print("The response of ConnectionApi->get_operations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->get_operations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the requested connection | 

### Return type

[**List[ConOperation]**](ConOperation.md)

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

# **get_production_cost**
> ConProductionCost get_production_cost(project_id, connection_id)

Get production cost of the connection

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_production_cost import ConProductionCost
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the requested connection

    try:
        # Get production cost of the connection
        api_response = api_instance.get_production_cost(project_id, connection_id)
        print("The response of ConnectionApi->get_production_cost:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->get_production_cost: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the requested connection | 

### Return type

[**ConProductionCost**](ConProductionCost.md)

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

# **update_connection_data**
> ConConnection update_connection_data(project_id, connection_id, con_connection=con_connection)

Update data of a specific connection in the project

### Example


```python
import connection_restapi_client_poc
from connection_restapi_client_poc.models.con_connection import ConConnection
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
    api_instance = connection_restapi_client_poc.ConnectionApi(api_client)
    project_id = 'project_id_example' # str | The unique identifier of the opened project in the ConnectionRestApi service
    connection_id = 56 # int | Id of the connection to be update
    con_connection = connection_restapi_client_poc.ConConnection() # ConConnection | New connection data to be set (optional)

    try:
        # Update data of a specific connection in the project
        api_response = api_instance.update_connection_data(project_id, connection_id, con_connection=con_connection)
        print("The response of ConnectionApi->update_connection_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ConnectionApi->update_connection_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**| The unique identifier of the opened project in the ConnectionRestApi service | 
 **connection_id** | **int**| Id of the connection to be update | 
 **con_connection** | [**ConConnection**](ConConnection.md)| New connection data to be set | [optional] 

### Return type

[**ConConnection**](ConConnection.md)

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

