#### BriefcaseDefinition

Represents a briefcase definition. A briefcase makes selected records available for users to view when they’re offline in the Salesforce
Field Service mobile app for iOS and Android. This object is available in API version 50.0 and later.

##### Special Access Rules

This object is read-only.

Briefcase objects are available in orgs that have Briefcase Builder and Field Service enabled.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Packaging Considerations

```
An org can have up to 5 briefcases. Installed briefcases are counted against this limit. You can’t install a package that includes a briefcase
if your org already has 5 briefcases. When a managed package includes a briefcase, the only changes allowed for the briefcase are
activating or deactivating and assigning users or groups to the briefcase.

##### Fields

```
Description

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort


-----

```
DeveloperName
IsActive
Language

```

**Description**
Description of the briefcase definition. Limited to 1024 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Limited to 80 characters. Label is Name.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the briefcase is available for use (true) or not (false). Label is Active.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language for the briefcase. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned.

Possible values are:

**•** Chinese (Simplified): `zh_CN`

**•** Chinese (Traditional): `zh_TW`

**•** Danish: `da`

**•** Dutch: `nl_NL`

**•** English: `en_US`

**•** Finnish: `fi`

**•** French: `fr`

**•** German: `de`

**•** Italian: `it`


-----

```
MasterLabel
NamespacePrefix

```


**•** Japanese: `ja`

**•** Korean: `ko`

**•** Norwegian: `no`

**•** Portuguese (Brazil): `pt_BR`

**•** Russian: `ru`

**•** Spanish: `es`

**•** Spanish (Mexico): `es_MX` Spanish (Mexico) defaults to Spanish for customer-defined
translations.

**•** Swedish: `sv`

**•** Thai: `th The Salesforce user interface is fully translated to Thai, but Help is in English.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The master label for the briefcase. This internal label doesn’t get translated. Limited to 80
characters.

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

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


-----

##### Usage

Use this object to query a briefcase or a list of briefcases with selected records and user assignments. For example:
```
SELECT Id, Description FROM BriefcaseDefinition
WHERE Id in (SELECT BriefcaseId FROM BriefcaseRule
WHERE TargetEntity='Account')
AND Id in (SELECT BriefcaseId FROM BriefcaseAssignment where
UserOrGroupId='00GR0000000VtwUMAS')

##### Associated Objects

```
This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseDefinitionChangeEvent (API version 55.0)**
Change events are available for the object.
