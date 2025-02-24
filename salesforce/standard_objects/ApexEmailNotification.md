#### ApexEmailNotification

Stores a Salesforce user ID or external email address to be notified when unhandled Apex exceptions occur. This object is available in
API version 35.0 and later.

Note: Each ApexEmailNotification contains either an email or a user ID, but not both.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(),upsert()

 Fields

```
```
Email
UserId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The external email address to which the notification is sent. Mutually exclusive with the
`UserId` field.

**Type**
reference


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the user to which the notification is sent. Mutually exclusive with the `Email` field.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

##### Usage

To notify users of your org at the email addresses they have on record, use UserId. To notify external users or alternate email addresses,
use `Email.`
