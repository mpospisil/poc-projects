# SystemIOMemoryStreamSystemPrivateCoreLib


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
from connection_restapi_client_poc.models.system_io_memory_stream_system_private_core_lib import SystemIOMemoryStreamSystemPrivateCoreLib

# TODO update the JSON string below
json = "{}"
# create an instance of SystemIOMemoryStreamSystemPrivateCoreLib from a JSON string
system_io_memory_stream_system_private_core_lib_instance = SystemIOMemoryStreamSystemPrivateCoreLib.from_json(json)
# print the JSON string representation of the object
print(SystemIOMemoryStreamSystemPrivateCoreLib.to_json())

# convert the object into a dict
system_io_memory_stream_system_private_core_lib_dict = system_io_memory_stream_system_private_core_lib_instance.to_dict()
# create an instance of SystemIOMemoryStreamSystemPrivateCoreLib from a dict
system_io_memory_stream_system_private_core_lib_from_dict = SystemIOMemoryStreamSystemPrivateCoreLib.from_dict(system_io_memory_stream_system_private_core_lib_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


