#### ExtlRecShrObject

Represents a shared object for Partner Connect. This object is available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
DefaultRecordOwnerId
ExtlObjectType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the shared record owner. The owner can be a user or a queue, represented by a Group
ID.

This field is a polymorphic relationship field.

**Relationship Name**
DefaultRecordOwner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Object type in the external org or system that is part of the object field mapping.

Possible values are:


-----

```
ExtlRecShrCnctId
FieldMapStatus
InternalObjectType

```


**•** `ExtlRecShrLead`

**•** `ExtlRecShrOpportunity`

**•** `Lead`

**•** `Opportunity`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Exporter’s status of the field mapping.

Possible values are:

**•** `ActiveMapping`

**•** `Selected`

**•** `SystemOverride`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object type in your org or system used to group field selections and field mappings.

Possible values are:

**•** `ExtlRecShrLead`

**•** `ExtlRecShrOpportunity`

**•** `Lead`

**•** `Opportunity`


-----
