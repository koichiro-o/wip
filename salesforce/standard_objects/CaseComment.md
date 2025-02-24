#### CaseComment

Represents a comment that provides additional information about the associated Case.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CommentBody
ConnectionReceivedId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Text of the CaseComment. The maximum size of the comment body is 4,000 bytes. Label is
**Body.**

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
ConnectionSentId
CreatorFullPhotoUrl
CreatorName
CreatorSmallPhotoUrl
IsDeleted

```

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
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

URL of the user’s profile photo from the feed. Chatter Answers must be enabled to view this
field. This field is available in API version 26.0 and later.

**Type**
string

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
boolean


-----

```
IsNotificationSelected
IsPublished
ParentId

```

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Create, Defaulted on create, Update

**Description**
Indicates whether an email notification is sent to the case contact when a CaseComment is
created or updated. When this field is queried, it always returns null.

This field is available only when the Enable Case Comment Notification to
`Contacts` setting is enabled on the Support Settings page in Setup. To send email
notifications for CaseComment, you must use the EmailHeader triggerUserEmail.

Available in API version 43.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the CaseComment is visible to customers in the Self-Service portal (true)
or not (false). Label is Published. This is the only CaseComment field that can be updated
via the API.

**Type**
reference

**Properties**
Create, Filter, Group, Sort,

**Description**
Required. ID of the parent Case of the CaseComment.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Case


-----

Note: If you're importing CaseComment data and must set the value for an audit field, such as CreatedDate, contact Salesforce.
Record id's can't delete CaseComments entities when calling the Database.delete() Apex method or its analogous SOAP API. Audit
fields are automatically updated during API operations unless you request to set these fields yourself.

##### Usage

In the Salesforce user interface, comments are entered by a User working on a Case. All users have access to create and view CaseComment
in the Salesforce user interface and when using the API. In the API, CaseComment records can't be modified after insertion unless the
user has the “Modify All Records” object-level permission for Cases or the “Modify All Data” permission. If not, users can only update the
`IsPublished` field, and can't delete CaseComment.

SEE ALSO:

Overview of Salesforce Objects and Fields
