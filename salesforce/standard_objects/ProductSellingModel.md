#### ProductSellingModel

Defines one method by which a product can be sold; for example, as a one-time sale, an evergreen subscription, or a term-defined
subscription. If the product is sold on subscription, this object defines the subscription’s term. A product can have multiple product
selling models. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Special Access Rules

This object is available with Revenue Cloud and Subscription Management. This object is available for Commerce when the Subscriptions
(Beta) permission is enabled.

##### Fields

```
Name
PricingTerm
PricingTermUnit
SellingModelType

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name given to the product selling model.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the duration of the pricing term for a given selling model. Used with
```
  PricingTermUnit. For example, if this field’s value is 1 and the PricingTermUnit

```
is `Months, the subscription is priced monthly.`

If the selling model is one-time, this field must be null.

Possible value is:

**•** `1`

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The unit of time used to define the pricing term. Used with `PricingTerm` to define the
length of the pricing term. For example, if this field is `Months` and `PricingTerm` is 1,
the subscription is priced monthly. If the selling model is one-time, this field must be null.

Possible values are:

**•** `Annual—UI label is` `Years`

**•** `Months`

**Type**
picklist


-----

```
Status

```

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the product is sold as a one-time sale, an evergreen subscription, or a
subscription with a defined term.

Possible values are:

**•** `Evergreen—A subscription without an end date. An evergreen subscription continues`
until the customer affirmatively cancels it.

**•** `OneTime—A product that isn’t sold as a subscription.`

**•** `TermDefined—A subscription with a defined end date. The subscription continues`
for a specified time period. When the term ends, the subscription ends.

The default value is `OneTime.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the product selling model.

Possible values are:

**•** `Active—An active product selling model can’t be deleted, and only the` `Name` and
`Status` fields can be modified. An active product selling model can’t be changed back
to draft.

**•** `Draft—A draft product selling model can be modified and deleted.`

**•** `Inactive—An inactive product selling model can’t be deleted, and only the` `Name`
and Status fields can be modified. An inactive product selling model can’t be changed
back to draft.

The default value is `Draft.`

