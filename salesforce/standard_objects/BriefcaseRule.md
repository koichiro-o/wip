#### BriefcaseRule

Represents a rule that specifies records for a briefcase definition. This object is available in API version 50.0 and later.

##### Special Access Rules

This object is read-only.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
BriefcaseId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is Briefcase Definition ID.

This field is a relationship field.

**Relationship Name**
Briefcase

**Relationship Type**
Lookup


-----

```
FilterLogic
IsAscendingOrder
OptionsIsRelatedFilesRule
OrderBy

```

**Refers To**
BriefcaseDefinition

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The filter logic for record selection, for example, 1 AND 2 where 1 and 2 correspond to
filter 1 and filter 2. Filter logic operators include `AND` and `OR. Limited to 255 characters.`
Label is Filter Logic.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Required. Indicates whether the records should be sorted in ascending order. Label is
**Ascending.**

**Type**
boolean

**Properties**
Filter

**Description**
Indicates whether the briefcase rule is part of a hierarchical set of rules that configure the
offline priming of file attachments. Available only for the Offline App (Salesforce Mobile App
Plus).

[Files Priming is a beta service that is subject to the Beta Services Terms at Agreements -](https://www.salesforce.com/company/legal/agreements/)
[Salesforce.com or a written Unified Pilot Agreement if executed by Customer, and applicable](https://www.salesforce.com/company/legal/agreements/)
[terms in the Product Terms Directory. Use of this beta service is at the Customer’s sole](https://ptd.salesforce.com/?_ga=2.247987783.1372150065.1709219475-629000709.1639001992)
discretion.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The field to order the records by, which determines how the records can be sorted. For
example, `AccountName` or `CreatedBy. Label is Order By.`


-----

```
ParentRuleId
QueryScope
RecordLimit
RelationshipField

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the parent rule of this briefcase rule. This field is a relationship field.

**Relationship Name**
ParentRule

**Relationship Type**
Lookup

**Refers To**
BriefcaseRule

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Required. A group of records to restrict the scope of this rule.

Possible values are:

**•** `assignedToMe`

**•** `everything`

**•** `mine`

The default value is `everything` (All Records). The value assignedToMe is available
only for the `ServiceAppointment` object.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record limit for the object. The recommended number for record limit is up to 500 records
per object for optimal performance. The maximum number is 2000. Label is Limit.

**Type**
picklist

**Properties**
Nillable, Restricted picklist


-----

```
RelationshipType
TargetEntity
