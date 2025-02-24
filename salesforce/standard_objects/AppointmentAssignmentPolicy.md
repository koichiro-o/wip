#### AppointmentAssignmentPolicy

Stores information about resource assignment rules. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
FullName
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name of the AppointmentAssignmentPolicy object.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the appointment assignment policy.

Possible values are:

**•** `Possible` values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US` (English)

**•** `es` (Spanish)

**•** `es_MX` (Spanish - Mexican)

**•** `fi` (Finnish)

**•** `fr` (French)

**•** `it` (Italian)

**•** `ja` (Japanese)

**•** `ko` (Korean)

**•** `nl_NL` (Dutch)

**•** `no` (Norwegian)

**•** `pt_BR` (Portuguese - Brazilian)

**•** `ru` (Russian)

**•** `sv` (Swedish)

**•** `th` (Thai)

**•** `zh_CN` (Chinese - Simplified)

**•** `zh_TW` (Chinese - Traditional)


-----

```
MasterLabel
PolicyApplicableDuration
PolicyType
UtilizationFactor

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the appointment assignment policy.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The frequency at which the utilization of service resources is calculated. This field is available
in API version 53.0 and later.

Possible values are:

**•** `Parameter-Based`

**•** `Monthly`

**•** `Weekly`

The default value is Parameter-Based.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of appointment assignment policy.

Possible values are:

**•** `loadBalancing`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the count type for the resource utilization. This field is available in API version 53.0
and later.

Possible values are:

**•** `NumberOfAppointments`

**•** `TotalAppointmentDuration`

The default value is TotalAppointmentDuration.


-----
