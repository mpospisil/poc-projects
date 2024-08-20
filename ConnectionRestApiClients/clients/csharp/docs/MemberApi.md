# connection_restapi_client_poc.Api.MemberApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**GetAllMemberData**](MemberApi.md#getallmemberdata) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members | Get information about all members in the connection |
| [**GetMemberData**](MemberApi.md#getmemberdata) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} | Get information about the requires member in the connection |
| [**UpdateMember**](MemberApi.md#updatemember) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/members/{memberId} | Update the member in the connection by newMemberData |

<a id="getallmemberdata"></a>
# **GetAllMemberData**
> List&lt;IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi&gt; GetAllMemberData (Guid projectId, int connectionId)

Get information about all members in the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetAllMemberDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its members

            try
            {
                // Get information about all members in the connection
                List<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> result = apiInstance.GetAllMemberData(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.GetAllMemberData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetAllMemberDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get information about all members in the connection
    ApiResponse<List<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi>> response = apiInstance.GetAllMemberDataWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.GetAllMemberDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its members |  |

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

<a id="getmemberdata"></a>
# **GetMemberData**
> IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi GetMemberData (Guid projectId, int connectionId, int memberId)

Get information about the requires member in the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetMemberDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its member
            var memberId = 56;  // int | Id of the requested member in the connection

            try
            {
                // Get information about the requires member in the connection
                IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi result = apiInstance.GetMemberData(projectId, connectionId, memberId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.GetMemberData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMemberDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get information about the requires member in the connection
    ApiResponse<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> response = apiInstance.GetMemberDataWithHttpInfo(projectId, connectionId, memberId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.GetMemberDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its member |  |
| **memberId** | **int** | Id of the requested member in the connection |  |

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

<a id="updatemember"></a>
# **UpdateMember**
> IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi UpdateMember (Guid projectId, int connectionId, int memberId, IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi? ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi = null)

Update the member in the connection by newMemberData

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateMemberExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MemberApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to to update is membar memberId
            var memberId = 56;  // int | Id of the member to be ubdated in the connection
            var ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi? | New mwmbwr data (optional) 

            try
            {
                // Update the member in the connection by newMemberData
                IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi result = apiInstance.UpdateMember(projectId, connectionId, memberId, ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MemberApi.UpdateMember: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateMemberWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update the member in the connection by newMemberData
    ApiResponse<IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi> response = apiInstance.UpdateMemberWithHttpInfo(projectId, connectionId, memberId, ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MemberApi.UpdateMemberWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to to update is membar memberId |  |
| **memberId** | **int** | Id of the member to be ubdated in the connection |  |
| **ideaStatiCaApiConnectionModelConMemberIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConMemberIdeaStatiCaApi?.md) | New mwmbwr data | [optional]  |

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
