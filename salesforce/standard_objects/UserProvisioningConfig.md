#### UserProvisioningConfig

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The last name as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

The unique identifier for the user as stored in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username as stored in the target system for the associated user account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

The user ID of the owner of this object—typically a Salesforce administrator.


Represents information for a flow to use during a user provisioning request process, such as the attributes for an update. This object is
available in API version 34.0 and later.


-----

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ApprovalRequired
ConnectedAppId
DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Denotes whether approvals are required for provisioning users for the associated
connected app. If the value is null, no approval is required.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The 18-digit application ID for the connected app.

This is a relationship field.

**Relationship Name**
ConnectedApp

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the


-----

```
Enabled
EnabledOperations
Language
LastReconDateTime

```

object’s name in a managed package, and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether user provisioning is enabled for the associated connected app
(true) or not (false).

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the operations, as comma-separated values, that create a
UserProvisioningRequest object for the associated connected app. Allowed values
are:

**•** `Create`

**•** `Update`

**•** `EnableAndDisable` (activation and deactivation)

**•** `SuspendAndRestore` (freeze and unfreeze)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The two- to five-character code that represents the language and locale ISO. This
code controls the language for labels displayed in an application.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
MasterLabel
NamedCredentialId
NamespacePrefix

```

**Description**

The date and time when user accounts were last reconciled between Salesforce
and the target system.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The primary label for this object. This value is the internal label that doesn’t get
translated.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the named credential that’s used for a request. The named
credential identifies the third-party system and the third-party authentication
settings.

This is a relationship field.

**Relationship Name**
NamedCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the


-----

```
Notes
OnUpdateAttributes
ReconFilter
UserAccountMapping

```

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

A utility field for administrators to add any additional information about the
configuration. This field is for internal reference only, and is not used by any
process.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Lists the user attributes, as comma-separated values, that generate a
UserProvisioningRequest object during an update.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
When collecting and analyzing users on a third-party system, the plug-in uses
this filter to limit the scope of the collection.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Stores the attributes used to link the Salesforce user to the account on the
third-party system, in JSON format.

For example:


-----
