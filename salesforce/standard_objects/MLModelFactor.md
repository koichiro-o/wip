#### MLModelFactor

Represents a field value that has a positive or negative effect on the model’s score. This object is available in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Available with Einstein Prediction Builder and Einstein Recommendation Builder.

##### Fields

```
Correlation
FactorType

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows the strength of association between the variable and the outcome. The higher the
correlation, the greater the association.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of factor.

Possible values are:

**•** `ModelFactlet—The field value strongly influences the outcome because the model`
determined that this field is always important. For example, the model can decide that
the field `Industry` is always important to the outcome, regardless of its value.

**•** `ModelFactor—The field value is important to the outcome because the field’s value`
is significant. For example, the model can decide that the `Annual Revenue` field
value is important to the outcome because the value is above $1,000,000 or below
$50,000.


-----

```
Importance
ModelId
Name
Type

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Shows how much the variable influences the outcome. The higher the value, the greater
the impact.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related model.

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
The type of model factor.

Possible values are:

**•** `And`

**•** `Basic`

**•** `Or`


-----

```
Weight

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Indicates how significant the field value is to the outcome or score. Model factlets tend to
have higher weights than model factors.

