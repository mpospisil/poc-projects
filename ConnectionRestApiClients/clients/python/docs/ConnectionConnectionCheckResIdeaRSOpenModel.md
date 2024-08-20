# ConnectionConnectionCheckResIdeaRSOpenModel

Results for connection in project

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_res_summary** | [**List[ConnectionCheckResSummaryIdeaRSOpenModel]**](ConnectionCheckResSummaryIdeaRSOpenModel.md) | List of CheckResSummary | [optional] 
**check_res_plate** | [**List[ConnectionCheckResPlateIdeaRSOpenModel]**](ConnectionCheckResPlateIdeaRSOpenModel.md) | List of check results for plates | [optional] 
**check_res_weld** | [**List[ConnectionCheckResWeldIdeaRSOpenModel]**](ConnectionCheckResWeldIdeaRSOpenModel.md) | List of check results for welds | [optional] 
**check_res_bolt** | [**List[ConnectionCheckResBoltIdeaRSOpenModel]**](ConnectionCheckResBoltIdeaRSOpenModel.md) | List of check results for bolts | [optional] 
**check_res_anchor** | [**List[ConnectionCheckResAnchorIdeaRSOpenModel]**](ConnectionCheckResAnchorIdeaRSOpenModel.md) | List of check results for anchors | [optional] 
**check_res_concrete_block** | [**List[ConnectionCheckResConcreteBlockIdeaRSOpenModel]**](ConnectionCheckResConcreteBlockIdeaRSOpenModel.md) | List of check results for concrete blocks | [optional] 
**buckling_results** | [**List[ConnectionBucklingResIdeaRSOpenModel]**](ConnectionBucklingResIdeaRSOpenModel.md) | List of results of buckling analysis | [optional] 
**name** | **str** | Name of connection | [optional] 
**connection_id** | **str** | Guid of connection | [optional] 
**id** | **int** | Integer Id of connection | [optional] 
**messages** | [**MessageOpenMessagesIdeaRSOpenModel**](MessageOpenMessagesIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_connection_check_res_idea_rs_open_model import ConnectionConnectionCheckResIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConnectionCheckResIdeaRSOpenModel from a JSON string
connection_connection_check_res_idea_rs_open_model_instance = ConnectionConnectionCheckResIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionConnectionCheckResIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_connection_check_res_idea_rs_open_model_dict = connection_connection_check_res_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionConnectionCheckResIdeaRSOpenModel from a dict
connection_connection_check_res_idea_rs_open_model_from_dict = ConnectionConnectionCheckResIdeaRSOpenModel.from_dict(connection_connection_check_res_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


