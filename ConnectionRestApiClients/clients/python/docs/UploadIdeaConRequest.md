# UploadIdeaConRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idea_con_file** | **bytearray** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.upload_idea_con_request import UploadIdeaConRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UploadIdeaConRequest from a JSON string
upload_idea_con_request_instance = UploadIdeaConRequest.from_json(json)
# print the JSON string representation of the object
print(UploadIdeaConRequest.to_json())

# convert the object into a dict
upload_idea_con_request_dict = upload_idea_con_request_instance.to_dict()
# create an instance of UploadIdeaConRequest from a dict
upload_idea_con_request_from_dict = UploadIdeaConRequest.from_dict(upload_idea_con_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


