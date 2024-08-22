# CreateConDesignSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**ConDesignSetType**](ConDesignSetType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.create_con_design_set import CreateConDesignSet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConDesignSet from a JSON string
create_con_design_set_instance = CreateConDesignSet.from_json(json)
# print the JSON string representation of the object
print(CreateConDesignSet.to_json())

# convert the object into a dict
create_con_design_set_dict = create_con_design_set_instance.to_dict()
# create an instance of CreateConDesignSet from a dict
create_con_design_set_from_dict = CreateConDesignSet.from_dict(create_con_design_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


