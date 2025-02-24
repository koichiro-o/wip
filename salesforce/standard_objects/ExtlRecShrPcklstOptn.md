#### ExtlRecShrPcklstOptn

Represents a picklist option of an external record share picklist field shared between a partner and vendor for Partner Connect. This
object is available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
ExtlRecShrFieldId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the associated external record share field of type picklist.

This field is a relationship field.

**Relationship Name**
ExtlRecShrField


-----

```
IsDefaultOption
SharedOptionLabel
SharedOptionValue

```

**Refers To**
ExtlRecShrField

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this picklist option is set as the default option (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label of the picklist option.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Value of the picklist option.

