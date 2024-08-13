# connection_restapi_client_poc.Api.ParameterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPost**](ParameterApi.md#api1projectsprojectidconnectionsconnectionidevaluateexpressionpost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/evaluate-expression |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdParametersGet**](ParameterApi.md#api1projectsprojectidconnectionsconnectionidparametersget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/parameters |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdParametersPut**](ParameterApi.md#api1projectsprojectidconnectionsconnectionidparametersput) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/parameters |  |

<a id="api1projectsprojectidconnectionsconnectionidevaluateexpressionpost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPost**
> string Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPost (Guid projectId, int connectionId, string? body = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var body = "body_example";  // string? |  (optional) 

            try
            {
                string result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPost(projectId, connectionId, body);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<string> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPostWithHttpInfo(projectId, connectionId, body);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdEvaluateExpressionPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **body** | **string?** |  | [optional]  |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/*+xml, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidconnectionsconnectionidparametersget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdParametersGet**
> List&lt;IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdParametersGet (Guid projectId, int connectionId, bool? includeHidden = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdParametersGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var includeHidden = false;  // bool? |  (optional)  (default to false)

            try
            {
                List<IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdParametersGet(projectId, connectionId, includeHidden);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdParametersGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdParametersGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdParametersGetWithHttpInfo(projectId, connectionId, includeHidden);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdParametersGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **includeHidden** | **bool?** |  | [optional] [default to false] |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidparametersput"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdParametersPut**
> List&lt;IdeaRSCommonParametersParameterDataCIBasicTypes&gt; Api1ProjectsProjectIdConnectionsConnectionIdParametersPut (Guid projectId, int connectionId, List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>? ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdParametersPutExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi = new List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>?(); // List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>? |  (optional) 

            try
            {
                List<IdeaRSCommonParametersParameterDataCIBasicTypes> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdParametersPut(projectId, connectionId, ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdParametersPut: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdParametersPutWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaRSCommonParametersParameterDataCIBasicTypes>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdParametersPutWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.Api1ProjectsProjectIdConnectionsConnectionIdParametersPutWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi** | [**List&lt;IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi&gt;?**](IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi.md) |  | [optional]  |

### Return type

[**List&lt;IdeaRSCommonParametersParameterDataCIBasicTypes&gt;**](IdeaRSCommonParametersParameterDataCIBasicTypes.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/*+xml, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

