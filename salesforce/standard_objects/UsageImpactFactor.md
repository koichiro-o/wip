#### UsageImpactFactor

Represents a collection of fields to set up the Usage Impact Factors used across jurisdictions and programs.This object is available in API
version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only with the EAndU Cloud Usage Impact Access permission set.


-----

##### Fields

**Field**
```
IsActive
Name
ShortForm
Type

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Usage Impact Factor is active.

The default value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Usage Impact Factor.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The acronym of the Usage Impact Factor.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of Usage Impact Factor

Possible values are:

**•** `AdjustedGrossAnnual—Adjusted Gross Annual`

**•** `AdjustedGrossAnnualMMBTU—Adjusted Gross Annual MMBTU`

**•** `AdjustedGrossAnnualkW—Adjusted Gross Annual kW`

**•** `AdjustedGrossAnnualkWSummer—Adjusted Gross Annual kW Summer`

**•** `AdjustedGrossAnnualkWWinter—Adjusted Gross Annual kW Winter`

**•** `AdjustedGrossAnnualkWh—Adjusted Gross Annual kWh`

**•** `GrossAnnualMMBTU—Gross Annual MMBTU`

**•** `GrossAnnualkW—Gross Annual kW`

**•** `GrossAnnualkWh—Gross Annual kWh`


-----

**•** `NetAnnual—Net Annual`

**•** `NetLifetime—Net Lifetime`

**•** `NetToGross—Net To Gross`

**•** `NetToGrossFR—Net To Gross FR`

**•** `UsefulLife—Useful Life`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[UsageImpactFactorChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[UsageImpactFactorFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[UsageImpactFactorHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[UsageImpactFactorOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[UsageImpactFactorShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
