# connection_restapi_client_poc.Api.ReportApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdReportsConnectionIdPdfGet**](ReportApi.md#api1projectsprojectidreportsconnectionidpdfget) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/pdf | Generates report for projectId and connectionId |
| [**Api1ProjectsProjectIdReportsConnectionIdWordGet**](ReportApi.md#api1projectsprojectidreportsconnectionidwordget) | **GET** /api/1/projects/{projectId}/reports/{connectionId}/word | Generates report for projectId and connectionId |

<a id="api1projectsprojectidreportsconnectionidpdfget"></a>
# **Api1ProjectsProjectIdReportsConnectionIdPdfGet**
> Stream Api1ProjectsProjectIdReportsConnectionIdPdfGet (Guid projectId, int connectionId, Object? body = null)

Generates report for projectId and connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdReportsConnectionIdPdfGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ReportApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var body = null;  // Object? |  (optional) 

            try
            {
                // Generates report for projectId and connectionId
                Stream result = apiInstance.Api1ProjectsProjectIdReportsConnectionIdPdfGet(projectId, connectionId, body);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ReportApi.Api1ProjectsProjectIdReportsConnectionIdPdfGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdReportsConnectionIdPdfGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Generates report for projectId and connectionId
    ApiResponse<Stream> response = apiInstance.Api1ProjectsProjectIdReportsConnectionIdPdfGetWithHttpInfo(projectId, connectionId, body);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ReportApi.Api1ProjectsProjectIdReportsConnectionIdPdfGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **body** | **Object?** |  | [optional]  |

### Return type

[**Stream**](Stream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidreportsconnectionidwordget"></a>
# **Api1ProjectsProjectIdReportsConnectionIdWordGet**
> Stream Api1ProjectsProjectIdReportsConnectionIdWordGet (Guid projectId, int connectionId, Object? body = null)

Generates report for projectId and connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdReportsConnectionIdWordGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ReportApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var body = null;  // Object? |  (optional) 

            try
            {
                // Generates report for projectId and connectionId
                Stream result = apiInstance.Api1ProjectsProjectIdReportsConnectionIdWordGet(projectId, connectionId, body);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ReportApi.Api1ProjectsProjectIdReportsConnectionIdWordGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdReportsConnectionIdWordGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Generates report for projectId and connectionId
    ApiResponse<Stream> response = apiInstance.Api1ProjectsProjectIdReportsConnectionIdWordGetWithHttpInfo(projectId, connectionId, body);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ReportApi.Api1ProjectsProjectIdReportsConnectionIdWordGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **body** | **Object?** |  | [optional]  |

### Return type

[**Stream**](Stream.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

