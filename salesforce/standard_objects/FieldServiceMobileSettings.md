#### FieldServiceMobileSettings

Represents a configuration of settings that control the Field Service iOS and Android mobile app experience. This object is available in
API version 38.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
AscAutomaticMode

```
AscCancellationTimerInSec

AscCompletedStatus


**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Describes how status changes are handled. Possible values are:

**•** `Off—No automatic status changes.`

**•** `Manual—The mobile worker can cancel or update the status change.`

**•** `Timed—The mobile worker has a time period to prevent the status change.`
When the timer ends, the status changes.

**•** `Automated—The mobile worker is notified that the status has changed.`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
For the Timed mode only. Time that the user has to cancel the appointment
status change.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
AscOnSiteStatus
AscRadiusInMeters
AscTimeLimitationInMin

```

**Description**
Status that indicates that a mobile worker completed a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is at a service appointment. Possible
values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Service appointment radius that can trigger a status change.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
AscTravelStatus
BgGeoLocationAccuracy
BgGeoLocationMinUpdateFreqMins

```

**Description**
A time period when status changes can occur, before an appointment’s scheduled
start time and after the scheduled end time. The time is applied only if
IsAscTimeLimitEnabled is `true.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status that indicates that a mobile worker is traveling to a service appointment.
Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of geolocation tracking of services resources while the app is running
in the background. Lowering accuracy reduces battery consumption for mobile
devices. Available in API version 41.0 and later. Picklist options:

**•** `Medium—Accurate to within about 100 meters.`

**•** `Coarse—Accurate to within about 1 kilometer.`

**•** `Very Coarse—Accurate to within about 3 kilometers.`

The default value is `Coarse.`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The frequency of geolocation poling of services resources while the app is running
in the background. Less frequent poling decreases battery consumption for


-----

```
BrandInvertedColor
ContrastInvertedColor
ContrastPrimaryColor
ContrastQuaternaryColor
ContrastQuinaryColor
ContrastSecondaryColor

```

mobile devices. The label in the UI is Minimum Update Frequency of Geo
**Location in Minutes (Background). Available in API version 41.0 and later.**

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of toasts and the contrast color of the floating action button.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary text.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of secondary lines that delineate different areas of the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of primary backgrounds in the UI.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
ContrastTertiaryColor
DaysBeforeCurrentServiceDate
DayAfterCurrentServiceDate
DefaultListViewDeveloperName

```
DestinationType


**Description**
The color of secondary text.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the icons on the settings screen and of primary lines that delineate
different areas of the UI.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days before the current service date during which to prime service documents
for offline use.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Days after the current service date during which to prime service documents for
offline use.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The API name of the default service appointment list view on the schedule screen.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Determines if the mobile worker navigates to the destination based on the address
or based on the latitude and longitude. Possible values are:

**•** `Address`


-----

```
DeveloperName
FeedbackPrimaryColor
FeedbackSecondaryColor
FeedbackSelectedColor
FutureDaysInDatePicker

```


**•** `Latitude and Longitude`

The default value is `Address.`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the set of field service mobile settings.

Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of error messages.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of success messages.

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The color indicating the user’s current selection.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the future that a user can select from the date picker
on the schedule screen.


-----

```
GeoLocationAccuracy
GeoLocationMinUpdateFreqMins
IsAscTimeLimitEnabled
IsAssignmentNotification
IsDefault

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The accuracy of service resource geolocation tracking. Lowering accuracy reduces
battery consumption for mobile devices. Picklist values:

**•** `Fine—Accurate to within 10 meters.`

**•** `Medium—Accurate to within 100 meters.`

**•** `Coarse—Accurate to within 1 kilometer.`

The default value is `Medium.`

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to poll geolocation.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether AscTimeLimitationInMin is applied. Default is `true`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is assigned the appointment. Default is `false. This field is available`
in API version 46.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
IsDispatchNotification

```
IsLimitedLocTrackingEnabled

IsOptimizedImageUploadEnabled
```
IsScheduleViewResourceAbsences

```

**Description**
Indicates that the set of field service mobile settings is the default set that is
automatically assigned to users. You can’t make a different settings record the
default, but you can modify the default settings record. Default is `false.`
Available in API version 41.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether service appointment notifications are sent when the service
resource is dispatched for the appointment. Default is `false. This field is`
available in API version 46.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
When limited tracking for Appointment Assistant is enabled, the mobile worker’s
location is shown only on the way to a service appointment. The default value
is false.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether to configure the size of images uploaded by your mobile
workers. To optimize upload speeds, you can limit your file size to a defined
maximum size using the OptimizeImageSizeInMb field. Resizing your images
affects the resolution of your images. The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether resource absences appear in the Schedule tab of the mobile
app. This field is available in API version 55.0 and later.


-----

```
IsSendLocationHistory
IsShowEditFullRecord
IsTimeSheetEnabled
IsTimeZoneEnabled
IsUseSalesforceMobileActions

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether geolocation tracking of services resources is enabled. Default
is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can edit records with the field service mobile app. Default
is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether users can access time sheets on their mobile devices (Beta).
Default is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Controls whether the time zone of timesheet entries on the mobile app is
recorded. The current time zone is recorded in the LocationTimeZone field
of the TimeSheetEntry object. Default is `false. Available in API version 50.0`
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Reserved for future use.


-----

```
Language
MasterLabel
MaxNumberOfServiceAppointments
MetadataCacheTimeDays
NavbarBackgroundColor

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The localization preference for a user. The format is a two letter language code
and, if there’s a dialect, followed by the two letter dialect, for example, `fr` for
French, and fr_BE for Belgian French

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label in the UI for the set of field service mobile settings. Available in API
version 41.0 and later.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Sets the maximum number of service appointments to use for offline priming
of service documents. If you don’t have dates on your service appointments, this
setting helps to optimize offline priming in place of
```
  DaysBeforeCurrentServiceDate and
  DaysBeforeCurrentServiceDate fields.

```
**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days that org metadata, such as layouts, is kept in the app’s local
cache of memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of the top bar in the app.


-----

```
NavbarInvertedColor

```
OptimizeImageSizeInMb
```
PastDaysInDatePicker
PrimaryBrandColor
QuickStatusChangeFlowName

```

**Type**
string

**Properties**
Create, Defaulted on create, Group, Sort, Update

**Description**
The secondary color of the tap bar in the app.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Configure the size of images uploaded by your mobile workers. To optimize
upload speeds, you can limit your file size to a defined maximum size. Resizing
your images affects the resolution of your images. Enter 0.2 or higher. Used only
if IsOptimizedImageUploadEnabled is true.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of days into the past that a user can select from the date picker on
the schedule screen.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The main branding color used throughout the UI.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of an existing Field Service flow with a Quick Status Change action to
change the work order or service appointment status or both. This applies to
flows invoked on the mobile app only. This field is available in API version 51.0
and later.


-----

```
RecordDataCacheTimeMins
SecondaryBrandColor
TimeIntervalSetupMins
UpdateScheduleTimeMins

##### Usage

```

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The number of minutes that record data is kept in the app’s local cache of
memory.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The color of action buttons.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Controls the spacing of picklist options for time values such as when creating
resource absences.

**Type**
int

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The minimum number of minutes between attempts to update a user’s
schedule.The user’s schedule might not refresh on this cadence if the user’s
device isn’t connected to a network or doesn’t have adequate battery life.


Field Service Mobile settings allow you to create sets of settings to apply to different field service mobile users. The settings apply to
both the Android and iOS versions of the app.

For example, suppose you want to accommodate workers that are color blind, or who work in dark or bright conditions. You can choose
different branding options for different workers to suit their needs, and assign them to their profiles.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**FieldServiceMobileSettingsChangeEvent (API version 55.0)**
Change events are available for the object.
