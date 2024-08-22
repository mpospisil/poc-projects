# ConPart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stiffness** | [**StiffnessCategoryTypes**](StiffnessCategoryTypes.md) |  | [optional] 
**category** | [**ConPartCategoryTypes**](ConPartCategoryTypes.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_part import ConPart

# TODO update the JSON string below
json = "{}"
# create an instance of ConPart from a JSON string
con_part_instance = ConPart.from_json(json)
# print the JSON string representation of the object
print(ConPart.to_json())

# convert the object into a dict
con_part_dict = con_part_instance.to_dict()
# create an instance of ConPart from a dict
con_part_from_dict = ConPart.from_dict(con_part_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


