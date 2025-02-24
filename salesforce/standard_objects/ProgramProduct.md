#### ProgramProduct

Represents a junction between Program and Product2. This will hold Product2 values related to a Program. This object is available in
API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with the EAndU Cloud Program Access permission set.

##### Fields

```
Name
ProductId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ProgramProduct object.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Program.

This field is a relationship field.


-----

```
ProgramId
Status

##### Associated Objects

```

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Program parent object associated with the record.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup

**Refers To**
Program

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of the ProgramProduct object.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `Pending For Approval`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[ProgramProductChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[ProgramProductFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.


-----

**[ProgramProductHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[ProgramProductOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[ProgramProductShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
