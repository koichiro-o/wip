#### AdAvailabilityDimensions

Table containing lookup references to specific objects with common, filterable fields between media types. This object is available in
API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
AdOrderItemId
AdQuoteLineId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The advertising order item that's associated with the advertisement slot sale.

This field is a relationship field.

**Relationship Name**
AdOrderItem

**Relationship Type**
Lookup

**Refers To**
AdOrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The advertising quote line that's associated with the advertisement slot sale.

This field is a relationship field.

**Relationship Name**
AdQuoteLine

**Relationship Type**
Lookup


-----

```
AdServer
AdSpaceSpecificationId
DealType
DeliveredUnits

```

**Refers To**
AdQuoteLine

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the advertising server that's used to retrieve the dimension details.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The advertising space specification that's associated with the advertising slot sale.

This field is a relationship field.

**Relationship Name**
AdSpaceSpecification

**Relationship Type**
Lookup

**Refers To**
AdSpaceSpecification

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of deal to sell advertising slot units.

Possible values are:

**•** `Direct-sales`

**•** `Preferred (Non-Guaranteed)`

**•** `Programmatic Guaranteed`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of slots that were delivered in a specified period.


-----

```
JobId
MediaChannelId
MediaContentTitleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Ad Availability Job that's associated with the dimension.

This field is a relationship field.

**Relationship Name**
Job

**Relationship Type**
Lookup

**Refers To**
AdAvailabilityJob

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The media channel that's associated with the advertising slot sale.

This field is a relationship field.

**Relationship Name**
MediaChannel

**Relationship Type**
Lookup

**Refers To**
MediaChannel

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The media content title that's associated with advertising slot sale.

This field is a relationship field.

**Relationship Name**
MediaContentTitle

**Relationship Type**
Lookup


-----

```
MediaType
Name
OwnerId
PricingModel

```

**Refers To**
MediaContentTitle

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of media plan that's used to run the advertisements.

Possible values are:

**•** `Digital`

**•** `Other`

**•** `Outdoor`

**•** `Print`

**•** `Radio`

**•** `TV`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of ad availability dimensions.

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
string


-----

```
ProductId

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the pricing model for the media plan.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The product that's associated with the advertisement sale.

This field is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdAvailabilityDimensionsChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdAvailabilityDimensionsFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdAvailabilityDimensionsHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdAvailabilityDimensionsOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdAvailabilityDimensionsShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
