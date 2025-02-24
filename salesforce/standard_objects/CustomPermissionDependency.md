#### CustomPermissionDependency

Represents the dependency between two custom permissions when one custom permission requires that you enable another custom
permission. This object is available in API version 32.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only users with View Setup and Configuration permission can access this object.


-----

##### Fields

**Field Name**
```
CustomPermissionId
RequiredCustomPermissionId

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that requires the permission that’s specified in
```
  RequiredCustomPermissionId.

```
This is a relationship field.

**Relationship Name**
CustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the custom permission that must be enabled when
`CustomPermissionId` is enabled.

This is a relationship field.

**Relationship Name**
RequiredCustomPermission

**Relationship Type**
Lookup

**Refers To**
CustomPermission


The following Apex class contains a method that returns the IDs of all custom permissions that are required for the given custom
permission ID. To use this class, save it in your organization.


-----

[For more information about using Apex classes, see the Apex Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_dev_guide.htm)

SEE ALSO:

CustomPermission
