#### LeadStatus

Represents the status of a Lead record, such as Open, Qualified, or Converted.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.


-----

```
IsConverted
IsDefault
MasterLabel
SortOrder

##### Usage

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this lead status value represents a converted lead (true) or not (false).
Multiple lead status values can represent a converted lead.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default lead status value (true) or not (false) in the picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this lead status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the lead status picklist. These numbers are not guaranteed
to be sequential, as some previous lead status values might have been deleted.


This object represents a value in the lead status picklist (see Lead on page 2891). The lead status picklist provides additional information
about the status of a Lead on page 2891, such as whether a given status value represents a converted Lead on page 2891. Query this object
to retrieve the set of values in the lead status picklist, and then use that information while processing Lead on page 2891 objects to


-----

determine more information about a given lead. For example, the application could test whether a given lead is converted based on its
Status value and the value of the `IsConverted` property in the associated LeadStatus record.

SEE ALSO:

LeadOwnerSharingRule

LeadShare
