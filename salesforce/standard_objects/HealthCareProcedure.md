#### HealthCareProcedure

Represents information related to industry-standard healthcare procedure codes.

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

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Category of the procedure code such as anesthesia, surgery, radiology, and so
on.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Industry standard procedure code such as CPT or HCPCS.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
CodeShortDescription
CodeType
EffectiveDate
EndDate
IsActive
LastReferencedDate

```

**Description**

Description of the procedure code.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Short description of the procedure code.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**

Type of procedure code represented in the record such as CPT or HCPCS.

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
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the diagnosis code is available for use.

**Type**
dateTime


-----

```
LastViewedDate
Name
OwnerId

```

**Properties**
Filter, Nillable, Sort

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
95115: Allergy injection.

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


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**[HealthCareProcedureChangeEvent (API version 60.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.

**[HealthCareProcedureHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[HealthCareProcedureOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[HealthCareProcedureShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
