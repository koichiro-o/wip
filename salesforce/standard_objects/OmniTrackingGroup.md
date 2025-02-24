#### OmniTrackingGroup

Represents a group of FlexCard and OmniScript components that have their user interactions tracked together in OmniAnalytics. This
object is available in API version 60.0 and later.

Note: This object is part of OmniStudio Standard, not OmniStudio for Vlocity.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Using OmniAnalytics requires having an OmniStudio license and enabling OmniAnalytics in Setup.

##### Fields

```
Description
DeveloperName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of the OmniTrackingGroup.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the OmniTrackingGroup in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. Limit: 80 characters.


-----

```
EndDate
GroupType
IsActive
Language
MasterLabel

```

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the OmniTrackingGroup became inactive.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies whether this OmniTrackingGroup sends tracking data to a third-party Analytics
system such as Google Analytics.

Possible values are:

**•** `External—A third-party Analytics system is used.`

**•** `Internal—No third-party Analytics system is used.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the OmniTrackingGroup is active.

The default value is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for the OmniTrackingGroup.

**Type**
string


-----

```
MaxAgeInDays
OmniExtTrackingDef
OmniTrackingGroupKey
StartDate

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique master label of the OmniTrackingGroup. This internal label doesn’t get translated.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum number of days the group and its analytics data is active beyond which the
data is deleted.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the related OmniExtTrackingDef object. Required if `GroupType` is set to
```
  External.

```
This field is a relationship field.

**Relationship Name**
OmniExtTrackingDef

**Relationship Type**
Lookup

**Refers To**
OmniExtTrackingDef

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
A UUID generated internally by Salesforce to uniquely identify an OmniTrackingGroup record
across all orgs.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
The date when the OmniTrackingGroup became active.
