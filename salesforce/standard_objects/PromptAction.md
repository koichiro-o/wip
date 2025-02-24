#### PromptAction

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label. Maximum of 80 characters.

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

**•** In orgs that aren't Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


Represents how the user interacted with the in-app guidance prompt or walkthrough. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

```

-----

##### Special Access Rules

To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_wt_license.htm&language=en_US)

##### Fields

```
LastDisplayDate
LastResult
LastResultDate
Name

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last displayed to the user.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the last user interaction. Valid values are:

**•** `CustomAction`

**•** `Dismiss`

**•** `Error`

**•** `Finish—(walkthroughs only)`

**•** `NoAction`

**•** `NotSeen`

**•** `Snooze`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date the in-app guidance was last interacted with.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the in-app guidance.


-----

```
OwnerId
PromptVersionId
SnoozeUntil
StepCount

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the PromptVersion object.

This is a relationship field.

**Relationship Name**
PromptVersion

**Relationship Type**
Lookup

**Refers To**
PromptVersion

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The timestamp for when the user’s snooze request expires. The user won’t see the prompt
again until they navigate to the page after the snooze time expires.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
StepNumber
TimesActionTaken
TimesDismissed
TimesDisplayed
TimesSnoozed
UserId

```

**Description**
Indicates the total number of steps in the walkthrough. Available in API version 49.0 and
later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the number of the last step the user viewed or interacted with in a walkthrough.
Maximum value is 10. Available in API version 49.0 and later.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user took action on the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the user dismissed the in-app guidance.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of times that the in-app guidance was displayed to the user.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The total number of times the user snoozes the prompt.

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

##### Associated Objects

This object has the following associated objects. They are available in API version 46.0 and later.

**PromptActionOwnerSharingRule**

Sharing rules are available for the object.

**PromptActionShare**

Sharing is available for the object.
