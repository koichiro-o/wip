#### PaymentSchedulePolicy

Contains configuration information for the payment schedule policy. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available with Subscription Management and the PaymentScheduleAutomation permission.

##### Fields

```
DefaultTreatmentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The default payment schedule treatment.

This field is a relationship field.


-----

```
Description
IsOrgDefault
LastReferencedDate
LastViewedDate
Name

```

**Relationship Name**
DefaultTreatment

**Relationship Type**
Lookup

**Refers To**
PaymentScheduleTreatment

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
User-entered description of the payment schedule policy.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
`true` if the payment schedule policy is the default policy for the org, otherwise `false.`
An org can have a maximum of one default payment policy.

The default value is `false.`

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
Status
TreatmentSelection

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The user-entered name of the payment policy.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the creator of this object.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The payment schedule policy’s status.

Possible values are:

**•** `Active`

**•** `Canceled`

**•** `Draft`

**•** `Inactive`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the payment schedule treatment.

Possible values are:

**•** `Default—use the payment schedule treatment indicated by`
```
   DefaultTreatmentId.

```

-----
