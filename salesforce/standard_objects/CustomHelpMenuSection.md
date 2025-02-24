#### CustomHelpMenuSection

Represents a section of the Lightning Experience help menu that the admin added to display custom, org-specific help resources. This
object is available in API version 44.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Packaging Considerations

Although you can package custom Help Menu section information, the section won't appear in the Help Menu Setup page or the Help
Menu user interface of orgs where the package is installed. Instead, customers must view the data in the CustomHelpMenuItem and
CustomHelpMenuSection objects and then manually add resources on the Help Menu Setup page.

##### Fields

```
DeveloperName
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the custom help section in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. The label corresponds to section title in the user interface. Limit:
80 characters.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required. Language of the label. Possible values are:

**•** da (Danish)

**•** de (German)

**•** en_US (English)

**•** es (Spanish)

**•** es_MX (Spanish (Mexico))

**•** fi (Finnish)

**•** fr (French)

**•** it (Italian)

**•** ja (Japanese)

**•** ko (Korean)

**•** nl_NL (Dutch)


-----

```
MasterLabel
NamespacePrefix
