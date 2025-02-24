#### MediaChannel

Defines a web page, a TV program, or a publication. A media channel may contain one to many Ad Spaces, into which Ad Servers can
place or serve up ad creatives. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AvailableLanguages
Circulation
CoreAudience
EndDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
Captures the language of the media contents hosted on the Media Channel.

Possible values are:

**•** `English`

**•** `Hindi`

**•** `German`

**•** `Spanish`

**•** `French`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Number of copies of a publication distributed during a specified time period.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A specific group of consumers, most likely to sample the product or service.

**Type**
date


-----

```
IsActive
LastReferencedDate
LastViewedDate
MediaType

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date of the media channel.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the media channel is active.

The default value is `false.`

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
Indicates the media type.

Possible values are:

**•** `Digital`

**•** `Other`

**•** `Outdoor`

**•** `Print`

**•** `Radio`


-----

```
Name
OwnerId
PeriodicalType
PricingCategory

```


**•** `TV`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the media channel.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the media channel.

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
Specifies the type of periodical.

Possible values are:

**•** `Advertorial`

**•** `Magazine`

**•** `NewsPaper`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Categorizes the Media Channel as Premium or Standard from an advertising pricing
perspective. 'Premium' is an evaluation based on traffic, Nielsen ratings or Comscore rank.

Possible values are:

**•** `Premium`


-----

```
PublicationFrequency
PublisherId
PublisherPrimaryContactId

```


**•** `Standard`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Captures the frequency of the Media Channel publication

Possible values are:

**•** `Daily`

**•** `Monthly`

**•** `Other`

**•** `Quarterly`

**•** `Weekly`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Captures the Publisher field of the Media Channel record.

This is a relationship field.

**Relationship Name**
PublisherId__r

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Captures the primary contact details of the publisher.

This is a relationship field.

**Relationship Name**
PublisherPrimaryContactId__r

**Relationship Type**
Lookup


-----

```
Reach
StartDate

##### Associated Objects

```

**Refers To**
Contact

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The total number of unique people or households exposed, at least once, to a medium in a
given period.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date of the media channel.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[MediaChannelFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[MediaChannelHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[MediaChannelOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[MediaChannelShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
