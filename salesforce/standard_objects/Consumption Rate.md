#### Consumption Rate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

The timeout value for a JWT-based access token that's issued to an unknown
user as a result of the guest user variation of the Authorization Code and
Credentials Flow. JWT-based access tokens issued during this flow variation
always contain a UVID.

Possible values are:

**•** `1—1 Minute`

**•** `5—5 Minutes`

**•** `10—10 Minutes`

**•** `15—15 Minutes`

**•** `30—30 Minutes`

Available in API version 59.0 and later.


Consumption rates describe the billing rate for a range of usage within a consumption schedule. All consumption schedules require at
least one consumption rate in order to rate usage on a usage product. This object is available in API version 45.0 and later.

The consumption rate sets a quantity-based boundary for usage and defines how much your product costs when its usage falls within
that boundary. Consumption rates price usage at a per-unit fee or a flat fee across the entire range of usage.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
ConsumptionScheduleId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The consumption schedule that contains the consumption rate.


-----

```
CurrencyIsoCode
Description
LowerBound
Name

```

This is a relationship field.

**Relationship Name**
ConsumptionSchedule

**Relationship Type**
Lookup

**Refers To**
ConsumptionSchedule

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

**Properties**
Create, Nillable, Update

**Description**
Description of the consumption rate.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The lowest quantity of usage for the consumption rate.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Required. Default name of this record. Label is Product Name.


-----

```
Price
PricingMethod
ProcessingOrder
UpperBound

```

**Type**
currency

**Properties**
Create, Filter, Sort, Update

**Description**
The price for usage that falls within the consumption rate’s bounds.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
How Salesforce applies the consumption rate’s price to the total quantity of usage within a
usage summary.

Possible values are:

**•** `FlatFee—Salesforce applies the rate’s price to the entire quantity of usage.`

**•** `PerUnit—Salesforce applies the rate’s price to each individual quantity of usage`
within the usage summary.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order for processing the usage rate across multiple rates. Consumption rates are evaluated
beginning with the lowest processing order.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The highest quantity of usage for the consumption rate.

