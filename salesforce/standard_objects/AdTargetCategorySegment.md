#### AdTargetCategorySegment

Represents an individual Targeting Segment, which has available options among which selections can be made. For example, Gender,
Education Demographics, Country, and State. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AvailableValues
Code

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Stores all optional values for a particular targeting segment as a JSON file, based on the
identifiers configured by the user.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
DataType
DependentCategorySegmentId
Description

```

**Description**
Represents the Code on the Category Segment record, which is mapped to the Ad Server's
Segment Code for the same record. Each Segment Record is represented as a separate node
when the payload is sent to the Ad Server.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Configures the type of data stored in the targeting segment.

Possible values are:

**•** `Text`

**•** `Number`

**•** `Boolean`

**•** `Picklist`

**•** `MultiSelectPicklist`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A self-referenced foreign key to support the dependent picklist feature. For example, Country,
State, City are three targeting options having dependency. Value selected in Country option
decide the optional values to be shown under State option.

This is a relationship field.

**Relationship Name**
DependentCategorySegment

**Relationship Type**
Lookup

**Refers To**
AdTargetCategorySegment

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents description for a particular category segment record. Data for this field can be
imported and mapped from the Ad Server.


-----

```
DisplaySequence
DisplayType
IsActive
IsAvailableForSelfService

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the sequence of the multiple records configured for a particular category. Based
on the number configured here, sequence is decided on the UI.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used to configure how data is rendered in the UI.

Possible values are:

**•** `Checklist`

**•** `RadioButton`

**•** `Checkbox`

**•** `Picklist`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is a published Segment or not. If not activated, it is not available
for the run time configuration for the user.

The default value is 'false'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this segment record is available only at the Agent Console or at self care
portal as well. By default, once activated all segments are available at Agent Console, but
can be available on the Self Service Console only when this field's value is set to true. Some
of the categories contain segments, which can be filled only by the Agent and they mainly
contain the configurations needed by Ad Server.

The default value is 'false'.


-----

```
MediaType
Name
ProductId
TargetCategoryId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Media Type against which a particular Target Category is mapped

Possible values are:

**•** `Digital`

**•** `TV`

**•** `Radio`

**•** `Print`

**•** `Outdoor`

**•** `Other`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Represents the category name or label shown to the user.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Foreign key to Product record for mapping a particular category with it.

This is a relationship field.

**Relationship Name**
Product

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**
Foreign key to Target Category record for grouping the segments under it.

This is a relationship field.

**Relationship Name**
TargetCategory

**Relationship Type**
Lookup

**Refers To**
AdTargetCategory

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdTargetCategorySegmentChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdTargetCategorySegmentFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdTargetCategorySegmentHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdTargetCategorySegmentOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdTargetCategorySegmentShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
