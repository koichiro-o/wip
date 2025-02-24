#### FieldSecurityClassification

Represents a field’s data sensitivity value selected from the SecurityClassification picklist. This object is available in API version 46.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To view this object, you need the Customize Application or Modify Data Classification permission.

##### Fields

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The API name of the data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential


-----

```
Description
IsHighRiskLevel
MasterLabel
SortOrder

##### Usage

```


**•** Restricted

**•** MissionCritical

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the data sensitivity picklist value.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates that fields with this picklist value contain data highly sensitive to your
company.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The data sensitivity picklist value. Default values:

**•** Public

**•** Internal

**•** Confidential

**•** Restricted

**•** MissionCritical

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value’s position in the picklist.


Use this object to return information about data sensitivity values in the SecurityClassification picklist. This object is read-only, but you
[can update the SecurityClassification picklist using the StandardValueSet Metadata API type.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_standardvalueset.htm)


-----
