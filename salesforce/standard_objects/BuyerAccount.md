#### BuyerAccount

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label of the customer lifecycle map.


Represents an account that is enabled as a buyer for Lightning B2B Commerce. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The BuyerAccount object is available only if the B2B Commerce license is enabled.

##### Fields

```
AvailableCredit
BuyerId

```

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount of credit available to a buyer account.

This is a calculated field.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the buyer account.

This is a relationship field.


-----

```
BuyerStatus
CommerceType
CreditLimit

```

**Relationship Name**
Buyer

**Relationship Type**
Lookup

**Refers To**
Account

Note: This field is unique within your organization.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
Status of the buyer account.

Possible values are:

**•** `Active`

**•** `Inactive`

**•** `On Hold`

**•** `Pending`

The default value is 'Pending'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type of commerce that the buyer account is conducting, using the Commerce app.

Possible values are:

**•** `Buyer`

**•** `Reseller`

**•** `Seller`

The default value is 'Buyer'.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The limit of credit available to the buyer account.


-----

```
CreditStatus
CurrencyIsoCode
CurrentBalance
IsActive
MaximumOrderLimit

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The type or status of the buyer account's credit ranking.

Possible values are:

**•** `Bad Credit`

**•** `Delinquent`

**•** `Good Credit`

**•** `On Hold`

The default value is 'Good Credit'.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Three-letter ISO currency code associated with the buyer account record.

Possible values are:

**•** `USD—U.S. Dollar`

The default value is 'USD'.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The balance carried by the buyer account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the buyer account is active (true) or not (false).

The default value is 'false'.

**Type**
currency


-----

```
MinimumOrderLimit
Name
OwnerId
PayerId

```

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The maximum number of orders that can be placed by the buyer account.

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The minimum number of orders that can be placed by the buyer account.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the buyer account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the buyer account owner.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the buyer account payer.

This is a relationship field.


-----

```
SendToId

##### Associated Objects

```

**Relationship Name**
Payer

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of account that an order is sent to.

This is a relationship field.

**Relationship Name**
SendTo

**Relationship Type**
Lookup

**Refers To**
Account


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BuyerAccountFeed on page 54**
Feed tracking is available for the object.

**BuyerAccountHistory on page 62**
History is available for tracked fields of the object.

**BuyerAccountShare on page 66**
Sharing is available for the object.
