#### ExtlRecShrLead

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrField record containing the field data sent from the external system.

This field is a relationship field.

**Relationship Name**
ImportedField

**Refers To**
ExtlRecShrField

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrField record containing the field data received on the internal system.

This field is a relationship field.

**Relationship Name**
InternalField

**Refers To**
ExtlRecShrField


Represents the Lead record of a vendor org if you’re a partner. If you’re a vendor for Partner Connect, this object represents a partner
org. This object is available in API version 62.0 and later.

In a related list, the label of this object is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
ExtlRecShrCnctId
LeadId
Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the partner lead.

This field is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Master-detail

**Refers To**
Lead (the master object)

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

**Description**
For internal use only.
