#### Crisis

Represents a major crisis event that affects an Employee in an InternalOrganizationUnit. This object is available in API version 48.0 and
later. In API version 49.0 and later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude
individual fields from custom page layouts.

Work.com uses this object to track and describe crisis situations.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, you must be assigned a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission.

##### Fields

```
CrisisType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The type or category of crisis.

Possible values are:


-----

```
Description
EndDate
LastReferencedDate
LastViewedDate
Name

```


**•** `Economic Crisis`

**•** `Natural Disaster`

**•** `Pandemic`

**•** `War`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The crisis description.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date the crisis ended.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The crisis record name.


-----

```
OwnerId
StartDate

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The date the crisis started.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CrisisHistory (API version 49.0)**
History is available for tracked fields of the object.

**CrisisOwnerSharingRule**

Sharing rules are available for the object.

**CrisisShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide: Extend Work.com with Custom Solutions](https://developer.salesforce.com/docs/atlas.en-us.254.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_
