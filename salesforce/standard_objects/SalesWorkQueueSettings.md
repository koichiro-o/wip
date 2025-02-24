#### SalesWorkQueueSettings

Represents settings used to customize work queue options for third-party scoring. Third-party scoring enables custom number fields
on person accounts, contacts, and leads. You must be a Sales Engagement customer to update this object. Previously, you could only
use the Einstein Intelligence Score for third-party scoring. Available starting in Version 47.0.

Note: This object can’t be packaged.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
FeatureName
TargetEntity

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
A value that represents the name of the work queue settings.

To use custom number fields in the work queue, the value must be entered as
```
  ThirdPartyScore.

```
**Type**
picklist


-----

```
TargetField

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The related record object of the custom number field. Acceptable SObjects include
PersonAccount, Contact, and Lead.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A value that represents the DeveloperName of the custom number field related to the
TargetEntity. Custom fields must have a custom number data type.

**•** To use Einstein Intelligence Score for lead scoring, enter
`ScoreIntelligence.Score` for the DeveloperName.

**•** To remove custom number fields from the work queue, enter `None.`

