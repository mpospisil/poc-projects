# connection-restapi-client-poc.MemberApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api1_projects_project_id_connections_connection_id_members_get**](MemberApi.md#api1_projects_project_id_connections_connection_id_members_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members | 
[**api1_projects_project_id_connections_connection_id_members_member_id_get**](MemberApi.md#api1_projects_project_id_connections_connection_id_members_member_id_get) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} | 
[**api1_projects_project_id_connections_connection_id_members_member_id_put**](MemberApi.md#api1_projects_project_id_connections_connection_id_members_member_id_put) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} | 


# **api1_projects_project_id_connections_connection_id_members_get**
> List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin] api1_projects_project_id_connections_connection_id_members_get(project_id, connection_id)



### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.MemberApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_members_get(project_id, connection_id)
        print("The response of MemberApi->api1_projects_project_id_connections_connection_id_members_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api1_projects_project_id_connections_connection_id_members_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 

### Return type

[**List[IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin]**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_members_member_id_get**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_members_member_id_get(project_id, connection_id, member_id)



### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.MemberApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    member_id = 56 # int | 

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_members_member_id_get(project_id, connection_id, member_id)
        print("The response of MemberApi->api1_projects_project_id_connections_connection_id_members_member_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api1_projects_project_id_connections_connection_id_members_member_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **member_id** | **int**|  | 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin.md)

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

# **api1_projects_project_id_connections_connection_id_members_member_id_put**
> IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin api1_projects_project_id_connections_connection_id_members_member_id_put(project_id, connection_id, member_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin)



### Example


```python
import connection-restapi-client-poc
from connection-restapi-client-poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin
from connection-restapi-client-poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = connection-restapi-client-poc.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with connection-restapi-client-poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = connection-restapi-client-poc.MemberApi(api_client)
    project_id = 'project_id_example' # str | 
    connection_id = 56 # int | 
    member_id = 56 # int | 
    idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin = connection-restapi-client-poc.IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin() # IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin |  (optional)

    try:
        api_response = api_instance.api1_projects_project_id_connections_connection_id_members_member_id_put(project_id, connection_id, member_id, idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin=idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin)
        print("The response of MemberApi->api1_projects_project_id_connections_connection_id_members_member_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api1_projects_project_id_connections_connection_id_members_member_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 
 **connection_id** | **int**|  | 
 **member_id** | **int**|  | 
 **idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_member_idea_stati_ca_plugin** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin.md)|  | [optional] 

### Return type

[**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConMemberIdeaStatiCaPlugin.md)

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

