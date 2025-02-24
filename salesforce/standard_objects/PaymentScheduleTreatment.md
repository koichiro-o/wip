#### PaymentScheduleTreatment

Contains configuration information for the payment schedule. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management.

##### Fields

```
Description
LastReferencedDate
LastViewedDate
Name

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user-entered description of the payment schedule treatment.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string


-----

```
OwnerId
PaymentSchedulePolicyId
Status

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-entered name of the payment schedule treatment.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related payment schedule policy.

This field is a relationship field.

**Relationship Name**
PaymentSchedulePolicy

**Relationship Type**
Lookup

**Refers To**
PaymentSchedulePolicy

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The payment schedule treatment’s status.

Possible values are:


-----

```
TriggerSource

```


**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the action that caused the payment schedule treatment to be created.

Possible values are:

**•** `InvoicePosted—an invoice is posted`

