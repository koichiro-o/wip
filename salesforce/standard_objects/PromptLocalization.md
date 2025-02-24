#### PromptLocalization

```

**Description**
Indicates the access level of users for in-app guidance. Valid values are `Read,` `Edit, and`
```
  All.

```
**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited. Valid values
include:

**•** `Rule—The User or Group has access via a sharing rule.`

**•** `GuestRule—The User or Group has access via a guest user sharing rule.`

**•** `Manual—The User or Group has access because a User with “All” access manually`
shared the prompt action with them.

**•** `Owner—The User is the owner of the prompt action.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the User or Group.


Represents the translated value of a label for record details about in-app guidance when the Translation Workbench is enabled for your
org. Available in API version 48.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_wt_license.htm&language=en_US)

##### Prompts and Walkthroughs in Managed Packages

[For considerations about including in-app guidance in a managed package, see Guidelines for In-App Guidance in Managed Packages](https://help.salesforce.com/articleView?id=customhelp_iag_packages.htm&language=en_US)
in Salesforce Help.

[For more information about creating managed packages, see Create a First-Generation Managed Package.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/creating_packages.htm)

[Unmanaged packages must contain a namespace prefix. For more information, see Register a Namespace for a First-Generation Managed](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)
[Packages and What happens to my namespace prefix when I install a package?.](https://developer.salesforce.com/docs/atlas.en-us.pkg1_dev.meta/pkg1_dev/register_namespace_prefix.htm)

##### Fields

```
Language
NamespacePrefix

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates the language used in the org where the in-app guidance was created.

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


-----

```
ParentId
Value
