# LoadEffectDataIdeaStatiCaConnectionChecks


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**internal_forces** | **List[int]** |  | [optional] 
**purpose** | [**DataEPurposeIdeaRSConnections**](DataEPurposeIdeaRSConnections.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.load_effect_data_idea_stati_ca_connection_checks import LoadEffectDataIdeaStatiCaConnectionChecks

# TODO update the JSON string below
json = "{}"
# create an instance of LoadEffectDataIdeaStatiCaConnectionChecks from a JSON string
load_effect_data_idea_stati_ca_connection_checks_instance = LoadEffectDataIdeaStatiCaConnectionChecks.from_json(json)
# print the JSON string representation of the object
print(LoadEffectDataIdeaStatiCaConnectionChecks.to_json())

# convert the object into a dict
load_effect_data_idea_stati_ca_connection_checks_dict = load_effect_data_idea_stati_ca_connection_checks_instance.to_dict()
# create an instance of LoadEffectDataIdeaStatiCaConnectionChecks from a dict
load_effect_data_idea_stati_ca_connection_checks_from_dict = LoadEffectDataIdeaStatiCaConnectionChecks.from_dict(load_effect_data_idea_stati_ca_connection_checks_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


