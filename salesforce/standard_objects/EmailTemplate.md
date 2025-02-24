#### EmailTemplate


This is a relationship field.

**Relationship Name**
Task

**Relationship Type**
Lookup

**Refers To**
Task

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of times the recipient opened the email.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The WhoId represents a human such as a lead or a contact. WhoIds are polymorphic.
Polymorphic means a WhoId is equivalent to a contact’s ID or a lead’s ID. The label is `Name`
```
  ID.

```
This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead


Represents a template for an email, mass email, list email, or Sales Engagement email. Supported in first-generation managed packages
only.

Note: You can’t send a mass email using a Visualforce email template.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.

##### Fields

```
ApiVersion
Body
BrandTemplateId
DeliveryRate

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The API version for this class. Every class has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Content of the email. Limit: 384 KB.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required. ID of the BrandTemplate associated with this email template. The brand template
supplies letterhead information for the email template.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**

Read-only. The percentage of the emails that were delivered compared to the number that
bounced (soft and hard). Note: this data includes emails that were delivered to the recipient's
spam folder.


-----

```
Description
DeveloperName
Encoding
EnhancedLetterheadId

```

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the template, for example, Promotion Mass Mailing.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is Template Unique Name.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Character set encoding for the template.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the enhanced letterhead associated with the email template.

Note: To use an enhanced letterhead, associate it with a Lightning email template
that uses the HML merge language.


-----

```
EntityType
FolderId
FolderName

```

This is a relationship field.

**Relationship Name**
EnhancedLetterhead

**Relationship Type**
Lookup

**Refers To**
EnhancedLetterhead

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort,

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
```
  EntityType indicates which entities this template can be used with (for example, account

```
or lead). Valid values are standard object ID prefixes: 001 for account, 003 for contact, 006
for opportunity, and 00Q for lead, 500 for case, and 701 for campaign.

This field has been removed in API version 39.0. Use `RelatedEntityType` instead.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the folder that contains the template.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, Organization, User

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The name of the folder that contains the template.


-----

```
HasSalesforceFiles
HtmlValue
IsActive
IsBuilderContent
LastUsedDate
Markup

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the email template has attachments from Salesforce Files. The default value is false.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
This field contains the content of the email message, including HTML coding to render the
email message. Limit: 384 KB.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates that this template is active if `true, or inactive if` `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If the email template was made in Email Template Builder. The default value is false.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when this email template was last used.

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

**Type**
textarea


-----

```
Name
NamespacePrefix
OwnerId

```

**Properties**
Create, Nillable, Update

**Description**
The Visualforce markup, HTML, JavaScript, or any other Web-enabled code that defines the
content of the template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the template. Label is Email Template Name.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

This field can’t be accessed unless the logged-in user has the Customize Application
permission.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the template.

This is a relationship field.


-----

```
RelatedEntityType
Subject
TemplateStyle

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
When `UIType` is `2` (Lightning Experience) or `3` (Lightning ExperienceSample),
`RelatedEntityType` indicates which entities this template can be used with. Valid
values are the entity API name: "Account" for account, "Contact" for contact, "Opportunity"
for opportunity, "Lead" for lead, and so on. The value can be any entity the user has read
access to (including custom entities) but not virtual entities, setup entities, or platform entities.

No restrictions exist at the schema level.

**Type**
string

**Properties**
Create, Nillable, Sort, Update

**Description**
Content of the subject line.

The limit is 1,000 characters for Lightning email templates and 230 characters for Classic
email templates.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Style of the template.

Possible values are:

**•** `formalLetter—Formal Letter`

**•** `freeForm—Free Form Letter`

**•** `newsletter—Newsletter`

**•** `none—No Email Layout`

**•** `products—Products`

**•** `promotionLeft—Promotion (Left)`


-----

```
TemplateType
TimesUsed
TotalDelivered
TotalHardBounced

```


**•** `promotionRight—Promotion (Right)`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Type of template.

Possible values are:

**•** `custom—Custom`

**•** `html—HTML`

**•** `text—Text`

**•** `visualforce—Visualforce`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of times this email template has been used.

Used with Salesforce Classic templates.

Not typically used with Lightning Experience templates.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of emails sent minus hard and soft bounces. Note: this data
includes emails that were delivered to the recipient's spam folder.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
TotalOpens
TotalSent
TotalSoftBounced

```

**Description**

Read-only. The total number of emails that permanently bounced back to the sender because
the address is invalid. A hard bounce can occur because the domain name doesn't exist or
because the recipient is unknown.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

Read-only. The total number of times a prospect’s email client loaded the images in the
HTML version of the email. We also record an open if the prospect clicks a link within the
HTML or text email without downloading images. A click indicates that they viewed the
message. Some email clients (Outlook, Apple Mail, Thunderbird) don’t display images by
default. Pardot counts an open each time the images load.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Read-only. The total number of emails sent, including bounced, opted-out, and invalid To:
addresses.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
UIType

##### Usage

```

**Description**

Read-only. The total number of times a recipient’s mail server acknowledged the email, but
returned it to the sender. Sometimes it is because the recipient's mailbox is full or the mail
server is temporarily unavailable. A soft bounce message can sometimes be delivered at
another time. After 5 soft bounces, Pardot opts the prospect out of emails.

This field is available in API version 46.0 and later. To access this field, your org must use Sales
Engagement and users need the Sales Engagement User or Sales Engagement Cadence
Creator permission set. This field value includes emails sent via the ListEmail object or Sales
Engagement cadences.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the user interface where this template is usable.

Possible values are:

**•** `Aloha`

**•** `SFX`

**•** `SFX_Sample—SFXSample`


To retrieve this object, issue a describe call on an object, which returns a query result for each activity since the object was created. You
can't query these records.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**EmailTemplateChangeEvent (API version 48.0)**
Change events are available for the object.

SEE ALSO:

Attachment

EmailStatus

DocumentAttachmentMap


-----
