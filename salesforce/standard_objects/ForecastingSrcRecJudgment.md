#### ForecastingSrcRecJudgment

Represents forecast managers’ judgment of whether they consider an opportunity-related deal to be certain to close. This object is
available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Fields

```
```
CurrencyIsoCode
JudgmentOwnerId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**

The currency code of the judgment. If omitted, the default is USD.

**Type**
reference


-----

```
JudgmentValue
ReferenceObjectId
Territory2Id

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast manager.

This field is a relationship field.

**Relationship Name**
JudgmentOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Whether the deal is likely to close (IN) or not (OUT).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the opportunity-related object.

This field is a polymorphic relationship field.

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the territory that the judgment is on.

This field is a polymorphic relationship field.


-----

**Relationship Name**
ReferenceObject

**Relationship Type**
Lookup

**Refers To**
Territory2
