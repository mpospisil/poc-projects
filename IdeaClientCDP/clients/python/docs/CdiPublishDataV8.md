# CdiPublishDataV8


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**con_design_item** | [**ConDesignItem**](ConDesignItem.md) |  | [optional] 
**picture_upload_id** | **str** |  | [optional] 
**project_upload_id** | **str** |  | [optional] 
**scene3_d_upload_id** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.cdi_publish_data_v8 import CdiPublishDataV8

# TODO update the JSON string below
json = "{}"
# create an instance of CdiPublishDataV8 from a JSON string
cdi_publish_data_v8_instance = CdiPublishDataV8.from_json(json)
# print the JSON string representation of the object
print(CdiPublishDataV8.to_json())

# convert the object into a dict
cdi_publish_data_v8_dict = cdi_publish_data_v8_instance.to_dict()
# create an instance of CdiPublishDataV8 from a dict
cdi_publish_data_v8_from_dict = CdiPublishDataV8.from_dict(cdi_publish_data_v8_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


