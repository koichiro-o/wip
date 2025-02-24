#### BusinessProcess

Represents a business process.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.

##### Fields

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
IsActive
Name
NamespacePrefix
TableEnumOrId

```

**Description**
Description of this business process. Limit: 255 characters.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this business process can be presented to users in the Salesforce user
interface (true) or not (false) when creating a new record type or changing the business
process of an existing record type.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of this business process. Limit: 80 characters.

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
Create, Filter, Group, Restricted picklist, Sort


-----

**Description**
Required. One of the following values: Case, Opportunity, or Solution. Label is Entity
**Enumeration Or ID.**

##### Usage

Use the BusinessProcess object to offer different subsets of picklist values to different users for the LeadStatus, CaseStatus, and
OpportunityStage fields. Similar to a RecordType, a BusinessProcess identifies the type of a row in a Case, Lead, or Opportunity and
implies a subset of picklist values for these three fields. The values for the remaining picklist fields are driven by RecordType.

SEE ALSO:

Overview of Salesforce Objects and Fields
