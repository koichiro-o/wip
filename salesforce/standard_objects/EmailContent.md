#### EmailContent

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the electronic media.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of implementor. Available implementors of ElectronicMediaUse include:

**•** ProductMedia

**•** ProductCategoryMedia

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The order that electronic media is displayed in.


Represents a marketing email asset for use with Account Engagement. This object is available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
EmailContent is only available for orgs that use Account Engagement. The Manage Email Content user permission is required. Users also
need the CRM User, Sales, or Service User permission set. EmailContent isn’t available for custom portal or guest users.


-----

##### Fields

**Field**
```
ClickThroughRate
ClickToOpenRatio
DeliveryRate
Description
HtmlBody
LastReferencedDate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of visitors who click links contained in emails delivered (sent minus bounces)
to them. Multiple clicks for a same link are counted.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The number of unique clicks divided by unique HTML opens.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of the emails that were delivered compared to the number that bounced
(soft and hard). Note: this data includes emails that were delivered to the recipient's spam
folder.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the email content, for example, Promotion Mass Mailing.

**Type**
textarea

**Properties**
Nillable

**Description**
The body of the email in HTML format. The field is read-only.

**Type**
dateTime


-----

```
LastViewedDate
Name
OpenRate
OptOutRate
SpamComplaintRate

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp that indicates when the current user last viewed the record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, the
record could have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the email asset.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique HTML opens compared to the total number of emails delivered
(sent minus bounces).

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of users that have opted out compared to the total number of emails sent.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of spam complaints compared to the total number emails sent.


-----

```
Subject
TemplateId
TextBody
TotalDelivered
TotalHardBounced
TotalOpens

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Update

**Description**
Content of the subject line.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Email Template field is mostly read-only. You can populate the Email Template field only
during record create to prevent overwriting data on the email content record.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The body of the email in plain text format. The character limit is 384, 000.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of emails minus hard and soft bounces. Note: this data includes emails
that were delivered to the recipient's spam folder.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of emails that permanently returned to the sender because the address is
invalid. A hard bounce can occur because the domain name doesn't exist or because the
recipient is unknown.

**Type**
int


-----

```
TotalSent
TotalSoftBounced
TotalSpamComplaints
TotalTrackedLinkClicks
UniqueClickThroughRate

```

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The total number of times a prospect’s email client loaded the images in the HTML version
of the email. We also record an open if the prospect clicks a link within the HTML or text
email without downloading images. A click indicates that they viewed the message. Some
email clients (Outlook, Apple Mail, Thunderbird) do not display images by default. Account
Engagement counts an open each time the images load.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of list emails sent, including bounced, opted-out, and
invalid To: addresses.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of times a recipient’s mail server acknowledged the email,
but returned it to the sender. Sometimes it is because the recipient's mailbox is full or the
mail server is temporarily unavailable. After 5 soft bounces, Account Engagement opts the
prospect out of emails.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that reported the email as spam.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times prospects clicked a link in the email.

**Type**
percent


-----

```
UniqueOpens
UniqueOptOuts
UniqueTrackedLinkClicks
