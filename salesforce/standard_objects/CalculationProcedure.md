#### CalculationProcedure

Performs a series of calculations using matrix lookups and user-defined variables and constants. The label for this object is Expression
Set. This object is available in API version 53.0 and later.

Note: This object has been deprecated as of API version 55.0. In API version 55.0 and later, use the new Expression Set objects in
Business Rules Engine instead.

Expression Sets accept input variables and return output variables, both in JSON format. Expression Sets are especially useful for determining
prices, rates, and quotes.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Access to Expression Sets requires OmniStudio licenses.

##### Fields

```
Description
InputVariablesMetadata

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A text description of the Expression Set.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's input variables.


-----

```
LastReferencedDate
LastViewedDate
Name
OutputVariablesMetadata
OwnerId

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user only accessed this record or list view (LastReferencedDate) but
didn't view it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The Expression Set name.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Metadata for the Expression Set's output variables.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this Expression Set. Default value is the user logged
in to the API to perform the create action.

This is a polymorphic relationship field.

**Relationship Name**
Owner


-----

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Usage

OmniScripts and Integration Procedures can call Expression Sets. Expression Sets can call Decision Matrices.
