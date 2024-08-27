# connection_restapi_client_poc.Api.TemplateApi

All URIs are relative to *http://localhost*

| Method | HTTP request | Description |
|--------|--------------|-------------|
| [**ApplyTemplate**](TemplateApi.md#applytemplate) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/apply-template | Apply the connection template applyTemplateParam on the connection connectionId in the project projectId |
| [**GetDefaultTemplateMapping**](TemplateApi.md#getdefaulttemplatemapping) | **POST** /api/1/projects/{projectId}/connections/{connectionId}/get-default-mapping | Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId |

<a id="applytemplate"></a>
# **ApplyTemplate**
> Object ApplyTemplate (Guid projectId, int connectionId, ConTemplateApplyParam? conTemplateApplyParam = null)

Apply the connection template applyTemplateParam on the connection connectionId in the project projectId

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class ApplyTemplateExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new TemplateApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection where to apply the template
            var conTemplateApplyParam = new ConTemplateApplyParam?(); // ConTemplateApplyParam? | Template to apply (optional) 

            try
            {
                // Apply the connection template applyTemplateParam on the connection connectionId in the project projectId
                Object result = apiInstance.ApplyTemplate(projectId, connectionId, conTemplateApplyParam);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling TemplateApi.ApplyTemplate: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the ApplyTemplateWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Apply the connection template applyTemplateParam on the connection connectionId in the project projectId
    ApiResponse<Object> response = apiInstance.ApplyTemplateWithHttpInfo(projectId, connectionId, conTemplateApplyParam);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling TemplateApi.ApplyTemplateWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection where to apply the template |  |
| **conTemplateApplyParam** | [**ConTemplateApplyParam?**](ConTemplateApplyParam?.md) | Template to apply | [optional]  |

### Return type

**Object**

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

<a id="getdefaulttemplatemapping"></a>
# **GetDefaultTemplateMapping**
> TemplateConversions GetDefaultTemplateMapping (Guid projectId, int connectionId, ConTemplateMappingGetParam? conTemplateMappingGetParam = null)

Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId

The result IdeaStatiCa.Api.Connection.Model.TemplateConversionsDefault mapping to apply the passed template.  It can be modified by a user and used for the application of a template M:IdeaStatiCa.ConnectionRestApi.Controllers.TemplateController.ApplyConnectionTemplateAsync(System.Guid,System.Int32,IdeaStatiCa.Api.Connection.Model.ConTemplateApplyParam) method.

### Example
```csharp
using System.Collections.Generic;
using System.Diagnostics;
using connection_restapi_client_poc.Api;
using connection_restapi_client_poc.Client;
using connection_restapi_client_poc.Model;

namespace Example
{
    public class GetDefaultTemplateMappingExample
    {
        public static void Main()
        {
            Configuration config = new Configuration();
            config.BasePath = "http://localhost";
            var apiInstance = new TemplateApi(config);
            var projectId = "projectId_example";  // Guid | The unique identifier of the opened project in the ConnectionRestApi service
            var connectionId = 56;  // int | Id of the connection to get default mapping
            var conTemplateMappingGetParam = new ConTemplateMappingGetParam?(); // ConTemplateMappingGetParam? | Data of the template to get default mapping (optional) 

            try
            {
                // Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId
                TemplateConversions result = apiInstance.GetDefaultTemplateMapping(projectId, connectionId, conTemplateMappingGetParam);
                Debug.WriteLine(result);
            }
            catch (ApiException  e)
            {
                Debug.Print("Exception when calling TemplateApi.GetDefaultTemplateMapping: " + e.Message);
                Debug.Print("Status Code: " + e.ErrorCode);
                Debug.Print(e.StackTrace);
            }
        }
    }
}
```

#### Using the GetDefaultTemplateMappingWithHttpInfo variant
This returns an ApiResponse object which contains the response data, status code and headers.

```csharp
try
{
    // Get the default mappings for the application of the connection template passed in templateToApply  on connectionId in the project projectId
    ApiResponse<TemplateConversions> response = apiInstance.GetDefaultTemplateMappingWithHttpInfo(projectId, connectionId, conTemplateMappingGetParam);
    Debug.Write("Status Code: " + response.StatusCode);
    Debug.Write("Response Headers: " + response.Headers);
    Debug.Write("Response Body: " + response.Data);
}
catch (ApiException e)
{
    Debug.Print("Exception when calling TemplateApi.GetDefaultTemplateMappingWithHttpInfo: " + e.Message);
    Debug.Print("Status Code: " + e.ErrorCode);
    Debug.Print(e.StackTrace);
}
```

### Parameters

| Name | Type | Description | Notes |
|------|------|-------------|-------|
| **projectId** | **Guid** | The unique identifier of the opened project in the ConnectionRestApi service |  |
| **connectionId** | **int** | Id of the connection to get default mapping |  |
| **conTemplateMappingGetParam** | [**ConTemplateMappingGetParam?**](ConTemplateMappingGetParam?.md) | Data of the template to get default mapping | [optional]  |

### Return type

[**TemplateConversions**](TemplateConversions.md)

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

