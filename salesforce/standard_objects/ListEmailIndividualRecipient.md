#### ListEmailIndividualRecipient

For a list email in Salesforce, represents a recipient. Each record represents a link from a list email to exactly one recipient for that list
email. Recipients can be contacts, leads, or campaign members. Has a one-to-many relationship with ListEmail. This object is available
in API version 44.0 and later.

The visibility and accessibility of this object is inherited from the related list email.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ActionCadenceStepTrackerId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Understand which action cadence step tracker the list email individual recipient is related
to. Used for automated emails in Sales Engagement.

Users must have the Sales Engagement Cadence Creator or Sales Engagement User permission
enabled.

This field is available in API version 54.0 and later.

**Relationship Name**
ActionCadenceStepTracker

**Relationship Type**
Lookup

**Refers To**
ActionCadenceStepTracker

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `EUR` (Euro)

**•** `INR` (Indian Rupee)

**•** `USD` (US Dollars)


-----

```
ListEmailId
Name
RecipientId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The related list email record. Required on record creation; read-only otherwise.

This is a relationship field.

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated name of the list email recipient source.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
the contact, lead, person account, or campaign member ID of the individual list email recipient.

This is a relationship field.

**Relationship Name**
Recipient

**Relationship Type**
Lookup

**Refers To**
CampaignMember, Contact, Lead


-----

##### Usage
