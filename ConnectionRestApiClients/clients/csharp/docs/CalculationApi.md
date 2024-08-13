# connection_restapi_client_poc.Api.CalculationApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Calculate**](CalculationApi.md#calculate) | **POST** /api/1/projects/{projectId}/calculate | Run CBFEM caluclation and return the summary of the results |
| [**GetRawJsonResults**](CalculationApi.md#getrawjsonresults) | **POST** /api/1/projects/{projectId}/rawresults-text | Get json string which represents raw CBFEM results (an instance of CheckResultsData) |
| [**GetRawResults**](CalculationApi.md#getrawresults) | **POST** /api/1/projects/{projectId}/rawresults | Get raw CBFEM results (an instance of CheckResultsData) |
| [**GetResults**](CalculationApi.md#getresults) | **POST** /api/1/projects/{projectId}/results | Get detailed results of the CBFEM analysis |

<a id="calculate"></a>
# **Calculate**
> List&lt;IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi&gt; Calculate (Guid projectId, IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = null)

Run CBFEM caluclation and return the summary of the results

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class CalculateExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new CalculationApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? | List of connections to calculate and a type of CBFEM analysis (optional) 

            try
            {
                // Run CBFEM caluclation and return the summary of the results
                List<IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi> result = apiInstance.Calculate(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CalculationApi.Calculate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CalculateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Run CBFEM caluclation and return the summary of the results
    ApiResponse<List<IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi>> response = apiInstance.CalculateWithHttpInfo(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CalculationApi.CalculateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?.md) | List of connections to calculate and a type of CBFEM analysis | [optional]  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConResultSummaryIdeaStatiCaApi.md)

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

<a id="getrawjsonresults"></a>
# **GetRawJsonResults**
> string GetRawJsonResults (Guid projectId, IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = null)

Get json string which represents raw CBFEM results (an instance of CheckResultsData)

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetRawJsonResultsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new CalculationApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened connection in the ConnectionRestApi service
            var ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? | Type of requested analysis and connection to calculate (optional) 

            try
            {
                // Get json string which represents raw CBFEM results (an instance of CheckResultsData)
                string result = apiInstance.GetRawJsonResults(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CalculationApi.GetRawJsonResults: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetRawJsonResultsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get json string which represents raw CBFEM results (an instance of CheckResultsData)
    ApiResponse<string> response = apiInstance.GetRawJsonResultsWithHttpInfo(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CalculationApi.GetRawJsonResultsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened connection in the ConnectionRestApi service |  |
| **ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?.md) | Type of requested analysis and connection to calculate | [optional]  |

### Return type

**string**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/xml, text/xml, application/*+xml, application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: text/plain


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getrawresults"></a>
# **GetRawResults**
> CheckResultsDataIdeaStatiCaConnectionChecks GetRawResults (Guid projectId, IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = null)

Get raw CBFEM results (an instance of CheckResultsData)

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetRawResultsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new CalculationApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened connection in the ConnectionRestApi service
            var ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? | Type of requested analysis and connection to calculate (optional) 

            try
            {
                // Get raw CBFEM results (an instance of CheckResultsData)
                CheckResultsDataIdeaStatiCaConnectionChecks result = apiInstance.GetRawResults(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CalculationApi.GetRawResults: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetRawResultsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get raw CBFEM results (an instance of CheckResultsData)
    ApiResponse<CheckResultsDataIdeaStatiCaConnectionChecks> response = apiInstance.GetRawResultsWithHttpInfo(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CalculationApi.GetRawResultsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened connection in the ConnectionRestApi service |  |
| **ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?.md) | Type of requested analysis and connection to calculate | [optional]  |

### Return type

[**CheckResultsDataIdeaStatiCaConnectionChecks**](CheckResultsDataIdeaStatiCaConnectionChecks.md)

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

<a id="getresults"></a>
# **GetResults**
> List&lt;ConnectionConnectionCheckResIdeaRSOpenModel&gt; GetResults (Guid projectId, IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = null)

Get detailed results of the CBFEM analysis

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetResultsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new CalculationApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi? | List of connections to calculate and a type of CBFEM analysis (optional) 

            try
            {
                // Get detailed results of the CBFEM analysis
                List<ConnectionConnectionCheckResIdeaRSOpenModel> result = apiInstance.GetResults(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling CalculationApi.GetResults: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetResultsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get detailed results of the CBFEM analysis
    ApiResponse<List<ConnectionConnectionCheckResIdeaRSOpenModel>> response = apiInstance.GetResultsWithHttpInfo(projectId, ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling CalculationApi.GetResultsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **ideaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConCalculationParameterIdeaStatiCaApi?.md) | List of connections to calculate and a type of CBFEM analysis | [optional]  |

### Return type

[**List&lt;ConnectionConnectionCheckResIdeaRSOpenModel&gt;**](ConnectionConnectionCheckResIdeaRSOpenModel.md)

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

