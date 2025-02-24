#### ExtlRecShrField

Represents an imported, exported, or updated external record share field for Partner Connect. This object is available in API version 62.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
ExtlRecShrObjectId
FieldDefaultValue
FieldSetType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ExtlRecShrObject record.

This field is a relationship field.

**Relationship Name**
ExtlRecShrObject

**Refers To**
ExtlRecShrObject

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Default value of the field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Set of fields associated with this record.


-----

```
IsFieldNillable
SendFieldUpdates
SharedFieldDevName
SharedFieldLabel
SharedFieldLength

```

Possible values are:

**•** `ExportedFields`

**•** `ImportedFields`

**•** `InternalFields`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this field can be set to null (true) or not (false).

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether updates are tracked for this field, sent to the connected org, and stored
in the ExtlRecShrLead or ExlRecShrOpportunity objects (true) or not (false).

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Developer name of the field.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Label of the field.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SharedFieldType
