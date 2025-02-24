#### UsageImpactGroupPgmMeasure

Represents a junction between the program, product, and Usage Impact Group version. This object is available in API version 58.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with EAndU Cloud Usage Impact Access permission set.


-----

##### Fields

**Field**
```
Description
Name
Product2Id
ProgramId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Program Measure.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Program Measure.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Product2 object associated with the Usage Impact Group Program Measure.

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Program object associated with the Usage Impact Group Program Measure.

This field is a relationship field.

**Relationship Name**
Program

**Relationship Type**
Lookup


-----

```
UsageImpactGroupVersionId

##### Associated Objects

```

**Refers To**
Program

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version associated with the Energy Saving Group Association.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroupVersion


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupPgmMeasureChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupPgmMeasureFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupPgmMeasureHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupPgmMeasureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupPgmMeasureShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
