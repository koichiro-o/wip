#### AdQuote

An extension to Quote and captures quote attributes specific to Advertising Sales Management. This object is available in API version
54.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ImpliedTotalAmount
Quote
RequestedSplitsInterval
TotalAdTime

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Presents the sum of the Implied Total of all Media Plan Placement records.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies a quote, which is a record showing proposed prices for products and services.

This is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The interval at which the requested splits for units are displayed, whether weekly or daily.

**Type**
double

**Properties**
Filter, Nillable, Sort


-----

```
TotalBonusAdTime
TotalCostPerRatingPoint
TotalGrossRatingPoint
TotalPaidAdTime

##### Associated Objects

```

**Description**
Represents the Total Ad Time for the Media Placement.

This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the Total Bonus Ad Time for the Media Placement.

This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the Total Cost Per Rating Point for the Media Placement.

This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the Total Gross Rating Point for the Media Placement.

This is a calculated field.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Represents the Total Paid Ad Time for the Media Placement.

This is a calculated field.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**[AdQuoteFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdQuoteHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdQuoteOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdQuoteShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
