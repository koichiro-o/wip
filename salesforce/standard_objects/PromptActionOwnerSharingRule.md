#### PromptActionOwnerSharingRule

Represents a rule which determines `PromptAction` sharing access for the owners. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_wt_license.htm&language=en_US)


-----

##### Fields

**Field**
```
AccessLevel
Description
DeveloperName
GroupId
Name

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates the access level of users for in-app guidance. Valid values are `Read` and `Edit.`

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the in-app guidance. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the group whose `PromptAction` are shared.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
UserOrGroupID
