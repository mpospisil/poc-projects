# IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**conenction_point_id** | **int** |  | [optional] 
**beams** | [**List[IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionBeamDataIdeaRSOpenModel.md) |  | [optional] 
**plates** | [**List[IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionPlateDataIdeaRSOpenModel.md) |  | [optional] 
**folded_plates** | [**List[IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionFoldedPlateDataIdeaRSOpenModel.md) |  | [optional] 
**bolt_grids** | [**List[IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel]**](IdeaRSOpenModelConnectionBoltGridIdeaRSOpenModel.md) |  | [optional] 
**anchor_grids** | [**List[IdeaRSOpenModelConnectionAnchorGridIdeaRSOpenModel]**](IdeaRSOpenModelConnectionAnchorGridIdeaRSOpenModel.md) |  | [optional] 
**welds** | [**List[IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionWeldDataIdeaRSOpenModel.md) |  | [optional] 
**concrete_blocks** | [**List[IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionConcreteBlockDataIdeaRSOpenModel.md) |  | [optional] 
**cut_beam_by_beams** | [**List[IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCutBeamByBeamDataIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection-restapi-client-poc.models.idea_rs_open_model_connection_connection_data_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_connection_data_idea_rs_open_model_instance = IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_connection_data_idea_rs_open_model_dict = idea_rs_open_model_connection_connection_data_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel from a dict
idea_rs_open_model_connection_connection_data_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionConnectionDataIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_connection_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


