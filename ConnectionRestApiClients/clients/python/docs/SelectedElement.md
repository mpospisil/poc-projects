# SelectedElement


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**table_id** | **str** |  | [optional] 
**element_id** | **str** |  | [optional] 
**container_type** | [**TableContainerType**](TableContainerType.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.selected_element import SelectedElement

# TODO update the JSON string below
json = "{}"
# create an instance of SelectedElement from a JSON string
selected_element_instance = SelectedElement.from_json(json)
# print the JSON string representation of the object
print(SelectedElement.to_json())

# convert the object into a dict
selected_element_dict = selected_element_instance.to_dict()
# create an instance of SelectedElement from a dict
selected_element_from_dict = SelectedElement.from_dict(selected_element_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


