#### ForecastingSubmission

Represents a submitted forecast. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available for forecast types that aren’t grouped by product family forecast.

##### Fields

```
CurrencyIsoCode
ForecastOwnerId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The currency code of the forecast submission. If omitted, the default is USD.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast owner.

This field is a relationship field.

**Relationship Name**
ForecastOwner


-----

```
ForecastingGroupItemId
ForecastingTypeId
IsLatest
Name

```

**Refers To**
User

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use. Forecast submissions aren't supported in forecast types with groups.

**Relationship Name**
ForecastingGroupItem

**Refers To**
ForecastingGroupItem

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the forecast type.

This field is a relationship field.

**Relationship Name**
ForecastingType

**Refers To**
ForecastingType

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if the forecast submission is the most recent submission.

The default value is `false.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only. ID of this record.


-----

```
Note
PeriodId
PeriodStartDate
ProductFamily
SubmissionDateTime

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
The note attached to the submitted forecast.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the period to which the submission applies.

This field is a relationship field.

**Relationship Name**
Period

**Refers To**
Period

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Indicates the start date of the forecast period.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Must be set to `none. Forecast submissions aren't supported in forecast types grouped by`
product families.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time that the forecast submission was made. Calculated internally.


-----

```
Territory2Id

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the territory to forecast on.

This field is a relationship field.

**Relationship Name**
Territory2

**Refers To**
Territory2


ForecastingSubmission is a detail object that contains the submitted item category values. Each record represents the values for a single
item category. ForecastingSubmission is always used as a detail object for the submission, and inserted only as part of a transaction that
includes all detail objects.
