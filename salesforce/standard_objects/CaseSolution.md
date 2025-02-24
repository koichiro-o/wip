#### CaseSolution

Represents the association between a Case and a Solution.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
CaseId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Case associated with the Solution.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case


-----

```
 IsDeleted
 SolutionId

##### Usage

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Solution associated with the case.

This is a relationship field.

**Relationship Name**
Solution

**Relationship Type**
Lookup

**Refers To**
Solution


You can't update this object via the API. If you attempt to create a record that matches an existing record, the request simply returns
the existing record.

SEE ALSO:

CaseShare

SolutionStatus
