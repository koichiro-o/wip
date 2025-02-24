#### Campaign

Represents and tracks a marketing campaign, such as a direct mail promotion, webinar, or trade show.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
ActualCost
AmountAllOpportunities

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of money spent to run the campaign. Label is Actual Cost in Campaign.

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign, including closed/won
opportunities. Label is Value Opportunities in Campaign.


-----

```
AmountWonOpportunities
BriefId
BudgetedCost
CampaignImageId
CampaignMemberRecordTypeId

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in closed or won opportunities associated with the campaign. Label is
Value Won Opportunities in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the brief that's associated with the campaign. A brief contains additional context
about the goals and audience for the campaign. The label is Brief.

**Relationship Name**
Brief

**Relationship Type**
Lookup

**Refers To**
Record

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money budgeted for the campaign. Label is Budgeted Cost in Campaign.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the campaign image. Available in API version 42.0 and later. Only available to orgs with
Partner Community licenses and Digital Experience enabled or orgs that have installed the
Direct Marketing Managed package.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
CampaignStage
CreatedByID
CurrencyIsoCode

```

**Description**
The record type ID for CampaignMember records associated with the campaign.

This is a relationship field.

**Relationship Name**
CampaignMemberRecordType

**Relationship Type**
Lookup

**Refers To**
RecordType

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
This field is available with Marketing Cloud Growth and Advanced editions. The lifecycle
stage of the campaign based on the status of all of its related flows. Possible values are:

**•** In Planning

**•** In Progress

**•** Completed

**•** Error

**•** Canceled

**•** Paused

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who created the campaign.

This is a relationship field.

**Relationship Name**
Creator

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist


-----

```
Description
EndDate
ExpectedResponse
ExpectedRevenue
HierarchyActualCost

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
textarea

**Properties**
Nillable

**Description**
Description of the campaign. Limit: 32 KB. Only the first 255 characters display in reports.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Ending date for the campaign. Responses received after this date are still counted.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of responses you expect to receive for the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Amount of money you expect to generate from the campaign.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money spent to run the campaigns in a campaign
hierarchy. Label is Total Actual Cost in Hierarchy.


-----

```
HierarchyAmountAllOpportunities
HierarchyAmountWonOpportunities
HierarchyBudgetedCost
HierarchyExpectedRevenue
HierarchyNumberOfContacts
HierarchyNumberOfConvertedLeads

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
Amount of money in all opportunities associated with the campaign in a campaign hierarchy,
including closed/won opportunities. Label is Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Sort

**Description**
The amount of money in closed or won opportunities associated with the campaign in a
campaign hierarchy. Label is Value Won Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money budgeted for the campaigns in a campaign
hierarchy. Label isTotal Budgeted Cost in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the total amount of money you expect to generate from the campaign
in a campaign hierarchy. Label is Total Expected Revenue in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the number of contacts associated with the campaign hierarchy. Label
is Total Contacts in Hierarchy.

**Type**
currency


-----

```
HierarchyNumberOfLeads
HierarchyNumberOfOpportunities
HierarchyNumberOfResponses
HierarchyNumberOfWonOpportunities
HierarchyNumberSent

```

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of converted leads from the campaign in a campaign
hierarchy. Label is Converted Leads in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of leads from the campaign in a campaign hierarchy. Label
is Leads in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated field for the number of opportunities related to the campaign in a campaign
hierarchy. Label is Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Number of contacts and unconverted leads with a Member Status equivalent to “Responded”
for the campaign in a campaign hierarchy. Label is Responses in Hierarchy.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Hierarchy.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
HierarchyTotalEmailsDelivered
HierarchyTotalFormSubmissions
HierarchyTotalFormViews
HierarchyTotalLandingPageFormSubmissions
HierarchyTotalLandingPageViews

```

**Description**
Calculated field for the total number of individuals targeted by the campaign in a campaign
hierarchy. For example, the number of email messages sent. The label is Num Sent in
Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign in a campaign hierarchy. Label
is Total Emails Delivered in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign in a campaign hierarchy. Label
is Total Form Submissions in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign in a campaign hierarchy. Label is
Total Form Views in Hierarchy. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign in a
campaign hierarchy. Label is Total Landing Page Form Submissions in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
int


-----

```
HierarchyUniqueEmailOpens
HierarchyUniqueEmailTrackedLinkClicks
HierarchyUniqueMarketingLinkClicks
IsActive

```

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign in a campaign hierarchy.
Label is Total Landing Page Views in Hierarchy. This field is available with Marketing Cloud
Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign in a campaign hierarchy. Excludes
repeat opens. Label is Unique Email Opens in Hierarchy. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign in a campaign hierarchy.
Excludes repeat clicks. Label is Unique Email Clicks in Hierarchy. This field is available with
Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign in a campaign
hierarchy. Excludes repeat clicks. Label is Unique Marketing Link Clicks in Hierarchy. This field
is available with Marketing Cloud Account Engagement.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this campaign is active (true) or not (false). The default value is
```
  false. The label is Active.

```

-----

```
LastActivityDate
LastModifiedById
LastReferencedDate
LastViewedDate

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** The due date of the most recent event logged against the record.

**•** The due date of the most recently closed task associated with the record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who last updated the campaign.

This is a relationship field.

**Relationship Name**
Last Modified

**Relationship Type**
Lookup

**Refers To**
User

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.


-----

```
Name
NumberOfContacts
NumberOfConvertedLeads
NumberOfLeads
NumberOfOpportunities
NumberOfResponses

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Required. Name of the campaign. Limit: is 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of contacts associated with the campaign. Label is Total Contacts.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of leads that were converted to an account and contact due to the marketing efforts
in the campaign. Label is Converted Leads.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of leads associated with the campaign. Label is Leads in Campaign.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of opportunities associated with the campaign. Label is Opportunities in
Campaign.

**Type**
int

**Properties**
Filter, Group, Sort


-----

```
NumberOfWonOpportunities
NumberSent
OwnerId
ParentCampaign

```

**Description**
The number of contacts and unconverted leads with a Member Status equivalent to
“Responded” for the campaign. Label is Responses in Campaign.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The number of closed or won opportunities associated with the campaign. Label is Won
Opportunities in Campaign.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of individuals targeted by the campaign. For example, the number of emails
sent. Label is Num Sent.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user who owns this campaign. Default value is the user logging in to the API to
perform the create.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
The campaign above the selected campaign in the campaign hierarchy.


-----

```
ParentId
RecordTypeId
StartDate
Status
TenantId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

ID of the parent Campaign record, if any.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Starting date for the campaign.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Status of the campaign, for example, Planned, In Progress. Limit: 40 characters.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
TotalAmountAllOpportunities
TotalAmountAllWonOpportunities
TotalEmailsDelivered
TotalFormSubmissions

```

**Description**
ID of the associated Marketing Cloud Account Engagement business unit. Read-only. Available
with Marketing Cloud Account Engagement in API version 51.0 and later.

This is a relationship field.

**Relationship Name**
Business Unit

**Relationship Type**
Lookup

**Refers To**
PardotTenant

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for total amount of all opportunities associated with the campaign hierarchy,
including closed/won opportunities. Label is Total Value Opportunities in Hierarchy.

**Type**
currency

**Properties**
Filter

**Description**
Calculated field for amount of all closed/won opportunities associated with the campaign
hierarchy. Label is Total Value Won Opportunities in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for emails delivered related to the campaign. Label is Total Emails Delivered
in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions related to the campaign. Label is Total Form Submissions
in Campaign. This field is available with Marketing Cloud Account Engagement.


-----

```
TotalFormViews
TotalLandingPageFormSubmissions
TotalLandingPageViews
TotalNumberofLeads
TotalNumberofOpportunities

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form views related to the campaign. Label is Total Form Views in Campaign.
This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for form submissions from a landing page related to the campaign. Label is
Total Landing Page Form Submissions in Campaign. This field is available with Marketing
Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for landing page views related to the campaign. Label is Total Landing Page
Views in Campaign. This field is available with Marketing Cloud Account Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for total number of leads associated with the campaign hierarchy. This
number also includes converted leads. Label is Total Leads in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of opportunities associated with the campaign hierarchy.
Label is Total Opportunities in Hierarchy.


-----

```
TotalNumberofResponses
TotalNumberofWonOpportunities
Type
UniqueEmailOpens
UniqueEmailTrackedLinkClicks

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for number of contacts and unconverted leads that have a `Member`
```
  Status equivalent to “Responded” for the campaign hierarchy. Label is Total Responses

```
in Hierarchy.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for the total number of won opportunities associated with the campaign
hierarchy. Label is Total Won Opportunities in Hierarchy.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Type of campaign, for example, Direct Mail or Referral Program. Limit: 40 characters.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for email opens related to the campaign. Excludes repeat opens. Label is
Unique Email Opens in Campaign. This field is available with Marketing Cloud Account
Engagement.

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique email link clicks related to the campaign. Excludes repeat clicks.
Label is Unique Email Clicks in Campaign. This field is available with Marketing Cloud Account
Engagement.


-----

```
UniqueMarketingLinkClicks

##### Usage

```

**Type**
int

**Properties**
Filter

**Description**
Calculated field for unique marketing link clicks related to the campaign. Excludes repeat
clicks. Label is Unique Marketing Link Clicks in Campaign. This field is available with Marketing
Cloud Account Engagement.


Client applications can create, update, delete, and query Attachment records associated with a campaign via the API.

The Campaign object is defined only for those organizations that have the marketing feature enabled and valid marketing licenses. In
addition, it is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature
or valid marketing licenses, this object does not appear in the describeGlobal() call, and you can’t use describeSObjects()
or `query()` with the Campaign object.

Note: The main constituent of a campaign is a CampaignMember. You will commonly need to update campaigns with
CampaignMember.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CampaignChangeEvent (API version 44.0)**
Change events are available for the object.

**CampaignFeed (API version 18.0)**
Feed tracking is available for the object.

**CampaignHistory (API version 40.0)**
History is available for tracked fields of the object.

**CampaignOwnerSharingRule**

Sharing rules are available for the object.

**CampaignShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields
