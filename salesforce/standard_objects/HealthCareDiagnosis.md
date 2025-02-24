#### HealthCareDiagnosis

Represents information related to industry-standard healthcare diagnosis codes.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
Category
Code
CodeDescription
CodeType

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates the category for this diagnosis such as newborn, pediatric, maternity,
or adult.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry-standard diagnosis code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Description of the diagnosis code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Type of diagnosis code represented in the record such as ICD-9 or ICD-10.


-----

```
EffectiveDate
EndDate
Gender
IsActive
IsComplicationOrComorbidity
IsHospitalAcquiredCondition

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Start date for the code.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

End date for the code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Indicates whether this diagnosis is for males, females, or all genders.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the diagnosis code is available for use.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a complication or
comorbidity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
IsMajorComplicationOrComorbidity
IsPresentOnAdmissionExempt
IsPrimaryDiagnosis
IsUnacceptablePrincipalDxIpAdmit
LastReferencedDate

```

**Description**

Indicates whether this diagnosis represents a condition acquired while in the
hospital.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether this diagnosis is used to represent a major complication or
comorbidity.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is exempt from the diagnosis present on
admission requirement.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code can be used as primary diagnosis only, or can
be used in any diagnosis sequence.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether diagnosis code is an unacceptable principal diagnosis for
inpatient admission per Medicare Code Edits.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId

##### Associated Objects

```

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate) and not
viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

The name of the code that displays in search and lookup fields. Salesforce
recommends using the code along with the description to populate this field.
For example, use <Code>: <Description> or <Code>-<Description> such as
(E08.37X9 - Diabetes mellitus due to underlying condition).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who owns this record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


This object has the following associated objects. Unless noted, they are available in the same API version as this object.


-----

**[HealthCareDiagnosisChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareDiagnosisHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareDiagnosisOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareDiagnosisShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
