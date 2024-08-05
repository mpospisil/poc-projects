# ConnectionConnectionDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conenction_point_id** | **int** |  | [optional] 
**beams** | [**List[ConnectionBeamDataIdeaRSOpenModel]**](ConnectionBeamDataIdeaRSOpenModel.md) |  | [optional] 
**plates** | [**List[ConnectionPlateDataIdeaRSOpenModel]**](ConnectionPlateDataIdeaRSOpenModel.md) |  | [optional] 
**folded_plates** | [**List[ConnectionFoldedPlateDataIdeaRSOpenModel]**](ConnectionFoldedPlateDataIdeaRSOpenModel.md) |  | [optional] 
**bolt_grids** | [**List[ConnectionBoltGridIdeaRSOpenModel]**](ConnectionBoltGridIdeaRSOpenModel.md) |  | [optional] 
**anchor_grids** | [**List[ConnectionAnchorGridIdeaRSOpenModel]**](ConnectionAnchorGridIdeaRSOpenModel.md) |  | [optional] 
**welds** | [**List[ConnectionWeldDataIdeaRSOpenModel]**](ConnectionWeldDataIdeaRSOpenModel.md) |  | [optional] 
**concrete_blocks** | [**List[ConnectionConcreteBlockDataIdeaRSOpenModel]**](ConnectionConcreteBlockDataIdeaRSOpenModel.md) |  | [optional] 
**cut_beam_by_beams** | [**List[ConnectionCutBeamByBeamDataIdeaRSOpenModel]**](ConnectionCutBeamByBeamDataIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_connection_data_idea_rs_open_model import ConnectionConnectionDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConnectionDataIdeaRSOpenModel from a JSON string
connection_connection_data_idea_rs_open_model_instance = ConnectionConnectionDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionConnectionDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_connection_data_idea_rs_open_model_dict = connection_connection_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionConnectionDataIdeaRSOpenModel from a dict
connection_connection_data_idea_rs_open_model_from_dict = ConnectionConnectionDataIdeaRSOpenModel.from_dict(connection_connection_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


