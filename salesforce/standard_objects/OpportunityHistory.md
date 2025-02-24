#### OpportunityHistory

Represents the stage history of an opportunity.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Amount

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Estimated total sale amount.


-----

```
CloseDate
ExpectedRevenue
ForecastCategory
IsDeleted
OpportunityId

```

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Date when the opportunity is expected to close.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Calculated revenue based on the `Amount` and `Probability` fields.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Category that determines the column in which an opportunity is totaled in a forecast. Label
is To ForecastCategory.

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

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


-----

```
PrevAmount
PrevCloseDate
Probability
StageName

```

**Description**
ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The value in the opportunity’s Amount field before the update of the opportunity.

Note: In OpportunityHistory records created before Winter ’21, the value is null.

Available in API version 50.0 and later.

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value in the opportunity’s Close Date field before the update of the opportunity.

Note: In OpportunityHistory records created before Winter ’21, the value is null.

Available in API version 50.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
Percentage of estimated confidence in closing the opportunity.

**Type**
picklist

**Properties**
Filter, Group, Sort


-----

**Description**
Name of the current stage of the opportunity (for example, Prospect or Proposal).

##### Usage

This object represents the history of a change to the `Amount,` `Probability,` `Stage, or` `Close Date` fields of an Opportunity.
The OpportunityFieldHistory object represents the history of a change to any of the fields of an Opportunity. To obtain information about
how a particular opportunity is progressing, query the OpportunityHistory records associated with a given Opportunity. Please note that
if an opportunity's `Amount,` `Probability,` `Stage, or` `Close Date` fields have not changed, nothing will be returned in the
OpportunityHistory objects. In this case, query the OpportunityFieldHistory records associated with a given Opportunity to get more
information about changes to the opportunity.

This object is read-only. The system generates a new record whenever a user or client application changes the value of any of the above
fields; the then-current values of all of these major fields are saved in the newly-generated object.

This object respects field-level security on the parent object.

Note: The record is automatically deleted if its parent Opportunity is deleted.

SEE ALSO:

Opportunity
