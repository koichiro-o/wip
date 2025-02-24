#### PaymentScheduleTreatmentDtl

Contains configuration information for the payment schedule treatment detail. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management.


-----

##### Fields

**Field**
```
DateOffset
Description
InstallmentPaymentType
LastReferencedDate
LastViewedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
A number equal to or less than 0. The date offset is subtracted from the processing date
reference to determine the processing date.

For example, suppose that the invoice due date is 01/17/2022 and offset is -7. In this case,
the payment schedule item is processed by the jobs that run on or before 01/10/2022.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The user-entered description of the payment schedule treatment detail.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the payment amount is divided into multiple payments.

Possible values are:

**•** `Percentage`

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


-----

```
PaymentMethodSelectionType
PaymentRunMatchingValue
PaymentScheduleTreatmentDetailNumber
PaymentScheduleTreatmentId

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the payment method is specified.

Possible values are:

**•** `Manual—the payment method is entered by a user`

**•** `MostRecentAutopay—the payment method is the most recent automatic payment`
method used

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Possible values are:

**•** `AMER`

**•** `APAC`

**•** `EMEA`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
System-generated unique identifier for this payment schedule treatment detail.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the related payment schedule treatment.

This field is a relationship field.


-----

```
Percentage
ProcessingDateReference
PymtSchdDistributionMethodId

```

**Relationship Name**
PaymentScheduleTreatment

**Relationship Type**
Lookup

**Refers To**
PaymentScheduleTreatment

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the percentage of the source amount that is used to create the payment schedule.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the source of the reference date.

Possible values are:

**•** `InvoiceDueDate—use the invoice’s due date as the date reference`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distribution method that contains the information on how to create the payment schedule
items.

This field is a relationship field.

**Relationship Name**
PymtSchdDistributionMethod

**Relationship Type**
Lookup

**Refers To**
PymtSchdDistributionMethod


-----
