#### WebStoreMessageContent

Represents the assocation of a managed content message record in CMS to a web store, along with other attributes that specify the
application and intent of the message content. This object is available in API version 61.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```
Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Special Access Rules

This object is available only if a B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
IsActive
ManagedContentId
MessageApp

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this message content is active (true) or not (false).

The default value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the managed content in CMS.

This field is a relationship field.

**Relationship Name**
ManagedContent

**Refers To**
ManagedContent

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The application type that uses the message content.

Possible values are:

**•** `Email`


-----

```
MessageUsage
Name
WebStoreId
