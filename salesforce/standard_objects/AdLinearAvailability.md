#### AdLinearAvailability

Table for Daily, Weekly, and Monthly view of offered, available, booked, and forecasted units for the Linear media type calendar view.
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

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Ad Availability Dimension that's associated with the linear availability.

This field is a relationship field.

**Relationship Name**
AdAvailabilityDimensions

**Relationship Type**
Lookup


-----

```
CalendarPeriodType
FromDate
Name
OwnerId

```

**Refers To**
AdAvailabilityDimensions

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
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the availability of the linear advertisement slot.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of ad linear availability.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who created the relationship record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner


-----

```
ProgramRunType
PublisherDayPart
SponsorshipType
ToDate

```

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The program during which the advertisement is scheduled to run.

Possible values are:

**•** `Premiere`

**•** `Regular`

**•** `Repeat`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The daypart schedule to run the advertising campaign.

Possible values are:

**•** `Non-Prime Time`

**•** `Prime Time`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The sponsorship type for the linear advertisement slot.

Possible values are:

**•** `Co Presented By`

**•** `Presented By`

**•** `Sponsored By`

**Type**
date


-----

```
Units
UnitsStatus

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the availability of the linear advertisement slot.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of units assigned for the linear advertisement slot.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the unit type for the linear advertisement slot.

Possible values are:

**•** `Available`

**•** `Booked`

**•** `Offered`

**•** `Total`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdLinearAvailabilityChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdLinearAvailabilityFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdLinearAvailabilityHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdLinearAvailabilityOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdLinearAvailabilityShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


-----
