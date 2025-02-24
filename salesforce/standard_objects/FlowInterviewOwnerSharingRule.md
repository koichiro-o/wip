#### FlowInterviewOwnerSharingRule

Represents the rules for sharing a FlowInterview with users other than the owner. This object is available in API version 33.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
Description
DeveloperName
GroupId
Name

```

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit—In API version 42.0 and later, when Let users resume shared flow`
**interviews is enabled for your org, users can resume all flow interviews that they**
have edit access to.

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts
on package installations. With this field, a developer can change the object’s name
in a managed package and the changes are reflected in a subscriber’s organization.
Corresponds to Rule Name in the user interface.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is specified,
performance slows down while Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the source group.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
UserOrGroupId

##### Usage

```

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to Label on the user interface.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target user or group that’s given access.


Use this object to manage the sharing rules for FlowInterview records. General sharing uses this object.

In API version 42.0 and later, when Let users resume shared flow interviews is enabled for your org, users can resume all flow interviews
that they have edit access to. When that setting is disabled, only the owner or a flow admin can resume a flow interview. To disable this
setting, go to your org’s Process Automation Settings in Setup.
