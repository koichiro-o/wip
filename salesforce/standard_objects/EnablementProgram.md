#### EnablementProgram

Represents an Enablement program, which includes exercises and measurable milestones to help users such as sales reps achieve specific
outcomes related to your company’s revenue goals. This object is available in API version 56.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
**•** For Enablement admins to create, update, and delete Enablement programs, the Design and Deliver Enablement Programs permission
is required. This permission is enabled by default as part of the Manage Enablement Essentials permission set, which comes with
the Enablement add-on license.

**•** For users who take Enablement programs, the Take Enablement Programs permission is required. This permission is enabled by
default as part of the Use Enablement Programs permission set, which comes with the Enablement add-on license.

**•** For partner users who take Partner Enablement programs, the Take Partner Enablement Programs permission is required. This
permission is enabled by default as part of the Use Partner Enablement Programs permission set, which comes with the Enablement
[add-on license. Partner Enablement also requires a supported Partner Relationship Management (PRM) add-on license.](https://help.salesforce.com/s/articleView?id=sf.prm_support_license_template.htm&language=en_US)

##### Fields

```
Description
DoesAllowSelfEnrollment

```

**Type**
textarea

**Properties**
Create, Update

**Description**

A summary of the program’s goals and content that’s visible to users.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether users can self-enroll in programs that are shared with them (true) or
take only assigned programs (false). The default value is `false.`


-----

```
EnablementProgramDefinitionId
IsOutcomeBased
LastReferencedDate
LastViewedDate
Name

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The representation for the program in Metadata API. This field is a relationship field.

Available in API version 61.0 and later.

**Relationship Name**
EnablementProgramDefinition

**Relationship Type**
Lookup

**Refers To**
EnablementProgramDefinition

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the program includes a final, measurable outcome (true) or not (false).
The default value is `false.`

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
The timestamp when the current user last viewed this record. If this value is null, maybe the
user accessed this record (LastReferencedDate) but not viewed it yet.

**Type**
string


-----

```
NetworkId
OwnerId
PublishedDateTime

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the program that’s visible to users. For example, `AE Onboarding,` `Event`
```
  Prep, or New Product Launch.

```
**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the supported Experience Cloud site where a partner program is available. For site
[requirements, see Considerations for Partner Enablement Programs.](https://help.salesforce.com/s/articleView?id=sf.enablement_partner_considerations.htm&language=en_US)

Available in API version 60.0 and later.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the program. This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date that the program is published.


-----

```
Status
TotalAssigned
TotalBehind
TotalCompleted
TotalDays

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The status of the program. Only a published program is available for an Enablement admin
to assign to users or share with users so they can self-enroll.

Possible values are:

**•** `Archived`

**•** `Draft`

**•** `Published`

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments in this program. For example, if the program is assigned to 3
users, then `TotalAssigned=3.`

**Type**
int

**Properties**
Nillable

**Description**
The number of assignments that are behind in this program. For example, if the program is
assigned to 3 users, and 2 users are behind on their assignments, then `TotalBehind=2`

**Type**
int

**Properties**
Nillable

**Description**
The number of completed assignments in this program. For example, if the program is
assigned to 3 users, and 1 user has completed the program, then `TotalCompleted=1.`

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort


-----

```
Type

##### Associated Objects

```

**Description**
Total days of the program. This value is derived from the latest day of all items in the program,
including exercises, milestones, and the outcome. This field is a calculated field. For example,
a program has Task A on day 1 and Task B on day 2. Since Task B has the latest days of all
tasks, then `TotalDays=2.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the program. Possible values are:

**•** `Enablement—A sales program in Lightning Experience.`

**•** `PtnrEnablement—A partner program in a supported Experience Cloud site. Available`
in API version 60.0 and later.

**•** `EmployeeServiceEnablement—An employee enablement program in Employee`
Portal. Available in API version 63.0 and later.


This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**EnablementProgramOwnerSharingRule (API version 60.0)**
Sharing rules are available for the object.

**EnablementProgramShare (API version 60.0)**
Sharing is available for the object.
