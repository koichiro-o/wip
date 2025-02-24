#### MatchingRuleItem

Represents criteria used by a matching rule to identify duplicate records. This object is available in API version 33.0 and later.

A matching rule item determines which field the matching rule uses to identify a duplicate record. It also determines the method used
to compare value that two records have for the field. For example, a matching rule item might specify that the Email field values of
two records must match exactly in order for the records to be considered duplicates.

When a matching rule has multiple matching rule items, it means that multiple fields must match in order for the records to be identified
as dupcliates.


-----

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
BlankValueBehavior
Field
MatchingMethod

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Specifies how blank fields affect whether the fields being compared are considered
matches. Valid values are:

**•** `MatchBlanks`

**•** `NullNotAllowed (default)`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates which field to compare when determining if a record is similar enough
to an existing record to be considered a match.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Defines how the fields are compared. Choose between the exact matching
method and various fuzzy matching methods. Valid values are:

**•** `Exact`

**•** `FirstName`

**•** `LastName`

**•** `CompanyName`

**•** `Phone`

**•** `City`


-----

```
MatchingRuleId
SortOrder

##### Usage

```


**•** `Street`

**•** `Zip`

**•** `Title`

For details on each matching method, see “Matching Methods Used with
Matching Rules” in the Salesforce Help.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID for the matching rule.

This is a relationship field.

**Relationship Name**
MatchingRule

**Relationship Type**
Lookup

**Refers To**
MatchingRule

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The order of the matching rule items for a matching rule.


Use the Salesforce SOAP API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API
to create, update, or delete these objects.

SEE ALSO:

MatchingRule

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_matchingrule.htm)


-----
