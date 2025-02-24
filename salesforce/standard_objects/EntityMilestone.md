#### EntityMilestone

Represents a required step in a customer support process on a work order. The Salesforce user interface uses the term “object milestone.
This object is available in API version 37.0 and later.

Note: Milestones on cases use the CaseMilestone object type.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete(),
update()

 Special Access Rules

```
**•** As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

**•** Entitlement management must be enabled.

**•** Work orders or Field Service must be enabled.

##### Fields

```
ActualElapsedTimeInDays

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)


-----

```
ActualElapsedTimeInHrs
ActualElapsedTimeInMins
BusinessHoursId
CompletionDate

```

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that it took to complete a milestone. (Elapsed Time) –
(Stopped Time) = (Actual Elapsed Time)

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The business hours on the milestone. If business hours aren’t specified, the
entitlement process business hours are used. If business hours are also not
specified on the entitlement process, the business hours on the record are used.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time the milestone was completed.


-----

```
CurrencyIsoCode
ElapsedTimeInDays
ElapsedTimeInHrs
ElapsedTimeInMins
IsCompleted

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days it took to complete a milestone, including time during which
the milestone was stopped. Automatically calculated to include the business
hours on the record. Elapsed time is calculated only after the Completion Date
field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes it took to complete a milestone, including time during
which the milestone was stopped. Automatically calculated to include the
business hours on the record. Elapsed time is calculated only after the Completion
Date field is populated. (Elapsed Time) – (Stopped Time) = (Actual Elapsed Time).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsViolated
MilestoneTypeId
Name
ParentEntityId
SlaProcessId
StartDate

```

**Description**
Green checkmark icon that indicates a milestone completion.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Red exclamation point icon that indicates a milestone violation.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the milestone (for instance, First Response).

**Type**
string

**Properties**
Filter, Group, Sort, Update

**Description**
The name of the milestone.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the record—for example, a work order—that contains the milestone.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entitlement process associated with the milestone.

**Type**
dateTime


-----

```
StoppedTimeInDays
StoppedTimeInHrs
StoppedTimeInMins

```

**Properties**
Filter, Nillable, Sort, Update

**Description**
The date and time that milestone tracking started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days that an agent has been blocked from completing a milestone.
For example, an agent may be waiting for a customer to reply with more
information.

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes that an agent has been blocked from completing a
milestone. For example, an agent may be waiting for a customer to reply with
more information.

Note: To display this field, select Enable stopped time and actual
**elapsed time on the Entitlement Settings page and add the field to the**
object milestone page layout.


-----

```
TargetDate
TargetResponseInDays
TargetResponseInHrs
TargetResponseInMins
TimeRemainingInDays
TimeRemainingInHrs

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time to complete the milestone.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of days to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The number of hours to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of minutes to complete the milestone. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string


-----

```
TimeRemainingInMins
TimeSinceTargetInDays
TimeSinceTargetInHrs
TimeSinceTargetInMins

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The hours that remain before a milestone violation. Automatically calculated to
include the business hours on the record.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The minutes that remain before a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The days that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The hours that have elapsed since a milestone violation. Automatically calculated
to include the business hours on the record.

**Type**
string

**Properties**
Group, Nillable, Sort

**Description**
The minutes that have elapsed since a milestone violation. Automatically
calculated to include the business hours on the record.


When you create an entitlement process, you select its type based on the type of record that you want the process to run on: Case or
Work Order. Processes created before Summer ’16 use the Case type. When a Work Order entitlement process runs on a work order, the


-----

resulting milestones on the work order are object milestones. Conversely, when a Case entitlement process runs on a case, the resulting
milestones are case milestones, a separate standard object.

Tip: If an entitlement has an entitlement process associated with it, don’t use the entitlement for multiple types of support records.
An entitlement process works only on records that match the process’s type. For example, when a Case entitlement process is
applied to an entitlement, the process runs only on cases associated with that entitlement. If a work order is also associated with
the entitlement, the process doesn’t run on the work order. To ensure that the milestones you set up work as expected, associate
a customer’s work orders and cases with different entitlements.

Customize page layouts, validation rules, and more for object milestones from the Object Milestones node in Setup under Entitlement
Management.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**EntityMilestoneFeed**

Feed tracking is available for the object.

**EntityMilestoneHistory**

History is available for tracked fields of the object.
