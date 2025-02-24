#### OpportunityFieldHistory

Represents the history of changes to the values in the fields of an opportunity. This object is available in versions 13.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


-----

##### Fields

**Field**
```
DataType
Field
IsDeleted
OpportunityId
 NewValue

```

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
The name of the field that was changed.

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
Filter, Group, Sort

**Description**
ID of the Opportunity. Label is Opportunity ID.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
anyType


-----

```
 OldValue

##### Usage

```

**Properties**
Nillable, Sort

**Description**
The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**
The latest value of the field before it was changed.


Use this object to identify changes to any fields on an Opportunity. The OpportunityHistory object represents the history of a change to
the `Amount,` `Probability,` `Stage, or` `Close Date` fields of an Opportunity.

This object respects field level security on the parent object.

SEE ALSO:

Opportunity
