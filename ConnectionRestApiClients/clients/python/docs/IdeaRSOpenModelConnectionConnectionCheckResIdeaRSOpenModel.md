# IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_res_summary** | [**List[IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResSummaryIdeaRSOpenModel.md) |  | [optional] 
**check_res_plate** | [**List[IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResPlateIdeaRSOpenModel.md) |  | [optional] 
**check_res_weld** | [**List[IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResWeldIdeaRSOpenModel.md) |  | [optional] 
**check_res_bolt** | [**List[IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResBoltIdeaRSOpenModel.md) |  | [optional] 
**check_res_anchor** | [**List[IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResAnchorIdeaRSOpenModel.md) |  | [optional] 
**check_res_concrete_block** | [**List[IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel]**](IdeaRSOpenModelConnectionCheckResConcreteBlockIdeaRSOpenModel.md) |  | [optional] 
**buckling_results** | [**List[IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel]**](IdeaRSOpenModelConnectionBucklingResIdeaRSOpenModel.md) |  | [optional] 
**name** | **str** |  | [optional] 
**connection_id** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**messages** | [**IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel**](IdeaRSOpenModelMessageOpenMessagesIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection-restapi-client-poc.models.idea_rs_open_model_connection_connection_check_res_idea_rs_open_model import IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel from a JSON string
idea_rs_open_model_connection_connection_check_res_idea_rs_open_model_instance = IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel.to_json())

# convert the object into a dict
idea_rs_open_model_connection_connection_check_res_idea_rs_open_model_dict = idea_rs_open_model_connection_connection_check_res_idea_rs_open_model_instance.to_dict()
# create an instance of IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel from a dict
idea_rs_open_model_connection_connection_check_res_idea_rs_open_model_from_dict = IdeaRSOpenModelConnectionConnectionCheckResIdeaRSOpenModel.from_dict(idea_rs_open_model_connection_connection_check_res_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


