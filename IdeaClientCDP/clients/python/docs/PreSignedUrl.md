# PreSignedUrl


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.pre_signed_url import PreSignedUrl

# TODO update the JSON string below
json = "{}"
# create an instance of PreSignedUrl from a JSON string
pre_signed_url_instance = PreSignedUrl.from_json(json)
# print the JSON string representation of the object
print(PreSignedUrl.to_json())

# convert the object into a dict
pre_signed_url_dict = pre_signed_url_instance.to_dict()
# create an instance of PreSignedUrl from a dict
pre_signed_url_from_dict = PreSignedUrl.from_dict(pre_signed_url_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


