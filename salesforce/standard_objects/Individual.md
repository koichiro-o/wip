#### Individual

Represents a customer’s data privacy and protection preferences. Data privacy records based on the Individual object store your customers’
preferences. Data privacy records are associated with related leads, contacts, person accounts, and users. This object is available in API
version 42.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), merge(),
query(), retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
**•** This object is available if Data Protection and Privacy is enabled.

##### Fields

```
BirthDate
CanStorePiiElsewhere
ChildrenCount
ConsumerCreditScore

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s birthdate.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indication that you can store the customer’s personally identifiable information
(PII) outside of their legislation area. For example, you could store an EU citizen’s
PII data in the US.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of children the customer has.

**Type**
int


-----

```
ConsumerCreditScoreProviderName
ConvictionsCount
DeathDate
FirstName
HasOptedOutGeoTracking
HasOptedOutProcessing

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The person's credit score (for example, 740).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company that provided the credit score.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of convictions for the customer.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s death date.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s first name. Maximum size is 40 characters.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track geolocation on mobile devices.

**Type**
boolean


-----

```
HasOptedOutProfiling
HasOptedOutSolicit
HasOptedOutTracking
IndividualsAge
InfluencerRating

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process personal data, which can include collecting, storing,
and sharing personal data.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not process data for predicting personal attributes, such as interests,
behavior, and location.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not solicit products and services.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to not track customer web activity and whether the customer opens
email sent through Salesforce.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer is considered to be a minor.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
IsHomeOwner
LastName
LastViewedDate
MasterRecordId

```

**Description**
A measure of the person's influence, irrespective of how we do business with
them.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the customer owns a home.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The customer’s last name. Maximum size is 80 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the
record that was kept. If this object was deleted for any other reason, or hasn’t
been deleted, the value is `null.`

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Individual


-----

```
MilitaryService
Name
Occupation
OwnerId
Salutation

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the customer has served in the military.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and LastName. Maximum size is 203
characters, including whitespaces.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer’s occupation. Maximum size is 150 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SendIndividualData
ShouldForget
Website

##### Associated Objects

```

**Description**
The title for addressing the customer, such as Dr. or Mrs.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to export personal data for delivery to the customer.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Preference to delete records and personal data related to this customer.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL for the customer’s website.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**IndividualChangeEvent (API version 47.0)**
Change events are available for the object.

**IndividualHistory**

History is available for tracked fields of the object.

**IndividualShare**

Sharing is available for the object.
