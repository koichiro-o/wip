#### SlaProcess

Represents an entitlement process associated with an Entitlement. This object is available in API version 19.0 and later.

An entitlement process is a timeline that includes all the steps (MilestoneType records) that your support team must complete to resolve
cases. Each process includes the logic necessary to determine how to enforce the correct service level for your customers.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), search(), describeLayout()

 Special Access Rules

```
As of Summer ’20 and later, only Salesforce admin users, users with access to the Case, Entitlement, or Work Order objects, and users
with the View Setup and Configuration permission can access this object.


-----

##### Fields

**Field**
```
BusinessHoursId
Description
IsActive
IsVersionDefault
LastViewedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Required. ID of the BusinessHours associated with the entitlement. Must be a valid
business hours ID.

**Type**
textarea

**Properties**
Filter, Nillable

**Description**
A description of the entitlement process.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the entitlement process is active (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the entitlement process is the default version (true) or not
(false).

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the SlaProcess was last viewed.


-----

```
Name
NameNorm
SObjectType
StartDateField

```

**Type**
string

**Properties**
Filter, idLookup

**Description**
The name of the entitlement process.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The read-only value for the unique name of the entitlement process or the entitlement
process version. If entitlement versioning is enabled, this value is automatically
generated for each version of an entitlement process in this form: `process`
`name+_v +` `x, where` `x` is the version number (for example, “gold_support_v2”).

If entitlement versioning isn’t enabled, this value is the same as `Name.`

This field is available in API version 28.0 and later.

**Type**
picklist

**Properties**
Restricted picklist, Filter, Group, Sort

**Description**
The type of records that the entitlement process can run on. Its values are:

**•** `Case`

**•** `Work Order`

An entitlement process runs only on records that match its type. For example, a Case
entitlement process that’s applied to an entitlement runs only on cases associated
with the entitlement, not on work orders. As a best practice, therefore, manage
customers’ work orders and cases on separate entitlements.

The field label in the user interface is Entitlement Process Type.

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
The criteria for cases to enter the entitlement process. Cases can enter the process
based on:

**•** The creation date on a case


-----

```
VersionMaster
VersionNotes
VersionNumber

##### Usage

```


**•** A custom date/time field on a case

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Identifies the sequence of versions to which this entitlement process belongs. This
field’s contents can be any value as long as it is identical among all versions of the
entitlement process.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the entitlement process version.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The version number of the entitlement process. Must be 1 or greater.

This field is available in API version 28.0 and later in organizations that have entitlement
versioning enabled.


Use this object to query entitlement processes on entitlements.

SEE ALSO:

Entitlement

MilestoneType

CaseMilestone


-----
