#### MLModelFactorComponent

Represents information about the related MLModelFactor. For example, this object can represent a field value or a field range such as
“Title = CEO” or “Annual Revenue >10000000”. This object is available in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available with Einstein Prediction Builder and Einstein Recommendation Builder.

##### Fields

```
FactorLabelKey
FeatureType

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Maps the model factor component to a label that can be displayed to the user.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
`FeatureType` and FeatureValue indicate a feature that doesn’t have a corresponding
field. For example, to indicate the feature “Percent = 97%”, the FeatureType is Percent
and the `FeatureValue` is `97.`

Possible values are:


-----

```
FeatureValue
LeftHandDerivedField
ModelFactorId

```


**•** `Binary`

**•** `Combobox`

**•** `Currency`

**•** `Date`

**•** `DateTime`

**•** `Email`

**•** `ID`

**•** `Integral`

**•** `MultiPicklist`

**•** `Percent`

**•** `Phone`

**•** `Picklist`

**•** `Real`

**•** `Text`

**•** `TextArea`

**•** `URL`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The feature’s value. See `FeatureType.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If the model factor component is an equation, this field represents the name of the field on
the left side of the equation. For example, if the model factor component is `Title =`
```
  CEO, this value is Title.

```
**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related MLModelFactor.

This field is a relationship field.


-----

```
ModelId
Name
Operator

```

**Relationship Name**
ModelFactor

**Relationship Type**
Lookup

**Refers To**
MLModelFactor

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the related MLModel.

This field is a relationship field.

**Relationship Name**
Model

**Relationship Type**
Lookup

**Refers To**
MLModel

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The automatically generated ID that uniquely identifies the model.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
If the model factor component is an equation, this field represents the operator. For example,
if the model factor component is `Title = CEO, the operator is` `Equals.`

Possible values are:

**•** `Contains`

**•** `EndsWith`

**•** `Equals`

**•** `GreaterThan`


-----

```
RightHandDerivedField
SortOrder
Value
