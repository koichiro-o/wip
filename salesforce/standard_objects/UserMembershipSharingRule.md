#### UserMembershipSharingRule

Represents the rules for sharing user records from a source group to a target group. A user record contains details about a user. Users
who are members of the source group can be shared with members of the target group. The source and target groups can be based
on roles, portal roles, public groups, or territories. This object is available in API version 26.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update()

 Special Access Rules

```
As of Spring ’20 and later, only users with the View Setup and Configuration permission can access this object, and only users with the
Manage Sharing permission can edit this object.

##### Fields

```
Description
DeveloperName

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
A description of the sharing rule. Maximum size is 1000 characters. This field is available
in API version 29.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with a
letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming conflicts


-----

```
GroupId
Name
UserAccessLevel
UserOrGroupId

```

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

**Description**
Label of the sharing rule as it appears in the user interface. Limited to 80 characters.
Corresponds to Label on the user interface.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the type of sharing being allowed. The possible values are:

**•** `Read`

**•** `Edit`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID representing the target group being given access.


-----

##### Usage

Use this object to manage sharing rules for user records. Source and target groups can include internal users, portal users, Chatter or
Chatter External users.
