# Geometry2DRegion2DIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**outline** | [**Geometry2DPolyLine2DIdeaRSOpenModel**](Geometry2DPolyLine2DIdeaRSOpenModel.md) |  | [optional] 
**openings** | [**List[Geometry2DPolyLine2DIdeaRSOpenModel]**](Geometry2DPolyLine2DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.geometry2_d_region2_d_idea_rs_open_model import Geometry2DRegion2DIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry2DRegion2DIdeaRSOpenModel from a JSON string
geometry2_d_region2_d_idea_rs_open_model_instance = Geometry2DRegion2DIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(Geometry2DRegion2DIdeaRSOpenModel.to_json())

# convert the object into a dict
geometry2_d_region2_d_idea_rs_open_model_dict = geometry2_d_region2_d_idea_rs_open_model_instance.to_dict()
# create an instance of Geometry2DRegion2DIdeaRSOpenModel from a dict
geometry2_d_region2_d_idea_rs_open_model_from_dict = Geometry2DRegion2DIdeaRSOpenModel.from_dict(geometry2_d_region2_d_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


