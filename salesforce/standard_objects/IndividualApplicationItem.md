#### IndividualApplicationItem

Captures individual application input data that is used during run-time. This object is available in API version 58.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with the EAndU Cloud Program Access permission set.

##### Fields

```
IndividualApplicationId
Name
RelatedItemId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Individual Application parent object associated with the Individual Application Item.

This field is a relationship field.

**Relationship Name**
IndividualApplication

**Relationship Type**
Lookup

**Refers To**
IndividualApplication

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the object related to the Individual Application.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The related object associated with the Individual Application Item.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedItem


-----

```
Status

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
Benefit, ProgramProduct

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the approval status of the Individual Application.

Possible values are:

**•** `Approved`

**•** `Declined`

**•** `In Progress`

**•** `Pending`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[IndividualApplicationItemChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[IndividualApplicationItemFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[IndividualApplicationItemHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[IndividualApplicationItemOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[IndividualApplicationItemShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
