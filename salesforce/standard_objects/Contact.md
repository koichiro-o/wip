#### Contact

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing taxes usage summary invoice lines based off the summary's related tax
rule.


Represents a contact, which is a person associated with an account.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), merge(),
query(), retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Customer Portal users can access only portal-enabled contacts.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account that’s the parent of this contact.

We recommend that you update up to 50 contacts simultaneously when changing the
accounts on contacts enabled for a Customer Portal or partner portal. We also recommend
that you make this update after business hours.

This is a relationship field.

**Relationship Name**
Account


-----

```
ActionCadenceAssigneeId
ActionCadenceId
ActionCadenceState

```

**Relationship Type**
Lookup

**Refers To**
Account

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

**•** `Initializing`

**•** `Paused`

**•** `Processing`

**•** `Running`


-----

```
ActiveTrackerCount
ActivityMetricId
ActivityMetricRollupId
AssistantName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of cadences that are actively running on this contact. This field is available in
API version 57.0 and later when the Sales Engagement license is enabled. To see this field,
the user also needs the Sales Engagement User or Sales Engagement Quick Cadence Creator
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

**Refers To**
ActivityMetricRollup

**Type**
string


-----

```
AssistantPhone
Birthdate
BuyerAttributes

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s name.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The assistant’s phone number. Label is Asst. Phone.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s birthdate.

Filter criteria for report filters, list view filters, and SOQL queries ignore the year portion of
the Birthdate field. For example, this SOQL query returns contacts with birthdays later
in the year than today:
```
  SELECT Name, Birthdate
  FROM Contact
  WHERE Birthdate > TODAY

```
**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the role of the contact in the opportunity or account. Possible values are:

**•** `BusinessUser—For example, an end user. Key value.`

**•** `Buyer—Key value`

**•** `Champion—Key value`

**•** `DecisionMaker—Shown in green on a contact in the buyer relationship map UI.`
Key value.

**•** `Detractor—Shown in red on a contact in the buyer relationship map UI. Key value.`

**•** `Evaluator`

**•** `ExecutiveSponsor—Key value`

**•** `TechnicalExpert`


-----

```
CanAllowPortalSelfReg
CleanStatus
ConnectionReceivedId
ConnectionSentId

```

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success.

Warning: To ensure that the buyer relationship map feature works as expected,
don't modify field values. For example, if you change `Detractor` to `Detract,`
the value isn’t shown in red in a buyer relationship map.

This field is available with all profiles except custom and minimum-access. To provide access,
use field-level security in Object Manager.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this contact can self-register for your Customer Portal (true) or not
(false).

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the record’s clean status as compared with Data.com. Values include: Matched,
```
  Different, Acknowledged, NotFound, Inactive, Pending, SelectMatch,

```
or Skipped.

Several values for `CleanStatus` appear with different labels on the contact record.

**•** `Matched` appears as In Sync

**•** `Acknowledged appears as Reviewed`

**•** `Pending` appears as Not Compared

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference


-----

```
ContactSource
Department
DepartmentGroup

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Creation is enabled, this field indicates whether the contact was created
automatically. A possible value is:

**•** `Auto Create`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s department.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the business unit, function, or department that the contact belongs to in the organization.
Possible values are:

**•** `chiefExecutive—Key value`

**•** `customerSuccess—For example, wealth management, consumer banking, subject`
matter experts, or healthcare research experts.

**•** `finance—Includes pricing and procurement. Key value.`

**•** `humanResources`

**•** `legal—Key value`

**•** `marketing`

**•** `other`

**•** `sales`


-----

```
Description
DoNotCall
Email
EmailBouncedDate
EmailBouncedReason

```


**•** `support—For example, tech support or customer support.`

**•** `tech—For example, IT or engineering. Key value.`

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t have contacts with key values, then Salesforce prompts you to add them. Having all
key values represented on the map provides a full view of the deal or account, increasing
sales success. This field is available with all profiles except custom and minimum-access. To
provide access, use field-level security in Object Manager.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the contact. Label is Contact Description up to 32 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that the contact doesn’t want to receive calls.

**Type**
email

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The contact’s email address.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the date and time of the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
string


-----

```
Fax
FirstCallDateTime
FirstEmailDateTime
FirstName

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If bounce management is activated and an email sent to the contact results in a hard bounce,
the reason for the bounce.

Note: Email bounce functionality isn't triggered by record updates, including updates
to this field.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s fax number. Label is Business Fax.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first call placed to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time of the first email sent to the contact. This field is available in API version
48.0 and later when the Sales Engagement license is enabled. To see this field, the user also
needs the Sales Engagement User or Sales Engagement Quick Cadence Creator user
permission set.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s first name up to 40 characters.


-----

```
GenderIdentity
HasOptedOutOfEmail
HasOptedOutOfFax
HomePhone
IndividualId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s internal experience of their gender, which may or may not correspond to their
designated sex at birth.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact doesn’t want to receive email from Salesforce (true) or does
(false). Label is Email Opt Out.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the contact prohibits receiving faxes.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s home phone number. Label is Home Phone.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data privacy record associated with this contact. This field is available if Data
Protection and Privacy is enabled.

This is a relationship field.

**Relationship Name**
Individual


-----

```
IsDeleted
IsEmailBounced
IsPersonAccount
IsPriorityRecord
Jigsaw

```

**Relationship Type**
Lookup

**Refers To**
Individual

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
Defaulted on create, Filter, Group, Sort

**Description**
If bounce management is activated and an email is sent to a contact, indicates whether the
email results in a soft or hard bounce (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read only. Indicates whether this account has a record type of Person Account (true) or
not (false). Label is Is Person Account.

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the contact as important (True) or not (False). The
default value is false. Available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
JigsawContactId
LastActivityDate
LastName
LastReferencedDate

```

**Description**
References the company’s ID in Data.com. If an account has a value in this field, it means
that the account was imported from Data.com. If the field value is null, the account wasn’t
imported from Data.com. Maximum size is 20 characters. Available in API version 22.0 and
later. Label is Data.com Key.

Important: The Jigsaw field is exposed in the API to support troubleshooting for
import errors and reimporting of corrected data. Do not modify this value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the contact in reference to Jigsaw.

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
Required. Last name of the contact up to 80 characters.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.


-----

```
LastViewedDate
LeadSource
MailingAddress
MailingCity
MailingCountry
MailingCountryCode

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The source of the lead that was converted to this contact.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the mailing address. Read-only. For details on compound address
fields, see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
MailingGeocodeAccuracy
MailingLatitude
MailingLongitude
MailingPostalCode
MailingState

```

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update, Query, Restricted picklist, Nillable

**Description**
Accuracy level of the geocode for the mailing address. For details on geolocation compound
field, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with MailingLongitude to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with MailingLatitude to specify the precise geolocation of a mailing address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Mailing address details.


-----

```
MailingStateCode
MailingStreet
MasterRecordId
MiddleName
MobilePhone

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the mailing address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street address for mailing address.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this record was deleted as the result of a merge, this field contains the ID of the record that
remains. If this record was deleted for any other reason, or hasn’t been deleted, the value is
```
  null.

```
This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact’s middle name. Maximum size is 40 characters.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Name
OtherAddress
OtherCity
OtherCountry
OtherCountryCode
OtherGeocodeAccuracy

```

**Description**
Contact’s mobile phone number. Label is Mobile Phone.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName, MiddleName, LastName, and Suffix` up to 203
characters, including whitespaces.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The compound form of the other address. Read-only. For details on compound address fields,
see Address Compound Fields.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
picklist


-----

```
OtherLatitude
OtherLongitude
OtherPhone
OtherPostalCode
OtherState

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Accuracy level of the geocode for the other address. For details on geolocation compound
fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with OtherLongitude to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –90 and 90 up to 15 decimal places. For details on
geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with OtherLatitude to specify the precise geolocation of an alternate address.
Acceptable values are numbers between –180 and 180 up to 15 decimal places. For details
on geolocation compound fields, see Compound Field Considerations and Limitations.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone for alternate address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Alternate address details.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
OtherStateCode
OtherStreet
OwnerId
Phone
PhotoUrl

```

**Description**
Alternate address details.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ISO codes for the alternate address’s state and country.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Street for alternate address.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this contact.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number for the contact. Label is Business Phone.

**Type**
url


-----

```
Pronouns
RecordTypeId
ReportsToId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

Path to be combined with the URL of a Salesforce instance (Example:
https://yourInstance.salesforce.com/) to generate a URL to request the social network
profile image associated with the contact. Generated URL returns an HTTP redirect (code
302) to the social network profile image for the contact.

Empty if Social Accounts and Contacts isn't enabled or if Social Accounts and Contacts is
disabled for the requesting user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The contact’s personal pronouns, reflecting their gender identity. Others can use these
pronouns to refer to the contact in the third person. The entry is selected from a picklist of
available values, which the administrator sets. Maximum 40 characters.

Possible values are:

**•** `He/Him`

**•** `He/They`

**•** `Not Listed`

**•** `She/Her`

**•** `She/They`

**•** `They/Them`

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contact that this contact reports to.

This is a relationship field.


-----

```
Salutation
ScheduledResumeDateTime
Suffix
Title
TitleType

```

**Relationship Name**
ReportsTo

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Honorific abbreviation, word, or phrase to be used in front of name in greetings, such as Dr.
or Mrs.

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
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name suffix of the contact. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the contact, such as CEO or Vice President.

**Type**
picklist


-----

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
If Automatic Contact Enhancements or Buyer Relationship Map is enabled, this field contains
the hierarchical position that the contact holds in the organization. In the UI, this field is
shown as Seniority Level. Possible values are:

**•** `ceo—Key value`

**•** `directorOrManager—Key value`

**•** `executive—Key value`

**•** `individualContributor`

**•** `vp—VP or Head of Department. Key value.`

Key values represent key contacts on an opportunity or account. If a buyer relationship map
doesn’t show contacts with key values, then Salesforce prompts you to add them. Having
all key values represented on the map provides a complete picture of the deal or account,
increasing sales success. This field is available with all profiles except custom and
minimum-access. To provide access, use field-level security in Object Manager.

Note: If you’re importing contact data and need to set the value for an audit field, such as CreatedDate, contact Salesforce.
Audit fields are automatically updated during API operations unless you request to set these fields yourself.

##### Usage

Use this object to manage individual people who are associated with an account. You can create, query, delete, or update any attachment
associated with a contact.

Create or update contacts by converting a lead with the `convertLead()` call.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**AccountChangeEvent (API version 44.0)**
Change events are available for the object.

**ContactFeed (API version 18.0)**
Feed tracking is available for the object.

**ContactHistory (API version 11.0)**
History is available for tracked fields of the object.

**ContactOwnerSharingRule**

Sharing rules are available for the object.


-----

**ContactShare**

Sharing is available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields
