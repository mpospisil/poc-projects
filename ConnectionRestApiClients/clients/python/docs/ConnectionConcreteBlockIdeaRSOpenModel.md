# ConnectionConcreteBlockIdeaRSOpenModel

Data of concrete block

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lenght** | **float** | Lenght of ConcreteBlock | [optional] 
**width** | **float** | Width of ConcreteBlock | [optional] 
**height** | **float** | Height of ConcreteBlock | [optional] 
**material** | **str** | Material of ConcreteBlock | [optional] 

## Example

```python
from connection_restapi_client_poc.models.connection_concrete_block_idea_rs_open_model import ConnectionConcreteBlockIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionConcreteBlockIdeaRSOpenModel from a JSON string
connection_concrete_block_idea_rs_open_model_instance = ConnectionConcreteBlockIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ConnectionConcreteBlockIdeaRSOpenModel.to_json())

# convert the object into a dict
connection_concrete_block_idea_rs_open_model_dict = connection_concrete_block_idea_rs_open_model_instance.to_dict()
# create an instance of ConnectionConcreteBlockIdeaRSOpenModel from a dict
connection_concrete_block_idea_rs_open_model_from_dict = ConnectionConcreteBlockIdeaRSOpenModel.from_dict(connection_concrete_block_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


