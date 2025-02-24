#### ProcessInstanceWorkitem

Represents a user’s pending approval request.

Note: Exceptions apply to approval history data retrieved with this object and are available only via SOAP API. For each approval
process instance that was pending when Summer '14 became available for your organization, some field values are never populated
or are populated only after the rollout. Other fields are populated only after the approval process instance is next acted upon—such
as when a user approves, rejects, or reassigns an approval request—after the Summer '14 rollout.

ProcessInstanceWorkitem fields are never populated for approval process instances that were completed before the Summer ’14 rollout.
For approval process instances that were pending during the Summer ’14 rollout, all ProcessInstanceWorkitem fields are populated after
the approval process instance is next acted upon after the Summer ’14 rollout, with three exceptions. The `ElapsedTimeInDays,`
`ElapsedTimeInHours, and` `ElapsedTimeInMinutes` fields are never populated in ProcessInstanceWorkitem records for
which equivalent ProcessInstanceStep records were created before the Summer ’14 rollout.

For all other ProcessInstanceWorkitem records, these three fields are populated after the approval process instance is next acted upon
after the Summer ’14 rollout.

ProcessInstanceHistory combines fields from ProcessInstanceStep and ProcessInstanceWorkitem. As a result, incorrect elapsed times of
0 can appear in ProcessInstanceHistory records because the elapsed time fields were never populated in the related
ProcessInstanceWorkitem record.

Note: Knowledge articles use ProcessInstanceWorkitem records to track the article history, so ProcessInstanceWorkitems records
associated with Knowledge articles can’t be deleted.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve(), update()

 Fields

```
```
ActorId

```

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user responsible for approving an approval request.


-----

```
ElapsedTimeInDays
ElapsedTimeInHours
ElapsedTimeInMinutes
OriginalActorId

```

This field is a polymorphic relationship field.

**Relationship Name**
Actor

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in days since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in hours since this approval request was started.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The total time in minutes since this approval request was started.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the user originally assigned this approval request.

This field is a polymorphic relationship field.

**Relationship Name**
OriginalActor

**Relationship Type**
Lookup


-----

```
 ProcessInstanceId

##### Usage

```

**Refers To**
Group, User

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
ID of the ProcessInstance associated with this approval request.

This field is a relationship field.

**Relationship Name**
ProcessInstance

**Relationship Type**
Lookup

**Refers To**
ProcessInstance


Use this object to manage a pending approval request for a user.

SEE ALSO:

ProcessInstance

ProcessInstanceHistory

ProcessInstanceStep
