#### OpportunityCompetitor

Represents a competitor on an Opportunity.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Fields

```
```
CompetitorName
IsDeleted
OpportunityId
Strengths

```

**Type**
combobox

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Name of the competitor.

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
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
 Weaknesses

##### Usage

```

**Description**
Description of the competitor’s strengths. Limit: 1,000 characters.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the competitor’s weaknesses. Limit: 1,000 characters.


Use this object to manage competitors on an Opportunity, associating multiple competitors on a opportunity and specifying the strengths
and weaknesses of each competitor.

SEE ALSO:

Opportunity
