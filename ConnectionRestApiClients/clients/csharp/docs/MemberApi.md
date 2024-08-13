# connection_restapi_client_poc.Api.MemberApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdConnectionsConnectionIdMembersGet**](MemberApi.md#api1projectsprojectidconnectionsconnectionidmembersget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGet**](MemberApi.md#api1projectsprojectidconnectionsconnectionidmembersmemberidget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPut**](MemberApi.md#api1projectsprojectidconnectionsconnectionidmembersmemberidput) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} |  |

<a id="api1projectsprojectidconnectionsconnectionidmembersget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMembersGet**
> List&lt;IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdMembersGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMembersGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                List<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMembersGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidconnectionsconnectionidmembersmemberidget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGet**
> IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGet (Guid projectId, int connectionId, int memberId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var memberId = 56;  // int | 

            try
            {
                IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGet(projectId, connectionId, memberId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGetWithHttpInfo(projectId, connectionId, memberId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **memberId** | **int** |  |  |

### Return type

[**IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidconnectionsconnectionidmembersmemberidput"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPut**
> IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPut (Guid projectId, int connectionId, int memberId, IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi? ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPutExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var memberId = 56;  // int | 
            var ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi? |  (optional) 

            try
            {
                IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPut(projectId, connectionId, memberId, ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPut: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPutWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPutWithHttpInfo(projectId, connectionId, memberId, ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.Api1ProjectsProjectIdConnectionsConnectionIdMembersMemberIdPutWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **memberId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

