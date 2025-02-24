#### WorkOrderShare

Represents a sharing entry on a work order. This object is available in API version 36.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Work orders or Field Service must be enabled in your organization. External users can’t access this object.

##### Fields

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the work order. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn’t valid for create or update calls.)

Set to an access level that is at least equal to the organization’s default work order
access level.


-----

```
ParentId
RowCause
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The work order associated with the sharing entry.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
WorkOrder

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is Manual. If no value is specified, the field defaults to Manual.
All other RowCause values are read-only. After the sharing entry is created,
this field can’t be edited. Valid values include:

**•** `Manual—The User or Group has access because a user with “All” access`
manually shared the work order.

**•** `Owner—The User is the owner of the work order.`

**•** `Rule—The User or Group has access via a work order sharing rule.`

**•** `GuestRule—The User or Group has access via a work order guest user`
sharing rule.

**•** `LpuImplicit—The User has access to records owned by high-volume`
Experience Cloud site users via a share group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
(Read Only) ID of the user or group that has access to the work order.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup


-----

**Relationship Type**
Lookup

**Refers To**
Group, User
