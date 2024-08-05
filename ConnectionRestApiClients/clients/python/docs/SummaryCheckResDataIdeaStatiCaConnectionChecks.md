# SummaryCheckResDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**check_value** | **float** |  | [optional] 
**check_context** | [**SummaryCheckResDataContextIdeaStatiCaConnectionChecks**](SummaryCheckResDataContextIdeaStatiCaConnectionChecks.md) |  | [optional] 
**msg_context** | [**SummaryCheckResDataMessageContextIdeaStatiCaConnectionChecks**](SummaryCheckResDataMessageContextIdeaStatiCaConnectionChecks.md) |  | [optional] 
**limit** | **float** |  | [optional] 
**txt_message** | **str** |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**check_status** | **bool** |  | [optional] 
**limit_check_status** | **bool** |  | [optional] 
**load_case_id** | **int** |  | [optional] 
**load_case** | **str** |  | [optional] 
**max_unity_check** | **float** |  | [optional] 
**form** | **str** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.summary_check_res_data_idea_stati_ca_connection_checks import SummaryCheckResDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of SummaryCheckResDataIdeaStatiCaConnectionChecks from a JSON string
summary_check_res_data_idea_stati_ca_connection_checks_instance = SummaryCheckResDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(SummaryCheckResDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
summary_check_res_data_idea_stati_ca_connection_checks_dict = summary_check_res_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of SummaryCheckResDataIdeaStatiCaConnectionChecks from a dict
summary_check_res_data_idea_stati_ca_connection_checks_from_dict = SummaryCheckResDataIdeaStatiCaConnectionChecks.from_dict(summary_check_res_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


