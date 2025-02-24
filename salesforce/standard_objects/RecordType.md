#### RecordType

Represents a record type.


-----

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Fields

```
Important: Don’t use record types as an access control mechanism. Profile assignment governs create and edit access for an
object but doesn’t govern read access. For example, a user assigned to a profile that isn't enabled for a particular record type can't
create records with that record type, but can access records associated with that record type. Users with access to an object can
read all record type information for that object. We strongly recommend against storing sensitive information in the record type
description, name, or label. Instead, store sensitive information in a separate object or fields to which you’ve applied appropriate
access controls.

```
BusinessProcessId
Description
DeveloperName

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for Opportunity and Lead record types in API version 17.0 and later. ID of an
associated BusinessProcess.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of this record. Limit: 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a letter,
not include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is Record Type Name.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.


-----

```
IsActive
IsPersonType
Name
NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active (true) or not (false). Only active record types can
be applied to records. Label is Active.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this record has been designated as a person account (true) or not
(false). Visible only if the organization has the person account feature enabled.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Label of the record type in the user interface. Limit: 80 characters. Label is Record
**Type Label.**

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


-----

```
 SobjectType

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Object to which this record type applies, including custom objects.


Use this object to offer different BusinessProcess records and subsets of picklist values to different users based on their Profile. Your client
application can describe or query RecordType records.

Client applications can create or update values in `RecordTypeId` on these objects, specifying a valid record type ID associated with
these objects.

Note: You can’t create or update the `RecordTypeId` field on the CampaignMember records. Set the CampaignMember
record type using the `CampaignMemberRecordTypeId` field on Campaign.

A client application can retrieve the list of valid record type IDs for a given object by querying the RecordType.

SEE ALSO:

Record Type Objects
