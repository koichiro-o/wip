#### RecordsetFltrCritMonitor

Monitors whether the value of an asset attribute is within the threshold of a recordset filter criteria (RFC). You can monitor one or more
RFCs for an Asset. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Description
IsWithinThreshold
Name
LastReferencedDate
LastViewedDate

```

**Description**
The ID of the asset to link the RFC to.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the RFC associated with the recordset filter criteria monitor.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the value of the asset attribute is within the threshold of the RFC.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recordset filter criteria monitor.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last referenced.

**Type**
dateTime


-----

```
RecordsetFilterCriteriaId

##### Associated Objects

```

**Properties**
Filter, Nillable, Sort

**Description**
The date the value was last viewed.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the recordset filter criteria.

This field is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RecordsetFltrCritMonitorChangeEvent on page 67**
Change events are available for the object.

**RecordsetFltrCritMonitorHistory on page 62**
History is available for tracked fields of the object.

SEE ALSO:

AssetAttribute

AttributeDefinition

AttributePicklist

AttributePicklistValue
