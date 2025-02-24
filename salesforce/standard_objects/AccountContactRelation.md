#### AccountContactRelation

Represents a relationship between a contact and one or more accounts.

This object is available in API version 37.0. The AccountContactRelation object supports person accounts. That means that a person
account can be either a related contact on a business account or a related account on a contact. A person account can also be related
to another person account as either a related contact or related account.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
AccountContactRelationshipCurrency
AccountId
ContactId
EndDate
IsActive

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains
the ISO code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the account that is related to the contact. Field can't be modified when
updating existing account-contact relationship records.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the contact that is related to the account. Field can't be modified when
updating existing account-contact relationship records.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date a relationship between a contact and account ended. Use with the
`Start Date` to keep a history of the relationship.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether relationship is active (true) or not (false).


-----

```
IsDirect
Roles
StartDate

##### Usage

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the account associated with the contact is the contact's primary
account (true) or not (false).

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
The contact’s participating role in the account. Values are `Business User,`
```
  Decision Maker, Economic Buyer, Economic Decision Maker,
  Evaluator, Executive Sponsor, Influencer, Technical
  Buyer, and Other.

```
**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date a relationship between a contact and account began. Use with the End
`Date` to keep a history of the relationship.


Use this object to associate a single contact record to multiple account records so you can easily track the relationships between the
people and businesses they work with.

When you insert a non-private contact in your org that associates a contact to multiple accounts, an AccountContactRelation is created
and its validation rules, database insertion, and triggers are executed immediately after the contact is saved to the database. When you
change a contact's primary account, an AccountContactRelation may be created or edited, and the AccountContactRelation validation
[rules, database changes, and triggers are executed immediately after the contact is saved to the database. See Order of Execution.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountContactRelationChangeEvent on page 67 (API version 59.0)**
Change events are available for the object.


-----

**AccountContactRelationHistory on page 62—Available in API version 62.0 and later.**
History is available for tracked fields of the object.
