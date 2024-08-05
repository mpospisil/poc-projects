# IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_id** | **str** |  | [optional] 
**project_info** | [**IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi**](IdeaStatiCaApiConnectionModelConProjectDataIdeaStatiCaApi.md) |  | [optional] 
**connections** | [**List[IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi]**](IdeaStatiCaApiConnectionModelConConnectionIdeaStatiCaApi.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api import IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi

# TODO update the JSON string below
json = "{}"
# create an instance of IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi from a JSON string
idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api_instance = IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.from_json(json)
# print the JSON string representation of the object
print(IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.to_json())

# convert the object into a dict
idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api_dict = idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api_instance.to_dict()
# create an instance of IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi from a dict
idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api_from_dict = IdeaStatiCaApiConnectionModelConProjectIdeaStatiCaApi.from_dict(idea_stati_ca_api_connection_model_con_project_idea_stati_ca_api_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


