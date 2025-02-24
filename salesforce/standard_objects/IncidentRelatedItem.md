#### IncidentRelatedItem

Represents a junction object that relates an Incident to an Asset or Product. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Asset ID that's linked to the Incident.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


-----

```
Comment
ImpactLevel
ImpactType
IncidentId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the incident as it relates to the item.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The related item’s impact on the incident.

Possible values are:

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `High.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The effect of the related item on business operations.

Possible values are:

**•** `Business-Blocking`

**•** `Not Business-Blocking`

**•** `Partially Business-Blocking`

The default value is `Business-Blocking.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The Incident ID that's linked to the Asset.

This field is a relationship field.


-----

```
Name
Product2Id

##### Associated Objects

```

**Relationship Name**
Incident

**Relationship Type**
Lookup

**Refers To**
Incident

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated ID of the incident-related item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The product (Product2) ID that's linked to the Incident..

This field is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IncidentRelatedItemChangeEvent on page 67**
Change events are available for the object.

**IncidentRelatedItemFeed on page 54**
Feed tracking is available for the object.

**IncidentRelatedItemHistory on page 62**
History is available for tracked fields of the object.


-----
