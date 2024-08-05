# ConnectionFoldedPlateDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plates** | [**List[ConnectionPlateDataIdeaRSOpenModel]**](ConnectionPlateDataIdeaRSOpenModel.md) |  | [optional] 
**bends** | [**List[ConnectionBendDataIdeaRSOpenModel]**](ConnectionBendDataIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_folded_plate_data_idea_rs_open_model import ConnectionFoldedPlateDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionFoldedPlateDataIdeaRSOpenModel from a JSON string
connection_folded_plate_data_idea_rs_open_model_instance = ConnectionFoldedPlateDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionFoldedPlateDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_folded_plate_data_idea_rs_open_model_dict = connection_folded_plate_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionFoldedPlateDataIdeaRSOpenModel from a dict
connection_folded_plate_data_idea_rs_open_model_from_dict = ConnectionFoldedPlateDataIdeaRSOpenModel.from_dict(connection_folded_plate_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


