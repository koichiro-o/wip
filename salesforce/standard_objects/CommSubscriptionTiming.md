#### CommSubscriptionTiming

Represents a customer's timing preferences for receiving a communication subscription. This object is available in API version 48.0 and
later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
CommSubscriptionConsentId
LastReferencedDate
LastViewedDate
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated communication subscription consent record.

This is a relationship field.

**Relationship Name**
CommSubscriptionConsent

**Relationship Type**
Lookup

**Refers To**
CommSubscriptionConsent

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
Offset
PreferredTimeEnd
PreferredTimeStart
PreferredTimeZone
Unit

```

**Description**
Required. Name of the communication subscription timing record.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The amount of time before or after an event or the specific day of the week to communicate
with the contact point. Set the unit of time in the `Unit` field.

For example, if you set Unit as Week and Offset as -4, communicate with the contact
point four weeks before the event. If you set Offset as 4, communicate with the contact
point four weeks after the event.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
End of the preferred time span in which to reach the customer.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Start of the preferred time span in which to reach the customer.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Time zone of the preferred time span.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of time that works with the Offset field to determine the communication timing.


-----

Possible values are:

**•** `Day`

**•** `DayOfWeek`

**•** `Hour`

**•** `Month`

**•** `Week`

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionTimingChangeEvent (API version 62.0)**
Change events are available for the object.

**CommSubscriptionTimingFeed**

Feed tracking is available for the object.

**CommSubscriptionTimingHistory**

History is available for tracked fields of the object.
