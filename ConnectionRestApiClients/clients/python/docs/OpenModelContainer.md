# OpenModelContainer

OpenModelContainer is used to keep structural data and results of a finite element analysis in one place.  The main reason is easier moving (passing) pass the instance of OpenModel and corresponding instace of OpenModelResults.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**open_model** | [**OpenModel**](OpenModel.md) |  | [optional] 
**open_model_result** | [**OpenModelResult**](OpenModelResult.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.open_model_container import OpenModelContainer

# TODO update the JSON string below
json = "{}"
# create an instance of OpenModelContainer from a JSON string
open_model_container_instance = OpenModelContainer.from_json(json)
# print the JSON string representation of the object
print(OpenModelContainer.to_json())

# convert the object into a dict
open_model_container_dict = open_model_container_instance.to_dict()
# create an instance of OpenModelContainer from a dict
open_model_container_from_dict = OpenModelContainer.from_dict(open_model_container_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


