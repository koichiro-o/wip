#### ForecastingColumnDefinition

Represents a custom calculated column or a custom reference data column in a forecast type. This object is available in API version 56.0
and later.

For a custom calculated column, a Formula field value is required. For a custom reference data column, a ReferenceField field
value is required.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
DeveloperName
ForecastingTypeId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer (API) name of the custom calculated column or custom reference data column.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the forecast type. This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup


-----

```
Formula
Language
MasterLabel
ReferenceField

```

**Refers To**
ForecastingType

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Required for custom calculated columns. The formula for the custom calculated column.
Use API column names in your formula (such as ForecastAmount0), not column header
names (such as Closed or Closed Only). For details on API column names, operators, and
functions to use in formulas, see ForecastingColumnDefinition Formula Field Details.

**Example**
The following formula calculates the gap to quota: `ForecastingQuotaAmount -`
```
  ForecastAmount0

```
**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the custom calculated column or custom reference data column.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for this object, which displays in Setup and in the column header on the forecasts
page. The label is in the default language locale for the organization. If there’s no default
language locale, the label is in en_US.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Required for custom reference data columns. The number or currency custom field from the
ForecastingCustomData object. For example,
```
  ForecastingCustomData.Realized_Revenue__c. Data from this field appears

```
in a column in the forecasts summary. This field is available in API version 58.0 and later.


-----

```
ResultField

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The field name to represent the custom calculated column or custom reference data column
result. Possible values are:

**Custom Calculated Column Result**

**•** CalculatedAmount0 or CalculatedQuantity0

**•** CalculatedAmount1 or CalculatedQuantity1

**•** CalculatedAmount2 or CalculatedQuantity2

**•** CalculatedAmount3 or CalculatedQuantity3

**•** CalculatedAmount4 or CalculatedQuantity4

If the formula’s result is null or invalid, “-” is the value. For example, if the formula divided by
0. If you want to show “-” for 0 or negative values in your forecast, use the IF function in your
formula to detect 0 or negative numbers.

**Custom Reference Data Column Result Use the appropriate field based on whether your**
column output is of Currency or Number type.

**•** ExtensionCurrency0 or ExtensionNumber0

**•** ExtensionCurrency1 or ExtensionNumber1

**•** ExtensionCurrency2 or ExtensionNumber2

**•** ExtensionCurrency3 or ExtensionNumber3

**•** ExtensionCurrency4 or ExtensionNumber4


Each forecast type can include any combination of custom calculated columns and reference data columns, as long as they don’t exceed
five in number. For example, a forecast type can have two custom calculated columns and three custom reference data columns.

Custom calculated columns can’t be adjusted and aren’t included in rollups. In the UI, custom calculated columns can’t indicate changes
in the last 7 days.

If you have at least one custom calculated column in an active or inactive forecast type, you can’t do the following until you’ve removed
the column.

**•** Switch from single category to cumulative rollups in Forecast Settings

**•** Enable the Most Likely category

**•** Disable Show Quotas (only if your custom calculated column’s formula refers to a quota value)


-----

ForecastingColumnDefinition Formula Field Details
Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

##### ForecastingColumnDefinition Formula Field Details

Use these API names, operators, and functions to construct formulas for the Formula field in the ForecastingColumnDefinition object.
The API names apply to both singular and cumulative category rollups. For simplification, we included only the single category rollup
column header name next to each API name.

**API Column Names – General**

**•** ForecastingQuotaAmount – Quota (currency)

**•** ForecastingQuotaQuantity – Quota quantity (double)

**•** `DeveloperName` of any custom calculated column or custom reference data column shown in the forecasts page

**API Column Names for Forecast Category Columns**

If the Most Likely category isn’t enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Best Case

**•** ForecastAmount3 or ForecastQuantity3 – Pipeline

If the Most Likely category is enabled:

**•** ForecastAmount0 or ForecastQuantity0 – Closed

**•** ForecastAmount1 or ForecastQuantity1 – Commit

**•** ForecastAmount2 or ForecastQuantity2 – Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – Best Case

**•** ForecastAmount4 or ForecastQuantity4 – Pipeline

**API Column Names for Adjustment Columns – Original Forecast Value Without Adjustments**

If your org shows adjustments in columns, use these API column names for the original forecast value without adjustments. Adjustment
columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutAdjustments1 or QuantityWithoutAdjustments1 – Commit

**•** AmountWithoutAdjustments2 or QuantityWithoutAdjustments2 – Most Likely

**•** AmountWithoutAdjustments3 or QuantityWithoutAdjustments3 – Best Case

**API Column Names for Adjustment Columns – Team Adjustment Value**

If your org shows adjustments in columns, use these API column names for the team’s adjusted value that includes a subordinate’s
owner and manager adjustments, but not a forecast manager’s owner and manager adjustments. These adjustment columns are
available in API version 61.0 and later.


-----

If the Most Likely category isn’t enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Best Case

If the Most Likely category is enabled:

**•** SubordinateOverrideAmount1 or SubordinateOverrideQuantity1 - Commit

**•** SubordinateOverrideAmount2 or SubordinateOverrideQuantity2 - Most Likely

**•** SubordinateOverrideAmount3 or SubordinateOverrideQuantity3 - Best Case

Use these API column names for the team’s adjusted value that includes owner adjustments without manager adjustments. The
adjustment value includes a subordinate’s manager adjustments that they made. These adjustment columns are available in API
version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Best Case

If the Most Likely category is enabled:

**•** AmountWithoutManagerAdjustment1 or QuantityWithoutManagerAdjustment1 – Commit

**•** AmountWithoutManagerAdjustment2 or QuantityWithoutManagerAdjustment2 – Most Likely

**•** AmountWithoutManagerAdjustment3 or QuantityWithoutManagerAdjustment3 – Best Case

**API Column Names for Adjustment Columns – My Adjusted Value**

The column that represents the adjusted value from the forecast user viewing the page is the same as the API column name for the
standard forecast category. Adjustment columns are available in API version 60.0 and later.

If the Most Likely category isn’t enabled:

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Best Case

If the Most Likely category is enabled:

**•** ForecastAmount1 or ForecastQuantity1 – My Commit

**•** ForecastAmount2 or ForecastQuantity2 – My Most Likely

**•** ForecastAmount3 or ForecastQuantity3 – My Best Case

**API Column Names for Custom Reference Data**

Use the appropriate field based on whether the custom reference data is of Currency or Number type.

**•** ExtensionCurrency0

**•** ExtensionCurrency1

**•** ExtensionCurrency2

**•** ExtensionCurrency3

**•** ExtensionCurrency4

**•** ExtensionNumber0

**•** ExtensionNumber1

**•** ExtensionNumber2

**•** ExtensionNumber3

**•** ExtensionNumber4


-----

**Supported Math Operators**

**•** + (Add) – Calculates the sum of two values.

**•**  - (Subtract) – Calculates the difference of two values.

**•**  - (Multiply) – Multiplies its values.

**•** / (Divide) – Divides its values.

**•** () (Open Parenthesis and Closed Parenthesis) – Specifies that the expressions within the open parenthesis and close parenthesis
are evaluated first. All other expressions are evaluated using standard operator precedence.

**Supported Logical Operators**

**•** = and == (Equal) – Evaluates if two values are equivalent. The = and == operators are interchangeable.

**•** <> and != (Not Equal) – Evaluates if two values aren’t equivalent.

**•** < (Less Than) – Evaluates if a value is less than the value that follows this symbol.

**•**  - (Greater Than) – Evaluates if a value is greater than the value that follows this symbol.

**•** <= (Less Than or Equal) – Evaluates if a value is less than or equal to the value that follows this symbol.

**•** >= (Greater Than or Equal) – Evaluates if a value is greater than or equal to the value that follows this symbol.

**Supported Functions**

**•** IF – Determines if expressions are true or false. Returns a given value if true and another value if false.

**•** NULL can be used as a constant. For example, `IF((expression) < 0, NULL, (expression)).`
