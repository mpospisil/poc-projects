# connection_restapi_client_poc.Api.ExportApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGet**](ExportApi.md#api1projectsprojectidconnectionsconnectionidexportifcget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-ifc |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGet**](ExportApi.md#api1projectsprojectidconnectionsconnectionidexportiomconnectiondataget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-iom-connection-data |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdExportIomGet**](ExportApi.md#api1projectsprojectidconnectionsconnectionidexportiomget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/export-iom |  |

<a id="api1projectsprojectidconnectionsconnectionidexportifcget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGet**
> SystemIOMemoryStreamSystemPrivateCoreLib Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ExportApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                SystemIOMemoryStreamSystemPrivateCoreLib result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<SystemIOMemoryStreamSystemPrivateCoreLib> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIfcGetWithHttpInfo: " + e.Message);
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

[**SystemIOMemoryStreamSystemPrivateCoreLib**](SystemIOMemoryStreamSystemPrivateCoreLib.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/xml, text/xml, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidconnectionsconnectionidexportiomconnectiondataget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGet**
> ConnectionConnectionDataIdeaRSOpenModel Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ExportApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                ConnectionConnectionDataIdeaRSOpenModel result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<ConnectionConnectionDataIdeaRSOpenModel> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIomConnectionDataGetWithHttpInfo: " + e.Message);
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

[**ConnectionConnectionDataIdeaRSOpenModel**](ConnectionConnectionDataIdeaRSOpenModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/xml


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="api1projectsprojectidconnectionsconnectionidexportiomget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdExportIomGet**
> void Api1ProjectsProjectIdConnectionsConnectionIdExportIomGet (Guid projectId, int connectionId, string? version = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdExportIomGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ExportApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var version = "version_example";  // string? |  (optional) 

            try
            {
                apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIomGet(projectId, connectionId, version);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIomGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdExportIomGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdExportIomGetWithHttpInfo(projectId, connectionId, version);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ExportApi.Api1ProjectsProjectIdConnectionsConnectionIdExportIomGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **version** | **string?** |  | [optional]  |

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
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

