#### CallCtrAgentFavTrfrDestShare

Represents a sharing entry on a favorite transfer destination in the Omni-Channel softphone for voice call transfers. This object is available
in API version 55.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
AccessLevel

```

**Type**
picklist


-----

```
ParentId
RowCause

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The level of access the User or Group has to the transfer destination that’s marked as a favorite.
Possible values are:

**•** `All` — Owner

**•** `Edit` — Read/Write

**•** `Read` — Read Only

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent object.

This field is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CallCtrAgentFavTrfrDest

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantDataSharing — Compliant Data Sharing`

**•** `GuestParentImplicit — Associated guest user sharing`

**•** `GuestPersonImplicit — Associated Guest User Sharing`

**•** `GuestRule` — Guest User Sharing Rule

**•** `ImplicitChild` — Account Sharing

**•** `ImplicitParent` — Associated record owner or sharing

**•** `ImplicitPerson` — Person Contact

**•** `LearningAssignment — Learning Assignment Share`


-----

```
UserOrGroupId
