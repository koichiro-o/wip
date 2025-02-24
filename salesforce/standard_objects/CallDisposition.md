#### CallDisposition

```


**•** `LearningAssignmentImplicit` — Learning Assignment Implicit Share

**•** `LearningItemAssignment — Learning Item Assignment Share`

**•** `Manual` — Manual Sharing

**•** `MfgTargetShare` — Manufacturing Target Sharing Rule

**•** `Owner`

**•** `Rule` — Sharing Rule

**•** `SharingRecordCollection — Record Collection`

**•** `SurveyShare` — Survey Sharing Rule

**•** `Team` — Sales Team

**•** `Territory` — Territory Assignment Rule

**•** `Territory2AssociationManual` — Territory Manual

**•** `Territory2Forecast — Territory assignment for forecasting and reporting`

**•** `TerritoryManual — Territory Manual`

**•** `TerritoryRule` — Territory Sharing Rule

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the User or Group that has been given access to the favorite transfer
destination.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


Represents a call result value that sales reps select when logging a call. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
Disposition
DispositionCategoryId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The result of a phone call, such as whether a call was connected or the rep left a voicemail.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The related call outcome that is used in reports and branching criteria for cadences.

