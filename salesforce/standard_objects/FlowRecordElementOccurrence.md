#### FlowRecordElementOccurrence

Represents the execution metrics for a single element within a flow version. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

 Fields

```
```
CurrencyIsoCode

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The ISO code for the currency associated with the flow.

Possible values are:

**•** `USD—U.S. Dollar`


-----

```
Entries
Errors
Exits
FlowRecordElementId
FlowRecordId

```

The default value is `USD.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was initiated in all flow interviews after the flow version
was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of errors for the element in all flow interviews after the flow version was executed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times the element was executed to completion in all flow interviews after
the flow version was executed.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow element.

This field is a relationship field.

**Relationship Name**
FlowRecordElement

**Refers To**
FlowRecordElement

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
FlowRecordVersionId
FlowRecordVersionOccurrenceId
Name

```

**Description**
The ID of the flow.

This field is a relationship field.

**Relationship Name**
FlowRecord

**Refers To**
FlowRecord

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the flow version.

This field is a relationship field.

**Relationship Name**
FlowRecordVersion

**Refers To**
FlowRecordVersion

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the flow occurrence.

This field is a relationship field.

**Relationship Name**
FlowRecordVersionOccurrence

**Relationship Type**
Master-detail

**Refers To**
FlowRecordVersionOccurrence (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The API name of the flow element.


-----

```
Stopped
TotalDuration

##### Associated Objects

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times execution of the element was stopped in all flow interviews after the
flow version was executed.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total time in milliseconds spent executing the element in all flow interviews.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**FlowRecordElementOccurrenceChangeEvent on page 67**
Change events are available for the object.

**FlowRecordElementOccurrenceFeed on page 54**
Feed tracking is available for the object.

**FlowRecordElementOccurrenceHistory on page 62**
History is available for tracked fields of the object.

**FlowRecordElementOccurrenceOwnerSharingRule on page 64**
Sharing rules are available for the object.

**FlowRecordElementOccurrenceShare on page 66**
Sharing is available for the object.
