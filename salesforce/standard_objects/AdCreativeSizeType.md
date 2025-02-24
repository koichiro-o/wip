#### AdCreativeSizeType

Defines the size of the Ad Creative. Example: 728 x 90 pixels. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdServerAdCreativeIdentifier
CreativeType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier for the ad creative in an external ad server

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the type of ad creative.

Possible values are:

**•** `Billboard`


-----

```
Height
LastReferencedDate
LastViewedDate
MediaType

```


**•** `Bookend`

**•** `PiggyBack`

**•** `Standard`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The height of the creative asset.

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
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of the ad creative size type.

Possible values are:

**•** `Digital Banner`

**•** `Digital Video`

**•** `Outdoor`

**•** `Print`

**•** `Radio`

**•** `TV`


-----

```
Name
OwnerId
RunTime
StartX
StartY

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ad creative size type.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the ad creative size type.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The creative run time where applicable.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The x-axis coordinate for the start of the ad on the page

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The y-axis coordinate for the start of the ad on the page


-----

```
UnitOfMeasure
Width

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of measure for defining the size of the creative asset.

Possible values are:

**•** `Inches`

**•** `Minutes`

**•** `Pixels`

**•** `Seconds`

**•** `mm`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The width of the creative asset.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdCreativeSizeTypeFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdCreativeSizeTypeHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdCreativeSizeTypeOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdCreativeSizeTypeShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
