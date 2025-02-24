#### WorkGoalShare

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the source WorkGoal object

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the target WorkGoal object


Represents a sharing entry on a WorkGoal object. This object has been deprecated as of API version 35.0. Use the GoalShare object to
query information about sharing for WDC goals.

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
The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The user’s or group’s level of access to the goal. The possible values are:

**•** Read


-----

```
ParentId
RowCause
UserOrGroupId

```


**•** Edit

**•** All: This value is not valid when you create, update, or delete records

This field must be set to an access level that is higher than the organization’s
default access level for goals.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the WorkGoal object that is associated with this sharing entry.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only
permitted value is Manual. If no value is specified, the field defaults to Manual.
All other RowCause values are read-only. After the sharing entry is created,
this field can’t be edited.

Valid values include:

**•** `Owner—The User is the owner of the WorkGoal or is in a user role above`
the WorkGoal owner in the role hierarchy.

**•** `Manual—The User or Group has access, because a user with “All” access`
manually shared the WorkGoal with the user or group.

**•** `Rule—The User or Group has access via a WorkGoal sharing rule.`

**•** `GuestRule—The User or Group has access via a WorkGoal guest user`
sharing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the user or group that was given access to the goal. This field can’t be
updated.


-----
