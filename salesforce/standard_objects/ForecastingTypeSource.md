#### ForecastingTypeSource

```

**Refers To**
OpptyLineItemSplitType

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Indicates whether the role type has a forecasting type, and if so, which forecasting
type. Available in API version 41.0 and later.

Possible values are:

**•** `R—User role-based forecasting type`

**•** `T—Territory1-based forecasting type; not used`

**•** `Y—Territory2-based forecasting type`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Indicates whether the forecasting type has a Territory2 model, and if so, the name
of the Territory2 model. Available in API version 41.0 and later.


Maps a forecasting source definition to a forecast type. This object is available in API version 52.0 and later.

Note: The information in this topic applies only to forecast types created in Summer ’21 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
DeveloperName
ForecastingSourceDefinitionId
ForecastingTypeId
Language

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The developer name of the forecasting type source.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecasting source definition. This field is a relationship field.

**Relationship Name**
ForecastingSourceDefinition

**Relationship Type**
Lookup

**Refers To**
ForecastingSourceDefinition

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the forecast type. Can be linked only to forecast types created in Summer ’21 and later.
This field is a relationship field.

**Relationship Name**
ForecastingType

**Relationship Type**
Lookup

**Refers To**
ForecastingType

**Type**
picklist


-----

```
MasterLabel
ParentSourceDefinitionId
RelationField

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Language of the forecasting type source.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Controlling label for this forecasting type source.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
For forecast types not based on the opportunity object and not based on a custom measure,
this value represents the parent ForecastingSourceDefinition of the linked
ForecastingSourceDefinition. This field is a relationship field.

**•** Opportunity Product is the parent of Opportunity.

**•** Opportunity Split is the parent of Opportunity.

**•** Line Item Schedule is the parent of Opportunity Product.

**Relationship Name**
ParentSourceDefinition

**Relationship Type**
Lookup

**Refers To**
ForecastingSourceDefinition

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the field linking the source objects of the parent ForecastingSourceDefinition to
the child ForecastingSourceDefinition.

Possible values are:

**•** `OpportunityLineItem.OpportunityId`

**•** `OpportunityLineItem.Product2Id`

**•** `OpportunityLineItemSchedule.OpportunityLineItemId`


-----

```
SourceGroup

##### Usage

```


**•** `OpportunitySplit.OpportunityId`

**Type**
int

**Properties**
Create, Filter, Group, Sort

**Description**
Required. Represents a grouping of forecasting source definitions.


Use this object to define a forecast type’s structure. This junction object links `ForecastingSourceDefinition` to
```
ForecastingType.

```
For an example, see ForecastingSourceDefinition.
