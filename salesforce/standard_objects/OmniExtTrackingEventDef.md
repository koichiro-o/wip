#### OmniExtTrackingEventDef

Represents a format for FlexCard or OmniScript user interaction data that a third-party Analytics system such as Google Analytics can
accept. This object is available in API version 60.0 and later.

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
ComponentType
Description
DeveloperName

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of component for which user interactions are tracked.

Possible values are:

**•** `Flexcard`

**•** `Omniscript`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of the OmniExtTrackingEventDef.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
InclusionRule
Language
MasterLabel
OmniExtTrackingDef

```

**Description**
The unique name of the OmniExtTrackingEventDef in the API. This name can contain only
underscores and alphanumeric characters and must be unique in your organization. It must
begin with a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. Limit: 80 characters.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance may slow while
Salesforce generates one for each record.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A true-or-false condition that determines whether an event is sent to the third-party Analytics
system.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for the OmniExtTrackingEventDef.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique master label of the OmniExtTrackingEventDef. This internal label doesn’t get
translated.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the related OmniExtTrackingDef object.

This field is a relationship field.


-----

```
OmniExtTrackingEventDefKey
PayloadTemplate

```

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
A UUID generated internally by Salesforce to uniquely identify an OmniExtTrackingEventDef
record across all orgs.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The payload template structure with placeholders for runtime data. This is used at runtime
to generate the actual payload to be sent to the external Analytics service.

