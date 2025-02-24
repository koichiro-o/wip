#### Lead

Represents a prospect or lead.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), merge(),
query(), retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActionCadenceAssigneeId
ActionCadenceId
ActionCadenceState

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the sales rep designated to work the lead through their assigned cadence. This
field is available in API version 48.0 and later when the Sales Engagement license is enabled.
To see this field, the user also needs the Sales Engagement User or Sales Engagement Quick
Cadence Creator user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the lead’s assigned cadence. This field is available in API version 48.0 and later when
the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The state of the current action cadence tracker. This field is available in API version 50.0 and
later when the Sales Engagement license is enabled. To see this field, the user also needs
the Sales Engagement User or Sales Engagement Quick Cadence Creator user permission
set.

Possible values are:

**•** `Complete`

**•** `Error`


-----

```
ActiveTrackerCount
ActivityMetricId
ActivityMetricRollupId

```


**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cadences that are actively running on this lead. This field is available in API
version 57.0 and later when the Sales Engagement license is enabled. To see this field, the
user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

This field is available in API version 41.0 and later.

**Relationship Name**
ActivityMetricRollup


-----

```
Address
AnnualRevenue
City
CleanStatus

```

**Refers To**
ActivityMetricRollup

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the address. Read-only. For details on compound address fields, see
Address Compound Fields.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Annual revenue for the lead’s company.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
City for the lead’s address.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the record's clean status compared with Data.com. .

Several values for `CleanStatus` appear with different labels on the lead record.

Values include:

**•** `Acknowledged - Reviewed`

**•** `Different`

**•** `Inactive`

**•** `Matched - In Sync`

**•** `NotFound - Not Found`

**•** `Pending - Not Compared`

**•** `SelectMatch - Select Match Skipped`


-----

```
Company
CompanyDunsNumber
ConvertedAccountId
ConvertedContactId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. The lead’s company.

If person account record types have been enabled, and if the value of Company is null, the
lead converts to a person account.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Data Universal Numbering System (D-U-N-S) number, which is a unique, nine-digit
number assigned to every business location in the Dun & Bradstreet database that has a
unique, separate, and distinct operation. Industries and companies use D-U-N-S numbers
as a global standard for business identification and tracking. Maximum size is 9 characters.

This field is only available to organizations that use Data.com Prospector or Data.com Clean.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the account into which the lead converted.

This is a relationship field.

**Relationship Name**
ConvertedAccount

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the contact into which the lead converted.

This is a relationship field.


-----

```
ConvertedDate
ConvertedOpportunityId
ConnectionReceivedId
ConnectionSentId

```

**Relationship Name**
ConvertedContact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Date on which this lead was converted.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Object reference ID that points to the opportunity into which the lead has been converted.

This is a relationship field.

**Relationship Name**
ConvertedOpportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your org. This field is
available when Salesforce to Salesforce is enabled.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
Country
CountryCode
CurrencyIsoCode
DandBCompanyId
Description

```

**Description**
ID of the PartnerNetworkConnection that this record is shared with. This field is available
Salesforce to Salesforce is enabled. In API version 16.0 and later, this value is `null. Use`
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO country code for the lead’s address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference ID to a Dun & Bradstreet[®] company record, associated with an account added
from Data.com.

**Relationship Name**
DandbCompany

**Refers To**
DandbCompany

**Type**
textarea


-----

```
Division
Email
EmailBouncedDate
EmailBouncedReason
ExportStatus

```

**Properties**
Create, Nillable, Update

**Description**
The lead’s description.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as North
America, Healthcare, or Consulting. Available only when the Division permission is enabled.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The lead’s email address.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the lead bounced, the date and
time of the bounce. Email bounce functionality isn't triggered by record updates, including
updates to this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the lead bounced, the reason for
the bounce. Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
picklist


-----

```
Fax
FirstCallDateTime
FirstEmailDateTime
FirstName
GeocodeAccuracy

```

**Properties**
Filter, Restricted picklist, Sort

**Description**
Derived field for the record map for Partner Connect. The export status of this opportunity
to the partner’s connected org. To see this field, enable Partner Connect and add the Export
Vendor Records to an Authorized Partner Org user permission to the cosell export user. See
[Set Up Partner Connect as a Vendor in Salesforce Help. Available in API version 62.0 and later.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s fax number.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the lead. This field is available in API version 48.0
when the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the lead. This field is available in API version 48.0
when the Sales Engagement license is enabled. To see this field, the user also needs the Sales
Engagement User or Sales Engagement Quick Cadence Creator user permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s first name up to 40 characters.

**Type**
picklist


-----

```
GenderIdentity
HasOptedOutOfEmail
HasOptedOutOfFax
IndividualId

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the address. For details on geolocation compound fields,
see Compound Field Considerations and Limitations.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The lead’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the lead doesn’t want to receive email from Salesforce (true) or does
(false). Label is Email Opt Out.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the lead doesn’t want to receive faxes from Salesforce (true) or does
(false). Label is FaxOpt Out.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this lead. This field is available if you enabled
Data Protection and Privacy in Setup.

**Relationship Name**
Individual

**Relationship Type**
Lookup


-----

```
Industry
IsConverted
IsDeleted
IsPriorityRecord
IsUnreadByOwner

```

**Refers To**
Individual

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Industry in which the lead works.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the lead has been converted (true) or not (false). Label is Converted.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the lead as important (True) or not (False). The
default value is `false. Available in API version 59.0 and later.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If true, lead has been assigned, but not yet viewed. See Unread Leads for more information.
Label is Unread By Owner.


-----

```
Jigsaw
JigsawContactId
LastActivityDate
LastName
LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
References the ID of a contact in Data.com. If a lead has a value in this field, it means that a
contact was imported as a lead from Data.com. If the contact (converted to a lead) wasn’t
imported from Data.com, the field value is null. Maximum size is 20 characters. Available in
API version 22.0 and later. Label is Data.com Key.

Important: The Jigsaw field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
```
    Jigsaw field.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to `Jigsaw.`

Important: The Jigsaw field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Don’t modify the value in the
```
    Jigsaw field.

```
**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is the most recent of either:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the lead up to 80 characters.

**Type**
dateTime


-----

```
LastViewedDate
Latitude
LeadSource
Longitude
MasterRecordId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of an address. Acceptable values
are numbers between –90 and 90 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The origin or source of the lead.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an address. Acceptable values
are numbers between –180 and 180 up to 15 decimal places. For details on geolocation
compound fields, see Compound Field Considerations and Limitations.

**Type**
reference


-----

```
MiddleName
MobilePhone
Name
NumberOfEmployees

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this record was deleted for any other reason, or hasn’t been deleted, the value
is `null.`

When using Apex triggers to determine which record was deleted in a merge event, this
field’s value is the ID of the record that remains in `Trigger.old. In` `Trigger.new,`
the value is `null.`

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s middle name. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s mobile phone number.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName,` `MiddleName,` `LastName, and` `Suffix` up to 203
characters, including whitespaces.

**Type**
int


-----

```
OwnerId
PartnerAccountId
Phone
PhotoUrl

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of employees at the lead’s company. Label is Employees.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the lead’s owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner account for the partner user that owns this lead. Available if Partner
Relationship Management is enabled or if digital experiences is enabled and you have partner
portal licenses.

In API version 16.0 and later, the Partner Account field is set to the appropriate account
for the partner user that owns the lead. If the owner of the lead isn’t a partner user, this field
has no value.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s phone number.

**Type**
url


-----

```
PostalCode
Pronouns
Rating
RecordTypeId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance (Example:
https://yourInstance.salesforce.com/) to generate a URL to request the social network
profile image associated with the lead. Generated URL returns an HTTP redirect (code 302)
to the social network profile image for the lead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Postal code for the address of the lead. Label is Zip/Postal Code.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The lead’s personal pronouns, reflecting their gender identity. Others can use these pronouns
to refer to the lead in the third person. The entry is selected from a picklist of available values,
which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Rating of the lead.

**Type**
reference


-----

```
Salutation
ScheduledResumeDateTime
ScoreIntelligenceId
State
StateCode

```

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salutation for the lead.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the action cadence tracker is going to resume after it’s paused or
on a wait step. This field is available in API version 54.0 and later when the Sales Engagement
license is enabled. To see this field, the user also needs the Sales Engagement User or Sales
Engagement Quick Cadence Creator user permission set.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the intelligent field record that contains lead score.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
State for the address of the lead.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO state code for the lead’s address.


-----

```
Status
Street
Suffix
Title
Website

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Status code for this converted lead. Status codes are defined in `Status` and represented
in the API by the LeadStatus object.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street number and name for the address of the lead.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The lead’s name suffix. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title for the lead, such as CFO or CEO. The maximum size is 128 characters. When converting
a lead to a person account, the conversion fails if the lead Title field contains more than 80
characters.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Website for the lead.


Note: If lead data is imported and you need to set the value for an audit field, such as `CreatedDate, contact Salesforce`
Support. Audit fields are automatically updated during API operations unless you request to set these fields yourself.


-----

##### Converted Leads

Leads have a special state to indicate that they’ve been converted into an account, a contact, and an opportunity. Your client application
can convert leads via the `convertLead()` call. Users can also convert leads in Salesforce. After a lead has been converted, it’s read
only. However, you can query converted lead records. Only users with the View and Edit Converted Leads permission can update
converted lead records.

Leads have several fields that indicate their converted status. These special fields are set when converting the lead in the user interface.

**•** `ConvertedAccountId`

**•** `ConvertedContactId`

**•** `ConvertedDate`

**•** `ConvertedOpportunityId`

**•** `IsConverted`

**•** `Status`

##### Unread Leads

Leads have a special state to indicate that they haven’t been viewed or edited by the lead owner. In Salesforce, it’s helpful for users to
know which leads have been assigned to them but that they haven’t touched yet. `IsUnreadByOwner` is `true` if the lead owner
hasn’t yet viewed or edited the lead, and `false` if the lead owner has viewed or edited the lead at least one time.

##### Lead Status Picklist

Each `Status` value corresponds to either a converted or unconverted status in the lead status picklist, as defined in the user interface.
To obtain the lead status values in the picklist, a client application can query LeadStatus.

You can't convert a lead via the API by changing Status to one of the converted lead status values. When you convert qualified leads
into an account, contact, and opportunity, you can select one of the converted status types for the lead. Leads with a converted status
type are no longer available in the Leads tab, although you can include them in reports.

##### Usage

If lead data is imported and you need to set the value for an audit field, such as `CreatedDate, contact Salesforce Support. Audit`
fields are automatically updated during API operations unless you request to set these fields yourself.

To update a lead or to convert one with `convertLead(), log in to your client application with the Edit permission on leads.`

When you create, update, or upsert a lead, your client application can have the lead assigned to multiple user records based on assignment
rules that have been configured in Salesforce.

To use this feature, your client application needs to set either of these options (but not both) in the AssignmentRuleHeader used in
create or update:


`assignmentRuleId` reference


ID of the assignment rule to use. Can be an inactive assignment rule. If unspecified
and `useDefaultRule` is `true, then the default assignment rule is used.`

To find the ID for a given assignment rule, query the AssignmentRule object
(specifying RuleType="leadAssignment"), iterate through the returned


-----

AssignmentRule records, find the one you want to use, retrieve its ID, and then
specify its ID in this field in the AssignmentRuleHeader.

`useDefaultRule` boolean Specifies whether to use the default rule for rule-based assignment (true) or
not (false). Default rules are assigned in the user interface.

##### Java Sample

The following Java sample shows how to automatically assign a newly created lead.


-----

-----

##### C# Sample

The following C# sample shows how to automatically assign a newly created lead.


-----

-----

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**LeadChangeEvent (API version 44.0)**
Change events are available for the object.

**LeadFeed (API version 18.0)**
Feed tracking is available for the object.

**LeadHistory**

History is available for tracked fields of the object.

**LeadOwnerSharingRule**

Sharing rules are available for the object.


-----

**LeadShare**

Sharing is available for the object.

SEE ALSO:

LeadOwnerSharingRule

LeadShare

LeadStatus

PartnerNetworkConnection
