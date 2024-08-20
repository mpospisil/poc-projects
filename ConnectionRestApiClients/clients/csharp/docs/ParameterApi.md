# connection_restapi_client_poc.Api.ParameterApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**EvaluateExpression**](ParameterApi.md#evaluateexpression) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/evaluate-expression | Evaluate the expression and return the result |
| [**GetParameters**](ParameterApi.md#getparameters) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/parameters | Get all parameters which are defined for projectId and connectionId |
| [**UpdateParameters**](ParameterApi.md#updateparameters) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/parameters | Update parameters for the connection connectionId in the project projectId by values passed in parameters |

<a id="evaluateexpression"></a>
# **EvaluateExpression**
> string EvaluateExpression (Guid projectId, int connectionId, string? body = null)

Evaluate the expression and return the result

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class EvaluateExpressionExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to use for evaluation expression
            var body = "body_example";  // string? | Expreession to evaluate (optional) 

            try
            {
                // Evaluate the expression and return the result
                string result = apiInstance.EvaluateExpression(projectId, connectionId, body);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.EvaluateExpression: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the EvaluateExpressionWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Evaluate the expression and return the result
    ApiResponse<string> response = apiInstance.EvaluateExpressionWithHttpInfo(projectId, connectionId, body);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.EvaluateExpressionWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to use for evaluation expression |  |
| **body** | **string?** | Expreession to evaluate | [optional]  |

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

<a id="getparameters"></a>
# **GetParameters**
> List&lt;IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi&gt; GetParameters (Guid projectId, int connectionId, bool? includeHidden = null)

Get all parameters which are defined for projectId and connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetParametersExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its parameters
            var includeHidden = false;  // bool? | Iclude also hdden parameters (optional)  (default to false)

            try
            {
                // Get all parameters which are defined for projectId and connectionId
                List<IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi> result = apiInstance.GetParameters(projectId, connectionId, includeHidden);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.GetParameters: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetParametersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get all parameters which are defined for projectId and connectionId
    ApiResponse<List<IdeaStatiCaApiConnectionModelIdeaParameterIdeaStatiCaApi>> response = apiInstance.GetParametersWithHttpInfo(projectId, connectionId, includeHidden);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.GetParametersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its parameters |  |
| **includeHidden** | **bool?** | Iclude also hdden parameters | [optional] [default to false] |

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

<a id="updateparameters"></a>
# **UpdateParameters**
> List&lt;IdeaRSCommonParametersParameterDataCIBasicTypes&gt; UpdateParameters (Guid projectId, int connectionId, List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>? ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi = null)

Update parameters for the connection connectionId in the project projectId by values passed in parameters

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateParametersExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ParameterApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to apply template
            var ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi = new List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>?(); // List<IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi>? | New values of parameters (optional) 

            try
            {
                // Update parameters for the connection connectionId in the project projectId by values passed in parameters
                List<IdeaRSCommonParametersParameterDataCIBasicTypes> result = apiInstance.UpdateParameters(projectId, connectionId, ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ParameterApi.UpdateParameters: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateParametersWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update parameters for the connection connectionId in the project projectId by values passed in parameters
    ApiResponse<List<IdeaRSCommonParametersParameterDataCIBasicTypes>> response = apiInstance.UpdateParametersWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ParameterApi.UpdateParametersWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to apply template |  |
| **ideaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi** | [**List&lt;IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi&gt;?**](IdeaStatiCaApiConnectionModelIdeaParameterUpdateIdeaStatiCaApi.md) | New values of parameters | [optional]  |

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
