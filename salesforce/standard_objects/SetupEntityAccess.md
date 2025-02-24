#### SetupEntityAccess

```
Represents the enabled setup entity access settings (such as for Apex classes) for the parent PermissionSet. This object is available in
API version 25.0 and later.

To grant users access to an entity, associate the appropriate SetupEntityAccess record with a PermissionSet that’s assigned to a user.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

As of Spring ’20 and later, only users with "View Setup and Configuration" permission can access this object.

##### Fields

```
ParentId
SetupEntityId
SetupEntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the entity for which access is enabled, such as an Apex class or
Visualforce page.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of setup entity for which access is enabled. Valid values are:

**•** `ApexClass` for Apex classes

**•** `ApexPage` for Visualforce pages

**•** In API version 28.0 and later, `ConnectedApplication` for OAuth
connected apps

**•** In API version 48.0 and later, `CustomEntityDefinition` for Custom
Settings and Custom Metadata Types

**•** In API version 31.0 and later, CustomPermission for custom permissions


-----

**•** In API version 60.0 and later, `ExternalClientApplication` for
external client apps.

**•** In API version 58.0 and later, `ExternalCredentialParameter` for
external credential principals.

**•** In API version 58.0 and later, `FlowDefinition` for flows

**•** In API version 58.0 and later, `OrgWideEmailAddress` for
organization-wide email addresses

**•** In API version 28.0 and later, `ServiceProvider` for service providers

**•** In API version 60.0 and later, `StandardInvocableActionType` for
standard invocable actions.

**•** In API version 28.0 and later, `TabSet for apps`

**•** In API version 62.0 and later, EmailRoutingAddress for email routing
addresses.

##### Usage

Because SetupEntityAccess is a child of the PermissionSet object, the usage is similar to other PermissionSet child objects like
FieldPermissions and ObjectPermissions.

For example, the following code returns all permission sets that grant access to any setup entities for which access is enabled:
```
SELECT Id, ParentId, Parent.Name, SetupEntityId
FROM SetupEntityAccess

```
The following code returns permission sets that grant access only to Apex classes:
```
SELECT Id, ParentId, Parent.Name, SetupEntityId
FROM SetupEntityAccess
WHERE SetupEntityType='ApexClass'

```
The following code returns permission sets that grant access to any setup entities, and are not owned by a profile:
```
SELECT Id, ParentId, Parent.Name, SetupEntityId
FROM SetupEntityAccess
WHERE ParentId
IN (SELECT Id
  FROM PermissionSet
  WHERE isOwnedByProfile = false)

```
You may want to return only those permission sets that have access to a specific setup entity. To do this, query the parent object. For
example, this code returns all permission sets that grant access to the `helloWorld` Apex class:
```
SELECT Id, Name,
  (SELECT Id, Parent.Name, Parent.Profile.Name
  FROM SetupEntityAccessItems)
FROM ApexClass
WHERE Name = 'helloWorld'

```
While it’s possible to return permission sets that have access to a ConnectedApplication, ServiceProvider, or TabSet
by `SetupEntityId, it’s not possible to return permission sets that have access to these` `SetupEntityType fields by any other`


-----

AppMenuItem attribute, such as `Name` or `Description. For example, to find out if a user has access to the Recruiting app, you’d`
run two queries. First, query to get the AppMenuItem ID:
```
SELECT Id, Name, Label
FROM AppMenuItem
WHERE Name = 'Recruiting'

```
Let’s say the previous query returned the AppMenuItem `ApplicationId 02uD0000000GIiMIAW. Using this ID, you can now run a`
query to find out if a user has access to the Recruiting app:
```
SELECT Id, SetupEntityId, SetupEntityType
FROM SetupEntityAccess
WHERE ParentId
IN
  (SELECT PermissionSetId
  FROM PermissionSetAssignment
  WHERE AssigneeId = '005D0000001QOzF')
AND (SetupEntityId = '02uD0000000GIiMIAW')

```
SEE ALSO:

PermissionSet

FieldPermissions

ObjectPermissions

ApexClass

ApexPage
