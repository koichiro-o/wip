#### ActionLinkGroupTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking on an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external
server or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. Every action link belongs to an action
link group and action links within the group are mutually exclusive. This object is available in API version 33.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Only users with the “Customize Application” permission can modify or delete this object.

##### Fields

```
Category
DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The location of the action link group within the feed element. Values are:

**•** `Primary—The action link group is displayed in the body of the feed`
element.

**•** `Overflow—The action link group is displayed in the overflow menu of`
the feed element.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
ExecutionsAllowed
HoursUntilExpiration
IsPublished
Language

```

**Description**
The name of the action link group template to use in code.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The number of times an action link can be executed. Values are:

**•** `Once—An action link can be executed only once across all users.`

**•** `OncePerUser—An action link can be executed only once for each user.`

**•** `Unlimited—An action link can be executed an unlimited number of`
times by each user. If the action link’s actionType is Api or ApiAsync,
you can’t use this value.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The number of hours from when the action link group is created until it's removed
from associated feed elements and can no longer be executed. The maximum
value is 8,760.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If true, the action link group template is published. Action link group templates
shouldn’t be published until at least one ActionLinkTemplate is associated with
it. Once set to `true, this can’t be set back to` `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the MasterLabel.


-----

```
MasterLabel
NamespacePrefix

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.


Define action link templates in Setup and use ConnectApi in Apex or Connect REST API to instantiate action links from the templates
and to post feed elements with the action links.

If you delete a published action link group template, you delete all related action link information which includes deleting all action links
that were instantiated using the template from feed items.
