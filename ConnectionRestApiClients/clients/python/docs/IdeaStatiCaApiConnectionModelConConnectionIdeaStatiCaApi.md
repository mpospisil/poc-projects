# IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**analysis_type** | [**IdeaStatiCaApiConnectionModelConAnalysisTypeEnumIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConAnalysisTypeEnumIdeaStatiCaApi.md) |  | [optional] 
**load_options** | [**IdeaStatiCaApiConnectionModelConLoadingOptionsIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConLoadingOptionsIdeaStatiCaApi.md) |  | [optional] 
**bearing_member_id** | **int** |  | [optional] 
**is_calculated** | **bool** |  | [optional] [readonly] 

## Example

```python
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi from a JSON string
idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api_instance = IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.from_json(json)
# print the JSON string representation of the object
print(IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.to_json())

# convert the object into a dict
idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api_dict = idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api_instance.to_dict()
# create an instance of IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi from a dict
idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api_from_dict = IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.from_dict(idea_stati_ca_api_connection_model_con_connection_idea_stati_ca_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


