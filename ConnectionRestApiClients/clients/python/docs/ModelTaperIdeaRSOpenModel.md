# ModelTaperIdeaRSOpenModel

Defines haunches (variyng cross-sections) along the member.    One IdeaRS.OpenModel.Model.Taper may be assigned to multiple <see cref=\"T:IdeaRS.OpenModel.Model.Member1D\">Members</see>.  Sections of the member not covered by a span will use the member's cross-section.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Element Id | [optional] 

## Example

```python
from connection_restapi_client_poc.models.model_taper_idea_rs_open_model import ModelTaperIdeaRSOpenModel

# TODO update the JSON string below
json = "{}"
# create an instance of ModelTaperIdeaRSOpenModel from a JSON string
model_taper_idea_rs_open_model_instance = ModelTaperIdeaRSOpenModel.from_json(json)
# print the JSON string representation of the object
print(ModelTaperIdeaRSOpenModel.to_json())

# convert the object into a dict
model_taper_idea_rs_open_model_dict = model_taper_idea_rs_open_model_instance.to_dict()
# create an instance of ModelTaperIdeaRSOpenModel from a dict
model_taper_idea_rs_open_model_from_dict = ModelTaperIdeaRSOpenModel.from_dict(model_taper_idea_rs_open_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


