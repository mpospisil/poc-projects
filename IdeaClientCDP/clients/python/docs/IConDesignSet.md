# IConDesignSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**owner_id** | **str** |  | [optional] 
**created** | **datetime** |  | [optional] 
**modified** | **datetime** |  | [optional] 
**type** | [**ConDesignSetType**](ConDesignSetType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.i_con_design_set import IConDesignSet

# TODO update the JSON string below
json = "{}"
# create an instance of IConDesignSet from a JSON string
i_con_design_set_instance = IConDesignSet.from_json(json)
# print the JSON string representation of the object
print(IConDesignSet.to_json())

# convert the object into a dict
i_con_design_set_dict = i_con_design_set_instance.to_dict()
# create an instance of IConDesignSet from a dict
i_con_design_set_from_dict = IConDesignSet.from_dict(i_con_design_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


