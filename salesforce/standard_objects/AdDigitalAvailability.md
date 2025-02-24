#### AdDigitalAvailability

Table for Daily, Weekly, and Monthly view of offered, available, booked, and forecasted units for the Digital media type calendar view.
This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
AdAvailabilityDimensionsId
AdPlacementPriorityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Ad Availability Dimension that's associated with the digital availability.

This field is a relationship field.

**Relationship Name**
AdAvailabilityDimensions

**Relationship Type**
Lookup

**Refers To**
AdAvailabilityDimensions

**Type**
picklist


-----

```
CalendarPeriodType
CreativeSize
FromDate
Name

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of priority assigned to a digital advertisement slot.

Possible values are:

**•** `Sponsorship`

**•** `Standard`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The period that used to filter the unit count for a selected unit type.

Possible values are:

**•** `Continuous`

**•** `Daily`

**•** `Monthly`

**•** `Weekly`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The creative size of the digital advertisement slot.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the availability of the digital advertisement slot.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
OwnerId
ToDate
Units
UnitsStatus

```

**Description**
The name of ad digital availability.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the relationship record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the availability of the digital advertisement slot.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of units assigned for the digital advertisement slot.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the unit type for the digital advertisement slot.

Possible values are:

**•** `Available`

**•** `Booked`

**•** `Offered`


-----

**•** `Total`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdDigitalAvailabilityChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdDigitalAvailabilityFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdDigitalAvailabilityHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdDigitalAvailabilityOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdDigitalAvailabilityShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
