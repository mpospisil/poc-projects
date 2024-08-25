# ConDesignSetDto


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
**permissions** | [**List[Permission]**](Permission.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_design_set_dto import ConDesignSetDto

# TODO update the JSON string below
json = "{}"
# create an instance of ConDesignSetDto from a JSON string
con_design_set_dto_instance = ConDesignSetDto.from_json(json)
# print the JSON string representation of the object
print(ConDesignSetDto.to_json())

# convert the object into a dict
con_design_set_dto_dict = con_design_set_dto_instance.to_dict()
# create an instance of ConDesignSetDto from a dict
con_design_set_dto_from_dict = ConDesignSetDto.from_dict(con_design_set_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


