# Anchoring


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**anchoring_type** | [**AnchoringType**](AnchoringType.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.anchoring import Anchoring

# TODO update the JSON string below
json = "{}"
# create an instance of Anchoring from a JSON string
anchoring_instance = Anchoring.from_json(json)
# print the JSON string representation of the object
print(Anchoring.to_json())

# convert the object into a dict
anchoring_dict = anchoring_instance.to_dict()
# create an instance of Anchoring from a dict
anchoring_from_dict = Anchoring.from_dict(anchoring_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


