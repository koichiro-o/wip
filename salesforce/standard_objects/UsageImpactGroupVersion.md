#### UsageImpactGroupVersion

Represents a collection of fields to set up the versions of Usage Impact Groups. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available only with EAndU Cloud Usage Impact Access permission set.

##### Fields

```
ApprovedMeasureExtlid
Description
EndDate
IsActive
Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The approved Measure Category ID assigned by a regulator.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group Version.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version ends.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group Version is active.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Version.


-----

```
StartDate
TechResourceManualCode
UsageImpactGroupId
Version

##### Associated Objects

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the validity of Usage Impact Group Version begins.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The code and version of the Technical Reference Manual which is the source for the values
associated with this Usage Impact Group Version. This is necessary for regulatory reporting.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group object associated with the Usage Impact Group Version.

This field is a relationship field.

**Relationship Name**
UsageImpactGroup

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroup

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the Usage Impact Group Version.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**[UsageImpactGroupVersionChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupVersionFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupVersionHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupVersionOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupVersionShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
