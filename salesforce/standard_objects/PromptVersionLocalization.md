#### PromptVersionLocalization

Represents the translated value of a label for-app guidance when the Translation Workbench is enabled for your org. Available in API
version 48.0 and later.

Use prompts and walkthroughs to display announcements, training, or news to users within the app. Choose to add an action button
or link that links to a URL of your choice. Track views, action button clicks, and walkthrough completions.

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


-----

```
ParentId
Value
