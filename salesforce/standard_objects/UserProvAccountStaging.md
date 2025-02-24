#### UserProvAccountStaging

Temporarily stores user account information while a user completes the User Provisioning Wizard. This information that is stored in the
UserProvAccount object when you click the button to collect and analyze accounts on the target system.

User provisioning links a Salesforce user account with an account in a third-party (target) system. To configure user provisioning, you
use a User Provisioning Wizard that guides you through the setup process. As you enter values about account details in the wizard, these
values are stored in this object until you click the button to collect and analyze accounts on the target system. The general user provisioning
configuration details are stored in the UserProvisioningConfig object.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ConnectedAppId
ExternalEmail
ExternalFirstName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 15 character connected app ID.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

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


-----

```
ExternalLastName
ExternalUserId
ExternalUsername
LinkState
Name

```

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

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The state of the current connection between the user account in the Salesforce
organization and the associated user account in the target system. The valid
values are:

**•** `linked— a user account matches one in the target system.`

**•** `duplicate— an associated account in the target system exists.`

**•** `orphaned—no associated account exists in the target system.`

**•** `ignored— changes to the account in the Salesforce organization have`
no effect on the associated user account in the target system.

**Type**
string


-----

```
OwnerId
SalesforceUserId
Status

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**

The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The user ID for the user account in the Salesforce organization that is associated
with the user account in the target system.

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

##### Usage

When committing fields from a UserProvAccountStaging to a UserProvAccount object, Salesforce looks up the UserProvAccount record
where `UserProvAccountStaging.ExternalUserId = UserProvAccount.ExternalUserId.`

**•** If an `ExternalUserId` doesn't match an existing account, Salesforce creates a UserProvAccount record based on the
UserProvAccountStaging record.

**•** If an `ExternalUserId` matches, then Salesforce checks the UserProvAccount.isKnownLink value, and does the
following.

**–** If `UserProvAccount.IsKnownLink = true, Salesforce copies the UserProvAccountStaging values to the`
UserProvAccount object, except for the `ExternalUserId` and LinkState values.

**–** If `UserProvAccount.IsKnownLink = false, Salesforce copies all of the UserProvAccountStaging values to the`
UserProvAccount object.
