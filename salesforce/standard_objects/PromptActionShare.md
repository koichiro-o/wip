#### PromptActionShare

```

**Description**
Name of the in-app guidance.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user or group with whom `PromptAction` access is shared.


Represents a sharing entry on a prompt action record. Available in API version 46.0 and later.

Prompts and walkthroughs help users discover your products and services, adopt your processes, or learn how to use a new feature.
Add prompts and walkthroughs in Lightning Experience pages or apps or in supported Experience Cloud site pages. Add an optional
action button or link that goes to a URL. Track views, action button clicks, and walkthrough completions.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To add, edit, manage, and view prompts and walkthroughs in Lightning Experience or in Experience Cloud sites, multiple permissions
[are required. See Permissions for Creating and Accessing In-App Guidance in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.customhelp_lex_wt_license.htm&language=en_US)

##### Fields

```
AccessLevel

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
ParentId
RowCause
UserOrGroupId
