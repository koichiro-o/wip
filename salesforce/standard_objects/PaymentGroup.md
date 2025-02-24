#### PaymentGroup

```

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
User-friendly name of the payment gateway provider.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Namespace for the payment gateway platform.


Top-level object that groups all payment transactions that are processed for an order or invoice. PaymentGroup is a standalone object,
so it isn’t required for users to execute payment transactions (authorizations, captures, refunds, and sales). This object is available in API
version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access Commerce Payments entities, your org must have a Salesforce Order Management license with the Payment Platform org
permission activated. Commerce Payments entities are available only in Lightning Experience.

##### Fields

```
PaymentGroupNumber

```

**Type**
string


-----

```
SourceObjectId

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-defined unique ID for the payment group.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order or invoice related to all the payment transactions in the payment group.

This is a relationship field.

**Relationship Name**
SourceObject

**Relationship Type**
Lookup

**Refers To**
Order

