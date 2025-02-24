#### AdQuoteLineHiatus

Represents the hiatus details of the media placement in a quote line. This object is available in API version 60.0 and later.

The hiatus days during which an ad is not broadcast.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
AdQuoteLineId
Days

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Ad quote line that’s associated with the hiatus.

This field is a relationship field.

**Relationship Name**
AdQuoteLine

**Relationship Type**
Lookup

**Refers To**
AdQuoteLine

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Update

**Description**
Day in the week when the quote line hiatus is in effect.


-----

```
EndDate
LastReferencedDate
LastViewedDate
Name

```

Possible values are:

**•** `Sunday`

**•** `Monday`

**•** `Tuesday`

**•** `Wednesday`

**•** `Thursday`

**•** `Friday`

**•** `Saturday`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
End date of the ad hiatus interval.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp for when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or lit view. If this value is null, it’s
possible that the user only accessed this record or list view (LastReferencedDate), but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the record.


-----

```
StartDate
Type

##### Associated Objects

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Start date of the ad hiatus interval.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of quote line hiatus.

Possible values are:

**•** `Days`

**•** `Interval`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdQuoteLineHiatusChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdQuoteLineHiatusFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdQuoteLineHiatusHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdQuoteLineHiatusOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdQuoteLineHiatusShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
