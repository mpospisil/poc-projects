# idea_cdp_client_poc.UploadDataApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api9_upload_data_pre_signed_url_get**](UploadDataApi.md#api9_upload_data_pre_signed_url_get) | **GET** /api/9/upload-data/pre-signed-url | 


# **api9_upload_data_pre_signed_url_get**
> List[PreSignedUrl] api9_upload_data_pre_signed_url_get(count=count)



### Example

* Bearer (JWT) Authentication (Bearer):

```python
import idea_cdp_client_poc
from idea_cdp_client_poc.models.pre_signed_url import PreSignedUrl
from idea_cdp_client_poc.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = idea_cdp_client_poc.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = idea_cdp_client_poc.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with idea_cdp_client_poc.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = idea_cdp_client_poc.UploadDataApi(api_client)
    count = 56 # int |  (optional)

    try:
        api_response = api_instance.api9_upload_data_pre_signed_url_get(count=count)
        print("The response of UploadDataApi->api9_upload_data_pre_signed_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UploadDataApi->api9_upload_data_pre_signed_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **count** | **int**|  | [optional] 

### Return type

[**List[PreSignedUrl]**](PreSignedUrl.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

