#### CurrencyType

Represents the currencies used by an organization for which the multicurrency feature is enabled.

##### Supported Calls
```
create(), describeSObjects(), getUpdated(), query(), retrieve(), search(), update()

 Special Access Rules

```
**•** This object is not available in single-currency organizations.

**•** You need the “Customize Application” permission to edit this object.

**•** Your client application can't delete this object.

##### Fields

```
ConversionRate
DecimalPlaces
IsActive

```

**Type**
double

**Properties**
Filter

**Description**
Required. Conversion rate of this currency type against the corporate currency.

**Type**
int

**Properties**
Filter

**Description**
Required. For this currency, specifies the number of digits to the right of the decimal
point, such as zero (0) for JPY or `2` for USD.

**Type**
boolean

**Properties**
Defaulted on create, Filter


-----

```
 IsCorporate
 IsoCode

##### Usage

```

**Description**
Indicates whether this currency type is active (true) or not (false). Inactive
currency types do not appear in picklists in the user interface. Label is Active. This
field defaults to `false` if no value is provided when updating or inserting a record.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether this currency type is the corporate currency (true) or not (false).
Label is Corporate Currency. All other currency conversion rates are applied against
this corporate currency. If a currency is already defined as the corporate currency in
the user interface, it can't be unset. When a non-corporate currency is set to a
corporate currency, the system reconfigures all conversion rates based on the new
corporate currency.

**Type**
picklist

**Properties**
Filter, Restricted picklist

**Description**
Required. ISO code of the currency. Must be one of the valid alphabetic, three-letter
currency ISO codes defined by the ISO 4217 standard, such as `USD,` `GBP, or` `JPY.`
Must be unique within your organization. Label is Currency ISO Code.


This object is for multicurrency organizations only. Use this object to define the currencies your organization uses.

When updating an existing record, make sure to provide values for all fields to avoid undesired changes to the CurrencyType. For example,
if a value for `IsActive` is not provided, the default (false) is used, which could result in a currently active CurrencyType becoming
inactive.

SEE ALSO:

DatedConversionRate

Overview of Salesforce Objects and Fields
