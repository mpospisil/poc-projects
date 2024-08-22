# ConDesignData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**typology** | [**ConTypology**](ConTypology.md) |  | [optional] 
**manufacture** | [**ConManufacture**](ConManufacture.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_design_data import ConDesignData

# TODO update the JSON string below
json = "{}"
# create an instance of ConDesignData from a JSON string
con_design_data_instance = ConDesignData.from_json(json)
# print the JSON string representation of the object
print(ConDesignData.to_json())

# convert the object into a dict
con_design_data_dict = con_design_data_instance.to_dict()
# create an instance of ConDesignData from a dict
con_design_data_from_dict = ConDesignData.from_dict(con_design_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


