#### UsageImpactGroupFactor

Represents a junction between an Usage Impact Group version and Usage Impact Factor. This object is available in API version 58.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with EAndU Cloud Usage Impact Access permission set.

##### Fields

```
FactorValue
IsActive

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Defines the value of the Usage Impact Group Factor.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
Name
UnitOfMeasureId
UsageImpactFactorId
UsageImpactGroupVersionId

```

**Description**
Indicates whether the Usage Impact Group Factor is active.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Group Factor.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The UnitOfMeasure object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UnitOfMeasure

**Relationship Type**
Lookup

**Refers To**
UnitOfMeasure

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Factor object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactFactor

**Relationship Type**
Lookup

**Refers To**
UsageImpactFactor

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Usage Impact Group Version object associated with the Usage Impact Group Factor.

This field is a relationship field.

**Relationship Name**
UsageImpactGroupVersion

**Relationship Type**
Lookup

**Refers To**
UsageImpactGroupVersion

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactGroupFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactGroupFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactGroupFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactGroupFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactGroupFactorShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
