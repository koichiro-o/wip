#### QuoteItemTaxItem

The tax that is applied to a quote line item. This object is available in API version 55.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available if Subscription Management is enabled in your org.


-----

##### Fields

**Field**
```
Amount
CurrencyIsoCode
Description
Name
QuoteLineItemId

```

**Type**
currency

**Properties**
Filter, Sort

**Description**
The tax amount for the quote line item.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org.

Possible values are:

**•** `BHD—Bahraini Dinar`

**•** `EUR—Euro`

**•** `JPY—Japanese Yen`

**•** `USD—U.S. Dollar`

The default value is 'USD'.

**Type**
textarea

**Properties**
Nillable

**Description**
User-defined description of the tax. For example, state sales tax or value-added tax (VAT).

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the tax.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
Rate
TaxEffectiveDate
Type

```

**Description**
ID of the related quote line item.

This is a relationship field.

**Relationship Name**
QuoteLineItem

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
If the tax is a percentage tax, then this field contains the percent value. If the tax is a fixed
amount, then this field is null.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date used to calculate the tax rate.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Whether the tax is estimated or calculated by the tax provider.

Possible values are:

**•** `Actual`

**•** `Estimated`

