#### BusinessAlert

Represents information about insight notifications that Einstein Relationship Insights explores, such as news mentions, job updates, and
relationships. This object is available in API version 57.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The BusinessAlert object is available only if the ERI Growth User or ERI Starter User license is enabled.

##### Fields

```
AlertData
AlertRecordId
AlertType

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Data associated with each alert.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The record that's referenced by the insight alert.

This field is a polymorphic relationship field.

**Relationship Name**
AlertRecord

**Relationship Type**
Lookup

**Refers To**
Account, Asset, AuthorizationForm, AuthorizationFormConsent, AuthorizationFormDataUse,
AuthorizationFormText, BusinessBrand, CommSubscription, CommSubscriptionChannelType,
CommSubscriptionConsent, Contact, ContactPointAddress, ContactPointConsent,
ContactPointEmail, ContactPointPhone, ContactPointTypeConsent, ContentVersion, Customer,
DataUseLegalBasis, DataUsePurpose, EmailMessage, EngagementChannelType, Idea, Image,
Individual, Lead, Location, Opportunity, PartyConsent, Pricebook2, Product2, ProfileSkill,
QuickText, Recommendation, Scorecard, ScorecardMetric, Seller, SocialPersona, SocialPost,
Solution, VideoCall, WorkBadgeDefinition

In addition to the listed standard object fields, this field can refer to custom objects as well,

**Type**
picklist


-----

```
CurrentDesignation
CurrentEmployer
LastReferencedDate
LastViewedDate
Name

```

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the type of insight alert.

Possible values are:

**•** `JOB_CHANGE`

**•** `NEWS`

**•** `RELATIONSHIP`

The default value is `NEWS.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The current designation that's related to the job alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the current employer that's related to the job alert.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed a record related to this alert record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this alert.

**Type**
string


-----

```
OwnerId
PreviousDesignation
PreviousEmployer
