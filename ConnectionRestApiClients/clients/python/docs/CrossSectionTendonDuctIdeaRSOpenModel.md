# CrossSectionTendonDuctIdeaRSOpenModel


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**point** | [**Geometry2DPoint2DIdeaRSOpenModel**](Geometry2DPoint2DIdeaRSOpenModel.md) |  | [optional] 
**material_duct** | [**CrossSectionMaterialDuctIdeaRSOpenModel**](CrossSectionMaterialDuctIdeaRSOpenModel.md) |  | [optional] 
**is_debonding_tube** | **bool** |  | [optional] 
**diameter** | **float** |  | [optional] 

## Example

```python
from connection_restapi_client_poc.models.cross_section_tendon_duct_idea_rs_open_model import CrossSectionTendonDuctIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of CrossSectionTendonDuctIdeaRSOpenModel from a JSON string
cross_section_tendon_duct_idea_rs_open_model_instance = CrossSectionTendonDuctIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(CrossSectionTendonDuctIdeaRSOpenModel.to_json())

# convert the object into a dict
cross_section_tendon_duct_idea_rs_open_model_dict = cross_section_tendon_duct_idea_rs_open_model_instance.to_dict()
# create an instance of CrossSectionTendonDuctIdeaRSOpenModel from a dict
cross_section_tendon_duct_idea_rs_open_model_from_dict = CrossSectionTendonDuctIdeaRSOpenModel.from_dict(cross_section_tendon_duct_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


