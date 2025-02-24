#### PublicComplaint

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of proration policy.

Possible values are:

**•** `StandardTimePeriods—Indicates that the proration policy divides the subscription`
into similar time periods, and prorates the subscription using the time periods. For
example, a monthly subscription that's subscribed to for 12 months for a total amount
of $120 is prorated as $10 per month.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates how the leftover amount from the price calculation is allocated.

For example, if the total amount is $100 and the subscription has 12 periods, the price per
period is $8.33, with $0.04 remaining. To indicate that the $0.04 is included in the first period,
use the value `AddToFirst. To indicate that the $0.04 is included in the final period, use`
the value `AddToLast.`

Possible values are:

**•** `AddToFirst—Add the remaining amount to the first period.`

**•** `AddToLast—Add the remaining amount to the last period.`


Represents the complaints submitted by public users. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Fields added in API version 58.0 are available if the add-on license for Financial Services Cloud is enabled.


-----

##### Fields

**Field**
```
AccountId
BusinessAddress
BusinessName
CauseSubtype
CauseType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the Account associated with this complaint.

This field is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address of the business.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the business.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Misleading advertisement or documentation`

**Type**
picklist


-----

```
Comments
CompensationAmount
ComplaintCaseId
ComplaintCaseStatus

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of complaint cause. This field is available in API version 58.0 and later.

Possible values are:

**•** `Product Communication`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Additional details about the complaint. This field is available in API version 51.0 and later.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Any amount of money offered to resolve the complaint. This field is available in API version
58.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related Case. This field is available in API version 58.0 and later.

This field is a relationship field.

**Relationship Name**
ComplaintCase

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
ComplaintSubType

```

**Description**
The status of the related Case. This field is available in API version 58.0 and later.

Possible values are:

**•** `Closed`

**•** `Escalated`

**•** `In Progress`

**•** `Merged`

**•** `New`

**•** `On Hold`

**•** `Response Received`

**•** `Waiting for Customer`

**•** `Working`

The default value is `New.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subtype of complaint. All values except `Fire Safety` are available in API version
58.0 and later.

Possible values are:

**•** `Account Opening/Closure`

**•** `Amount Not Dispensed`

**•** `Attempts to Collect Debt not Owed`

**•** `Auto Debit Mandate`

**•** `Communication Tactics`

**•** `Credit Limit Changed`

**•** `Credit Report / Credit Score`

**•** `Delays / Timescales`

**•** `Disputes over sums/charges`

**•** `Errors / not following instructions`

**•** `Fire Safety`

**•** `Fraud Handling`

**•** `Inaccessible ATMs`

**•** `Inaccessible Branch Entrances`

**•** `Inaccessible Mobile banking features`

**•** `Inaccessible Website`


-----

```
ComplaintType
Description

```


**•** `Misleading Advertising`

**•** `Mobile Banking - Features or Functionality`

**•** `No Written Notification About Debt`

**•** `Online Banking - Features or Functionality`

**•** `Other General Admin/Customer Service`

**•** `Others`

**•** `Problem when Making Payments`

**•** `Product Disclosure Information`

**•** `Product Performance/Features`

**•** `Unauthorised Transaction(s)`

**•** `Unclear Arrangement`

**•** `Unclear Guidance`

**•** `Unsuitable Advice`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of complaint. All values except Safety are available in API version 58.0 and later.

Possible values are:

**•** `Accessibility Issues`

**•** `Advising, Selling and Arranging`

**•** `Digital or Technology`

**•** `Financial Hardship or Collections`

**•** `General Admin/ Customer Service`

**•** `Information, sums/ charges or Product Performance`

**•** `Lending / Credit`

**•** `Marketing or Corporate Communications`

**•** `Others`

**•** `Safety`

**•** `Transaction Related`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the complaint.


-----

```
Email
EscalationCause
FirstName
IncidentDate

```

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email of the complainant.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the complaint was escalated. This field is available in API version 58.0 and later.

Possible values are:

**•** `Alleged ADA Violation`

**•** `Alleged Discrimination`

**•** `Alleged MLA Violation`

**•** `Alleged SCRA Violation`

**•** `Alleged UDAAP Violation`

**•** `Consumer Protection Agency Involvement`

**•** `Lawsuit Filed`

**•** `Media Involvement`

**•** `None`

**•** `Received by Executive Leadership`

The default is `None.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The given name of the complainant.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The date of the incident.

The default is the date this record was created, but this field is editable.


-----

```
IsComplainantAuthorized
IsReporterConfidential
LastName
LastReferencedDate
LastViewedDate

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether the person who filed the complaint is an authorized representative of the Account.
This field is available in API version 58.0 and later.

The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The reporter's request for confidentiality.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The family name of the complainant.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
possibly the user only accessed this record or list view (LastReferencedDate) but
didn't view it.


-----

```
MobileNumber
Name
OwnerId
Priority

```

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The mobile number of the complainant.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the complaint.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the complaint owner.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The priority of the complaint.

Possible values are:

**•** `Critical`

**•** `High`

**•** `Low`

**•** `Medium`

The default value is `Medium.`


-----

```
ProductType
ReceivedDate
ReporterAddress
ReporterCategory

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The product that the complaint is about. This field is available in API version 58.0 and later.

Possible values are:

**•** `ATM / debit card`

**•** `Credit Card or Prepaid Card`

**•** `Insurance`

**•** `Investments`

**•** `Merchant Services`

**•** `Mobile / electronic banking`

**•** `Money transfers, virtual currency, and money services`

**•** `Mortgage / Home Finance`

**•** `Other`

**•** `Personal Loan / other loans`

**•** `Vehicle loan or lease`

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the complaint was received. This field is available in API version 58.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The address of the reporter for further communication.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Role of the reporter in the organization.

Possible values are:


-----

```
ReporterOrganization
ShouldInclInRegulatoryRpt
SourceType

```


**•** `Childcare Providers`

**•** `Healthcare worker`

**•** `Law Enforcement`

**•** `Medical Examiners`

**•** `Mental Health Professionals`

**•** `Other`

**•** `School Personnel`

**•** `Social Worker`

The default value is `School Personnel.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The organization the reporter is part of.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Whether this complaint must be included in a regulatory report. This field is available in API
version 58.0 and later.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The source of the complaint. This field is available in API version 58.0 and later.

Possible values are:

**•** `Branch`

**•** `Consumer Protection Agency`

**•** `Contact Centre`

**•** `Mobile App`

**•** `Regulatory Agency`

**•** `Social Media`

**•** `Web Chat`


-----

```
Status
Subject

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the complaint.

Possible values are:

**•** `In Review`

**•** `Resolved`

**•** `Submitted`

The default value is `Submitted.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Subject of the complaint. This field is available in API version 51.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PublicComplaintFeed on page 54**
Feed tracking is available for the object.

**PublicComplaintHistory on page 62**
History is available for tracked fields of the object.

**PublicComplaintOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PublicComplaintShare on page 66**
Sharing is available for the object.
