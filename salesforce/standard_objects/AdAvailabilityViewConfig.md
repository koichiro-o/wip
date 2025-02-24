#### AdAvailabilityViewConfig

Represents configuration table for storing configurations, filters, and legend colors active in the calender view for corresponding pivots
and media types. This object is available in API version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
ConfigurationKey
ConfigurationType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The key to the configuration that's used to map the advertisement availability slot in the
view.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of configuration that's saved for the availability view.

Possible values are:

**•** `Colour Scheme`


-----

```
ConfigurationValue
IsActive
LastReferencedDate
MediaType

```


**•** `Filter`

**•** `General Configuration`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value that's used to map the advertisement availability slot in the view.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the configuration is active (true) or not (false) in the availability view.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of media that's shown in the availability view.

Possible values are:

**•** `Digital`

**•** `Other`

**•** `Outdoor`

**•** `Print`

**•** `Radio`

**•** `TV`


-----

```
Name
OwnerId
PivotOn
UsageType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of ad availability view configuration.

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
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The pivot for the calendar availability view.

Possible values are:

**•** `Ad Space Specification`

**•** `Media Content Title`

**•** `Product`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The usage type of the calendar availability.

Possible values are:

**•** `Pricing`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdAvailabilityViewConfigChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdAvailabilityViewConfigFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdAvailabilityViewConfigHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdAvailabilityViewConfigOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdAvailabilityViewConfigShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
