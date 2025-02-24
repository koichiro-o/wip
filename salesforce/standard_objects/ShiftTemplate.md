#### ShiftTemplate

Represents a template for creating shifts. This object is available in API version 51.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
Field Service or Workforce Engagement must be enabled. For Field Service, users must have Field Service permission. For Workforce
Engagement, the user needs to have a Workforce Engagement Admin or Planner permission set.


-----

##### Fields

**Field**
```
BackgroundColor
Description
Duration
IsActive
IsNonStandard
JobProfileId

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Sets a background color when shifts are displayed in the UI. Use a 3- or 6-digit hexadecimal
format, for example #FF00FF. Available in API version 54.0 and later.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Additional information about the shift like number of breaks or activities.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
How long the shift lasts. The unit of measurement for this field is determined by
```
  ShiftTemplateDurationType.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is active or inactive.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the shift is nonstandard, such as overtime or on-call shifts.

The default value is false. Available in API version 54.0 and later.

**Type**
reference


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Job Profile record. This field is optional.

This is a relationship field.

**Relationship Name**
JobProfile

**Relationship Type**
Lookup

**Refers To**
JobProfile

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last modified. Its label in the user interface is Last
**Modified Date.**

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the shift template was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The shift template record name.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the shift template.

This is a polymorphic relationship field.


-----

```
RecordsetFilterCriteriaId
ShiftTemplateDurationType
StartTime

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the recordset filter criteria selected for the shift template. Available in API version
53.0 and later.

This is a relationship field.

**Relationship Name**
RecordsetFilterCriteria

**Relationship Type**
Lookup

**Refers To**
RecordsetFilterCriteria

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit of measurement for the shift template duration.

Possible values are:

**•** `H—Hours`

**•** `M—Minutes`

The default value is `H.`

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
The time of day when the shift starts.


-----

```
TimeSlotType

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of time slot. Possible values are:

**•** `Normal`

**•** `Extended`

You can use Extended to represent overtime shifts. Available in API version 55.0 and later.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ShiftTemplateOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ShiftTemplateShare on page 66**
Sharing is available for the object.

**ShiftTemplateChangeEvent on page 67**
Change Data Capture events are available for the object. Available in API version 54.0 and later.
