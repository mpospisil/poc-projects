# CssData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arc_segment_count** | **int** |  | [optional] 
**css_class** | [**CssClass**](CssClass.md) |  | [optional] 
**css_size** | [**CssSize**](CssSize.md) |  | [optional] 
**integrality_type** | [**IntegralityType**](IntegralityType.md) |  | [optional] 
**label** | **str** |  | [optional] 
**main_segment_count** | **int** |  | [optional] 
**shape** | [**Shape**](Shape.md) |  | [optional] 
**type** | **str** |  | [optional] 
**form_code** | [**FormCode**](FormCode.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.css_data import CssData

# TODO update the JSON string below
json = "{}"
# create an instance of CssData from a JSON string
css_data_instance = CssData.from_json(json)
# print the JSON string representation of the object
print(CssData.to_json())

# convert the object into a dict
css_data_dict = css_data_instance.to_dict()
# create an instance of CssData from a dict
css_data_from_dict = CssData.from_dict(css_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


