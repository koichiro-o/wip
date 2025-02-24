#### ApexTrigger

Represents an Apex trigger.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Fields

```
```
ApiVersion
Body

```
BodyCrc
```
IsValid
LengthWithoutComments

```

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
The API version for this trigger. Every trigger has an API version specified at creation.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Apex trigger definition.

Limit: 1 million characters.

**Type**
double

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The CRC (cyclic redundancy check) of the class or trigger file.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether any dependent metadata has changed since the trigger was last compiled
(true) or not (false).

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Name
NamespacePrefix
Status

```

**Description**
Length of the trigger without comments

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the trigger.

Limit: 255 characters

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
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The current status of the Apex trigger. The following string values are valid:

**•** `Active—The trigger is active.`

**•** `Inactive—The trigger is inactive, but not deleted.`

**•** `Deleted—The trigger is marked for deletion. This is useful for managed packages,`
because it allows a class to be deleted when a managed package is updated.


-----

```
TableEnumOrId
UsageAfterDelete
UsageAfterInsert
UsageAfterUndelete
UsageAfterUpdate
UsageBeforeDelete

```

Note: `Inactive` [is not valid for ApexClass. For more information, see the Metadata](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/)
_[API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/)_

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the object associated with the trigger, such as Account or Contact.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after delete` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after insert` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after undelete` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is an `after update` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update


-----

```
UsageBeforeInsert
UsageBeforeUpdate
UsageIsBulk

##### Usage

```

**Description**
Specifies whether the trigger is a `before delete` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before insert` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is a `before update` trigger (true) or not (false).

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Specifies whether the trigger is defined as a bulk trigger (true) or not (false).

Note: This field is not used for Apex triggers saved using Salesforce API version 10.0
or higher: all triggers starting with that version are automatically considered bulk, and
this field will always return `true.`


Although Apex classes and triggers have the Create and Update field properties, a runtime exception occurs if you try to create, update,
or delete them using the API. Instead, use the Salesforce Extensions for Visual Studio Code or the Ant Migration Tool to create or update
[Apex classes or triggers. Apex classes and triggers can’t be created, edited, or deleted in a production org. See Deploying Apex.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_deploying.htm)

SEE ALSO:

ApexClass

_[Developer Guide: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/)_
