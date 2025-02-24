#### ProductSellingModelOption

A junction object between Product Selling Model and Product2. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available when Subscription Management or Commerce Subscriptions is enabled. Some fields require Industries EPC to
be enabled.

##### Fields

```
Description
DisplayName
Increment
IsDefault
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the product selling model option.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model option to display to customers.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of pricing term units that can be used to increase a subscription term.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indcates the default product selling model for a product. Setting a default is optional. A
product can only have one default product selling model.

The default value is `false. This field requires Industries EPC.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Maximum
Minimum
Name
Product2Id

```

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view but not viewed it.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of pricing term units for a subscription term.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The minimum number of pricing term units for a subscription term.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the product selling model.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Product2 record associated with this ProductSellingModelOption record.

This is a relationship field.


-----

```
ProductSellingModelId
ProrationPolicyId

```

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the ProductSellingModel record associated with this ProductSellingModelOption
record.

This is a relationship field.

**Relationship Name**
ProductSellingModel

**Relationship Type**
Lookup

**Refers To**
ProductSellingModel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the ProrationPolicy record associated with this ProductSellingModelOption record.

This is a relationship field.

**Relationship Name**
ProrationPolicy

**Relationship Type**
Lookup

**Refers To**
ProrationPolicy

