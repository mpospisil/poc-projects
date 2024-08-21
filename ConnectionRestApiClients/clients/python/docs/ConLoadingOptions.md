# ConLoadingOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**loads_in_equilibrium** | **bool** |  | [optional] 
**loads_in_percentage** | **bool** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.con_loading_options import ConLoadingOptions

# TODO update the JSON string below
json = "{}"
# create an instance of ConLoadingOptions from a JSON string
con_loading_options_instance = ConLoadingOptions.from_json(json)
# print the JSON string representation of the object
print(ConLoadingOptions.to_json())

# convert the object into a dict
con_loading_options_dict = con_loading_options_instance.to_dict()
# create an instance of ConLoadingOptions from a dict
con_loading_options_from_dict = ConLoadingOptions.from_dict(con_loading_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


