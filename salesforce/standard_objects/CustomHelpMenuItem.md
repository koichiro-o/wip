#### CustomHelpMenuItem

Represents the items within a section of the Lightning Experience help menu that the admin added to display custom, org-specific help
resources. This object is available in API version 44.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Packaging Considerations

```
Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

##### Fields

```
LinkUrl

```

**Type**
url

**Properties**
Create, Filter, Sort, Update


-----

```
MasterLabel
ParentId
SortOrder

```

**Description**
Required. The URL for the resource. Specify up to 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The name of the resource. Specify up to 100 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the custom help section the item belongs to.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
CustomHelpMenuSection

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The order of the item within the custom section. Valid values are 1 through 15.

