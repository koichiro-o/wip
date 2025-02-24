#### AdOrderItem

An extension to the Order LineItem and captures the details specific to an Ad Placement. This object is available in API version 54.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AdBleedAmount
AdBleedAmountUom
AdCreativeSizeTypes
AdCreativeUrl
AdPlacementPriorityType

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The distance from the edge.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies bleed height and width measurement.

Possible values are:

**•** `Inches`

**•** `Pixels`

**•** `mm`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Semicolon separated user-selected Creative SizeTypes from the possible choices presented
by each Ad Space. For example: 720 X 350; 400 X 350.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the URL of the Ad Creative. It may or may not be hosted by Salesforce platform.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the placement priority type chosen from the Ad Server's AdPriorityType record.


-----

```
AdRequestedEndDate
AdRequestedQuantity
AdRequestedStartDate
AdServerOrderIdentifier
AdServerOrderLineIdentifier
AdServerProposalLineStatus

```

Possible values are:

**•** `Standard`

**•** `Sponsorship`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested end date for the LineItem.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested units of the ad order item.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The requested start date for the placement.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order ID generated from the ad server.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The order line item ID generated at the ad server.

**Type**
picklist


-----

```
AdSpaceSpecificationId
AdTimePerEpisode
BillingCycle

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the status of an ad order line item proposal in the ad server.

Possible values are:

**•** `Completed`

**•** `Delivering`

**•** `Draft`

**•** `Paused`

**•** `Ready`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ad space specification related to the ad order item.

This is a relationship field.

**Relationship Name**
AdSpaceSpecificationId__r

**Relationship Type**
Lookup

**Refers To**
AdSpaceSpecification

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The Ad Time in seconds for each episode Customer will be paying for .

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the billing cycle for an order line item.

Possible values are:

**•** `Broadcast`


-----

```
BillingMode
BonusAdTime
ContractedQuantity
CostPerRatingPoint
CustomerDayPart

```


**•** `Calendar`

**•** `End Of Flight`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the billing mode for an order line item.

Possible values are:

**•** `Fractional`

**•** `Retail`

**•** `Threshold`

**•** `Usage`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Bonus commercial times in seconds provided to the customers.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contracted quantity of the ad order item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Cost Per Rating Point calculated on the basis of `QuoteLineItem.ImpliedRate /`
```
  AdSpaceSpecification.AudienceSizeRating.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
EstimatedQuantity
GrossRatingPoint
ImpliedRate
ImpliedTotal
IsAdBleedEnabled

```

**Description**
Customer PrimeTime depends on the combination of genre of the show, audience interest,
demographics, and, so on.

Possible values are:

**•** `Non Prime Time`

**•** `Prime Time`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contracted quantity of the ad order item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Calculated on the basis of AdSpaceSpecification.AudienceSizeRating

`* Paid Commercial Time` per 'Linear Commercial Time Slot Unit of the Org'.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used by publishers to organize the revenue structure within the deal. This value is often
internal to the publisher organization and not customer facing.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Calculated from the ImpliedRate and is used by publishers to organize the revenue structure
within the deal. This value is often internal to the publisher organization and not customer
facing.

**Type**
boolean


-----

```
LastReferencedDate
LastViewedDate
MaxDuration
MaximumFrequency
MaximumFrequencyInterval

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the Ad extends all the way to the edge of the page on at least one side.

The default value is 'false'.

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
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
and LastReferenceDateis not null, the user accessed this record or list view indirectly.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum duration of the ad order item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Identifies maximum number of times the Ad is served for frequency capping.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
MaximumUserFrequency
MaximumUserFrequencyInterval
MediaType

```

**Description**
Identifies the maximum frequency unit used for frequency capping.

Possible values are:

**•** `Day`

**•** `Hour`

**•** `Minute`

**•** `Second`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Maximum number of times a unique user sees the Ad over a given time period.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Identifies the maximum user frequency interval used for frequency capping.

Possible values are:

**•** `Day`

**•** `Hour`

**•** `Minute`

**•** `Second`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The media type of the placement.

Possible values are:

**•** `Digital`

**•** `Other`

**•** `Outdoor`

**•** `Print`

**•** `Radio`


-----

```
Name
OrderId
OrderItemId
PaidAdTime

```


**•** `TV`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ad order item.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Refers to the Order record.

This is a relationship field.

**Relationship Name**
OrderId__r

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Captures the Order Product for which the extension record is to be created.

This is a relationship field.

**Relationship Name**
OrderItemId__r

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
PrimaryCostPerMille
PrimaryDemographicCodeId
PrimaryGrpPercentage
PrimaryImpressions
PrimaryImpsPercentage

```

**Description**
Indicates total commercial time slots customer are paying for in seconds.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The cost per mile of the ad order item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the primary demographic code associated with the ad quote item.

This field is a relationship field.

**Relationship Name**
PrimaryDemographicCode

**Refers To**
AdDemographicCode

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The primary group percentage of the ad order item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary impressions of the ad order item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
PrimaryRating
PrimaryTotalImps
PriorOrderLineItemId
PriorUsedAmount
QuoteLineItemId

```

**Description**
The primary impression percentage of the ad order item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The primary rating of the ad order item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The primary total impressions of the ad order item.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The prior order item in case of existing or changed order item, for new it will be blank.

This field is a relationship field.

**Relationship Name**
PriorOrderLineItem

**Relationship Type**
Lookup

**Refers To**
OrderItem

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
This is the amount billed in prior orders in case of modified order, for new orders it will be
zero.

**Type**
reference


-----

```
RequestedIssues
RequestedSplits
SecondaryCostPerMille
SecondaryCostPerRatingPoint

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Captures the Quote LineItem if the order is to be created for a Quote.

This is a relationship field.

**Relationship Name**
QuoteLineItemId__r

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The issues selected for a placement or line item for which the selected or defined ad creatives
are to be inserted.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The break-up of the requested units for each placement or line item, based on the selected
frequency, whether daily or weekly.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The seconday cost per mile of the ad order item.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The secondary cost per rating point of the ad order item.


-----

```
SecondaryDemographicCodeId
SecondaryGrossRatingPoint
SecondaryGrpPercentage
SecondaryImpressions
SecondaryImpsPercentage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the secondary demographic code of the ad order item.

This field is a relationship field.

**Relationship Name**
SecondaryDemographicCode

**Refers To**
AdDemographicCode

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The secondary gross rating point of the ad order item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The secondary group percentage of the ad order item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The secondary impressions of the ad order item.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The secondary impression percentage of the ad order item.


-----

```
SecondaryRating
SecondaryTotalImps
Skippable
SponsorshipType
TargetingParameters

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The secondary rating of the ad order item.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The secondary total impressions of the ad order item.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates whether the an order item can be skipped.

Possible values are:

**•** `Any`

**•** `Disable`

**•** `Enable`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures advertiser's sponsorship interests for the Ad Space Specification.

Possible values are:

**•** `Co Presented By`

**•** `Presented By`

**•** `Sponsored By`

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
TotalAdTime
UserEngagementGoalType
UserEngagementGoalUnit
UserEngagementGoalUnitType

```

**Description**
The ad creative targeting parameters stored in JSON format.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The sum of bonus and paid ad time or ad time per episode multiplied by number of episodes
on media content title of ad space specification.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the user engagement goal defined in terms of clicks, impressions, and so on. This
is derived from Ad Space Available GoalType.

Possible values are:

**•** `LIFETIME`

**•** `DAILY`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number or percentage of impressions or clicks for the ad creative.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of goal unit.

Possible values are:

**•** `IMPRESSIONS`

**•** `CLICKS`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdOrderItemConfigFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdOrderItemHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.
