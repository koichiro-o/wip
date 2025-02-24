### Salesforce Scheduler Resources

```
Use Salesforce Scheduler REST APIs to get appointment time slots or available service resources based on work type groups and service
territories.

IN THIS SECTION:

Scheduling
Returns a list of available Salesforce Scheduler REST resources and corresponding URIs. This resource is available in REST API version
45.0 and later.

Get Appointment Slots
Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

Get Appointment Candidates
Returns a list of service resources (appointment candidates) based on work type group or work type and service territories.

Request Bodies

Response Bodies

SEE ALSO:

_[Connect REST API Developer Guide: Lightning Scheduler Resources](https://developer.salesforce.com/docs/atlas.en-us.252.0.chatterapi.meta/chatterapi/connect_resources_lightning_scheduler.htm)_

#### Scheduling

Returns a list of available Salesforce Scheduler REST resources and corresponding URIs. This resource is available in REST API version 45.0
and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/scheduling/

```
**Formats**
JSON, XML

**HTTP methods**
GET


-----

**Authentication**
```
  Authorization: Bearer token

##### Example

```
**Example Response Body**
```
  {
   "getAppointmentCandidates" : "/services/data/v62.0/scheduling/getAppointmentCandidates",
   "getAppointmentSlots" : "/services/data/v62.0/scheduling/getAppointmentSlots"
  }

#### Get Appointment Slots

```
Returns a list of available appointment time slots for a resource based on given work type group or work type and service territories.

The appointment time slots are determined based on your Salesforce Scheduler data model configurations. Here are some prerequisites
that you can consider while setting up data.

**•** Set up Salesforce Scheduler before making your requests. The setup includes creating or configuring Service Resources, Service
[Territory Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Manage](https://help.salesforce.com/s/articleView?id=sf.ls_set_up.xml&language=en_US)
[Business Information in Salesforce Scheduler for more information.](https://help.salesforce.com/s/articleView?id=sf.ls_set_up.xml&language=en_US)

**•** Configure a work type mapped for each territory in the request body via Service Territory Work Type. Map the same work type to
the work type group, via work type group member.

The following factors affect how time slots are calculated and returned.

**•** Timezones that differ across operating hours are handled and results are always returned in UTC.

**•** The resource must be marked as a required resource on the assigned resource object.

**•** The resource is considered unavailable If the status categories of the resource assigned to service appointments are other than
```
  Canceled, Cannot Complete, and Completed.

```
**•** Resource Absences of all types are considered unavailable from start to end.

**•** The following fields of Work Type records, if configured, are used to fine-tune time slot requirements. For more information, see
[Create Work Types in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=sf.ls_create_work_types.xml&language=en_US)

**Parameter** **Description**

`Timeframe Start` Time slots sooner than `current time + Timeframe Start aren’t`
returned.

`Timeframe End` Time slots later than `current time + Timeframe End` aren’t returned.

`Block Time Before Appointment` The time period before the appointment is considered as unavailable.

`Block Time After Appointment` The time period after the appointment is considered as unavailable.

```
Operating Hours

```

The overlap of all operating hours from the account, work type, service territory, and
service territory member are considered while determining time slots. For more
[information, see Set Up Operating Hours in Salesforce Scheduler.](https://help.salesforce.com/s/articleView?id=sf.ls_set_up_oh.htm&language=en_US)


-----

**•** Only the time slots within the period of 31 days from the start date are returned.

**•** Salesforce Scheduler uses multiple factors, such as field values, scheduled appointments, absences, Scheduler Settings, and Scheduling
[Policies to determine available time slots, including the earliest and latest appointment slots. See How Does Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=sf.ls_how_are_time_slots_determined.htm&language=en_US)
[Determine Available Time Slots.](https://help.salesforce.com/s/articleView?id=sf.ls_how_are_time_slots_determined.htm&language=en_US)

Note: If asset scheduling is enabled, you can provide an asset-based service resource in `requiredResourceIds` to
retrieve available timeslots for the asset resource.

##### Syntax

**URI**
```
  /services/data/vXX.X/scheduling/getAppointmentSlots

```
**Available version**
45.0

**Formats**
JSON, XML

**HTTP methods**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Request body**

**Parameter** **Required** **Type** **Description**

`accountId` No String The ID of the associated account.


`allowConcurrentScheduling` No Boolean


If true, allows scheduling of concurrent appointments in a time slot.
If false, concurrent appointments aren’t allowed. The default is false.

Available in API version 47.0 and later.


`correlationId` No String The ID to pass custom information to the
`ServiceResourceScheduleHandler` Apex interface. For

example, you can use the correlation ID to identify the app, website,
or any other external system that calls this Apex interface
implementation. If you don’t pass a custom value, a randomly
generated identifier is passed.

This field is available in API version 53.0 and later.

`endTime` No String The latest time that a time slot can end (inclusive).


`engagementChannelTypeIds` No String[]


The ID of the engagement channel type record. The availability of
time slots is filtered based on the engagement channel type
selected. This field is available in API version 56.0 and later.

Note: This field supports only one engagement channel
type ID.

You can use engagement channel types with the
`getAppointmentSlots` API only if:


-----

**•** The Schedule Appointments Using Engagement Channels
setting is enabled in Salesforce Scheduler Settings in your
Salesforce org.

**•** Shifts are defined in the scheduling policy. For more information
[on setting up shifts in scheduling policy, see Define Shift Rules](https://help.salesforce.com/s/articleView?id=sf.ls_use_shifts_to_determine_time_slots.htm&language=en_US)
[in Scheduling Policy.](https://help.salesforce.com/s/articleView?id=sf.ls_use_shifts_to_determine_time_slots.htm&language=en_US)

Note: Engagement channel types are not supported
with operating hours rules in the scheduling policy.

`primaryResourceId` No String The ID of the primary resource in multi-resource scheduling. This
field is available in API version 48.0 and later.

Note: This field is required only when multi-resource
scheduling is enabled.

`requiredResourceIds` Yes String[] List of resource IDs that must be available during the time slot.

`schedulingPolicyId` No String The ID of the AppointmentSchedulingPolicy object. If no scheduling
policy is passed in the request body, the default configurations are

used. The only scheduling policy configuration that is used in
determining time slots is the enforcement of account visiting hours.

`startTime` No String The earliest time that a time slot can begin (inclusive). Defaults to
the current time of the request, if empty.

`territoryIds` Yes String[] List of IDs of service territories, where the work that is being
requested is performed.

`workType` Required if Work Type The type of the work to be performed.
```
              workTypeGroupId

```
isn’t
specified.

```
workTypeGroupId

```

Required if String The ID of the work type group containing the work types that are
`workType` being performed.
isn’t given.


Note: To determine the required fields in your request body, consider the following points:

**•** Provide either the `workTypeGroupId` or `workType` parameter in your request body, but not both.

**•** If the `workType parameter is specified, then you must provide either the` `id or durationInMinutes parameter.`

**•** If `id` of the `workType` parameter is specified, then the rest of the `workType` fields are optional.

**Response Body**
Execution of a successful request returns the response body containing a list of available time slots.


-----

`timeSlots` Yes

##### Example

**Example Request Body**
Using `workTypeGroupId:`
```
  {
   "startTime": "2019-01-23T00:00:00.000Z",
   "endTime": "2019-02-28T00:00:00.000Z",
   "workTypeGroupId": "0VSB0000000KyjBOAS",
   "accountId": "001B000000qAUAWIA4",
   "territoryIds": [
    "0HhB0000000TO9WKAW"
   ],
   "schedulingPolicyId": "0VrB0000000KyjB",
   "requiredResourceIds": [
    "0HnB0000000TO8gKAK"
   ],
   "engagementChannelTypeIds": [
    "0eFRM00000000Bv2AI"
   ]
  }

```
Using `workType:`
```
  {
   "startTime": "2019-01-23T00:00:00.000Z",
   "endTime": "2019-02-28T00:00:00.000Z",
   "workType": {
    "id": "08qRM00000003fkYAA"
   },
   "requiredResourceIds": [
    "0HnB0000000TO8gKAK"
   ],
   "territoryIds": [
    "0HhRM00000003OZ0AY"
   ],
   "accountId": "001B000000qAUAWIA4",
   "schedulingPolicyId": "0VrB0000000KyjB",
   "engagementChannelTypeIds": [
    "0eFRM00000000Bv2AI"
   ]
  }

```
**Example Response Body**


TimeSlots List of time slots included in each territory.
on page
340[]


-----

#### Get Appointment Candidates

Returns a list of service resources (appointment candidates) based on work type group or work type and service territories.

Set up Salesforce Scheduler before making requests. This setup includes creating or configuring Service Resources, Service Territory
[Members, Work Type Groups, Work Types, Work Type Group Members, and Service Territory Work Types. See Set Up Salesforce Scheduler](https://help.salesforce.com/s/articleView?id=sf.ls_set_up.htm&language=en_US)
for more information.

The appointment time slots are determined based on multiple factors, such as field values, scheduled appointments, absences, Scheduler
[Settings, and Scheduling Policies to determine available time slots. See How Salesforce Scheduler Determines Available Time Slots for](https://help.salesforce.com/s/articleView?id=sf.ls_how_are_time_slots_determined.htm&language=en_US)
more information.

The following factors are considered for returning start time and end time of resources.

**Resource Availability**
Determined using service territory member, service territory, work type, and account operating hours fields.

**Resource Unavailability**
Determined by resource absences, existing appointments that the resource is assigned to. The resource must be marked as a required
resource for the appointment with a status that isn’t in closed, canceled, or completed.

**Appointment Start Time Interval in the Scheduling Policy**
Appointment start time interval field in the Scheduling Policy is used to determine when the appointment can start. This interval
can be 5, 10, 15, 20, 30, or 60. By default, it’s set to 15.

**Work Type Duration**
The end time is calculated as start time + duration of the work type.

Note: If asset scheduling is enabled, the response also includes asset-based candidates.

##### Syntax

**URI**
```
  /services/data/vXX.X/scheduling/getAppointmentCandidates

```
**Available version**
45.0


-----

**Formats**
JSON, XML

**HTTP methods**
POST

**Request body**

**Parameter** **Required** **Type** **Description**

`accountId` No String The ID of the associated account.


`allowConcurrentScheduling` No Boolean


If true, allows scheduling of concurrent appointments in a time slot.
If false, concurrent appointments aren’t allowed. The default is false.

This field is available in API version 47.0 and later.


`correlationId` No String The ID to pass custom information to the
`ServiceResourceScheduleHandler` Apex interface. For

example, you can use the correlation ID to identify the app, website,
or any other external system that calls this Apex interface
implementation. If you don’t pass a custom value, a randomly
generated identifier is passed.

This field is available in API version 53.0 and later.

`endTime` No String The latest time that a time slot can end (inclusive).

Note: The API only returns time slots up to 31 days from
the `startTime.`


`engagementChannelTypeIds` No String[]


The ID of the engagement channel type record. The availability of
service resources is filtered based on the engagement channel type
selected. This field is available in API version 56.0 and later.

This field supports only one engagement channel type ID.

You can use engagement channel types with the
```
getAppointmentCandidates API only if:

```
**•** The Schedule Appointments Using Engagement Channels
setting is enabled in Salesforce Scheduler Settings in your
Salesforce org.

**•** Shifts are defined in the scheduling policy. For more information
[on setting up shifts in scheduling policy, see Define Shift Rules](https://help.salesforce.com/s/articleView?id=sf.ls_use_shifts_to_determine_time_slots.htm&language=en_US)
[in Scheduling Policy.](https://help.salesforce.com/s/articleView?id=sf.ls_use_shifts_to_determine_time_slots.htm&language=en_US)

Note: Engagement channel types are not supported
with operating hours rules in the scheduling policy.


`filterByResources` No String[] A comma-separated list of service resource IDs. API returns only
eligible service resources that are both in the list and in the selected

service territory. The resources are sorted by the order in which the
resource IDs are passed. Available in API version 51.0 and later.


-----

`resourceLimitApptDistribution` No Integer

`startTime` No String


Note: Scheduler doesn’t support appointment Distribution
when you’ve specified a list of resource IDs in the
filterByResources parameter.

Specify the maximum number of service resources that you want
to show during appointment scheduling when appointment
distribution is enabled. Available in API version 53.0 and later.

Note: The filterByResources field takes precedence over the
resourceLimitApptDistribution field.

The earliest time that a time slot can begin (inclusive). Defaults to
the current time of the request, if empty. You can also use a time
from the past.


`schedulingPolicyId` No String The ID of the AppointmentSchedulingPolicy object. If no scheduling
policy is passed in the request body, the default configurations are

used. All Scheduling Policy Configurations are considered when
using this API.

`territoryIds` Yes String[] List of service territory IDs, where the work that is being requested
is performed.

```
workType
workTypeGroupId

```

Required if Work Type The type of the work to be performed.
```
workTypeGroupId

```
isn’t given.

Required if String The ID of the work type group containing the work types that are
`workType` being performed.
isn’t given.


Note: To determine the required fields in your request body, consider the following points:

**•** Provide either the `workTypeGroupId` or `workType` parameter in your request body, but not both.

**•** If the `workType parameter is specified, then you must provide either the` `id or durationInMinutes parameter.`

**•** If `id` of the `workType` parameter is specified, then the rest of the `workType` fields are optional.

**Response Body**
Execution of a successful request returns the response body containing a list of available appointment resources.


`candidates` Yes


Candidates List of available appointment candidates.
on page
341[]


-----

##### Examples

**Example Request Body**
Using `workTypeGroupId:`
```
  {
   "accountId": "001B000000qAUAWIA4",
   "territoryIds": [
    "0HhB0000000TO9WKAW"
   ],
   "engagementChannelTypeIds": [
    "0eFRM00000000Bv2AI"
   ]
  }

```
Using `workTypeId:`
```
  {
   "workType": {
    "id": "08qRM00000003fkYAA"
   },
   "territoryIds": [
    "0HhRM00000003OZ0AY"
   ],
   "accountId": "001B000000qAUAWIA4",
   "engagementChannelTypeIds": [
    "0eFRM00000000Bv2AI"
   ]
  }

```
**Example Response Body**


-----

#### Request Bodies

To perform a POST, PATCH, or PUT request, create a request body formatted in either XML or JSON. This chapter lists the request bodies.

IN THIS SECTION:

Work Type
Details about the type of work to be performed.

Skill Requirement
List of skills that are required to complete a particular task for a work type.

##### Work Type

Details about the type of work to be performed.


`id` String


Required if Id of the work type.
```
durationInMinutes

```
is not given.


`durationInMinutes` Integer Required if id is not Contains the event length, in minutes.
given.

`timeframeStartInMinutes` String No The beginning of the timeframe.

`timeframeEndInMinutes` String No The end of the timeframe.

`blockTimeBeforeAppointmentInMinutes` String No The time period before the appointment is considered as
unavailable.


-----

`blockTimeAfterAppointmentInMinutes` String No The time period after the appointment is considered as
unavailable.


`operatingHoursId` String No


The overlap of all operating hours from the account, work
type, service territory, and service territory member are
considered while determining time slots.


`skillRequirements` Skill Requirement[] No List of skills that are required to complete a particular task
for a work type.

Note: Provide either `Id` or `durationInMinutes` in the request body, but not both.

##### Skill Requirement

List of skills that are required to complete a particular task for a work type.

**Name** **Type** **Required** **Description**

`skillId` String Yes The skill that is required.

`SkillLevel` String No The level of the skill required. Skill levels can range from
zero to 99.99. Depending on your business needs, you might

want the skill level to reflect years of experience, certification
levels, or license classes.

#### Response Bodies

Successful execution of a request to a Salesforce Scheduler resource can return a response body either in JSON or XML format. For
example, the request to get appointment time slots returns a list of available time slots for a selection of work type group and territories.

IN THIS SECTION:

Time Slots
Describes the result of Get Appointments Slots request.

Candidates
Describes the result of Get Appointments Candidates request.

##### Time Slots

Describes the result of Get Appointments Slots request.

List of time slots available for each territory.

**Name** **Type** **Description**

`endTime` String The end time of the appointment time slot.


-----

Results


`engagementChanneltypeIds` String[] The engagement channel type ID associated with this time slot. This
field is available in API version 56.0 and later.


`remainingAppointments` Integer


The number of appointments available in the time slot.
```
Appointments available in a time slot =
Maximum number of appointments defined for the
time slot - Number of appointments scheduled
so far in the time slot

```

`startTime` String The start time of the appointment time slot.

`territoryId` String The service territory associated with this time slot.

##### Candidates

Describes the result of Get Appointments Candidates request.

List of available service resources.

**Name** **Type** **Description**

`endTime` String The end time of the appointment time slot.

`engagementChanneltypeIds` String[] The engagement channel type ID associated with this resource for that
time slot. This field is available in API version 56.0 and later.

`resources` String[] List of service resource IDs that are available.

Important: At present, only one resource is returned on this list.
If there is more than one resource included in a territory, a new
child object is added for each resource in the response JSON
body.

`startTime` String The start time of the appointment time slot.

`territoryId` String The service territory associated with this resource.
