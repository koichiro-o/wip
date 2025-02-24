#### ExtlRecShrFieldMap

```

**Description**
Maximum length of the field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Field type of the imported, exported, or updated field.

Possible values are:

**•** `Address`

**•** `AddressCountry`

**•** `AddressState`

**•** `Boolean`

**•** `Currency`

**•** `DateOnly`

**•** `DateTime`

**•** `Double`

**•** `DynamicEnum`

**•** `Email`

**•** `EnumOrId`

**•** `Fax`

**•** `Integer`

**•** `MultiLineText`

**•** `Percent`

**•** `Phone`

**•** `StaticEnum`

**•** `Text`

**•** `Url`


Represents the external record share field mapping between the sender and receiver for Partner Connect. This object is available in API
version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
ImportedFieldId
InternalFieldId
