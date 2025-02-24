#### ServiceAppointment

Represents an appointment to complete work for a customer in Field Service, Lightning Scheduler,Intelligent Appointment Management,
and Virtual Care.This object is available in API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.


-----

##### Fields

**Field Name**
```
AccountId
ActualDuration
ActualEndTime
ActualStartTime

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The account associated with the appointment. If the parent record
is a work order or work order line item, this field’s value is inherited from the
parent. Otherwise, it remains blank.

This is a relationship field.

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The number of minutes that it took the resource to complete the appointment
after arriving at the address. When values are first added to the Actual
`Start` and Actual End fields, the Actual Duration is automatically
populated to list the difference between the `Actual Start` and Actual
`End. If the Actual Start` and Actual End fields are subsequently
updated, the `Actual Duration` field doesn’t re-update, but you can
manually update it.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The actual date and time the appointment ended.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update


-----

```
Address
AppointmentNumber
ArrivalWindowEndTime
ArrivalWindowStartTime
BundlePolicyId

```

**Description**
The actual date and time the appointment started.

**Type**
address

**Properties**
Filter

**Description**
The address where the appointment is taking place. The address is inherited from
the parent record if the parent record is a work order or work order line item.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-assigned number that identifies the appointment.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The end of the window of time in which the technician is scheduled to arrive at
the site. This window is typically larger than the Scheduled Start and End window
to allow time for delays and scheduling changes. You may choose to share the
Arrival Window Start and End with the customer, but keep the Scheduled Start
and End internal-only.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The beginning of the window of time in which the technician is scheduled to
arrive at the site. This window is typically larger than the Scheduled Start and
End window to allow time for delays and scheduling changes. You may choose
to share the Arrival Window Start and End with the customer, but keep the
Scheduled Start and End internal-only.

**Type**
reference


-----

```
City
ContactId
Country

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the bundle policy associated with this service appointment.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the appointment is completed. Maximum length is 40 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The contact associated with the parent record. If needed, you can manually
update the service appointment contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the work order is completed. Maximum length is 80 characters.


-----

```
Description
DueDate
Duration
DurationType
EarliestStartTime
GeocodeAccuracy

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the appointment.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date by which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

**Type**
double

**Properties**
Create, Nillable, Filter, Sort, Update

**Description**
The estimated length of the appointment. If the parent record is work order or
work order line item, the appointment inherits its parent’s duration, but it can
be manually updated. The duration is in minutes or hours based on the value
selected in the `Duration Type` field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of the Duration: Minutes or Hours.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date after which the appointment must be completed. Earliest Start Permitted
and Due Date typically reflect terms in the customer’s service-level agreement.

**Type**
picklist


-----

```
IsAnonymousBooking
IsBundle
IsBundleMember
IsManuallyBundled

```

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its
physical address. Usually provided by a geocoding service based on the address’s
latitude and longitude coordinates.

Note: This field is available in the API only.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a service resource was automatically assigned to the
appointment. The default value is false.

This field is available in API version 49.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle service appointment. The default
value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this service appointment is a bundle member service appointment.
The default value is false.

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this bundle was created manually. The default value is false.


-----

```
IsOffsiteAppointment
LastReferencedDate
LastViewedDate
Latitude
Longitude

```

This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Any type of work that can be done remotely.

This field is available in API version 58.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last modified. Its label in the user
interface is `Last Modified Date.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date when the service appointment was last viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with Longitude to specify the precise geolocation of the address where
the service appointments is completed. Acceptable values are numbers between
–90 and 90 with up to 15 decimal places.

To integrate data from an external data source for latitude, map your data to the
`ServiceAppointment.Latitude` and not the
```
  ServiceAppointment.FSL__InternalSLRGeolocation__Latitude__s

```
field.

Note: This field is available in the API only.

**Type**
double


-----

```
OwnerId
ParentRecordId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**

Used with Latitude to specify the precise geolocation of the address where
the service appointment is completed. Acceptable values are numbers between
–180 and 180 with up to 15 decimal places.

To integrate data from an external data source for longitude, map your data to
the ServiceAppointment.Longitude and not the
```
  ServiceAppointment.FSL__InternalSLRGeolocation__Longitude__s

```
field.

Note: This field is available in the API only.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the service appointment.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The parent record associated with the appointment. The parent record can’t be
updated after the service appointment is created.

This is a polymorphic relationship field.

**Relationship Name**
ParentRecord

**Relationship Type**
Lookup


-----

```
ParentRecordStatusCategory
ParentRecordType
PostalCode
RelatedBundleId

```

**Refers To**
Account, Asset, Lead, Opportunity, ServiceAppointmentGroup, WorkOrder,
WorkOrderLineItem

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
(Read only) The Status Category of the parent record. If the parent record
is a work order or work order line item, this field is populated; otherwise, it remains
blank.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
(Read only) The type of parent record: Account, Asset, Lead, Opportunity, Work
Order, or Work Order Line Item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the work order is completed. Maximum length is 20
characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The bundle that this service appointment is a member of.

This is a relationship field.

**Relationship Name**
RelatedBundle

**Relationship Type**
Lookup

**Refers To**
ServiceAppointment


-----

```
SchedEndTime
SchedStartTime
ServiceDocumentTemplate
ServiceTerritoryId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to end. If you are using the Field
Service managed package with the scheduling optimizer, this field is populated
once the appointment is assigned to a resource. Scheduled End –
`Scheduled Start` = Estimated Duration.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The time at which the appointment is scheduled to start. If you are using the
Field Service managed package with the scheduling optimizer, this field is
populated once the appointment is assigned to a resource.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The template ID which sets the template for each service document for the
Document Builder feature.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The service territory associated with the appointment. If the parent record is a
work order or work order line item, the appointment inherits its parent’s service
territory.

This is a relationship field.

**Relationship Name**
ServiceTerritory

**Relationship Type**
Lookup

**Refers To**
ServiceTerritory


-----

```
State
Status
StatusCategory
Street

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the service appointment is completed. Maximum length is 80
characters.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the appointment. The picklist includes the following values, which
can be customized:

**•** `None—Default value.`

**•** `Scheduled—Appointment has been assigned to a service resource.`

**•** `Dispatched—Assigned service resource has been notified about their`
assignment.

**•** `In Progress—Work has begun.`

**•** `Completed—Work is complete.`

**•** `Cannot Complete—Work could not be completed.`

**•** `Canceled—Work is canceled, typically before any work began`

While you can set the status to null via the API, setting the status to null returns
an error. To prevent errors, use one of the picklist values.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The category that each `Status` value falls into. The `Status Category`
field’s values are identical to the default Status values.

If you create custom `Status` values, you must indicate which category it
belongs to. For example, if you create a `Customer Absent` value, you may
decide that it belongs in the `Cannot Complete` category. To learn which
[processes reference StatusCategory, see How are Status Categories Used?](https://help.salesforce.com/articleView?id=fs_status_categories.htm&language=en_US)

**Type**
textarea


-----

```
Subject
WorkTypeId

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street number and name where the service appointment is completed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A short phrase describing the appointment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The work type associated with the service appointment. The work type is inherited
from the appointment’s parent record if the parent is a work order or work order
line item.

Note: If Lightning Scheduler is also in use, this field is editable. However,
users see an error if they update it to list a different work type than the
parent record’s work type.

This is a relationship field.

**Relationship Name**
WorkType

**Relationship Type**
Lookup

**Refers To**
WorkType


Service appointments always have a parent record, which can be a work order, work order line item, opportunity, account, or asset. The
type of parent record tells you about the nature of the service appointment:

**•** Service appointments on work orders and work order line items offer a more detailed view of the work being performed. While work
orders and work order line items let you enter general information about a task, service appointments are where you add the details
about scheduling and ownership.

**•** Service appointments on assets represent work being performed on the asset.

**•** Service appointments on accounts represent work being performed for the account.

**•** Service appointments on opportunities represent work that is related to the opportunity.


-----

**•** Service appointments on leads represent work that is related to lead—for example, a site visit to pursue a promising lead.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceAppointmentChangeEvent (API version 48.0)**
Change events are available for the object.

**ServiceAppointmentFeed**

Feed tracking is available for the object.

**ServiceAppointmentHistory**

History is available for tracked fields of the object.

**ServiceAppointmentOwnerSharingRule**

Sharing rules are available for the object.

**ServiceAppointmentShare**

Sharing is available for the object.
