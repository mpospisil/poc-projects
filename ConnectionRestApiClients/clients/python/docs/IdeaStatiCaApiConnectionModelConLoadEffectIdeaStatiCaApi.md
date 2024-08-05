# IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_percentage** | **bool** |  | [optional] 
**member_loadings** | [**List[IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConLoadEffectMemberLoadIdeaStatiCaApi.md) |  | [optional] 
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**active** | **bool** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi from a JSON string
idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api_instance = IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.from_json(json)
# print the JSON string representation of the object
print(IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.to_json())

# convert the object into a dict
idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api_dict = idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api_instance.to_dict()
# create an instance of IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi from a dict
idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api_from_dict = IdeaStatiCaApiConnectionModelConLoadEffectIdeaStatiCaApi.from_dict(idea_stati_ca_api_connection_model_con_load_effect_idea_stati_ca_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


