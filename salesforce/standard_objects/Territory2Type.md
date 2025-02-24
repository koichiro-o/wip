#### Territory2Type

Represents a category for territories (Territory2). Every Territory2 must have a Territory2Type. Available only if Sales Territories has been
enabled for your organization.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Standard and partner users can access this object.

##### Fields

```
Description
DeveloperName
Language

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The description of the territory type.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your
organization. It must begin with a letter, not include spaces, not end with an
underscore, and not contain two consecutive underscores. The field label in the
user interface is `Territory Type Name.`

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist


-----

```
MasterLabel
Priority

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the label in the user interface.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required The user interface label for the territory type.

**Type**
int

**Properties**
Create, Filter, Group, SortUpdate

**Description**
Required. Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring
’15 / API version 33). Lets you specify a priority for a territory type. For opportunity
assignments, the filter examines all territories assigned to the account that the
opportunity is assigned to. The account-assigned territory whose territory type
priority is highest is then assigned to the opportunity. The `priority` field
value on each territory type must be unique. Further, if there are multiple territories
with the same territory type (and therefore the same priority) assigned to the
account, no territory is assigned to the opportunity.

