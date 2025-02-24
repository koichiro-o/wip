#### AdTargetCategory

Represents an individual Targeting Category, which is used to group multiple targeting segments. This is mapped with Ad Server
categories, containing the segments. For example, Audience Targeting and Geo targeting. This object is available in API version 55.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Code
Description

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Represents the Code on the Category record, which is mapped to the Ad Server's Code for
the same record. Each Category record is represented as a separate node when the payload
is sent to the Ad Server.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
DisplaySequence
IsActive
IsAvailableForSelfService
MediaType

```

**Description**
Represents the descriptions for a category record. The data for this field can be imported
and mapped from the Ad Server.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sequence of multiple records configured for a particular product or media type.
The sequence is determined by the number of records configured.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a Category record is published. If not activated, the category is not available
for run-time configuration.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a category is available in the Agent Console and the Self Service Console.
By default, all categories are available in the Agent Console.

If the value of this field is set to `true, then the category is available in the Self Service`
Console.

The default value is 'false'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Media Type against which a particular Target Category is mapped.

Possible values are:

**•** `Digital`

**•** `TV`


-----

```
Name
ParentAdTargetCategoryId
ProductId

```


**•** `Radio`

**•** `Print`

**•** `Outdoor`

**•** `Other`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Represents the category name or label shown to the user.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A self-referencing foreign key, which defines subcategories.

This is a relationship field.

**Relationship Name**
ParentAdTargetCategory

**Relationship Type**
Lookup

**Refers To**
AdTargetCategory

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


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdTargetCategoryChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdTargetCategoryFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdTargetCategoryHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdTargetCategoryOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdTargetCategoryShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
