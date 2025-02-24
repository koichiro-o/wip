#### UserProvAccount

Represents information that links a Salesforce user account with an account in a third-party (target) system, such as Google, for users of
connected apps with Salesforce user provisioning enabled. This object is available in API version 33.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ConnectedAppId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The 15 character application ID.

This is a relationship field.


-----

```
DeletedDate
ExternalEmail
ExternalFirstName
ExternalLastName
ExternalUserId

```

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the associated user account in the target system was deleted. This
value is automatically updated during the provisioning and reconciling processes.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The first name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The last name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
ExternalUsername
IsKnownLink
LinkState

```

**Description**
The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The username as stored in the target system for the associated user account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Setting the `IsKnownLink` value to `true` implies the administrator or another user is
managing the relationship between the Salesforce user account and the third-party user
account, manually. This field helps Salesforce coordinate updates between the
UserProvAccountStaging object and the UserProvAccount object while committing staged
accounts. Typically, for a matching user account (the same `ExternalUserId` for both
objects), Salesforce copies the values from the UserProvAccountStaging object to the
UserProvAccount object.

However, if Salesforce encounters a UserProvAccountStaging object with a matching
`ExternalUserId` but different `LinkState` and `SalesforceUserId values`
during this process, Salesforce checks the UserProvAccount `IsKnownLink` value. If the
`IsKnownLinkvalue is` `true, Salesforce doesn’t copy the` `LinkState` and
`SalesforceUserId` values from the UserProvAccountStaging object to the
UserProvAccount object (all other values are copied).

The default is `false, meaning Salesforce manages the account relationship.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce organization
and the associated user account in the target system. The valid values are:

**•** `linked— changes to the account in the Salesforce organization are queued to be`
updated for the associated user account in the target system.

**•** `duplicate— an associated account in the target system exists.`

**•** `orphaned—no associated account exists in the target system.`


-----

```
Name
OwnerId
SalesforceUserId
Status

```


**•** `ignored— changes to the account in the Salesforce organization have no effect on`
the associated user account in the target system.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Namepointing, Sort, Update

**Description**
The user ID of the owner of this object—typically a Salesforce administrator.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID for the user account in the Salesforce organization that is associated with the
user account in the target system.

This is a relationship field.

**Relationship Name**
SalesforceUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the account in the target system. The valid values are:

**•** `Active`

**•** `Deactivated`

**•** `Deleted`


-----
