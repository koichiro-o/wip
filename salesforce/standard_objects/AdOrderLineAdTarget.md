#### AdOrderLineAdTarget

Represents the selections made by the user against a specific Ad Order Line item for a particular category. This object is available in API
version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdOrderItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the ad order item related to the selected values.

This is a relationship field.

**Relationship Name**
AdOrderItem

**Relationship Type**
Lookup

**Refers To**
AdOrderItem


-----

```
AdProductTargetCategoryId
ConditionRequirements
CustomConditionLogic
LastReferencedDate

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the ad product target category object related to the selected values.

This is a relationship field.

**Relationship Name**
AdProductTargetCategory

**Relationship Type**
Lookup

**Refers To**
AdProductTargetCategory

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The criteria that decides the selected values are eligible for an ad order line.

Possible values are:

**•** `All Conditions Are Met (AND)`

**•** `Any Condition Is Met (OR)`

**•** `Custom Condition Is Met`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The custom logic that decides when the selected values are eligible for an ad order line.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.


-----

```
LastViewedDate
Name
OwnerId
SelectedValues

##### Associated Objects

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDateis not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the ad order line ad target.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the ad quote line ad target.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Stores all the selected values for all the segments available under a particular category, in
context of a specific Ad Order Line record.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdOrderLineAdTargetChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.


-----

**[AdOrderLineAdTargetFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdOrderLineAdTargetHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdOrderLineAdTargetOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdOrderLineAdTargetShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
