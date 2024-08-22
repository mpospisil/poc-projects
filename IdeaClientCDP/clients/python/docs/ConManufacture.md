# ConManufacture


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**manufacturing_type** | [**ManufacturingTypes**](ManufacturingTypes.md) |  | [optional] 
**connection_template** | **str** |  | [optional] 
**con_parts** | [**List[ConPart]**](ConPart.md) |  | [optional] 
**operations_info** | [**OperationsInfo**](OperationsInfo.md) |  | [optional] 
**typology_code** | **str** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_manufacture import ConManufacture

# TODO update the JSON string below
json = "{}"
# create an instance of ConManufacture from a JSON string
con_manufacture_instance = ConManufacture.from_json(json)
# print the JSON string representation of the object
print(ConManufacture.to_json())

# convert the object into a dict
con_manufacture_dict = con_manufacture_instance.to_dict()
# create an instance of ConManufacture from a dict
con_manufacture_from_dict = ConManufacture.from_dict(con_manufacture_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


