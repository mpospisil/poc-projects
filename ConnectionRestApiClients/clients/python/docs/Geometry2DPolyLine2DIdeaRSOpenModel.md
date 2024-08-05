# Geometry2DPolyLine2DIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**start_point** | [**Geometry2DPoint2DIdeaRSOpenModel**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**segments** | [**List[Geometry2DSegment2DIdeaRSOpenModel]**](Geometry2DSegment2DIdeaRSOpenModel.md) |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.geometry2_d_poly_line2_d_idea_rs_open_model import Geometry2DPolyLine2DIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of Geometry2DPolyLine2DIdeaRSOpenModel from a JSON string
geometry2_d_poly_line2_d_idea_rs_open_model_instance = Geometry2DPolyLine2DIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(Geometry2DPolyLine2DIdeaRSOpenModel.to_json())

# convert the object into a dict
geometry2_d_poly_line2_d_idea_rs_open_model_dict = geometry2_d_poly_line2_d_idea_rs_open_model_instance.to_dict()
# create an instance of Geometry2DPolyLine2DIdeaRSOpenModel from a dict
geometry2_d_poly_line2_d_idea_rs_open_model_from_dict = Geometry2DPolyLine2DIdeaRSOpenModel.from_dict(geometry2_d_poly_line2_d_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


