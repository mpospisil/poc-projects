# IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**identifier** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**analysis_type** | [**IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelConnectionConAnalysisTypeEnumIdeaStatiCaPlugin.md) |  | [optional] 
**load_options** | [**IdeaStatiCaPluginApiConnectionRestModelModelSettingsConLoadingOptionsIdeaStatiCaPlugin**](IdeaStatiCaPluginApiConnectionRestModelModelSettingsConLoadingOptionsIdeaStatiCaPlugin.md) |  | [optional] 
**bearing_member_id** | **int** |  | [optional] 
**is_calculated** | **bool** |  | [optional] [readonly] 

## Example

```python
from connection_restapi_client_poc.models.idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin import IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin from a JSON string
idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin_instance = IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.from_json(json)
# print the JSON string representation of the object
print(IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.to_json())

# convert the object into a dict
idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin_dict = idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin_instance.to_dict()
# create an instance of IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin from a dict
idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin_from_dict = IdeaStatiCaPluginApiConnectionRestModelModelConnectionConConnectionIdeaStatiCaPlugin.from_dict(idea_stati_ca_plugin_api_connection_rest_model_model_connection_con_connection_idea_stati_ca_plugin_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


