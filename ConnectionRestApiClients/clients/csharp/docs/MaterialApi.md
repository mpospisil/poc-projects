# connection_restapi_client_poc.Api.MaterialApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGet**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialsboltassembliesget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPost**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialsboltassembliespost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGet**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialscrosssectionsget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPost**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialscrosssectionspost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGet**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialsget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGet**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialspinsget) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/pins |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPost**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialspinspost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/pins |  |
| [**Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPost**](MaterialApi.md#api1projectsprojectidconnectionsconnectionidmaterialspost) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials |  |

<a id="api1projectsprojectidconnectionsconnectionidmaterialsboltassembliesget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGet**
> List&lt;IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                List<IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesGetWithHttpInfo: " + e.Message);
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

[**List&lt;IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialsboltassembliespost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPost**
> IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPost (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi? ideaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi? |  (optional) 

            try
            {
                IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPost(projectId, connectionId, ideaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPostWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsBoltAssembliesPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjBoltAssemblyIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialscrosssectionsget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGet**
> List&lt;IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                List<IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsGetWithHttpInfo: " + e.Message);
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

[**List&lt;IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialscrosssectionspost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPost**
> IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPost (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi? ideaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi? |  (optional) 

            try
            {
                IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPost(projectId, connectionId, ideaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPostWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsCrossSectionsPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjCrossSectionIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialsget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGet**
> List&lt;IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGet (Guid projectId, int connectionId, IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes? type = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var type = new IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes?(); // IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes? |  (optional) 

            try
            {
                List<IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGet(projectId, connectionId, type);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGetWithHttpInfo(projectId, connectionId, type);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsGetWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **type** | [**IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes?**](IdeaRSWsLibCssServiceMaterialTypeCIBasicTypes?.md) |  | [optional]  |

### Return type

[**List&lt;IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialspinsget"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGet**
> List&lt;IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi&gt; Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGet (Guid projectId, int connectionId)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGetExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 

            try
            {
                List<IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi> result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGet(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGet: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGetWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<List<IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi>> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGetWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsGetWithHttpInfo: " + e.Message);
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

[**List&lt;IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialspinspost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPost**
> IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPost (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi? ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi? |  (optional) 

            try
            {
                IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPost(projectId, connectionId, ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPostWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPinsPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjPinIdeaStatiCaApi.md)

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

<a id="api1projectsprojectidconnectionsconnectionidmaterialspost"></a>
# **Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPost**
> IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPost (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi? ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi = null)



### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPostExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | 
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi? |  (optional) 

            try
            {
                IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi result = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPost(projectId, connectionId, ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPost: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPostWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    ApiResponse<IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi> response = apiInstance.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPostWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.Api1ProjectsProjectIdConnectionsConnectionIdMaterialsPostWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** |  |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelProjMaterialIdeaStatiCaApi.md)

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

