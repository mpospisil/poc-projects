# MessageOpenMessageIdeaRSOpenModel

Open message base class

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**number** | [**MessageMessageNumberIdeaRSOpenModel**](MessageMessageNumberIdeaRSOpenModel.md) |  | [optional] 
**description** | **str** | Description of message | [optional] 

## Example

```python
from connection_restapi_client_poc.models.message_open_message_idea_rs_open_model import MessageOpenMessageIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of MessageOpenMessageIdeaRSOpenModel from a JSON string
message_open_message_idea_rs_open_model_instance = MessageOpenMessageIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(MessageOpenMessageIdeaRSOpenModel.to_json())

# convert the object into a dict
message_open_message_idea_rs_open_model_dict = message_open_message_idea_rs_open_model_instance.to_dict()
# create an instance of MessageOpenMessageIdeaRSOpenModel from a dict
message_open_message_idea_rs_open_model_from_dict = MessageOpenMessageIdeaRSOpenModel.from_dict(message_open_message_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


