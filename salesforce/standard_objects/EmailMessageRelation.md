#### EmailMessageRelation

Represents the relationship between an email and contacts, leads, and users. This object is available in API version 37.0 and later.

##### Special Access Rules

EmailMessageRelation is only available for organizations that use Email-to-Case or Enhanced Email, which is automatically enabled for
most customers.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
EmailMessageId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the `EmailMessage record.`

This is a relationship field.


-----

```
RelationAddress
RelationId
RelationObjectType

```

**Relationship Name**
EmailMessage

**Relationship Type**
Lookup

**Refers To**
EmailMessage

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The email address of the sender or recipient.

Note: If a record relates an email to an existing contact, lead, or user record
in Salesforce, the value of RelationAddress is the current value of
the email address. If the value is not set, it is auto-populated from
```
    RelationId.

```
**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The `RecordId` of the sender or recipient.

Note: If a record relates an email to an email address that’s not associated
with an existing contact, lead, or user record in Salesforce, the value of
`RelationId` is null.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
RelationType

##### Usage

```

**Description**
The API name of the object type of the RecordId in the RelationId field.
It can be a contact, lead, or user.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of relationship the contact, lead, or user has with the email message.
Possible values include:

**•** `ToAddress`

**•** `CcAddress`

**•** `BccAddress`

**•** `FromAddress`

**•** `OtherAddress`

For an Experience Cloud site user who is not the sender of the email, no
`BccAddress` relations are returned.


EmailMessageRelation allows an email to be related to contacts, leads, and users.
