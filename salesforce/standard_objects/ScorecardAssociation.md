#### ScorecardAssociation

Represents a connection between a specific scorecard and the associated account, channel program, or channel program level. This
object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
undelete(), update(), upsert()

 Fields

```
```
LastReferencedDate
LastViewedDate
Name

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
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
ScorecardId
TargetEntityId
