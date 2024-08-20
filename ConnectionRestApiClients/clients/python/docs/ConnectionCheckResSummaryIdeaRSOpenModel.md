# ConnectionCheckResSummaryIdeaRSOpenModel

Check summary

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_value** | **float** | Check value | [optional] 
**check_status** | **bool** | Status of check | [optional] 
**load_case_id** | **int** | Id of Load Case | [optional] 
**name** | **str** | Name | [optional] 
**unity_check_message** | **str** | Detail message about overall check | [optional] 
**skipped** | **bool** | Whether the check was calculated or not.  If true, the check was not calculated and IdeaRS.OpenModel.Connection.CheckResSummary.CheckValue should be ignored, otherwise false. | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_check_res_summary_idea_rs_open_model import ConnectionCheckResSummaryIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionCheckResSummaryIdeaRSOpenModel from a JSON string
connection_check_res_summary_idea_rs_open_model_instance = ConnectionCheckResSummaryIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionCheckResSummaryIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_check_res_summary_idea_rs_open_model_dict = connection_check_res_summary_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionCheckResSummaryIdeaRSOpenModel from a dict
connection_check_res_summary_idea_rs_open_model_from_dict = ConnectionCheckResSummaryIdeaRSOpenModel.from_dict(connection_check_res_summary_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


