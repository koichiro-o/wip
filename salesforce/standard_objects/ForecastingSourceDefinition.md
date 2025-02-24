#### ForecastingSourceDefinition

Represents the object, measure, date type, and hierarchy that a forecast uses to project sales. This object is available in API version 52.0
and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
CategoryField
DateField
DeveloperName
FamilyField

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Name of the forecast category that is associated with the forecast type.

Possible values are:

**•** `Opportunity.ForecastCategoryName`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Field that is used for the forecast type’s date type. For example, the CloseDate field on
Opportunity is used for opportunity close date-based forecast types.

Possible values are:

**•** `Opportunity.CloseDate`

**•** `OpportunityLineItem.ServiceDate`

**•** `OpportunityLineItemSchedule.ScheduleDate`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting source definition.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Use this field to group forecasts by product family. Possible values are:

**•** `Product2.Family`


-----

```
Language
MasterLabel
MeasureField
SourceObject

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting source definition. For example, English.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting source definition.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Field that is used for the forecast type’s measure. For example, the Amount field on
Opportunity is associated with revenue-based forecast types.

Possible values are*:

**•** `Opportunity.Amount`

**•** `Opportunity.Custom`

**•** `Opportunity.TotalOpportunityQuantity`

**•** `OpportunityLineItem.Custom`

**•** `OpportunityLineItem.Quantity`

**•** `OpportunityLineItem.TotalPrice`

**•** `OpportunityLineItemSchedule.Custom`

**•** `OpportunityLineItemSchedule.Quantity`

**•** `OpportunityLineItemSchedule.Revenue`

**•** `OpportunitySplit.Custom`

**•** `OpportunitySplit.SplitAmount`

*Where `Custom represents the name of the custom field that a forecast type’s measure is`
based on. Example: Use `Megawatts__c` to forecast energy consumption.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

```
Territory2Field
UserField

##### Usage

```

**Description**
Object associated with this forecasting source definition.

Possible values are:

**•** `Opportunity`

**•** `OpportunityLineItem`

**•** `OpportunityLineItemSchedule`

**•** `OpportunitySplit`

**•** `Product2`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
For a territory-based forecast type, indicates the field that is used for territory information.

Possible values are:

**•** `Opportunity.Territory2Id`

For user role-based forecast types, this value is `null.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies who owns the forecast.

Possible values are:

**•** `Opportunity.OwnerId`

**•** `OpportunitySplit.SplitOwnerId`


Use ForecastingSourceDefinition to define a forecast type’s structure. A forecasting source definition is joined via
`ForecastingTypeSource` to `ForecastingType.`

In this example, a user role-based forecast type called Custom Amount Forecast is based on the Amount and Close Date fields on
opportunities.


-----
