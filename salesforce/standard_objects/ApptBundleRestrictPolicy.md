#### ApptBundleRestrictPolicy

Policy that defines the restrictions that are considered while forming a bundle. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
**•** Field Service must be enabled.

**•** Bundling must be enabled in the Field Service Settings.

**•** The Field Service Admin, Field Service Bundle for Dispatcher, and Field Service Integration permission sets must be enabled.

##### Fields

```
BundlePolicyId
DoesAllowEmpty
DoesRestrictAutomaticMode

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the parent bundle policy.

This is a relationship field.

**Relationship Name**
BundlePolicy

**Relationship Type**
Lookup

**Refers To**
ApptBundlePolicy

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Allows a bundle member service appointment with an empty Restriction Field Name to be
bundled.

**Type**
boolean


-----

```
DoesRestrictManualMode
IsRestrictByDateOnly
LastReferencedDate
LastViewedDate
Name

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the automatic mode.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want to apply this restriction when using the manual mode.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if you want the bundle to be restricted according to the calendar date only, ignoring
the time of day.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
RestrictionFieldName

```

**Description**
The name of the appointment bundle restriction policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Name of the field in the service appointment used for applying the restriction.

Possible values are: All default and custom Service Appointment fields.

