#### CaseStatus

Represents the status of a Case, such as New, On Hold, or In Process.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Fields

**Field**
```
ApiName
 IsClosed
 IsDefault
 MasterLabel
 SortOrder

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or primary label.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this case status value represents a closed Case (true) or not (false).
Multiple case status values can represent a closed Case.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this is the default case status value (true) or not (false) in the picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this case status value. This display value is the internal label that does not get
translated.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the case status picklist. These numbers are not guaranteed
to be sequential, as some previous case status values might have been deleted.


-----

##### Usage

This object represents a value in the case status picklist. The case status picklist provides additional information about the status of a
Case, such as whether a given `Status` value represents an open or closed case. Query the CaseStatus object to retrieve the set of
values in the case status picklist, and then use that information while processing Case records to determine more information about a
given case. For example, the application could test whether a given case is open or closed based on its `Status` value and the value
of the `IsClosed` property in the associated CaseStatus object.

SEE ALSO:

Overview of Salesforce Objects and Fields
