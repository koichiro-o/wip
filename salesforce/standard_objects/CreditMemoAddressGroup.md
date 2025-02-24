#### CreditMemoAddressGroup

Stores the buyer's address information, which is used to determine the amount of tax to credit to a buyer when a credit memo is issued.
This object is available in API version 55.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update()

 Special Access Rules

```
This object is available when Subscription Management is enabled.

##### Fields

```
Address
City
Country

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
Buyer’s address.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Buyer's city.

**Type**
string


-----

```
CreditMemoAddressGroupNumber
CreditMemoId
CurrencyIsoCode
GeocodeAccuracy

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Buyer's country.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number, such as 0000123, that represents the address group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the credit memo associated with the address group.

This field is a relationship field.

**Relationship Name**
CreditMemo

**Relationship Type**
Lookup

**Refers To**
CreditMemo

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO 4217 currency code associated with the credit memo.

The default value is USD.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The accuracy rating for the geocode of the address group. An accuracy rating contains
information about the location of a latitude and longitude.


-----

```
LastReferencedDate
LastViewedDate
Latitude
Longitude

```

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this address group.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this address group.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Latitude of the buyer’s address.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Longitude of the buyer’s address.


-----

```
PostalCode
State
Street

##### Associated Objects

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s postal code or ZIP code.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s state.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
The buyer’s street number and name.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CreditMemoAddressGroupHistory on page 62**
History is available for tracked fields of the object.
