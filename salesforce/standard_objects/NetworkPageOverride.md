#### NetworkPageOverride

Represents information about custom pages used to override the default pages in Experience Cloud sites. You can create Experience
Builder or Visualforce pages and override the default pages in a site. Using custom pages allows you to create a more personalized
experience for your users. This object is available in API version 34.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** Only users with the Create and Setup Experiences permission can update this object.

**•** You can’t override the Change Password Page with a page created using Experience Builder. You can only override it with a Visualforce
page.

##### Fields

```
NetworkId
OverrideSetting

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Experience Cloud site where a custom page is used to override a
default page.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of the page used to override a default page in the Experience Cloud
site. OverrideSetting can take the following values:

**•** `Standard—The standard page that comes by default with the site.`

**•** `Configurable—The page created when the Configurable Self-Reg`
registration page type or the Login Discovery login page type is selected.

**•** `Designer—A custom page created using Experience Builder.`

**•** `Visualforce—A custom page created using Visualforce.`


-----

```
OverrideType
