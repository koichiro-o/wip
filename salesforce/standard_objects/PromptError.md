#### PromptError

Represents the error or warning associated with the PromptAction. Available in API version 52.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_wt_license.htm&language=en_US)


-----

##### Fields

**Field**
```
IsError
Name
OwnerId
PromptActionId
StepNumber
Type

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the in-app guidance had an error true or a warning false. The default is
```
  false.

```
**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the PromptError record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User or Group.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptAction that the PromptError is related to.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the step number that the user encountered an error or warning in a walkthrough.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

**Description**
Indicates the type of error or warning. Possible values are:

**•** `NoAccessToApp—A step on this walkthrough is on an app that some of your users`
don’t have access to.

**•** `NoAccessToPage—A step on the walkthrough is on a page that some of your users`
don’t have access to.

**•** `ReferenceElementNotFound—The target element has moved or is no longer`
on your page. Targeted prompts attached to unavailable elements convert to floating
prompts. Check your access to the element, or enter targeting mode and reassign the
targeted prompt.

**•** `Unavailable—Users tried to open this walkthrough using its URL, but it's inactive`
or the users aren’t licensed to see it. To make it accessible to users, check its settings or
activate it.

##### Associated Objects

This object has the following associated objects. They are available in API version 52.0 and later.

**PromptErrorOwnerSharingRule**

Sharing rules are available for the object.

**PromptErrorShare**

Sharing is available for the object.
