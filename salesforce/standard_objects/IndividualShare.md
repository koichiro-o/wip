#### IndividualShare

Represents a list of access levels to a data privacy record along with an explanation of the access level. For example, if you have access
to a record because you own it, the `IndividualAccessLevel` is All and `RowCause` is Owner. This object is available in API
version 42.0 and later.

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
**•** This object is available if Data Protection and Privacy is enabled.

**•** The Individual object isn’t available to Customer Community, Partner Community, and Customer Portal users.


-----

##### Fields

**Field Name**
```
IndividualAccessLevel
IndividualId
RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the user or group has to the data privacy record. The possible
values include:

**•** `Read`

**•** `Edit`

**•** `All` (Except for create or update.)

Set this field to an access level that’s higher than your default access level for
individuals.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Individual associated with this sharing entry. This field isn’t available for
updates.

This is a relationship field.

**Relationship Name**
Individual

**Relationship Type**
Lookup

**Refers To**
Individual

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
manually shared the data privacy record with them.


-----

```
UserOrGroupId

##### Usage

```


**•** `Owner—The User is the owner of the data privacy record.`

**•** `Rule—The User or Group has access to the data privacy record via an`
Individual sharing rule.

**•** `LpuImplicit—The User has access to records owned by high-volume`
Experience Cloud site users via a share group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the data privacy record.
This field isn’t available for updates.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


This object lets you determine which users and groups can view or edit Individual records owned by other users.
