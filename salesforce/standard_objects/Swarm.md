#### Swarm

```

**Relationship Name**
RelatedInternalRecord

**Relationship Type**
Lookup

**Refers To**
Account, Address, Asset, AssociatedLocation, AuthorizationForm, AuthorizationFormConsent,
AuthorizationFormDataUse, AuthorizationFormText, BusinessBrand, Case, CommSubscription,
CommSubscriptionChannelType, CommSubscriptionConsent, CommSubscriptionTiming,
Contact, ContactPointAddress, ContactPointConsent, ContactPointEmail, ContactPointPhone,
ContactPointTypeConsent, Contract, ContractLineItem, Customer, DataUseLegalBasis,
DataUsePurpose, Employee, EngagementChannelType, Entitlement, Idea, Individual,
InternalOrganizationUnit, Lead, Location, MessagingEndUser, Opportunity, Order, OrderItem,
PartyConsent, Pricebook2, ProcessException, Product2, ProfileSkill, ProfileSkillEndorsement,
ProfileSkillUser, QuickText, Recommendation, Seller, ServiceContract, SocialPersona, SocialPost,
Solution, SurveyInvitation, SurveySubject, UserProvisioningRequest, VoiceCall

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The SvcCatalogRequest record.

This is a relationship field.

**Relationship Name**
SvcCatalogRequest

**Relationship Type**
Lookup

**Refers To**
SvcCatalogRequest


Represents a team of agents, Salesforce users, or Slack users in a Slack channel or thread dedicated to solving a problem. This problem
can be related to a support case, incident, sales opportunity, or change request. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

To access this object for swarming in Salesforce, enable the Run Flows and Service Cloud User user permissions. For swarming in Slack,
connect Salesforce to Slack and enable the Run Flows and Slack Service User user permissions.

##### Fields

```
CollaborationRoomId
CollaborationTool
CollaborationUrl
EndedDateTime

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the collaboration room.

This field is a relationship field.

**Relationship Name**
CollaborationRoom

**Relationship Type**
Lookup

**Refers To**
CollaborationRoom

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Tool used for swarming.

Possible values are:

**•** `None`

**•** `Slack`

The default value is `None.`

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL of the Slack channel or thread.

**Type**
dateTime


-----

```
HelpNeeded
IsDedicatedChannel
LastReferencedDate
LastViewedDate
MessageKey

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm ended.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Short description of the problem that the swarm is trying to solve.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the swarm is happening in a dedicated channel (true) or in an existing channel
(false).

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, the
user might have only accessed this record or list view (LastReferencedDate) but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Name
OwnerId
RelatedRecordId
StartedDateTime

```

**Description**
ID of the Slack thread or message.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the swarm.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the swarm owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the record the swarm’s problem is related to. The record can be of, for example, a case,
incident, sales opportunity, or change request.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Account, Case, ChangeRequest, Incident, Opportunity, Problem, User

**Type**
dateTime


-----

```
Status
UsageType

##### Associated Objects

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Date and time the swarm started.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status of the swarm.

Possible values are:

**•** `Closed`

**•** `In Progress`

**•** `New`

**•** `Waiting (Custom)`

The default value is `New.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of swarm.

Possible values are:

**•** `CareMgmt—Care Coordination`

**•** `DealRoom—Sales Channel`

**•** `PartnerChannel—Partner Account Channel`

**•** `Swarming`

The default value is `Swarming.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SwarmFeed on page 54**
Feed tracking is available for the object.

**SwarmHistory on page 62**
History is available for tracked fields of the object.


-----

**SwarmOwnerSharingRule on page 64**
Sharing rules are available for the object.

**SwarmShare on page 66**
Sharing is available for the object.
