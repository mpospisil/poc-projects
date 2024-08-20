# connection_restapi_client_poc.Api.LoadEffectApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AddLoadEffect**](LoadEffectApi.md#addloadeffect) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | Add new load effect to the connection |
| [**DeleteLoadEffect**](LoadEffectApi.md#deleteloadeffect) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Delete load effect loadEffectId |
| [**GetLoadEffect**](LoadEffectApi.md#getloadeffect) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Get load impulses from loadEffectId |
| [**GetLoadEffects**](LoadEffectApi.md#getloadeffects) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects | Get all load effects which are defined in connectionId |
| [**SetLoadsInEquilibrium**](LoadEffectApi.md#setloadsinequilibrium) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/set-equilibrium | Update the option &#39;LoadsInEquilibrium&#39; for connectionId |
| [**UpdateLoadEffect**](LoadEffectApi.md#updateloadeffect) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} | Update load impulses in loadEffectId |

<a id="addloadeffect"></a>
# **AddLoadEffect**
> LoadEffectDataIdeaStatiCaConnectionChecks AddLoadEffect (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = null)

Add new load effect to the connection

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddLoadEffectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? |  (optional) 

            try
            {
                // Add new load effect to the connection
                LoadEffectDataIdeaStatiCaConnectionChecks result = apiInstance.AddLoadEffect(projectId, connectionId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.AddLoadEffect: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddLoadEffectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add new load effect to the connection
    ApiResponse<LoadEffectDataIdeaStatiCaConnectionChecks> response = apiInstance.AddLoadEffectWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.AddLoadEffectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**LoadEffectDataIdeaStatiCaConnectionChecks**](LoadEffectDataIdeaStatiCaConnectionChecks.md)

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

<a id="deleteloadeffect"></a>
# **DeleteLoadEffect**
> int DeleteLoadEffect (Guid projectId, int connectionId, int loadEffectId)

Delete load effect loadEffectId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class DeleteLoadEffectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var loadEffectId = 56;  // int | 

            try
            {
                // Delete load effect loadEffectId
                int result = apiInstance.DeleteLoadEffect(projectId, connectionId, loadEffectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.DeleteLoadEffect: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DeleteLoadEffectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Delete load effect loadEffectId
    ApiResponse<int> response = apiInstance.DeleteLoadEffectWithHttpInfo(projectId, connectionId, loadEffectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.DeleteLoadEffectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **loadEffectId** | **int** |  |  |

### Return type

**int**

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

<a id="getloadeffect"></a>
# **GetLoadEffect**
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi GetLoadEffect (Guid projectId, int connectionId, int loadEffectId, bool? isPercentage = null)

Get load impulses from loadEffectId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetLoadEffectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var loadEffectId = 56;  // int | 
            var isPercentage = true;  // bool? |  (optional) 

            try
            {
                // Get load impulses from loadEffectId
                IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi result = apiInstance.GetLoadEffect(projectId, connectionId, loadEffectId, isPercentage);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.GetLoadEffect: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetLoadEffectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get load impulses from loadEffectId
    ApiResponse<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> response = apiInstance.GetLoadEffectWithHttpInfo(projectId, connectionId, loadEffectId, isPercentage);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.GetLoadEffectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **loadEffectId** | **int** |  |  |
| **isPercentage** | **bool?** |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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

<a id="getloadeffects"></a>
# **GetLoadEffects**
> List&lt;IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi&gt; GetLoadEffects (Guid projectId, int connectionId, bool? isPercentage = null)

Get all load effects which are defined in connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetLoadEffectsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var isPercentage = true;  // bool? |  (optional) 

            try
            {
                // Get all load effects which are defined in connectionId
                List<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> result = apiInstance.GetLoadEffects(projectId, connectionId, isPercentage);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.GetLoadEffects: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetLoadEffectsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get all load effects which are defined in connectionId
    ApiResponse<List<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi>> response = apiInstance.GetLoadEffectsWithHttpInfo(projectId, connectionId, isPercentage);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.GetLoadEffectsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **isPercentage** | **bool?** |  | [optional]  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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

<a id="setloadsinequilibrium"></a>
# **SetLoadsInEquilibrium**
> bool SetLoadsInEquilibrium (Guid projectId, int connectionId, bool? loadsInEquilibrium = null)

Update the option 'LoadsInEquilibrium' for connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class SetLoadsInEquilibriumExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var loadsInEquilibrium = true;  // bool? | Value to be set (optional) 

            try
            {
                // Update the option 'LoadsInEquilibrium' for connectionId
                bool result = apiInstance.SetLoadsInEquilibrium(projectId, connectionId, loadsInEquilibrium);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.SetLoadsInEquilibrium: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the SetLoadsInEquilibriumWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update the option 'LoadsInEquilibrium' for connectionId
    ApiResponse<bool> response = apiInstance.SetLoadsInEquilibriumWithHttpInfo(projectId, connectionId, loadsInEquilibrium);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.SetLoadsInEquilibriumWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **loadsInEquilibrium** | **bool?** | Value to be set | [optional]  |

### Return type

**bool**

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

<a id="updateloadeffect"></a>
# **UpdateLoadEffect**
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi UpdateLoadEffect (Guid projectId, int connectionId, int loadEffectId, IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = null)

Update load impulses in loadEffectId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateLoadEffectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var loadEffectId = 56;  // int | 
            var ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? |  (optional) 

            try
            {
                // Update load impulses in loadEffectId
                IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi result = apiInstance.UpdateLoadEffect(projectId, connectionId, loadEffectId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.UpdateLoadEffect: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateLoadEffectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update load impulses in loadEffectId
    ApiResponse<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> response = apiInstance.UpdateLoadEffectWithHttpInfo(projectId, connectionId, loadEffectId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.UpdateLoadEffectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **loadEffectId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.md)

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

