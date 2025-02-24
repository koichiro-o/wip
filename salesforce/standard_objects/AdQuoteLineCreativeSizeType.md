#### AdQuoteLineCreativeSizeType

Represents an intersection object between ad quote line and ad creative size. It records companion creative sizes for each ad creative
size and the number of times each parent creative needs to run. Users select this information in the media plan, which is then sent to
the downstream execution system. This object is available in API version 59.0 and later.

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
AdSpaceCreativeSizeTypeId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of Ad Quote Line.

This field is a relationship field.

**Relationship Name**
AdQuoteLine

**Relationship Type**
Lookup

**Refers To**
AdQuoteLine

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of Ad Space Creative Size Type.

This field is a relationship field.

**Relationship Name**
AdSpaceCreativeSizeType


-----

```
LastReferencedDate
LastViewedDate
Name
Total

##### Associated Objects

```

**Relationship Type**
Lookup

**Refers To**
AdSpaceCreativeSizeType

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
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the ad quote line creative size type.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The expected count of each of the parent creative sizes specified for the placement. The
default count for each parent creative size in the placement is 1, but users can modify it.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**[AdQuoteLineCreativeSizeTypeChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdQuoteLineCreativeSizeTypeFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdQuoteLineCreativeSizeTypeHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdQuoteLineCreativeSizeTypeOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdQuoteLineCreativeSizeTypeShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
