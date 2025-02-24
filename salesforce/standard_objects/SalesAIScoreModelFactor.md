#### SalesAIScoreModelFactor

Represents the factors that Sales Cloud Einstein uses to build a scoring model. Scoring models are used by features, such as Opportunity
Scoring, to score individual records. This object is available in API version 47.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To see model factor information, users need a Sales Cloud Einstein license with the “View Scoring Model Factors” permission enabled.
The permission isn’t enabled by default. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this
object.

##### Fields

```
Factor

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
FactorSummaryOrgLanguage
Name
OperatorType
PrimarySourceFieldName
PrimarySourceFieldValue

```

**Description**
A factor that contributes to a scoring model. For example, a factor could indicate that an
amount increase has a positive effect on an opportunity score (AmountIncreasePositive). Or,
it could indicate that a change to the close date has a negative effect on an opportunity
score (CloseDateChangeNegative).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Describes the factor in English. For example, the factor field value AmountChangePositive
is summarized as “Amount change has positive effect”.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the model factor. Currently, the name is a system-generated value.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The operator used to analyze field values. For example, the factor HighSuccessLeadSource
uses the Lead Source field as the primary source field. When building the scoring model,
Einstein uses the Equals operator to determine `PrimarySourceFieldValue =`
```
  Internet. The other supported operator is IsNull.

```
**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the primary field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field.

**Type**
string


-----

```
PrimarySourceFieldValueText
SalesAiScoreCycleId
ScoreCorrelation
SecondarySourceFieldName

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the PrimarySourceFieldValueText, such as a record ID or value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The value of the primary source field used in the model factor. For example, the factor
HighSuccessIndustry uses the account’s Industry as the primary field, and the value of the
Industry field is manufacturing.

Note: This field’s value is retrieved from the `PrimarySourceFieldValue`
field. If the `PrimarySourceFieldValue` field is a record ID, then

`PrimarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull, then` `PrimarySourceFieldValue`
returns `true` and `PrimarySourceFieldValueText` returns null.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the score cycle used to generate model factors. Each score cycle can have multiple
model factors associated to it.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The strength between a model factor and a score. If score correlation value is closer to `+1,`
it’s more likely that the model factor contributing toward a high score. If score correlation
value is closer to -1, it’s more likely that the model factor is contributing toward a low score.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort


-----

```
SecondarySourceFieldValue
SecondarySourceFieldValueText
Status

```

**Description**
The name of the secondary field used in the model factor. For example, the factor
HighAmountActivity uses Task as the primary field and Event as the secondary field. Not all
model factors use a secondary source field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Information used to retrieve the SecondarySourceFieldValueText, such as a record ID or value.
Not all model factors use a secondary source field. This field is available in API version 50.0
and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the model factor is based on two source fields, this field represents the value of the
secondary source field. For example, the factor HighSuccessMultipleSameFieldValue might
use the opportunity’s related product as the primary field and pricebook as the secondary
field. The product and pricebook names are indicated by the PrimarySourceFieldValueText
and SecondarySourceFieldValueText, respectively. Not all model factors use a secondary
source field. This field is available in API version 50.0 and later.

Note: This field’s value is retrieved from the SecondarySourceFieldValue
field. If the `SecondarySourceFieldValue` field is a record ID, then

`SecondarySourceFieldValueText` returns the name of the record. If
`OperatorType` returns `isNull, then` `SecondarySourceFieldValue`
returns `true` and `SecondarySourceFieldValueText` returns null.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Determines whether the model factor is active or inactive.


-----

##### Usage

Use the SalesAIScoreModelFactor object to run a query that retrieves the latest highest influencing model factors.
```
SELECT Id,Factor,ScoreCorrelation,FactorSummaryOrgLanguage
FROM SalesAIScoreModelFactor
WHERE Status='Active' and SalesAIScoreCycle.CycleType='OpportunityScoreModeling'
ORDER BY ScoreCorrelation desc
