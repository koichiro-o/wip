#### ContactShare

Represents a list of access levels to a Contact along with an explanation of the access level. For example, if you have access to a record
because you own it, the `ContactAccessLevel` is `All` and `RowCause` is Owner.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with access to the Contact object can access this object.

##### Fields

```
ContactId
ContactAccessLevel
IsDeleted

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Contact associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to cases associated with the account Contact. The
possible values are:

**•** `Read`

**•** `Edit`

**•** `All` This value is not valid for create or update.

This field must be set to an access level that is higher than the organization’s default access
level for contacts.

**Type**
boolean

**Properties**
Defaulted on create, Filter


-----

```
RowCause
UserOrGroupId

```

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule—The User or Group has access via a Contact sharing rule.`

**•** `GuestRule—The User or Group has access via a Contact guest user sharing rule.`

**•** `ImplicitChild—The User or Group has access to the Contact via sharing access on`
the associated Account. After faster account sharing recalculation is enabled for your org,
sharing entries with this value aren’t returned in queries. Instead of storing implicit child
shares, record access is determined dynamically.

**•** `ImplicitPerson—The User or Group has access to the business contact of a person`
account via access to the person account itself.

**•** `GuestPersonImplicit—The guest user has access to the business contact of a`
person account via a Contact sharing rule.

**•** `PortalImplicit—The Contact is associated with the portal user.`

**•** `LpuImplicit—The User has access to records owned by high-volume Experience`
Cloud site users via a share group.

**•** `ARImplicit—The User, who belongs to a partner or customer account, has access`
to the Contact via an account relationship data sharing rule.

**•** `Manual—The User or Group has access because a User with “All” access manually shared`
the Contact with them.

**•** `Owner—The User is the owner of the Contact.`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Contact. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup


-----

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Usage

This object allows you to determine which users and groups can view or edit Contact records owned by other users.

Note: After faster account sharing recalculation is enabled for your org, we no longer store implicit share records between accounts
and their child contact records. Sharing entries that have a value of `ImplicitChild` in the `RowCause` field aren’t returned
when you query this object. Instead, the system dynamically determines whether users can access child contact records when
they try to access them. This change speeds up ownership and sharing recalculation for accounts.

[For more information, see the Faster Account Sharing Recalculation knowledge article.](https://help.salesforce.com/s/articleView?id=000394638&type=1&language=en_US)

SEE ALSO:

AccountShare
