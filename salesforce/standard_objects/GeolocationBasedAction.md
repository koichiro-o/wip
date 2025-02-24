#### GeolocationBasedAction

Represents a geolocation-based action, which is an action that’s triggered when a user enters, exits, or is within the area of the associated
object. Available in API version 61.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
ActionData
ActionType
Description
InitialTimeInvoked

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The details of the selected action type.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action.

Possible values are:

**•** `PlatformAlert`

**•** `QuickAction`

**•** `ViewRecord`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the action.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
LastReferencedDate
LastTimeInvoked
LastViewedDate
Name
OwnerId

```

**Description**
Captures the first time the mobile worker invoked this action.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the last time the mobile worker invoked this action.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDate isn’t null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the action.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of this object.

This field is a polymorphic relationship field.


-----

```
Radius
ReferenceRecordId
TriggerType

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The distance in meters from the location of the associated object that triggers the action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the record that the action is associated with.

This field is a relationship field.

**Relationship Name**
ReferenceRecord

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The event that triggered this action.

Possible values are:

**•** `GeoFenceEnter—Enter`

**•** `GeoFenceExit—Exit`


-----
