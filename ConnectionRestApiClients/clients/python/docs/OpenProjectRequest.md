# OpenProjectRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**idea_con_file** | **bytearray** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.open_project_request import OpenProjectRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OpenProjectRequest from a JSON string
open_project_request_instance = OpenProjectRequest.from_json(json)
# print the JSON string representation of the object
print(OpenProjectRequest.to_json())

# convert the object into a dict
open_project_request_dict = open_project_request_instance.to_dict()
# create an instance of OpenProjectRequest from a dict
open_project_request_from_dict = OpenProjectRequest.from_dict(open_project_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


