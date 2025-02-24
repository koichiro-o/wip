#### InternalOrganizationUnit

```
Represents an organization that an Employee belongs to. This object is available in API version 48.0 and later. In API version 49.0 and
later, this object supports reports, criteria-based sharing rules, and history tracking, plus you can exclude individual fields from custom
page layouts.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, you have either a Workplace Command Center permission set license and the Provides access to Workplace
Command Center features system permission, or the Employee Management and Employee User add-on licenses. This object is also
available with the Referral Marketing license.

##### Fields

```
Description
LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A description of the organization the Employee is working in.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.


-----

```
LastViewedDate
OrganizationCode
OrganizationName
OwnerId
ParentOrganizationId
Type

```

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
Required. The code of the organization the Employee is working in.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the organization the Employee is working in.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this record. Default value is the user logged in to the
API to perform the create operation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A reference to the parent organization.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

**Description**
Specifies whether the record is for an internal or an external organization. This field is available
in API version 60.0 and later.

Possible values are:

**•** `EXTERNAL_BUSINESS_UNIT`

**•** `INTERNAL_ORGANIZATION`

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**InternalOrganizationUnitHistory (API version 49.0)**
History is available for tracked fields of the object.

**InternalOrganizationUnitOwnerSharingRule**

Sharing rules are available for the object.

**InternalOrganizationUnitShare (API version 49.0)**
Sharing is available for the object.

SEE ALSO:

_[Workplace Command Center for Work.com Developer Guide: Extend Work.com with Custom Solutions](https://developer.salesforce.com/docs/atlas.en-us.254.0.ajax.meta/workdotcom_dev_guide/wdc_cc_overview.htm)_
