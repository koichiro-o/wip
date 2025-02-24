#### FieldServiceOrgSettings

Represents the org settings for Field Service, such as Appointment Assistant settings. If Field Service is enabled, the org contains one
read-only record of this object. This object is available in API version 51.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To see this object, Field Service must be enabled. For specified fields in the table, Appointment Assistant must also be enabled.

##### Fields

```
ApptAssistantExpiration
ApptAssistantInfoUrl
ApptAssistantRadiusUnit

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The expiry time in minutes of when the customer stops seeing the mobile worker’s location.
Appointment Assistant must also be enabled to see this field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The page URL that enables Appointment Assistant. Appointment Assistant must also be
enabled to see this field.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The unit of the radius of the service appointment that prompts the Last Mile event for
Appointment Assistant. Appointment Assistant must also be enabled to see this field.


-----

```
ApptAssistantRadiusValue
ApptAssistantStatus
CanPopulateGoogleAddress

```

Possible values are:

**•** `Kilometer`

**•** `Meter`

**•** `Mile`

**•** `Yard`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The radius of the service appointment that prompts the Last Mile event for Appointment
Assistant. Appointment Assistant must also be enabled to see this field.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The value that prompts the En Route event for Appointment Assistant. Appointment Assistant
must also be enabled to see this field.

Possible values are:

**•** `Canceled`

**•** `Cannot Complete`

**•** `Completed`

**•** `Dispatched`

**•** `In Progress`

**•** `None`

**•** `Scheduled`

**•** `TestSharing`

The default value is 'None'.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows desktop and mobile to send geolocation and map data to Google and Apple. Available
in API version 57.0 and later.

The default value is `true.`


-----

```
CanSendAppCenterCrashReports
CanStoreMobileAnalytics
DeveloperName
DoesAvlCalcInclOvertime
DoesAvlCalcInclPrimOnly

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows Salesforce to send crash reports to Microsoft App Center. Available in API version 57.0
and later.

The default value is `true.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows third parties to store mobile analytics. Available in API version 57.0 and later.

The default value is `true.`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name of the object in the API.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether overtime is included in work capacity availability calculations. Available
in API version 59.0 and later.

The default value is `false.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Language
MasterLabel
