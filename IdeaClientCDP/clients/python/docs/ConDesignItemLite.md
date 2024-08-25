# ConDesignItemLite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**picture_url** | **str** |  | [optional] 
**design_code** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_design_item_lite import ConDesignItemLite

# TODO update the JSON string below
json = "{}"
# create an instance of ConDesignItemLite from a JSON string
con_design_item_lite_instance = ConDesignItemLite.from_json(json)
# print the JSON string representation of the object
print(ConDesignItemLite.to_json())

# convert the object into a dict
con_design_item_lite_dict = con_design_item_lite_instance.to_dict()
# create an instance of ConDesignItemLite from a dict
con_design_item_lite_from_dict = ConDesignItemLite.from_dict(con_design_item_lite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


