#### BriefcaseRuleFilter

```

**Description**
The Salesforce object field that relates the briefcase rule to another briefcase rule. For example,
an Account rule can be related to a Contact rule using the Account ID object field. In this
example, the value for the briefcase rule's `RelationshipField is` `AccountID.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The relationship of the briefcase rule to another briefcase rule. Possible values are:

**•** `ParentToChild`

**•** `ChildToParent`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The standard object, custom object, or custom metadata type that the briefcase rule selects
records from. The UI label is Target Object.


Represents a filter criteria for a briefcase rule. This object is available in API version 50.0 and later.

##### Special Access Rules

This object is read-only.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
BriefcaseRuleId

```

**Type**
reference


-----

```
FilterOperator
FilterSeqNumber
FilterValue
TargetEntityField

```

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase rule.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. The comparison operator for this rule filter.

Possible values are:

**•** `d—Ends with`

**•** `e— Equals`

**•** `g—Greater than`

**•** `h—Greater than or equal`

**•** `i—Like`

**•** `l—Less than`

**•** `m—Less than or equal`

**•** `s—Starts with`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Required. The filter number. When you apply multiple filters, the filters are numbered
sequentially, 1, 2, 3, and so on.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value for the field and criteria. For example, true or false for a boolean field whose
criteria or filter operator is Equals. Capitalization matters with date filter operators. Be sure
to specify date literals in uppercase. Some valid date literals include TODAY, YESTERDAY and
TOMORROW.

**Type**
picklist


-----

**Properties**
Restricted picklist

**Description**
Required. The field to filter by. Compound fields and encrypted fields aren’t supported. Label
is Field.
