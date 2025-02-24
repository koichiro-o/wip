#### AccountShare

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A way to further filter what data gets shared. This must be a deterministic formula and
spanning is not allowed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Must match the type of an account relationship for data to be shared according to the
`AccountToCriteriaField` and the `StaticForumulaCriteria.`


Represents a sharing entry on an account.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.


-----

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Summer ’20 and later, only users with access to the Account object can access this object. Customer Portal users can't access this
object.

##### Fields

The properties available for some fields depend on the default org-wide sharing settings. The properties listed are true for the default
settings of such fields.

```
AccountAccessLevel
AccountId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to the Account. The possible values are:

**•** `Read`

**•** `Edit`

**•** `All` (This value isn't valid for create or update calls.)

This field must be set to an access level that is at least equal to the organization’s default
Account access level. In addition, either this field, the `OpportunityAccessLevel`
field, or the CaseAccessLevel field must be set higher than the organization’s default
access level.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Account


-----

```
CaseAccessLevel
ContactAccessLevel
OpportunityAccessLevel

```

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Level of access that the User or Group has to cases associated with the account. The possible
values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
```
  CaseAccessLevel. This field can't be updated via the API if the
  AccountAccessLevel field is set to All. You can't update this field for the associated

```
account owner via the API. You must update the account owner’s `CaseAccessLevel`
via the Salesforce user interface.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Level of access that the User or Group has to contacts associated with the account. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
```
  ContactAccessLevel. This field can't be updated via the API if the

```
`ContactAccessLevel` field is set to “Controlled by Parent.” You can't update this field
for the associated account owner using the API. You must update the account owner’s
`ContactAccessLevel` via the Salesforce user interface.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update


-----

```
RowCause

```

**Description**
Level of access that the User or Group has to opportunities associated with the Account. The
possible values are:

**•** `None`

**•** `Read`

**•** `Edit`

This field must be set to an access level that is at least equal to the organization’s default
opportunity access level. This field can’t be updated via the API if the
`AccountAccessLevel` field is set to `All. You can't use the API to update this field`
for the associated Account owner. You must update the Account owner’s
opportunityAccessLevel via the Salesforce user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

Valid values include:

**•** `Manual—The User or Group has access because a User with “All” access manually`
shared the Account with the user or group.

**•** `Owner—The User is the owner of the Account`

**•** `Team—The User or Group has team access (is an AccountTeamMember).`

**•** `Rule—The User or Group has access via an Account sharing rule.`

**•** `GuestRule—The user or group has access via an Account guest user sharing rule.`

**•** `ImplicitParent—The User or Group has access because they’re the owner of or`
have sharing access to records related to the account, such as opportunities, cases,
contacts, contracts, or orders.

**•** `GuestParentImplicit—The guest user has access because they have access to`
records related to the Account, such as opportunities, cases, contacts, contracts, or orders.

**•** `LpuParentImplicit—The User has access because they have access to records`
related to the Account, which are owned by high-volume Experience Cloud site users
and shared via a share group.

**•** `LpuImplicit—The User has access to records owned by high-volume Experience`
Cloud site users via a share group.

**•** `PortalImplicit—The Account is associated with the portal user.`

**•** `ARImplicit—The User, who belongs to a partner or customer account, has access`
to the Account via an account relationship data sharing rule.


-----

```
UserOrGroupId

##### Usage

```


**•** `Territory2AssociationManual—With Sales Territories in API version 44.0`
and earlier, the TerritoryManual reason code was written to AccountShare records
when you manually assigned an account to a territory. In API version 45.0 and later,
`Territory2AssociationManual` replaces all instances of
`TerritoryManual, and the` `Territory2AssociationManual` reason
code is written to AccountShare records when you manually assign an account to a
territory.

**•** `Territory—The territory has access via a territory assignment rule.`

**•** `TerritoryManual—Deprecated starting in API version 45.0 and replaced by the`
`Territory2AssociationManual` value.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the User or Group that has been given access to the Account. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


This object allows you to determine which users and groups can view or edit Account records owned by other users.

If you attempt to create an AccountShare record that matches an existing record, the request updates any modified fields and returns
the existing record.

For example, the following code finds all accounts owned by a user and manually shares them to a portal user.


-----

This code shares the accounts that the user owns at the time, but not those accounts that are owned later. For these types of shares,
use an owner-based sharing rule, such as AccountOwnerSharingRule.

If an account is shared in multiple ways with a user, you don’t always see multiple sharing records. If a user has access to an account for
one or more of the following RowCause values, the records in the AccountShare object are compressed into one record with the highest
level of access.

**•** `ImplicitParent`

**•** `Manual`

**•** `Owner`

SEE ALSO:

Account

CaseShare

LeadShare

OpportunityShare
