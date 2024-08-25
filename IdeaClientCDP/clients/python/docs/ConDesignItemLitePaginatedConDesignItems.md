# ConDesignItemLitePaginatedConDesignItems


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**design_items** | [**List[ConDesignItemLite]**](ConDesignItemLite.md) |  | [optional] 
**is_last_page** | **bool** |  | [optional] 
**page_size** | **int** |  | [optional] 
**total_items** | **int** |  | [optional] 

## Example

```python
from idea_cdp_client_poc.models.con_design_item_lite_paginated_con_design_items import ConDesignItemLitePaginatedConDesignItems

# TODO update the JSON string below
json = "{}"
# create an instance of ConDesignItemLitePaginatedConDesignItems from a JSON string
con_design_item_lite_paginated_con_design_items_instance = ConDesignItemLitePaginatedConDesignItems.from_json(json)
# print the JSON string representation of the object
print(ConDesignItemLitePaginatedConDesignItems.to_json())

# convert the object into a dict
con_design_item_lite_paginated_con_design_items_dict = con_design_item_lite_paginated_con_design_items_instance.to_dict()
# create an instance of ConDesignItemLitePaginatedConDesignItems from a dict
con_design_item_lite_paginated_con_design_items_from_dict = ConDesignItemLitePaginatedConDesignItems.from_dict(con_design_item_lite_paginated_con_design_items_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


