#### ExtlRecShrPicklistMap

Represents the external record share picklist field mapping between the partner and vendor system for Partner Connect. This object is
available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)


-----

##### Fields

**Field**
```
ImportedPcklstOptionId
InternalPcklstOptionId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the external system.

This field is a relationship field.

**Relationship Name**
ImportedPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the external record share picklist option of the internal system.

This field is a relationship field.

**Relationship Name**
InternalPcklstOption

**Refers To**
ExtlRecShrPcklstOptn

