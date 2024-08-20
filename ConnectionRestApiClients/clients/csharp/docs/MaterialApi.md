# connection_restapi_client_poc.Api.MaterialApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**AddBoltAssembly**](MaterialApi.md#addboltassembly) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-assemblies | Add bolt assembly to the project |
| [**AddCrossSection**](MaterialApi.md#addcrosssection) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/cross-sections | Add cross section to the project |
| [**AddMaterialBoltGrade**](MaterialApi.md#addmaterialboltgrade) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-grade | Add material to the project |
| [**AddMaterialConcrete**](MaterialApi.md#addmaterialconcrete) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/concrete | Add material to the project |
| [**AddMaterialSteel**](MaterialApi.md#addmaterialsteel) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/steel | Add material to the project |
| [**AddMaterialWeld**](MaterialApi.md#addmaterialweld) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/materials/welding | Add material to the project |
| [**GetAllMaterials**](MaterialApi.md#getallmaterials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials | Get materials which are used in the connectionId |
| [**GetBlotGradeMaterials**](MaterialApi.md#getblotgradematerials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/bolt-grade | Get materials which are used in the connectionId |
| [**GetBoltAssemblies**](MaterialApi.md#getboltassemblies) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/bolt-assemblies | Get bolt assemblies which are used in the connectionId |
| [**GetConcreteMaterials**](MaterialApi.md#getconcretematerials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/concrete | Get materials which are used in the connectionId |
| [**GetCrossSections**](MaterialApi.md#getcrosssections) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/cross-sections | Get cross sections which are used in the connectionId |
| [**GetSteelMaterials**](MaterialApi.md#getsteelmaterials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/steel | Get materials which are used in the connectionId |
| [**GetWeldingMaterials**](MaterialApi.md#getweldingmaterials) | **GET** /api/1/projects/{projectId}/connections/{connectionId}/materials/welding | Get materials which are used in the connectionId |

<a id="addboltassembly"></a>
# **AddBoltAssembly**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi AddBoltAssembly (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = null)

Add bolt assembly to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddBoltAssemblyExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? | Definition of a new bolt assemby to be added to the project (optional) 

            try
            {
                // Add bolt assembly to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi result = apiInstance.AddBoltAssembly(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddBoltAssembly: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddBoltAssemblyWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add bolt assembly to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi> response = apiInstance.AddBoltAssemblyWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddBoltAssemblyWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?.md) | Definition of a new bolt assemby to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

<a id="addcrosssection"></a>
# **AddCrossSection**
> IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi AddCrossSection (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi = null)

Add cross section to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddCrossSectionExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi? | Definition of a new cross-section to be added to the project (optional) 

            try
            {
                // Add cross section to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi result = apiInstance.AddCrossSection(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddCrossSection: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddCrossSectionWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add cross section to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi> response = apiInstance.AddCrossSectionWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddCrossSectionWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi?.md) | Definition of a new cross-section to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlCrossSectionIdeaStatiCaApi.md)

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

<a id="addmaterialboltgrade"></a>
# **AddMaterialBoltGrade**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi AddMaterialBoltGrade (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = null)

Add material to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddMaterialBoltGradeExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? | Definition of a new material to be added to the project (optional) 

            try
            {
                // Add material to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi result = apiInstance.AddMaterialBoltGrade(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddMaterialBoltGrade: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddMaterialBoltGradeWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add material to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi> response = apiInstance.AddMaterialBoltGradeWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddMaterialBoltGradeWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?.md) | Definition of a new material to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

<a id="addmaterialconcrete"></a>
# **AddMaterialConcrete**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi AddMaterialConcrete (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = null)

Add material to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddMaterialConcreteExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? | Definition of a new material to be added to the project (optional) 

            try
            {
                // Add material to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi result = apiInstance.AddMaterialConcrete(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddMaterialConcrete: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddMaterialConcreteWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add material to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi> response = apiInstance.AddMaterialConcreteWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddMaterialConcreteWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?.md) | Definition of a new material to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

<a id="addmaterialsteel"></a>
# **AddMaterialSteel**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi AddMaterialSteel (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = null)

Add material to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddMaterialSteelExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? | Definition of a new material to be added to the project (optional) 

            try
            {
                // Add material to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi result = apiInstance.AddMaterialSteel(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddMaterialSteel: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddMaterialSteelWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add material to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi> response = apiInstance.AddMaterialSteelWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddMaterialSteelWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?.md) | Definition of a new material to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

<a id="addmaterialweld"></a>
# **AddMaterialWeld**
> IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi AddMaterialWeld (Guid projectId, int connectionId, IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = null)

Add material to the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class AddMaterialWeldExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | 
            var ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi = new IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?(); // IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi? | Definition of a new material to be added to the project (optional) 

            try
            {
                // Add material to the project
                IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi result = apiInstance.AddMaterialWeld(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.AddMaterialWeld: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the AddMaterialWeldWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Add material to the project
    ApiResponse<IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi> response = apiInstance.AddMaterialWeldWithHttpInfo(projectId, connectionId, ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.AddMaterialWeldWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** |  |  |
| **ideaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi** | [**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi?.md) | Definition of a new material to be added to the project | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelMaterialConMprlElementIdeaStatiCaApi.md)

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

<a id="getallmaterials"></a>
# **GetAllMaterials**
> List&lt;Object&gt; GetAllMaterials (Guid projectId, int connectionId)

Get materials which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetAllMaterialsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its materials

            try
            {
                // Get materials which are used in the connectionId
                List<Object> result = apiInstance.GetAllMaterials(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetAllMaterials: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetAllMaterialsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get materials which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetAllMaterialsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetAllMaterialsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its materials |  |

### Return type

**List<Object>**

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

<a id="getblotgradematerials"></a>
# **GetBlotGradeMaterials**
> List&lt;Object&gt; GetBlotGradeMaterials (Guid projectId, int connectionId)

Get materials which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetBlotGradeMaterialsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its materials

            try
            {
                // Get materials which are used in the connectionId
                List<Object> result = apiInstance.GetBlotGradeMaterials(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetBlotGradeMaterials: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetBlotGradeMaterialsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get materials which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetBlotGradeMaterialsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetBlotGradeMaterialsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its materials |  |

### Return type

**List<Object>**

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

<a id="getboltassemblies"></a>
# **GetBoltAssemblies**
> List&lt;Object&gt; GetBoltAssemblies (Guid projectId, int connectionId)

Get bolt assemblies which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetBoltAssembliesExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its bolt assemblies

            try
            {
                // Get bolt assemblies which are used in the connectionId
                List<Object> result = apiInstance.GetBoltAssemblies(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetBoltAssemblies: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetBoltAssembliesWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get bolt assemblies which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetBoltAssembliesWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetBoltAssembliesWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its bolt assemblies |  |

### Return type

**List<Object>**

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

<a id="getconcretematerials"></a>
# **GetConcreteMaterials**
> List&lt;Object&gt; GetConcreteMaterials (Guid projectId, int connectionId)

Get materials which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetConcreteMaterialsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its materials

            try
            {
                // Get materials which are used in the connectionId
                List<Object> result = apiInstance.GetConcreteMaterials(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetConcreteMaterials: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetConcreteMaterialsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get materials which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetConcreteMaterialsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetConcreteMaterialsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its materials |  |

### Return type

**List<Object>**

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

<a id="getcrosssections"></a>
# **GetCrossSections**
> List&lt;Object&gt; GetCrossSections (Guid projectId, int connectionId)

Get cross sections which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetCrossSectionsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its cross-sections

            try
            {
                // Get cross sections which are used in the connectionId
                List<Object> result = apiInstance.GetCrossSections(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetCrossSections: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetCrossSectionsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get cross sections which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetCrossSectionsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetCrossSectionsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its cross-sections |  |

### Return type

**List<Object>**

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

<a id="getsteelmaterials"></a>
# **GetSteelMaterials**
> List&lt;Object&gt; GetSteelMaterials (Guid projectId, int connectionId)

Get materials which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetSteelMaterialsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its materials

            try
            {
                // Get materials which are used in the connectionId
                List<Object> result = apiInstance.GetSteelMaterials(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetSteelMaterials: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetSteelMaterialsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get materials which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetSteelMaterialsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetSteelMaterialsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its materials |  |

### Return type

**List<Object>**

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

<a id="getweldingmaterials"></a>
# **GetWeldingMaterials**
> List&lt;Object&gt; GetWeldingMaterials (Guid projectId, int connectionId)

Get materials which are used in the connectionId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetWeldingMaterialsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new MaterialApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get its materials

            try
            {
                // Get materials which are used in the connectionId
                List<Object> result = apiInstance.GetWeldingMaterials(projectId, connectionId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling MaterialApi.GetWeldingMaterials: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetWeldingMaterialsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get materials which are used in the connectionId
    ApiResponse<List<Object>> response = apiInstance.GetWeldingMaterialsWithHttpInfo(projectId, connectionId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling MaterialApi.GetWeldingMaterialsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get its materials |  |

### Return type

**List<Object>**

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

