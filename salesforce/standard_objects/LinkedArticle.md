#### LinkedArticle

```

**Description**
The name of the page from which the user switched from Lightning Experience
to Salesforce Classic.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records per user and page.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
UserId of the user who views page.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


Represents a knowledge article that is attached to a work order, work order line item, or work type. This object is available in API version
37.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
Knowledge must be enabled in your org. Field Service must be enabled. Only users that have access to the Knowledge article and the
parent record linked to it can access this object.


-----

In Knowledge in Salesforce Classic, only Field Service objects such as Work Order, Work Type, and Work Order Line Item are supported
for linked articles. In Lightning Knowledge, other social objects such as Chat, Messaging, Voice Call, and Social Post are supported for
linked articles.

To call update() to attach or detach articles, enable the Read user permission on the Knowledge object and the Edit user permission
on the object whose article you update. Available in API version 58.0 and later.

##### Fields

```
CurrencyIsoCode
KnowledgeArticleId
KnowledgeArticleVersionId
LinkedEntityId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the Knowledge article attached to the record. The label in the user
interface is Knowledge Article ID.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The version of the Knowledge article attached to the record. This field lists the
title of the attached version and links to the version. The label in the user interface
is Article Version.

When you attach an article to a work order, that version of the article stays
associated with the work order, even if later versions are published. If needed,
you can detach and reattach an article to a work order to link the latest version.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort


-----

```
Name
RecordTypeId
Type

##### Usage

```

**Description**
The ID of the record that the Knowledge article is attached to. The label in the
user interface is Linked Record ID.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The title of the article. The label in the user interface is Article Title.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the article’s record type, if used. This field is only available for Lightning
Knowledge.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of record that the Knowledge article is attached to. For
example, work order. The label in the user interface is Linked Object Type.


Admins can customize linked articles’ page layouts, fields, validation rules, and more from the Linked Articles page in Setup.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**LinkedArticleChangeEvent (API version 62.0)**
Change events are available for the object.

**LinkedArticleFeed**

Feed tracking is available for the object.

**LinkedArticleHistory**

History is available for tracked fields of the object.


-----
