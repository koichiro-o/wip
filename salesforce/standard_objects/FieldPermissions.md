#### FieldPermissions

```
Represents the enabled field permissions for the parent PermissionSet. This object is available in API version 24.0 and later.

To grant a user access to a field, associate a FieldPermissions record with a PermissionSet that’s assigned to a user. FieldPermissions
records are only supported in PermissionSet, not in Profile.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
In API version 49.0 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

In API version 50.0 and later, for lookup field inserts and queries, you can leave off the Id in the field name or include it. The rows returned
always use the API name. For example:
```
SELECT SobjectType, Field
FROM FieldPermissions
WHERE Field='Contact.Account'

```
and


-----

both return
```
Contact, Contact.AccountId

```
**Field Name**
```
Field
ParentId
PermissionsEdit
PermissionsRead

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The field’s API name. This name must be prefixed with the `SobjectType. For example,`
```
  Merchandise__c.Description__c

```
**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The `Id` of the field’s parent PermissionSet.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
PermissionSet

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, users assigned to the parent PermissionSet can edit this field. Requires`
`PermissionsRead` for the same field to be `true.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, users assigned to the parent PermissionSet can view this field. A FieldPermissions`
record must have at minimum `PermissionsRead set to` `true, or it will be deleted.`


-----

```
SobjectType

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object’s API name. For example, `Merchandise__c.`


FieldPermissions work similarly to ObjectPermissions. However, FieldPermissions includes a Field attribute to return the name of the
field.

For example, the following query returns all FieldPermissions records that have at least the “Read” permission. The results include the
field, object, and permission set names.
```
SELECT SobjectType, Field, PermissionsRead, Parent.Name
FROM FieldPermissions
WHERE PermissionsRead = True

```
Include the field’s parent object when querying FieldPermissions. For example, to find all rows that match the Account object’s `Type`
field, create the following query:
```
SELECT Id, SobjectType, Field
FROM FieldPermissions
WHERE Field = 'Account.Type' AND SobjectType = 'Account'

```
To find which permission sets are backed by profiles with the Account object, you can use a query like the following example:
```
SELECT Id, ParentId, SobjectType, Field, PermissionsEdit, PermissionsRead, Parent.Name
FROM FieldPermissions
WHERE SobjectType = 'Account' and Parent.IsOwnedByProfile = true
ORDER BY SObjectType, Field

```
Both `SobjectType` and `Field` must be included in the `SELECT` line of the query. Provide the full API name of the field in the
form of `SobjectType.Field when querying for a field.`

Note: When using the FieldPermission object to download records, depending on the SOQL query you use, you might not receive
all expected records. Results can also appear incomplete. However, all records do download; fields that don't support field security
and rows for entities not visible to the org are hidden.

##### Special Properties for Field Permissions

The auto-number and formula fields have special rules for how field permissions work. Both have FieldPermissions records, but inserting
and updating is limited to `PermissionsRead.` `PermissionsEdit` isn’t allowed for either field type, since these fields must be
read-only for users.

The following field types don’t return a FieldPermissions record because they are assumed to always be readable.

**•** `Id`

**•** `CreatedById`


-----

**•** `CreatedDate`

**•** `IsDeleted`

**•** `LastModifiedById`

**•** `LastModifiedDate`

**•** `SystemModStamp`

The following field types don’t return a FieldPermissions record because they are assumed to always be readable and writable.

**•** `OwnerId`

**•** Master-detail custom (relationship) fields

**•** Universally required custom fields

As a result, the following query returns no records, even though users do have some access to some of the fields.
```
SELECT Field, SobjectType, PermissionsRead
FROM FieldPermissions
WHERE Field='Id'

```
To determine if a field can return a FieldPermissions record, you can call a `describeSObject()` on the field. For example,
```
describeSObject('Merchandise__c'), returns all the properties of the Merchandise custom object, including field properties.

```
If you use a field whose `permissionable` property is `false` (like the field types listed in this section), you can’t query, insert,
update, or delete field permissions records, because they don’t exist.

If the View All Fields object permission is enabled for an object in the permission set, the `PermissionsRead` field equals `true`
for all queried fields for that object.

##### Working with Custom Activity Fields

While tasks and events are considered separate objects, they share a common set of activity custom fields. As a result, when a custom
task field is created, a custom event field is also created, and vice versa. You can display the custom field on the event layout, task layout,
or both event and task layouts.

Although custom activity fields are shared between tasks and events, you see separate FieldPermissions records for the task and event.
However, changes made to one field permission record are automatically made to the other. For example, if you create a custom activity
field, assign field permissions to it in a permission set, and run the following query, the query returns two records with the same permission
value.
```
SELECT Field, Id, ParentId, PermissionsEdit, PermissionsRead, SobjectType
FROM FieldPermissions
WHERE SobjectType = 'event' OR SobjectType ='task'

```
If you then update one of the records with another set of field permission values and run the query, the same permission values for both
records are returned.

##### Nesting Field Permissions

You can nest FieldPermissions in a PermissionSet query. For example, the following returns any permission sets where “Edit Read Only
Fields” is `true. Also, the result set includes both the “Read” and “Edit” field permission on the Merchandise object. Get similar results`
by nesting the SOQL with a field permission query using the relationship name for field permissions: `FieldPerms.`


-----

As a result, it’s possible to traverse the relationship between the PermissionSet and any child-related objects (in this case, FieldPermissions).
You can do this from the PermissionSet object by using the child relationship (ObjectPerms, `FieldPerms, and so on) or from`
the child object by referencing the PermissionSet with `Parent.permission_set_attribute.`

It’s important to consider when to use a conditional `WHERE` statement to restrict the result set. To query based on an attribute on the
permission set object, nest the SOQL with the child relationship. However, to query based on an attribute on the child object, you must
reference the permission set parent attribute in your query.

The following two queries return the same columns with different results, based on whether you use the child relationship or parent
notation.
```
SELECT PermissionsEditReadonlyFields,
(SELECT SobjectType, Field, PermissionsRead, PermissionsEdit
FROM FieldPerms
WHERE SobjectType = 'Merchandise__c')
FROM PermissionSet
WHERE PermissionsEditReadonlyFields = true

```
Versus:
```
SELECT SobjectType, Field, PermissionsRead, PermissionsEdit, Parent.Name,
  Parent.PermissionsEditReadonlyFields
FROM FieldPermissions
WHERE SObjectType='Merchandise__c'

##### Muting Permissions

```
Field permissions with a parent muting permission set act differently than those enabled in a regular permission set. For a regular
permission set, if a FieldPermissions record grants full access to a field (for example, granting read and edit access), users have full access
to that field.

With muting permission sets, a FieldPermissions record defines the muting of access. So if a muting permission set is set for read and
edit, the read and edit access is muted.

For example, we have a permission set and a muting permission set that controls access to the Account object’s fields. Each permission
set has settings for the Website field.

Regular Permission Set

**Field** **PermissionsRead** **PermissionsEdit** **Result**

Account.Website `true` `false` The Account.Website field is
read only.

Account.Website `true` `true` The Account.Website field has
both read and edit permissions.

Muting Permission Set


-----

Account.Website `false` `true`

Account.Website `true` `true`


Edit permissions on the
Account.Website fields are
muted.

Read and edit permissions on
the Account.Website field are
muted.


Field permissions are aggregated by combining the permissions granted by the permission set and the permissions muted by the muting
permission set. For example, if you have a permission set that grants read and edit permissions for a field, and a muting permission that
mutes the same field’s edit permission, the result is that only the read permission is enabled.

SEE ALSO:

PermissionSet

ObjectPermissions
