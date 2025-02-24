#### AdOrderLineHiatus

Represents the hiatus details of the media placement in a order line. This object is available in API version 60.0 and later.

The hiatus days during which an ad is not broadcast, based on the ad order.

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
Days

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Ad order line item that’s associated with the hiatus.

This field is a relationship field.

**Relationship Name**
AdOrderItem

**Relationship Type**
Lookup

**Refers To**
AdOrderItem

**Type**
multipicklist


-----

```
EndDate
LastReferencedDate
LastViewedDate
Name

```

**Properties**
Create, Filter, Nillable, Update

**Description**
Days in the week when the hiatus is in effect.

Possible values are:

**•** `Friday`

**•** `Monday`

**•** `Saturday`

**•** `Sunday`

**•** `Thursday`

**•** `Tuesday`

**•** `Wednesday`

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
Timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp when the current user last viewed this record or list view. If this value is null, it’s
possible that the user only accessed this record or list view (LastReferencedDate), but not
viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
StartDate
Type

##### Associated Objects

```

**Description**
Name of the record.

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
Type of order line hiatus.

Possible values are:

**•** `Days`

**•** `Interval`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdOrderLineHiatusChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdOrderLineHiatusFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdOrderLineHiatusHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdOrderLineHiatusOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdOrderLineHiatusShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
