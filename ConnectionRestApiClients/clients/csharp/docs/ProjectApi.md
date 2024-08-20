# connection_restapi_client_poc.Api.ProjectApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**CloseProject**](ProjectApi.md#closeproject) | **GET** /api/1/projects/{projectId}/close | Close the project. Needed for releasing resources in the service. |
| [**ConnectClient**](ProjectApi.md#connectclient) | **GET** /api/1/connect-client | Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client. |
| [**DownloadProject**](ProjectApi.md#downloadproject) | **GET** /api/1/projects/{projectId}/download | Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls. |
| [**GetActiveProjects**](ProjectApi.md#getactiveprojects) | **GET** /api/1/projects | Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient |
| [**GetProjectData**](ProjectApi.md#getprojectdata) | **GET** /api/1/projects/{projectId}/project-data | Get data of the project. |
| [**GetSetup**](ProjectApi.md#getsetup) | **GET** /api/1/projects/{projectId}/connection-setup | Get setup from project |
| [**ImportIOM**](ProjectApi.md#importiom) | **POST** /api/1/projects/import-iom-file | Creates an IDEA Connection project. IOM is passed in the body of the request. |
| [**ImportIOMContainer**](ProjectApi.md#importiomcontainer) | **POST** /api/1/projects/import-iom | Creates an IDEA Connection project from model (model and results) |
| [**OpenProject**](ProjectApi.md#openproject) | **POST** /api/1/projects/open | Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method |
| [**UpdateFromIOM**](ProjectApi.md#updatefromiom) | **POST** /api/1/projects/{projectId}/update-iom-file | Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request. |
| [**UpdateFromIOMContainer**](ProjectApi.md#updatefromiomcontainer) | **POST** /api/1/projects/{projectId}/update-iom | Update an IDEA Connection project by model (model and results) |
| [**UpdateSetup**](ProjectApi.md#updatesetup) | **PUT** /api/1/projects/{projectId}/connection-setup | Update setup of the project |

<a id="closeproject"></a>
# **CloseProject**
> string CloseProject (string projectId)

Close the project. Needed for releasing resources in the service.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class CloseProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // string | The unique identifier of the project to be closed

            try
            {
                // Close the project. Needed for releasing resources in the service.
                string result = apiInstance.CloseProject(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.CloseProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the CloseProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Close the project. Needed for releasing resources in the service.
    ApiResponse<string> response = apiInstance.CloseProjectWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.CloseProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **string** | The unique identifier of the project to be closed |  |

### Return type

**string**

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

<a id="connectclient"></a>
# **ConnectClient**
> string ConnectClient ()

Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class ConnectClientExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);

            try
            {
                // Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.
                string result = apiInstance.ConnectClient();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.ConnectClient: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ConnectClientWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Connect a client to the ConnectionRestApi service. Methond returns a unique identifier of the client.
    ApiResponse<string> response = apiInstance.ConnectClientWithHttpInfo();
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.ConnectClientWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters
This endpoint does not need any parameter.
### Return type

**string**

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

<a id="downloadproject"></a>
# **DownloadProject**
> SystemIOMemoryStreamSystemPrivateCoreLib DownloadProject (Guid projectId)

Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class DownloadProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service

            try
            {
                // Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
                SystemIOMemoryStreamSystemPrivateCoreLib result = apiInstance.DownloadProject(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.DownloadProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the DownloadProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Download the actual ideacon project from the service. It includes alle changes which were made by previous API calls.
    ApiResponse<SystemIOMemoryStreamSystemPrivateCoreLib> response = apiInstance.DownloadProjectWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.DownloadProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |

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

<a id="getactiveprojects"></a>
# **GetActiveProjects**
> List&lt;IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi&gt; GetActiveProjects ()

Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetActiveProjectsExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);

            try
            {
                // Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient
                List<IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi> result = apiInstance.GetActiveProjects();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.GetActiveProjects: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetActiveProjectsWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get the list of projects in the service which were opened by the client which was connected by M:IdeaStatiCa.ConnectionRestApi.Controllers.ProjectController.ConnectClient
    ApiResponse<List<IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi>> response = apiInstance.GetActiveProjectsWithHttpInfo();
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.GetActiveProjectsWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters
This endpoint does not need any parameter.
### Return type

[**List&lt;IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi&gt;**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

<a id="getprojectdata"></a>
# **GetProjectData**
> IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi GetProjectData (Guid projectId)

Get data of the project.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetProjectDataExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the requested project

            try
            {
                // Get data of the project.
                IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi result = apiInstance.GetProjectData(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.GetProjectData: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetProjectDataWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get data of the project.
    ApiResponse<IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi> response = apiInstance.GetProjectDataWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.GetProjectDataWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the requested project |  |

### Return type

[**IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi.md)

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

<a id="getsetup"></a>
# **GetSetup**
> ConnectionSetupIdeaRSOpenModel GetSetup (Guid projectId)

Get setup from project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetSetupExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service to get setup

            try
            {
                // Get setup from project
                ConnectionSetupIdeaRSOpenModel result = apiInstance.GetSetup(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.GetSetup: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetSetupWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get setup from project
    ApiResponse<ConnectionSetupIdeaRSOpenModel> response = apiInstance.GetSetupWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.GetSetupWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service to get setup |  |

### Return type

[**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md)

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

<a id="importiom"></a>
# **ImportIOM**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi ImportIOM (List<int>? connectionsToCreate = null)

Creates an IDEA Connection project. IOM is passed in the body of the request.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class ImportIOMExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var connectionsToCreate = new List<int>?(); // List<int>? |  (optional) 

            try
            {
                // Creates an IDEA Connection project. IOM is passed in the body of the request.
                IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi result = apiInstance.ImportIOM(connectionsToCreate);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.ImportIOM: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ImportIOMWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Creates an IDEA Connection project. IOM is passed in the body of the request.
    ApiResponse<IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi> response = apiInstance.ImportIOMWithHttpInfo(connectionsToCreate);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.ImportIOMWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **connectionsToCreate** | [**List&lt;int&gt;?**](int.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

<a id="importiomcontainer"></a>
# **ImportIOMContainer**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi ImportIOMContainer (List<int>? connectionsToCreate = null, OpenModelContainerIdeaRSOpenModel? openModelContainerIdeaRSOpenModel = null)

Creates an IDEA Connection project from model (model and results)

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class ImportIOMContainerExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var connectionsToCreate = new List<int>?(); // List<int>? |  (optional) 
            var openModelContainerIdeaRSOpenModel = new OpenModelContainerIdeaRSOpenModel?(); // OpenModelContainerIdeaRSOpenModel? |  (optional) 

            try
            {
                // Creates an IDEA Connection project from model (model and results)
                IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi result = apiInstance.ImportIOMContainer(connectionsToCreate, openModelContainerIdeaRSOpenModel);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.ImportIOMContainer: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ImportIOMContainerWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Creates an IDEA Connection project from model (model and results)
    ApiResponse<IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi> response = apiInstance.ImportIOMContainerWithHttpInfo(connectionsToCreate, openModelContainerIdeaRSOpenModel);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.ImportIOMContainerWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **connectionsToCreate** | [**List&lt;int&gt;?**](int.md) |  | [optional]  |
| **openModelContainerIdeaRSOpenModel** | [**OpenModelContainerIdeaRSOpenModel?**](OpenModelContainerIdeaRSOpenModel?.md) |  | [optional]  |

### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

<a id="openproject"></a>
# **OpenProject**
> IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi OpenProject ()

Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class OpenProjectExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);

            try
            {
                // Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method
                IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi result = apiInstance.OpenProject();
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.OpenProject: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the OpenProjectWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Open ideacon project which is passed in the body of the request  TODO - should be the parameter of the method
    ApiResponse<IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi> response = apiInstance.OpenProjectWithHttpInfo();
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.OpenProjectWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters
This endpoint does not need any parameter.
### Return type

[**IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.md)

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

<a id="updatefromiom"></a>
# **UpdateFromIOM**
> bool UpdateFromIOM (Guid projectId)

Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateFromIOMExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service to be updated

            try
            {
                // Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.
                bool result = apiInstance.UpdateFromIOM(projectId);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.UpdateFromIOM: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateFromIOMWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update an IDEA Connection project based on OpenModelContainer (model and results). IOM is passed in the body of the request.
    ApiResponse<bool> response = apiInstance.UpdateFromIOMWithHttpInfo(projectId);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.UpdateFromIOMWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service to be updated |  |

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

<a id="updatefromiomcontainer"></a>
# **UpdateFromIOMContainer**
> bool UpdateFromIOMContainer (Guid projectId, OpenModelContainerIdeaRSOpenModel? openModelContainerIdeaRSOpenModel = null)

Update an IDEA Connection project by model (model and results)

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateFromIOMContainerExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service to be updated
            var openModelContainerIdeaRSOpenModel = new OpenModelContainerIdeaRSOpenModel?(); // OpenModelContainerIdeaRSOpenModel? |  (optional) 

            try
            {
                // Update an IDEA Connection project by model (model and results)
                bool result = apiInstance.UpdateFromIOMContainer(projectId, openModelContainerIdeaRSOpenModel);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.UpdateFromIOMContainer: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateFromIOMContainerWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update an IDEA Connection project by model (model and results)
    ApiResponse<bool> response = apiInstance.UpdateFromIOMContainerWithHttpInfo(projectId, openModelContainerIdeaRSOpenModel);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.UpdateFromIOMContainerWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service to be updated |  |
| **openModelContainerIdeaRSOpenModel** | [**OpenModelContainerIdeaRSOpenModel?**](OpenModelContainerIdeaRSOpenModel?.md) |  | [optional]  |

### Return type

**bool**

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

<a id="updatesetup"></a>
# **UpdateSetup**
> ConnectionSetupIdeaRSOpenModel UpdateSetup (Guid projectId, ConnectionSetupIdeaRSOpenModel? connectionSetupIdeaRSOpenModel = null)

Update setup of the project

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class UpdateSetupExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new ProjectApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service to update project setup
            var connectionSetupIdeaRSOpenModel = new ConnectionSetupIdeaRSOpenModel?(); // ConnectionSetupIdeaRSOpenModel? |  (optional) 

            try
            {
                // Update setup of the project
                ConnectionSetupIdeaRSOpenModel result = apiInstance.UpdateSetup(projectId, connectionSetupIdeaRSOpenModel);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling ProjectApi.UpdateSetup: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the UpdateSetupWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Update setup of the project
    ApiResponse<ConnectionSetupIdeaRSOpenModel> response = apiInstance.UpdateSetupWithHttpInfo(projectId, connectionSetupIdeaRSOpenModel);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling ProjectApi.UpdateSetupWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service to update project setup |  |
| **connectionSetupIdeaRSOpenModel** | [**ConnectionSetupIdeaRSOpenModel?**](ConnectionSetupIdeaRSOpenModel?.md) |  | [optional]  |

### Return type

[**ConnectionSetupIdeaRSOpenModel**](ConnectionSetupIdeaRSOpenModel.md)

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

