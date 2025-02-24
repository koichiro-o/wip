#### UsageImpactGroup

Represents a collection of fields to set up the Usage Impact Groups used across jurisdictions and programs. This object is available in
API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with the EAndU Cloud Usage Impact Access permission set.

##### Fields

```
Description

```

**Type**
string


-----

```
IsActive
Name
ShortForm
Type

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the Usage Impact Group.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Group is active.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Group.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Group.

Possible values are:

**•** `ForwardMarkets—Forward Markets`

**•** `Planning`

**•** `Production`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
