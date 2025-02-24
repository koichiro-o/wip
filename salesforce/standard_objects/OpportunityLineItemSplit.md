#### OpportunityLineItemSplit

Represents information about an opportunity product split, including percentages, amounts, and owner. This object is available in API
version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Before creating OpportunityLineItemSplit records, enable Team Selling, set up opportunity splits, and enable product splits on at least
one opportunity split type in Setup.

##### Fields

```
ArchivedTerritoryName

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort


-----

```
CurrencyIsoCode
OpportunityLineItemId
Split

```

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory model, the
field value is null. This field is available in API version 62.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 is specified on the opportunity
(that is, the Pricebook2Id field isn’t blank on the opportunity referenced by this object’s
OpportunityId), then the value of this field must match the currency of the CurrencyIsoCode
field on the PricebookEntry records that are associated with this object.

Possible values are:

**•** `BRL—Brazilian Real`

**•** `CAD—Canadian Dollar`

**•** `EUR—Euro`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated parent OpportunityLineItem. This field is a relationship field.

**Relationship Name**
OpportunityLineItem

**Relationship Type**
Lookup

**Refers To**
OpportunityLineItem

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
SplitAmount
SplitNote
SplitOwnerId
SplitPercentage
SplitTypeId

```

**Description**
Read-only. Automatically generated number identifying the split within the opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
The amount or value of the split.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional text about the split.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the user who is the owner of the split. This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
The percentage of the OpportunityLineItem's value that the split represents.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Territory2Id

##### Usage

```

**Description**
ID of the associated OpptyLineItemSplitType. This field is a relationship field.

**Relationship Name**
SplitType

**Relationship Type**
Lookup

**Refers To**
OpptyLineItemSplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in API version
62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2


Use the OpportunityLineItemSplit object to manage opportunity product splits for an opportunity.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityLineItemSplitHistory on page 62 (API version 59.0)**
History is available for tracked fields of the object.
