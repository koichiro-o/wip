#### SecurityCustomBaseline

Provides the ability to read, create, and delete user-defined custom security baselines, which define an org’s security standards. This
object is available in API version 39.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
You must have the “View Health Check” permission to read a custom baseline, and the “Manage Health Check” permission to create,
edit, or delete one.

##### Fields

```
Baseline
DeveloperName

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

The definition of an org’s security settings standards.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
IsDefault
Language
MasterLabel
NamespacePrefix

```

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no DeveloperName is specified,
performance may slow while Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Sets the baseline as the default in Security Health Check.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the category node.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with the package.


-----
