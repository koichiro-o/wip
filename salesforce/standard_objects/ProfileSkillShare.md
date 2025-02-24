#### ProfileSkillShare

Represents a sharing entry on a ProfileSkill.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

```
AccessLevel
ParentId
RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the ProfileSkill. The possible values
are:

**•** `Read`

**•** `Edit`

**•** `All` (This value is not valid for `create()` or `update()` calls.)

This value must be set to an access level that is higher than the organization’s
default access level for ProfileSkill objects.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent object, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
ProfileSkill

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
UserOrGroupId

##### Usage

```

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is Manual. If no value is specified, the field defaults to Manual.
All other `RowCause` values are read-only. After the sharing entry is created,
this field can’t be edited.

Values may include:

**•** `Manual—The User or Group has access because a user with “All” access`
manually shared the ProfileSkill with them.

**•** `Owner—The User is the owner of the ProfileSkill or is in a role above the`
ProfileSkill owner in the role hierarchy.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the ProfileSkill.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


This object is read only. It is visible because of constraints to the ProfileSkill object, but it is ignored and does not control which users
and groups can view and edit ProfileSkill records owned by other users.
