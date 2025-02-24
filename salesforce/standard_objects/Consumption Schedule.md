#### Consumption Schedule

A consumption schedule organizes a set of consumption rates by which usage-based products are quoted and billed. This object is
available in API version 45.0 and later.

Salesforce uses consumption schedules to group consumption rates. Your consumption schedule defines the unit of measurement and
rating method for the schedule's rates. It also defines the billing frequency that Salesforce Billing uses to invoice a usage product.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
BillingTerm
BillingTermUnit
CurrencyIsoCode
Description

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The number used with the billing term unit to determine billing frequency.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The unit used with the billing term to determine billing frequency

Possible values are:

**•** `Month—`

**•** `Quarter—`

**•** `Year—`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled.

Possible values are:

**•** `AUD—Australian Dollar`

**•** `CAD—Canadian Dollar`

**•** `GBP—British Pound`

**•** `JPY—Japanese Yen`

**•** `USD—U.S. Dollar`

**Type**
textarea


-----

```
IsActive
LastReferencedDate
LastViewedDate
MatchingAttribute
Name

```

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption schedule.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this record is active (true) or not (false). Label is Active.

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
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce Billing matches usage with a consumption schedule if the records share Matching
Attribute value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
NumberOfRates
OwnerId
RatingMethod
SBQQ__Category__c

```

**Description**
Required. Default name of this record. Label is Product Name.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of consumption rates in this consumption schedule.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns a consumption schedule record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
A specific use case to rate usage against the schedule. This field is the controlling picklist for
the Type field.

Possible values are:

**•** `Tier`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
This field is available only with Salesforce CPQ.


-----

```
Type
UnitOfMeasure
blng__BillingRule__c
blng__RevenueRecognitionRule__c

```

You can define custom categories to organize consumption schedules in separate tabs on
sales rep UI. If you do this, make sure to create a field set for each category.

Possible values are:

**•** `Rates`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines how rate tiers are calculated.

Possible values are:

**•** `Range—The schedule prices only using the tier that applies to the usage quantity.`

**•** `Slab—Usage within a given bound receives pricing equal to its tier’s value.`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unit of measure defines how you quantify instances of usage for your usage products. For
example, if your usage product is a cloud storage subscription, you could provide a value of
GB for your unit of measure.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing invoices usage summaries based off their related consumption schedule's
billing rule.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
This field is available only with Salesforce Billing.

Salesforce Billing recognizes usage summary revenue based off the summary's related revenue
recognition rule.


-----

```
 blng__TaxRule__c
