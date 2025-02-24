#### NamespaceRegistry

Represents a namespace that you can link to scratch orgs that were created from your org’s Dev Hub. You use the namespace when
developing, packaging, and releasing an app. You can’t create this object with the API. Use the Link Namespace action in the Dev Hub
graphical interface to insert a `NamespaceRegistry` record. This object is available in API version 41.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update()

 Fields

```
```
Name
NamespaceOrg

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
The name of this namespace registry entry.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
NamespacePrefix

##### Associated Objects

```

**Description**
The org ID of the Developer Edition org where you've registered the namespace
you want to link.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The namespace prefix that you want to link to the scratch org.


This object has these associated objects. Unless noted, they’re available in the same API version as this object.

**NamespaceRegistryFeed**

Feed tracking is available for the object.

**NamespaceRegistryHistory**

History is available for tracked fields of the object.

SEE ALSO:

ActiveScratchOrg

ScratchOrgInfo
