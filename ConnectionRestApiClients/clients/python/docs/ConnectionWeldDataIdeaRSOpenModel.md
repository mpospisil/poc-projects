# ConnectionWeldDataIdeaRSOpenModel

Provides data of the single weld

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Id of the weld | [optional] 
**name** | **str** | Name of the weld | [optional] 
**thickness** | **float** | Thickness of the weld | [optional] 
**material** | **str** | Name of the material | [optional] 
**weld_material** | [**ReferenceElementIdeaRSOpenModel**](ReferenceElementIdeaRSOpenModel.md) |  | [optional] 
**weld_type** | [**ConnectionWeldTypeIdeaRSOpenModel**](ConnectionWeldTypeIdeaRSOpenModel.md) |  | [optional] 
**connected_part_ids** | **List[str]** | Id of the weld | [optional] 
**start** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 
**end** | [**Geometry3DPoint3DIdeaRSOpenModel**](Geometry3DPoint3DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_weld_data_idea_rs_open_model import ConnectionWeldDataIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionWeldDataIdeaRSOpenModel from a JSON string
connection_weld_data_idea_rs_open_model_instance = ConnectionWeldDataIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionWeldDataIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_weld_data_idea_rs_open_model_dict = connection_weld_data_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionWeldDataIdeaRSOpenModel from a dict
connection_weld_data_idea_rs_open_model_from_dict = ConnectionWeldDataIdeaRSOpenModel.from_dict(connection_weld_data_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


