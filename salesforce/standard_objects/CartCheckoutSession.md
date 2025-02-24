#### CartCheckoutSession

```
Represents a checkout session used in Lightning B2B Commerce checkout. This object is available in API version 48.0 and later.

A checkout session is tied to a single web cart, but there can be multiple checkout sessions for a single cart.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
BackgroundOperationId
CurrencyIsoCode
IsArchived

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the in progress background operation.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency used for the checkout session. Default value is `USD.`

Possible values are:

**•** `USD—U.S. Dollar`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
IsError
IsProcessing
Name
NextState
OrderId

```

**Description**
Indicates whether checkout processing is archived (true) or not (false). After a session
is archived, it can’t be unarchived. Default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the session is in error state (true) or not (false). Default value is
```
  false.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines whether checkout processing is in progress (true) or not (false). Default
value is `false.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the checkout session.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The next state of the checkout session.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of a created order after the checkout session has gone from cart to order.


-----

```
OrderReferenceNumber
State
WebCartId
