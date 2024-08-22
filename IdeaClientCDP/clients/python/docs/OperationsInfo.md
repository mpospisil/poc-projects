# OperationsInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_plate** | [**EndPlate**](EndPlate.md) |  | [optional] 
**shifted_end_plate** | [**ShiftedEndPlate**](ShiftedEndPlate.md) |  | [optional] 
**stub** | [**Stub**](Stub.md) |  | [optional] 
**plate_to_plate** | [**PlateToPlate**](PlateToPlate.md) |  | [optional] 
**splice_plate** | [**SplicePlate**](SplicePlate.md) |  | [optional] 
**gusset_plate** | [**GussetPlate**](GussetPlate.md) |  | [optional] 
**connecting_plate** | [**ConnectingPlate**](ConnectingPlate.md) |  | [optional] 
**fin_plate** | [**FinPlate**](FinPlate.md) |  | [optional] 
**cleat** | [**Cleat**](Cleat.md) |  | [optional] 
**anchoring** | [**Anchoring**](Anchoring.md) |  | [optional] 
**opening** | [**Opening**](Opening.md) |  | [optional] 
**general_plate** | [**GeneralPlate**](GeneralPlate.md) |  | [optional] 
**stiffener** | [**Stiffener**](Stiffener.md) |  | [optional] 
**bolt_grid** | [**BoltGrid**](BoltGrid.md) |  | [optional] 
**pin_grid** | [**PinGrid**](PinGrid.md) |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.operations_info import OperationsInfo

# TODO update the JSON string below
json = "{}"
# create an instance of OperationsInfo from a JSON string
operations_info_instance = OperationsInfo.from_json(json)
# print the JSON string representation of the object
print(OperationsInfo.to_json())

# convert the object into a dict
operations_info_dict = operations_info_instance.to_dict()
# create an instance of OperationsInfo from a dict
operations_info_from_dict = OperationsInfo.from_dict(operations_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


