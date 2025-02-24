#### ExtlRecShrOpportunity

Represents the opportunity for Partner Connect in the vendor org if you’re a partner and the partner org if you’re the vendor. This object
is available in API version 62.0 and later.

The label of this object in the related list is Connected External Leads.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

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
Name
OpportunityId

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
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
ID of the associated opportunity.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Master-detail

**Refers To**
Opportunity (the master object)
