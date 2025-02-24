#### ContractStatus

Represents the status of a Contract, such as Draft, InApproval, Activated, Terminated, or Expired.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ApiName
IsDefault
MasterLabel

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
Indicates whether this is the default contract status value (true) or not (false) in the
picklist.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Label for this contract status value. This display value is the internal label that does not get
translated.


-----

```
 SortOrder
 StatusCode

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the contract status picklist. These numbers are not
guaranteed to be sequential, as some previous contract status values might have been
deleted.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Code indicating the status of a contract. One of the following values:

**•** `Draft`

**•** `InApproval`

**•** `Activated`

Two other values (Terminated and Expired) are defined but are not available for use
via the API.


This object represents a value in the contract status picklist. The contract status picklist provides additional information about the status
of a Contract, such as its current state (Draft, `InApproval, or` `Activated). You can query these records to retrieve the set of`
values in the contract status picklist, and then use that information while processing Contract objects to determine more information
about a given contract. For example, the application could test whether a given contract is activated based on its `Status` value and
the value of the `StatusCode` property in the associated ContractStatus object.

SEE ALSO:

ContractContactRole
