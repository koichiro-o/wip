#### DatedConversionRate

Represents the dated exchange rates used by an organization for which the multicurrency and the effective dated currency features are
enabled.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),

```

-----

##### Special Access Rules

Customer Portal users can't access this object.

##### Fields

```
ConversionRate
IsoCode
NextStartDate
StartDate

##### Usage

```

**Type**
double

**Properties**
Filter, Update

**Description**
Required. Conversion rate of this currency type against the corporate currency.

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter currency
ISO codes defined by the ISO 4217 standard, such as `USD,` `GBP, or` `JPY. Must be unique`
within your organization. Label is Currency ISO Code.

**Type**
date

**Properties**
Filter, Nillable

**Description**
Read only. The date on which the next effective dated exchange rate will start. Effectively
the day after the end date for this exchange rate.

**Type**
date

**Properties**
Filter

**Description**
The date on which the effective dated exchange rate starts.


This object is for multicurrency organizations with advanced currency management enabled. Use this object to define the exchange
rates your organization uses for a date range. This object is not available in single-currency organizations, nor is it available if the
organization does not have advanced currency management enabled.


-----
