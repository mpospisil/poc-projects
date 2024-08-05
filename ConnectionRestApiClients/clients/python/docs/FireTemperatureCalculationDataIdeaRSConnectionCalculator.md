# FireTemperatureCalculationDataIdeaRSConnectionCalculator


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_exposure_time** | **int** |  | [optional] 
**time_interval** | **int** |  | [optional] 
**init_temperature** | **float** |  | [optional] 
**fire_temperature** | **float** |  | [optional] 
**temperature_increase** | **float** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.fire_temperature_calculation_data_idea_rs_connection_calculator import FireTemperatureCalculationDataIdeaRSConnectionCalculator

# TODO update the JSON string below
json = "{}"
# create an instance of FireTemperatureCalculationDataIdeaRSConnectionCalculator from a JSON string
fire_temperature_calculation_data_idea_rs_connection_calculator_instance = FireTemperatureCalculationDataIdeaRSConnectionCalculator.from_json(json)
# print the JSON string representation of the object
print(FireTemperatureCalculationDataIdeaRSConnectionCalculator.to_json())

# convert the object into a dict
fire_temperature_calculation_data_idea_rs_connection_calculator_dict = fire_temperature_calculation_data_idea_rs_connection_calculator_instance.to_dict()
# create an instance of FireTemperatureCalculationDataIdeaRSConnectionCalculator from a dict
fire_temperature_calculation_data_idea_rs_connection_calculator_from_dict = FireTemperatureCalculationDataIdeaRSConnectionCalculator.from_dict(fire_temperature_calculation_data_idea_rs_connection_calculator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


