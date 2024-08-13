# connection_restapi_client_poc.Api.ConnectionApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**DeleteOperations**](ConnectionApi.md#deleteoperations) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/operations | Delete all operations for the connection |
| [**GetAllConnectionsData**](ConnectionApi.md#getallconnectionsdata) | **GET** /api/1/projects/{projectId}/connections | Get data about all connections in the project |
| [**GetConnectionData**](ConnectionApi.md#getconnectiondata) | **GET** /api/1/projects/{projectId}/connections/{connectionId} | Get data about a specific connection in the project |
| [**GetMissingWelds**](ConnectionApi.md#getmissingwelds) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/missing-welds | Get missing welds in the connection |
| [**GetOperations**](ConnectionApi.md#getoperations) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/operations | Get the list of operations for the connection |
| [**GetProductionCost**](ConnectionApi.md#getproductioncost) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/production-cost | Get production cost of the connection |
| [**UpdateConnectionData**](ConnectionApi.md#updateconnectiondata) | **PUT** /api/1/projects/{projectId}/connections/{connectionId} | Update data of a specific connection in the project |

<a id="deleteoperations"></a>
# **DeleteOperations**
> MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore DeleteOperations (Guid projectId, int connectionId)

Delete all operations for the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class DeleteOperationsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to be modified

            try
            {
                // Delete all operations for the connection
                MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore result = apiInstance.DeleteOperations(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.DeleteOperations: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeleteOperationsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Delete all operations for the connection
    ApiResponse<MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore> response = apiInstance.DeleteOperationsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.DeleteOperationsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to be modified |  |

### Return type

[**MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore**](MicrosoftAspNetCoreMvcOkObjectResultMicrosoftAspNetCoreMvcCore.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json


### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
| **200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

<a id="getallconnectionsdata"></a>
# **GetAllConnectionsData**
> List&lt;IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi&gt; GetAllConnectionsData (Guid projectId)

Get data about all connections in the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetAllConnectionsDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service

            try
            {
                // Get data about all connections in the project
                List<IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi> result = apiInstance.GetAllConnectionsData(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.GetAllConnectionsData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetAllConnectionsDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get data about all connections in the project
    ApiResponse<List<IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi>> response = apiInstance.GetAllConnectionsDataWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.GetAllConnectionsDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

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

<a id="getconnectiondata"></a>
# **GetConnectionData**
> IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi GetConnectionData (Guid projectId, int connectionId)

Get data about a specific connection in the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetConnectionDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | The id of the requested connection

            try
            {
                // Get data about a specific connection in the project
                IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi result = apiInstance.GetConnectionData(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.GetConnectionData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetConnectionDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get data about a specific connection in the project
    ApiResponse<IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi> response = apiInstance.GetConnectionDataWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.GetConnectionDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | The id of the requested connection |  |

### Return type

[**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

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

<a id="getmissingwelds"></a>
# **GetMissingWelds**
> List&lt;IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi&gt; GetMissingWelds (Guid projectId, int connectionId)

Get missing welds in the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetMissingWeldsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the requested connection in the project

            try
            {
                // Get missing welds in the connection
                List<IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi> result = apiInstance.GetMissingWelds(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.GetMissingWelds: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetMissingWeldsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get missing welds in the connection
    ApiResponse<List<IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi>> response = apiInstance.GetMissingWeldsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.GetMissingWeldsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the requested connection in the project |  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConMissingWeldIdeaStatiCaApi.md)

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

<a id="getoperations"></a>
# **GetOperations**
> List&lt;IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi&gt; GetOperations (Guid projectId, int connectionId)

Get the list of operations for the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetOperationsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the requested connection

            try
            {
                // Get the list of operations for the connection
                List<IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi> result = apiInstance.GetOperations(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.GetOperations: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetOperationsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get the list of operations for the connection
    ApiResponse<List<IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi>> response = apiInstance.GetOperationsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.GetOperationsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the requested connection |  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConOperationIdeaStatiCaApi.md)

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

<a id="getproductioncost"></a>
# **GetProductionCost**
> IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi GetProductionCost (Guid projectId, int connectionId)

Get production cost of the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetProductionCostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the requested connection

            try
            {
                // Get production cost of the connection
                IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi result = apiInstance.GetProductionCost(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.GetProductionCost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProductionCostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get production cost of the connection
    ApiResponse<IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi> response = apiInstance.GetProductionCostWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.GetProductionCostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the requested connection |  |

### Return type

[**IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProductionCostIdeaStatiCaApi.md)

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

<a id="updateconnectiondata"></a>
# **UpdateConnectionData**
> IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi UpdateConnectionData (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi? ideaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi = null)

Update data of a specific connection in the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateConnectionDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ConnectionApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to be update
            var ideaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi? | New connection data to be set (optional) 

            try
            {
                // Update data of a specific connection in the project
                IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi result = apiInstance.UpdateConnectionData(projectId, connectionId, ideaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ConnectionApi.UpdateConnectionData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateConnectionDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update data of a specific connection in the project
    ApiResponse<IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi> response = apiInstance.UpdateConnectionDataWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ConnectionApi.UpdateConnectionDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to be update |  |
| **ideaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi?.md) | New connection data to be set | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md)

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

