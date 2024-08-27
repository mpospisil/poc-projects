# MemoryStream


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**can_read** | **bool** |  | [optional] [readonly] 
**can_seek** | **bool** |  | [optional] [readonly] 
**can_write** | **bool** |  | [optional] [readonly] 
**capacity** | **int** |  | [optional] 
**length** | **int** |  | [optional] [readonly] 
**position** | **int** |  | [optional] 
**can_timeout** | **bool** |  | [optional] [readonly] 
**read_timeout** | **int** |  | [optional] 
**write_timeout** | **int** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.memory_stream import MemoryStream

# TODO update the JSON string below
json = "{}"
# create an instance of MemoryStream from a JSON string
memory_stream_instance = MemoryStream.from_json(json)
# print the JSON string representation of the object
print(MemoryStream.to_json())

# convert the object into a dict
memory_stream_dict = memory_stream_instance.to_dict()
# create an instance of MemoryStream from a dict
memory_stream_from_dict = MemoryStream.from_dict(memory_stream_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


