#### PaymentTermItem

Defines the attributes of a payment term that your company uses. The PaymentTermItem is used to determine the due date on invoices.
This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
User-defined field that describes the details of the payment term item.

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
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string


-----

```
PaymentTermId
PaymentTimeframe
Period
PeriodUnit

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated sequential number, such as PTI-000001.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the payment term that this payment term item is associated with.

This field is a relationship field.

**Relationship Name**
PaymentTerm

**Relationship Type**
Lookup

**Refers To**
PaymentTerm

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the time period when the payment is expected.

Possible values are:

**•** `Standard—Indicates that payment is expected by the date specified in the payment`
term. If payment isn't received by the due date, the payment becomes overdue.

The default value is `Standard.`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the number of units in the payment period. Used with the `PeriodUnit` field.

For example, to define a payment term of Net 30, enter `30` as the `Period` and select
`Days` as the `PeriodUnit.`

**Type**
picklist


-----

```
Type
