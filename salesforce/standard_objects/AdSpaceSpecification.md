#### AdSpaceSpecification

Defines a specific place or a group of places where an Ad Creative may be served. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdPageLayoutTypeId
AdServerAdSpaceIdentifier
AdServerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ad page layout type associated with the ad space specification.

This field is a relationship field.

**Relationship Name**
AdPageLayoutType

**Refers To**
AdPageLayoutType

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Identifies the unique Ad Server name and Id for the Ad Space Specification.

**Type**
reference


-----

```
AdSpaceType
AudienceSizeRating

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the Ad Server, which serves this Ad Space Specification.

This is a relationship field.

**Relationship Name**
AdServerId__r

**Relationship Type**
Lookup

**Refers To**
AdServer

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the AdSpace Type.

Possible values are:

**•** `1 Page Standard`

**•** `1/2 Page Horizontal`

**•** `2 Page Spread`

**•** `2/3 Page Vertical`

**•** `Billboard`

**•** `Full banner WF DFP`

**•** `Graphic Image`

**•** `Leaderboard`

**•** `Mid-Roll`

**•** `Post-Roll`

**•** `Pre-Roll`

**•** `Skyscraper`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the Audience Size rating for the Ad Space specification.


-----

```
BroadcastDays
CreativeFormatType
EndDateTime
EndTime

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Specifies the days of the week when the related ad creative can be served.

Possible values are:

**•** `Friday`

**•** `Monday`

**•** `Saturday`

**•** `Sunday`

**•** `Thursday`

**•** `Tuesday`

**•** `Wednesday`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the media format of the creative that's displayed on the ad space.

Possible values are:

**•** `Display`

**•** `Video or audio`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies the end date and time for a scheduled program specification.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies the end time for a scheduled program specification.


-----

```
EndWeekDay
IsActive
IsLiveBroadcast
LastReferencedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures the day of the week on which the Ad Space Specification ends.

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the Ad Space Specification is active.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a Broadcast schedule is a Live Telecast or a Recorded Telecast.

The default value is 'false'.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.


-----

```
LastViewedDate
MediaChannelId
MediaContentTitleId
Name

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDateis not null, the user accessed this record or list view indirectly.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the media channel related to the ad space specification.

This is a relationship field.

**Relationship Name**
MediaChannelId__r

**Relationship Type**
Lookup

**Refers To**
MediaChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the media content title related to the ad space specification.

This is a relationship field.

**Relationship Name**
MediaContentTitleId__r

**Relationship Type**
Lookup

**Refers To**
MediaContentTitle

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
OwnerId
Page
Position
Product2Id

```

**Description**
The name of the ad space specification.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the ad space specification.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Speicifes the type of page on which the related ad creative is displayed.

Possible values are:

**•** `Back cover`

**•** `Front cover`

**•** `Page 3`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the position of the related ad creative on the page.

Possible values are:

**•** `Above the fold`

**•** `Bottom right`

**•** `Top left`

**Type**
reference


-----

```
ProgramRunType
PublisherDayPart
Section

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Refers to the Product record associated with the Ad Space Specification. The product is added
to the Placement and is used to calculate the total cost of the Placement.

This is a relationship field.

**Relationship Name**
Product2Id__r

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures the schedule type.

Possible values are:

**•** `Premiere`

**•** `Regular`

**•** `Repeat`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures the day time type for the Publisher.

Possible values are:

**•** `Non Prime Time`

**•** `Prime Time`

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Specifies the section where the related ad creative is placed.


-----

```
StartDateTime
StartTime
StartWeekDay
SubSection

```

Possible values are:

**•** `Entertainment`

**•** `Politics`

**•** `Sports`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies the start date and time for a scheduled program specification.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies the start time for a scheduled program specification.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the day of the week on which the ad space specification begins.

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Specifies the subsection where the related ad creative is displayed.


-----

```
Type

##### Associated Objects

```

Possible values are:

**•** `Art`

**•** `Cricket`

**•** `Football`

**•** `India`

**•** `Movies`

**•** `Theatre`

**•** `World`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type for ad space specification.

Possible values are:

**•** `Ad Space`

**•** `Ad Space Group`

**•** `Scheduled Program`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdSpaceSpecificationChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdSpaceSpecificationFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdSpaceSpecificationHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdSpaceSpecificationOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdSpaceSpecificationShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
