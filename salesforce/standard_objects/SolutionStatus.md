#### SolutionStatus

Represents the status of a Solution, such as Draft, Reviewed, and so on.

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


-----

```
IsDefault
IsReviewed
MasterLabel
SortOrder

##### Usage

```

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default solution status value (true) or not (false) in the
picklist. Only one value can be the default value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this solution status value represents a reviewed Solution (true) or not
(false). Multiple solution status values can represent a reviewed Solution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this solution status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the solution status picklist. These numbers are not
guaranteed to be sequential, as some previous solution status values might have been
deleted.


This object represents a value in the solution status picklist. The solution status picklist provides additional information about the status
of a Solution, such as whether a given status value represents a reviewed or unreviewed solution. Your client application can query this


-----

object to retrieve the set of values in the solution status picklist, and then use that information while processing Solution objects to
determine more information about a given solution. For example, the application could test whether a given case has been reviewed
or not based on its `Status` value and the value of the `IsReviewed` property in the associated SolutionStatus record.

SEE ALSO:

Solution
