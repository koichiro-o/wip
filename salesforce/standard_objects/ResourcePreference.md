#### ResourcePreference

Represents an account’s preference for a specified service resource on field service work.

Resource preferences indicate which service resources can be assigned to field service work. You can designate service resources as
preferred, required, or excluded on specific accounts, assets, locations, work orders, or work order line items. Work orders inherit their
associated account’s resource preferences.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Special Access Rules

Field Service must be enabled.

##### Fields

**Field Name**
```
LastReferencedDate
LastViewedDate
PreferenceType
RelatedRecordId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource preference was last modified.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the resource preference was last viewed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Resource preference type. Values include:

**•** Preferred: Indicates that the customer would like their field service work
assigned to the resource.

**•** Required: Indicates that the resource must be assigned to the customer’s
field service work.

**•** Excluded: Indicates that the customer doesn’t want their field service work
assigned to the resource.

Resource preferences serve more as a suggestion than a requirement. You can
still assign a service appointment to any resource regardless of the related work
order’s resource preferences.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The work order or account with the resource preference.


-----

```
ResourcePreferenceNumber
ServiceResourceId

##### Associated Objects

```

This field is a polymorphic relationship.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Accounts, Assets, Locations, Work Orders, or Work Order Line Items

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the resource preference.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The service resource that is preferred, required, or excluded.

This is a relationship field.

**Relationship Name**
ServiceResource

**Relationship Type**
Lookup

**Refers To**
ServiceResource


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**ResourcePreferenceChangeEvent (API version 54.0)**
Change events are available for the object.

**ResourcePreferenceFeed**

Feed tracking is available for the object.

**ResourcePreferenceHistory**

History is available for tracked fields of the object.


-----
