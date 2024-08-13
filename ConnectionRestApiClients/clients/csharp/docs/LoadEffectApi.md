# connection_restapi_client_poc.Api.LoadEffectApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGet**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectsget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDelete**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectiddelete) | **DELETE** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGet**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectidget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPut**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectidput) | **PUT** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/{loadEffectId} |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPost**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectspost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPost**](LoadEffectApi.md#api1projectsprojectidconnectionsconnectionidloadeffectssetequilibriumpost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/load-effects/set-equilibrium |  |

<a id="api1projectsprojectidconnectionsconnectionidloadeffectsget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGet**
> List&lt;IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGet (Guid projectId, int connectionId, bool? isPercentage = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGetExample
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
                List<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGet(projectId, connectionId, isPercentage);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGetWithHttpInfo(projectId, connectionId, isPercentage);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsGetWithHttpInfo: " + e.Message);
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

<a id="api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectiddelete"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDelete**
> int Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDelete (Guid projectId, int connectionId, int loadEffectId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDeleteExample
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
                int result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDelete(projectId, connectionId, loadEffectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDelete: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDeleteWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<int> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDeleteWithHttpInfo(projectId, connectionId, loadEffectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdDeleteWithHttpInfo: " + e.Message);
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

<a id="api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectidget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGet**
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGet (Guid projectId, int connectionId, int loadEffectId, bool? isPercentage = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGetExample
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
                IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGet(projectId, connectionId, loadEffectId, isPercentage);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGetWithHttpInfo(projectId, connectionId, loadEffectId, isPercentage);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdGetWithHttpInfo: " + e.Message);
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

<a id="api1projectsprojectidconnectionsconnectionidloadeffectsloadeffectidput"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPut**
> IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPut (Guid projectId, int connectionId, int loadEffectId, IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPutExample
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
                IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPut(projectId, connectionId, loadEffectId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPut: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPutWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPutWithHttpInfo(projectId, connectionId, loadEffectId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsLoadEffectIdPutWithHttpInfo: " + e.Message);
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

<a id="api1projectsprojectidconnectionsconnectionidloadeffectspost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPost**
> LoadEffectDataIdeaStatiCaConnectionChecks Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPost (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi? ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPostExample
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
                LoadEffectDataIdeaStatiCaConnectionChecks result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPost(projectId, connectionId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<LoadEffectDataIdeaStatiCaConnectionChecks> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPostWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsPostWithHttpInfo: " + e.Message);
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

<a id="api1projectsprojectidconnectionsconnectionidloadeffectssetequilibriumpost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPost**
> bool Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPost (Guid projectId, int connectionId, bool? loadsInEquilibrium = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new LoadEffectApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var loadsInEquilibrium = true;  // bool? |  (optional) 

            try
            {
                bool result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPost(projectId, connectionId, loadsInEquilibrium);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<bool> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPostWithHttpInfo(projectId, connectionId, loadsInEquilibrium);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling LoadEffectApi.Api1ProjectsProjectIdConnectionsConnectionIdLoadEffectsSetEquilibriumPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **loadsInEquilibrium** | **bool?** |  | [optional]  |

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

