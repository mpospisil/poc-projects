# CdiDesignItemV9


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**con_design_item** | [**ConDesignItem**](ConDesignItem.md) |  | [optional] 
**picture_url** | **str** |  | [optional] 
**project_url** | **str** |  | [optional] 
**scene3d_url** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.cdi_design_item_v9 import CdiDesignItemV9

# TODO update the JSON string below
json = "{}"
# create an instance of CdiDesignItemV9 from a JSON string
cdi_design_item_v9_instance = CdiDesignItemV9.from_json(json)
# print the JSON string representation of the object
print(CdiDesignItemV9.to_json())

# convert the object into a dict
cdi_design_item_v9_dict = cdi_design_item_v9_instance.to_dict()
# create an instance of CdiDesignItemV9 from a dict
cdi_design_item_v9_from_dict = CdiDesignItemV9.from_dict(cdi_design_item_v9_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


