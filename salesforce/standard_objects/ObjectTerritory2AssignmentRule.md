#### ObjectTerritory2AssignmentRule

Represents a territory assignment rule that’s associated with an object, such as Account. ObjectTerritory2AssignmentRuleItem can be
created or deleted if the BooleanFilter field on its corresponding ObjectTerritory2AssignmentRule is `null. Available if Sales Territories`
has been enabled.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories, assignment rules, assigned records, and assigned users. Users cannot view territory models in other states (such as Planning
or `Archived).`


-----

##### Fields

**Field Name**
```
BooleanFilter
DeveloperName
IsActive
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents advanced filter conditions that were specified for the rule in the online
application. For example, “(1 AND 2) OR 3.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Unique Name.`

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the rule is active (true) or inactive (false). Via the API, active
rules run automatically when object records are created and edited. The exception
is when the value of the IsExcludedFromRealign field on an object record is true,
which prevents record assignment rules from evaluating that record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
MasterLabel
ObjectType
Territory2ModelId

```

**Description**
The language of the label in the user interface.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The user interface label for the territory type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The object that the rule is defined for. For API version 31, Account only.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the territory model.

