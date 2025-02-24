#### ExtlRecShrCnctAccnt

Represents an association between an account and an external record share connection for Partner Connect. This object is available in
API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
AccountId
ExtlRecShrCnctId
Name

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the account.

This field is a relationship field.

**Relationship Name**
Account

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the ExtlRecShrCnct record.

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


-----
