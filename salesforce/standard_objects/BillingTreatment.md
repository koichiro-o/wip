#### BillingTreatment

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The earliest start date from all billing schedules in the billing schedule group.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that has been invoiced for all billing schedules within the billing schedule group.

This field is a calculated field.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount that hasn't yet been invoiced for all billing schedules within the billing schedule
group.

This field is a calculated field.


Defines how Subscription Management bills an order item. The Exclude From Billing field controls whether the order item is invoiced.
Child billing treatment items control how much of the order item's balance is invoiced for each invoice across the subscription's lifecycle.
Billing treatments are assigned to order items based on the parent billing policy's Billing Treatment Selection field. This object is available
in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
BillingPolicyId

```

**Type**
reference


-----

```
Description
ExcludeFromBilling
LastReferencedDate
LastViewedDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the billing policy for the billing treatment.

This field is a relationship field.

**Relationship Name**
BillingPolicy

**Relationship Type**
Lookup

**Refers To**
BillingPolicy

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Optional user-defined description of the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Excludes any order items assigned to the treatment from creating billing schedules.

Possible values are:

**•** `No`

**•** `Yes`

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
LegalEntityId
Name
Status

```

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the legal entity used to assign the treatment to order items when the parent billing
policy's `BillingTreatmentSelection` is `LegalEntity.`

This field is a relationship field.

**Relationship Name**
LegalEntity

**Relationship Type**
Lookup

**Refers To**
LegalEntity

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Optional user-defined name for the billing treatment.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Draft or inactive billing treatments can't be assigned to order items.

Possible values are:

**•** `Active`

**•** `Draft`

**•** `Inactive`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BillingTreatmentHistory (API version 55.0)**
History is available for tracked fields of the object.
