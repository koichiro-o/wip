#### AdProductTargetCategory

An intersection table between Target Category and Product2. This object supports mapping the Target Category to all products, to a
specific Media Type, or to a specific Product. This object is available in API version 55.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
MediaType
ProductId
SegmentsDetails

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Media Type to which a particular Target Category is mapped.

Possible values are:

**•** `Digital`

**•** `TV`

**•** `Radio`

**•** `Print`

**•** `Outdoor`

**•** `Other`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key to Product record for mapping a particular category with it.

This is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
textarea

**Properties**
Create, Update


-----

```
TargetCategoryId

##### Associated Objects

```

**Description**
Stores the complete metadata for an entire category and all the segments associated with
it. Acts as the source of truth to represent a category across all products, media types, and
so on.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Foreign key to Target Category record for grouping the segments under it.

This is a relationship field.

**Relationship Name**
TargetCategory

**Relationship Type**
Lookup

**Refers To**
AdTargetCategory


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdProductTargetCategoryChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdProductTargetCategoryFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdProductTargetCategoryHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdProductTargetCategoryOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdProductTargetCategoryShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
