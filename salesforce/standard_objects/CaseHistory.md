#### CaseHistory

Represents historical information about changes that have been made to the associated Case.


-----

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)

##### Special Access Rules

This object is always read-only.

##### Fields

```
CaseId
DataType
Field

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the Case associated with this record.

This is a relationship field.

**Relationship Name**
Case

**Relationship Type**
Lookup

**Refers To**
Case

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was changed.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Name of the case field that was modified, or a special value to indicate some other
modification to the case. The possible values, in addition to the case field names, are:

**•** **ownerAssignment—The owner of the case was changed.**

**•** **ownerAccepted—A user took ownership of a case from a queue.**


-----

```
 IsDeleted
 NewValue
 OldValue

##### Usage

```


**•** **ownerEscalated—The owner of the case was changed due to case escalation.**

**•** **external—A user made the case visible to customers in the Customer Self-Service Portal.**

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
New value of the modified case field. Maximum of 255 characters.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
Previous value of the modified case field. Maximum of 255 characters.


Case history entries are indirectly created each time a case is modified.

Two rows are added to this record when foreign key fields change. One row contains the foreign key object names that display in the
online application. For example, `Jane Doe` is recorded as the name of a Contact. The other row contains the actual foreign key ID
that is only returned to and visible from the API.

This object respects field level security on the parent object.

SEE ALSO:

Overview of Salesforce Objects and Fields
