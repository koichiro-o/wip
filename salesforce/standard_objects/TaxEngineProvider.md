#### TaxEngineProvider

```

**Description**
The ID of the tax engine used in the tax calculation process.

This field is a relationship field.

**Relationship Name**
TaxEngine

**Relationship Type**
Lookup

**Refers To**
TaxEngine

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
A system-generated number for a log entry.


Represents general information about a service that manages a tax engine, such as the ID of the tax adapter Apex class in Salesforce,
and the engine’s namespace prefix. Tax engine providers have a one-to-many relationship with tax engines, where the tax engine record
represents a specific configuration of a tax engine that can be assigned to multiple order items. This object is available in API version
55.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management is enabled in your org.

##### Fields

```
ApexAdapterId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Description
DeveloperName
Language
MasterLabel

```

**Description**
The Id of the Apex adapter used by this tax provider. This field is unique within your
organization.

This field is a relationship field.

**Relationship Name**
ApexAdapter

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used by this tax engine provider. Values appear based on their language codes
in Salesforce, such as `da` for Danish or `th` for Thai.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label used for the tax engine’s API in Salesforce.


-----

```
NamespacePrefix
