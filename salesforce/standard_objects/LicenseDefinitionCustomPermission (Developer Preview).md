#### LicenseDefinitionCustomPermission (Developer Preview)

Represents a licensed custom permission that controls access to a license's features when included in a custom permission set license
definition. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access LicenseDefinitionCustomPermission, you must have the Partner Licensing Platform developer preview enabled. To participate
[in this developer preview, submit a participation request via the Partner Licensing Platform Developer Preview Partner Community](https://partners.salesforce.com/_ui/core/chatter/groups/GroupProfilePage?g=0F94V0000010zlV)
group.


-----

Note: The Partner Licensing Platform is available as a developer preview. The Partner Licensing Platform isn’t generally available
unless or until Salesforce announces its general availability in documentation or in press releases or public statements. All commands,
parameters, and other features are subject to change or deprecation at any time, with or without notice. Don't implement
functionality developed with these commands or tools in your production package.

##### Fields

```
LicenseDefinitionId
LicensedCustomPermissionId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the custom permission set license definition that contains the licensed custom
permission.

This is a relationship field.

**Relationship Name**
LicenseDefinition

**Relationship Type**
Lookup

**Refers To**
PermissionSetLicenseDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the licensed custom permission that you're including in the permission set license
definition. On the CustomPermission object, the `isLicensed` field must equal true.

This is a relationship field.

**Relationship Name**
LicensedCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission


[For more information, see the Partner Licensing Platform Developer Guide (Developer Preview).](https://developer.salesforce.com/docs/atlas.en-us.254.0.plp_dev.meta/plp_dev/partner_licensing_platform_intro.htm)


-----
