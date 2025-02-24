#### AdQuoteLine

An extension to the Quote LineItem and captures the details specific to an Ad Placement. This object is available in API version 54.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdBleedAmountUom
AdBleedAmount

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies Ad Bleed height and width measure.

Possible values are:

**•** `Inches`

**•** `Pixels`

**•** `mm`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the distance from the edge of the page.


-----

```
AdCreativeSizeTypes
AdCreativeUrl
AdPlacementPriorityType
AdQuoteId
AdRequestedEndDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Lists user selected, semicolon separated creative size types from the possible choices
presented by each Ad Space. For example: 720 X 350; 400 X 350.

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
Chosen from the Ad Server's AdPriorityType record. For example: STANDARD, PRICE_PRIORITY.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Captures the details of the Quote.

This is a relationship field.

**Relationship Name**
QuoteId__r

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
AdRequestedStartDate
AdSpaceSpecificationAdServer
AdSpaceSpecificationId
AdSpaceSpecificationMediaChannel

```

**Description**
Captures the requested end date for the line item.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the requested start date for the placement.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Refers to the AdServer responsible to serve the Ad Creative.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Lookup to the Ad Space Specification record.

This is a relationship field.

**Relationship Name**
AdSpaceSpecificationId__r

**Relationship Type**
Lookup

**Refers To**
AdSpaceSpecification

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Refers to the Media Channel of the Ad Space Specification record.

This is a calculated field.


-----

```
AdSpaceSpecificationType
AdTimePerEpisode
BonusAdTime
CostPerRatingPoint
CustomerDayPart

```

**Type**
picklist

**Properties**
Filter, Nillable, Sort

**Description**
Refers to the Ad Space Type for the Ad Space Specification record.

This is a calculated field.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the Ad Time for each episode customer is paying for in seconds.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Bonus Ad times in seconds provided to the customer.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Cost Per Rating Point calculated on the basis of `QuoteLineItem.Implied Rate`
```
  / AdSpaceSpec.Audience Size rating.

```
**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates Ad Space Specification chosen.

Possible values are:

**•** `Non Prime Time`

**•** `Prime Time`


-----

```
GrossRatingPoint
ImpliedRate
ImpliedTotal
IsAdBleedEnabled
MaximumFrequencyInterval

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Calculated on the basis of `AdSpaceSpec.Audience Size Rating * Paid`
```
  Commercial Time per TimeSlot.

```
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

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the Ad extends all the way to the edge of the page on at least one side.

The default value is 'false'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the maximum frequency unit used for frequency capping.

Possible values are:

**•** `Day`


-----

```
MaximumFrequency
MaximumUserFrequencyInterval
MaximumUserFrequency
MediaType

```


**•** `Hour`

**•** `Minute`

**•** `Second`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Specifies the maximum number of times Ad is served for frequency capping.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies maximum user frequency interval.

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
Indicates maximum number of times a unique user sees the Ad over a given time period.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures the Media Type field of the Placement record.

Possible values are:

**•** `Digital`

**•** `Other`

**•** `Outdoor`


-----

```
PaidAdTime
PercentageAdTime
QuoteLineItemId
QuoteLineItemProductCode

```


**•** `Print`

**•** `Radio`

**•** `TV`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Total Ad Time slots customer is paying for in seconds.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the percentage of the Commercial time slot the placement represents in the whole
deal.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Captures the Quote LineItem for which the extension record is to be created.

This is a relationship field.

**Relationship Name**
QuoteLineItemId__r

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Captures the Product Code of the Quote LineItem's product.

This is a calculated field.


-----

```
QuoteLineItemQuantity
RequestedIssues
RequestedSplits
SponsorshipType
TargetingParameters

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Refers to the Quantity field of the Quote LineItem record.

This is a calculated field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The Issues selected for a placement or line item for which the selected or defined ad creatives
are to be inserted.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The break-up of the requested units for each placement or line item, based on the selected
frequency, whether daily or weekly.

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

**Description**
Stores Ad Creative targeting parameters in JSON format.


-----

```
TotalAdTime
UserEngagementGoalType
UserEngagementGoalUnitType
UserEngagementGoalUnit

##### Associated Objects

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Captures the sum of Bonus and Paid Ad Time OR Ad Time Per Episode multiplied by No of
Episodes on Media Content Title of Ad Space Specification.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the user engagement goal defined in terms of clicks, impressions, and so on.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of goal unit.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the number or percentage of impressions or clicks that are reserved for the Ad
Creative.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdQuoteLineFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdQuoteLineHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.


-----
