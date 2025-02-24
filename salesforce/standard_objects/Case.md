#### Case

Represents a case, which is a customer issue or problem.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this case.

This is a relationship field.

**Relationship Name**
Account


-----

```
AssetWarrantyID
BusinessHoursId
Comments
CaseNumber
ClosedDate

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
ID of the Asset associated with the warranty. Must be a valid asset warranty ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the business hours associated with this case.

**Type**
textarea

**Properties**
Create, Delete, Layout, Nillable, Query, Retrieve, Search, Sort, Undelete, Update

**Description**
Used to insert a new CaseComment. Email textarea has a length of 4000 chars.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Assigned automatically when each case is inserted. It can't be set directly, and it can't be
modified after the case is created.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the case was closed.


-----

```
CommunityId
ConnectionReceivedId
ConnectionSentId
ContactEmail
ContactFax

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the zone associated with this case.

This field is available in API version 24.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**
Email address for the contact. The Case.ContactEmail field displays the Email field on the
contact on page 1340 that is referenced by Case.ContactId. Label is Contact Email. This
field is available in API version 38.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Fax number for the contact. Label is `Contact Fax. This field is available in API version`
38.0 and later.


-----

```
ContactId
ContactMobile
ContactPhone
CreatorFullPhotoUrl
CreatorName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Mobile telephone number for the contact. Label is Contact Mobile. This field is available
in API version 38.0 and later.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
Telephone number for the contact. Label is Contact Phone. This field is available in API
version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string


-----

```
CreatorSmallPhotoUrl
Description
FeedItemId
HasCommentsUnreadByOwner
HasSelfServiceComments

```

**Properties**
Filter, Group, Nillable, Sort

**Description**

Name of the user who posted the question or reply. Only the first name of internal users
(agents) appears to portal users in the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s thumbnail photo from the feed. Chatter Answers must be enabled to view
this field. This field is available in API version 26.0 and later.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A text description of the case. Limit: 32 KB.

**Type**
reference

**Properties**
Create, Group, Nillable, Sort

**Description**
ID of the question in Chatter associated with the case. This field is available in API version
33.0 and later, and is only accessible in organizations where Question-to-Case is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case contains comments that the case owner hasn’t read (true) or not
(false).

**Type**
boolean


-----

```
IsClosed
IsClosedOnCreate
IsDeleted
IsEscalated
IsSelfServiceClosed

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a case has comments added by a Self-Service user (true) or not (false).
Only visible when Customer Portal is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed (true) or open (false). This field is controlled by the
`Status` field; it can't be set directly. Label is Closed.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case was closed at the same time that it was created (true) or not
(false). This flag is read-only and is automatically set when a record is created. It can't be
set to `true` unless the `IsClosed` flag is also `true.`

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is `Deleted.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the case has been escalated (true) or not. A case's escalated state does
not affect how you can use a case, or whether you can query, delete, or update it. You can
set this flag via the API. Label is Escalated.

**Type**
boolean


-----

```
IsStopped
IsVisibleInSelfService
Language
LastReferencedDate
LastViewedDate

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case is closed for Self-Service users (true) or not (false).

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether an entitlement process on a case is stopped (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the case can be viewed in the Customer Service Portal, Partner Service
Portal, and Self-Service Portal (true) or not (false). This field is applied for case visibility
in the Partner Relationship Management, Customer Service Portal, and the earlier version of
Self Service Portal. The field does not alter sharing and will not prevent usage of a direct URL
to a case if a portal user has read or write access.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the case. The Language field is available when you enable Einstein Case
Classification in Enterprise, Performance, and Unlimited edition orgs with Service Cloud. By
default, only Einstein classification apps use this field.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime


-----

```
MasterRecordId
Origin
OwnerId

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
If this object was deleted as the result of a merge, this field contains the ID of the record that
was kept. If this object was deleted for any other reason, or has not been deleted, the value
is `null.`

This is a relationship field.

**Relationship Name**
MasterRecord

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable,Sort, Update

**Description**
The source of the case, such as `Email,` `Phone, or` `Web. Label is Case Origin.`

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the contact who owns the case.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup


-----

```
ParentId
Priority
QuestionId
Reason

```

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the parent case in the hierarchy. The label is Parent Case.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The importance or urgency of the case, such as `High,` `Medium, or` `Low.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The question in the answers zone that is associated with the case. This field does not appear
if you don't have an answers zone enabled.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The reason why the case was created, such as `Instructions not clear, or` `User`
```
  didn’t attend training.

```

-----

```
RecordTypeId
ServiceContractId
SlaStartDate
SourceId
Status
StopStartDate

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Required. ID of the ServiceContract associated with the entitlement. Must be a valid ID.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Shows the time that the case entered an entitlement process. If you have the Edit permission
on cases, you can update or reset the time.

This field is available in API version 18.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the social post source.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the case, such as New, Closed, or Escalated. This field directly controls the
`IsClosed` flag. Each predefined Status value implies an IsClosed flag value. For
more information, see CaseStatus.

**Type**
dateTime


-----

```
Subject
SuppliedCompany
SuppliedEmail
SuppliedName
SuppliedPhone

```

**Properties**
Filter, Nillable, Sort

**Description**
The date and time an entitlement process was stopped on the case.

This field is available in API version 18.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The subject of the case. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The company name that was entered when the case was created. Label is `Company.`

**Type**
email

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The email address that was entered when the case was created. Label is `Email.`

If your organization has an active auto-response rule, SuppliedEmail is required when
creating a case via the API. Auto-response rules use the email in the contact specified by
```
  ContactId. If no email address is in the contact record, the email specified here is used.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name that was entered when the case was created. Label is `Name.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Type

```

**Description**
The phone number that was entered when the case was created. Label is `Phone.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of case, such as `Feature Request` or `Question.`


Note: If you are importing Case data and need to set the value for an audit field, such as `CreatedDate, contact Salesforce.`
Audit fields are automatically updated during API operations unless you request to set these fields yourself.

##### Usage

Use the Case object to manage cases for your organization. Client applications can query, update, and delete Attachment records
associated with a case via the API.

##### Assignment Rules

When you query or update a case, your client application can have the case automatically assigned to one or more User records based
on assignment rules that have been configured in the user interface. To use this feature, your client application must set either of the
following options (but not both) in the AssignmentRuleHeader used in the create or update:

**Field** **Field Type** **Details**

`assignmentRuleId` reference ID of the assignment rule to use. Can be an inactive assignment
rule. If unspecified and `useDefaultRule` is true, then the

default assignment rule is used. To find the ID for a given
assignment rule, query the AssignmentRule object (specifying
```
                           RuleType="caseAssignment"), iterate through the

```
returned AssignmentRule objects, find the one you want to use,
retrieve its ID, and then specify its ID in this field in the
AssignmentRuleHeader.


`useDefaultRule` boolean


Specifies whether to use the default rule for rule-based assignment
(true) or not (false). The default rule is assigned by users in
the Salesforce user interface.


For a code example that shows setting the AssignmentRuleHeader for a Lead (which is similar to setting the AssignmentRuleHeader for
a Case), see Lead.


-----

##### Separating Accounts from Contacts in Cases

In releases before 8.0, the `AccountId` could not be specified, it was derived from the contact’s account. This behavior will continue
to be supported in future releases, but you can also now specify an AccountId. If you do not specify the AccountId during the
creation of a case, the value will default to the contact’s `AccountId.`

Note: When a record is updated, if the ContactId has not changed, then the AccountId is not regenerated. This prevents
the API from overwriting a value previously changed in the Salesforce user interface. However, if an API call changes the ContactId
and the `AccountId field is empty, then the` `AccountId` is generated using the contact’s account.

##### Using _case with Java

Depending on the development tool you use, you might need to write your application using _case instead of Case, because case
is a reserved word in Java.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CaseChangeEvent (API version 44.0)**
Change events are available for the object.

**CaseFeed (API version 18.0)**
Feed tracking is available for the object.

**CaseHistory**

History is available for tracked fields of the object.

**CaseOwnerSharingRule**

Sharing rules are available for the object.

**CaseShare**

Sharing is available for the object.

SEE ALSO:

Account

CaseMilestone
