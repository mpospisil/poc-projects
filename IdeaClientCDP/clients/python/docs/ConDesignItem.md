# ConDesignItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**picture_id** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**name** | **str** |  | 
**owner_id** | **str** |  | [optional] 
**design_code** | **str** |  | [optional] 
**con_design_set_id** | **str** |  | [optional] 
**con_design_item_id** | **str** |  | [optional] 
**design_data** | [**ConDesignData**](ConDesignData.md) |  | [optional] 
**company_name** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**load_transfer_type** | [**LoadTransferType**](LoadTransferType.md) |  | [optional] 
**author_name** | **str** |  | [optional] 
**activity** | **bool** |  | [optional] 
**priority** | **bool** |  | [optional] 
**imported** | **bool** |  | [optional] 
**is_parametric** | **bool** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_design_item import ConDesignItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConDesignItem from a JSON string
con_design_item_instance = ConDesignItem.from_json(json)
# print the JSON string representation of the object
print(ConDesignItem.to_json())

# convert the object into a dict
con_design_item_dict = con_design_item_instance.to_dict()
# create an instance of ConDesignItem from a dict
con_design_item_from_dict = ConDesignItem.from_dict(con_design_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


