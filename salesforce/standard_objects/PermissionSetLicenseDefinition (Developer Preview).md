#### PermissionSetLicenseDefinition (Developer Preview)

Represents the definition of a custom permission set license, which entitles specified features in a package. This object is available in API
version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access PermissionSetLicenseDefinition, you must have the Partner Licensing Platform developer preview enabled. To participate in
[this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community group.](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)


-----

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

##### Fields

```
DeveloperName
IsSupplementLicense
Language
LicenseExpirationPolicy

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters and must be unique in your organization. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two consecutive
underscores. In managed packages, this field prevents naming conflicts on package
installations. With this field, a developer can change the object’s name in a managed package
and the changes are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the custom permission set license is a supplement license (true) or a
foundation license (false). The default value is false. This field is available in API version
55.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The two- to five-character code that represents the language and locale ISO. This code
controls the language for labels displayed in an application.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
MasterLabel
NamespacePrefix
UserLicenseRestrictions

```

**Description**
The license expiration policy of the custom permission set license.

Possible values are:

**•** `BlockNamespaceAccess—Package access is blocked for existing users when all`
custom permission set licenses expire. This is the default value.

**•** `AllowNamespaceAccess—Package access isn’t blocked for existing users when`
all custom permission set licenses expire.

This field is available in API version 55.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for this PermissionSetLicenseDefinition value. This display value is the internal label
that does not get translated.

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

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

**Description**
The user license categories that can be assigned the custom permission set license. If no
user license categories are specified, all users can be assigned the license. Possible values
include:

**•** `${communities}`

**•** `${communitiesLogin}`

**•** `${customerCommunities}`

**•** `${customerCommunitiesLogin}`

**•** `${internal}`

**•** `${partnerCommunity}`

**•** `${partnerCommunityLogin}`

**•** `${platform}`

[For more information, see User License Restriction Categories (Developer Preview). This field](https://developer.salesforce.com/docs/atlas.en-us.254.0.packagingGuide.meta/packagingGuide/partner_licensing_platform_restriction_categories.htm)
is available in API version 55.0 and later.

##### Usage

After the PermissionSetLicenseDefinition is created, it must be referenced in LicenseDefinitonCustomPermission.

[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.254.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)
