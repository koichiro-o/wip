#### MatchingRule

Represents a matching rule that is used to identify duplicate records. This object is available in API version 33.0 and later.


-----

A matching rule compares field values to determine whether a record is similar enough to existing records to be considered a duplicate.
For example, a matching rule can specify that if the `Email` and `Phone` values of two records match exactly, the records are possible
duplicates. Your organization uses matching rules with duplicate rules to define what happens when duplicates are identified.

If the rule is for a Person Account, `SobjectSubType` is automatically set to `PersonAccount.`

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only users with the View Setup and Configuration permission can access this object.

##### Fields

```
BooleanFilter
Description
DeveloperName
Language

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Specifies filter logic conditions.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the matching rule.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name for the matching rule.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist


-----

```
MasterLabel
MatchEngine
NamespacePrefix
RuleStatus

```

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language selected for your organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the matching rule.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The match engine used by the matching rule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for matching rules for your organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Required. The activation status of the matching rule. Values are:

**•** `Inactive`

**•** `Deactivating`

**•** `DeactivationFailed`

**•** `Active`

**•** `Activating`

**•** `ActivationFailed`

Important: The only valid values you can declare when deploying a
package are Active and `Inactive.`


-----

```
SobjectSubtype
SobjectType

##### Usage

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Read-only. Indicates if the matching rule is defined for the Person subtype of
```
  Account. Valid values are:

```
**•** `PersonAccount`

**•** `None`

If the rule is for a Person Account, SobjectSubType is automatically set to
```
PersonAccount.

```
**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The object for the matching rule.


Use the Salesforce API to retrieve and view details about MatchingRule and MatchingRuleItem. Use the Salesforce Metadata API to create,
update, or delete these objects.

SEE ALSO:

MatchingRuleItem

DuplicateRule

[MatchingRule in the Salesforce Metadata API Developer's Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_matchingrule.htm)
