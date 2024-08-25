# CdiPublishDataWithoutSceneV9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**con_design_item** | [**ConDesignItem**](ConDesignItem.md) |  | [optional] 
**picture_upload_id** | **str** |  | [optional] 
**project_upload_id** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.cdi_publish_data_without_scene_v9 import CdiPublishDataWithoutSceneV9

# TODO update the JSON string below
json = "{}"
# create an instance of CdiPublishDataWithoutSceneV9 from a JSON string
cdi_publish_data_without_scene_v9_instance = CdiPublishDataWithoutSceneV9.from_json(json)
# print the JSON string representation of the object
print(CdiPublishDataWithoutSceneV9.to_json())

# convert the object into a dict
cdi_publish_data_without_scene_v9_dict = cdi_publish_data_without_scene_v9_instance.to_dict()
# create an instance of CdiPublishDataWithoutSceneV9 from a dict
cdi_publish_data_without_scene_v9_from_dict = CdiPublishDataWithoutSceneV9.from_dict(cdi_publish_data_without_scene_v9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


