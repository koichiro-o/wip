#### OpportunityLineItem

Represents an opportunity line item, which is a member of the list of Product2 products associated with an Opportunity.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

```

-----

##### Special Access Rules

The user must have the “Edit” permission on Opportunity records to create or update opportunity line items on an opportunity.

##### Fields

```
CanUseQuantitySchedule
CanUseRevenueSchedule
ConnectionReceivedId
ConnectionSentId
CurrencyIsoCode

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a quantity schedule (true) or not
(false). This field is read-only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the opportunity product can have a revenue schedule (true) or not
(false). This field is read-only.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
picklist


-----

```
Description
Discount
HasQuantitySchedule
HasRevenueSchedule

```

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency enabled, and a Pricebook2 isn’tspecified on the parent
opportunity (that is, the Pricebook2Id field is blank on the opportunity referenced by
this object’s OpportunityId), then the value of this field must match the currency of
the CurrencyIsoCode field on the PricebookEntry records that are associated with this
object.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Text description of the opportunity line item. Limit: 255 characters.

**Type**
percent

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Discount for the product as a percentage.

When updating these records:

**•** If you specify `Discount without specifying TotalPrice, the TotalPrice` is
adjusted to accommodate the new `Discount value, and the` `UnitPrice` is held
constant.

**•** If you specify both Discount and Quantity, you must also specify either
`TotalPrice` or UnitPrice so the system knows which one to automatically
adjust.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether a quantity schedule has been created for this object (true)
or not (false).

**Type**
boolean


-----

```
HasSchedule
LastReferencedDate
LastViewedDate
ListPrice

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a revenue schedule has been created for this object (true) or not
(false).

If this object has a revenue schedule, the Quantity and TotalPrice fields can’t be
updated. In addition, the Quantity field can’t be updated if this object has a quantity
schedule. Update requests aren’t rejected but the updated values are ignored.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If either HasQuantitySchedule or HasRevenueSchedule is true, this field is
also `true.`

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record. Available
in API version 50.0 and later.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed. Available in
API version 50.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Corresponds to the `UnitPrice` on the PricebookEntry that is associated with this line
item, which can be in the standard price book or a custom price book. A client application


-----

```
Name
OpportunityId
PricebookEntryId

```

can use this information to show whether the unit price (or sales price) of the line item differs
from the price book entry list price.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The opportunity line item name (known as “Opportunity Product” in the user interface). This
read-only field is available in API version 30.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the associated Opportunity.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. ID of the associated PricebookEntry. Exists only for those organizations that have
Products enabled as a feature. In API versions 1.0 and 2.0, you can specify values for either
this field or ProductId, but not both. For this reason, both fields are declared nillable. In
API version 3.0 and later, you must specify values for this field instead of `ProductId.`

This is a relationship field.

**Relationship Name**
PricebookEntry

**Relationship Type**
Lookup

**Refers To**
PricebookEntry


-----

```
ProductId
Product2Id
ProductCode
Quantity

```

**Type**
reference

**Properties**
Create, Filter, Nillable

**Description**
ID of the related Product record. This field is unavailable as of version 3.0 and is only provided
for backward compatibility. The Product object is unavailable beginning with version 8.0.
Use the PricebookEntryId field instead, specifying the ID of the PricebookEntry record.

This is a relationship field.

**Relationship Name**
Product2

**Relationship Type**
Lookup

**Refers To**
Product2

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the related Product2 record. This is a read-only field available in API version 30.0
and later.

Use the PricebookEntryId field instead, specifying the ID of the PricebookEntry record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This read-only field is available in API version 30.0 and later. It references the value in the
ProductCode field of the related Product2 record.

**Type**
double

**Properties**
Create, Filter, Sort, Update

**Description**
Read-only if this record has a quantity schedule, a revenue schedule, or both a quantity and
a revenue schedule.

When updating these records:


-----

```
RecalculateTotalPrice
ServiceDate
SortOrder
Subtotal

```


**•** If you specify `Quantity` without specifying the UnitPrice, the UnitPrice
value is adjusted to accommodate the new Quantity value, and the TotalPrice
is held constant.

**•** If you specify both Discount and Quantity, you must also specify either TotalPrice
or UnitPrice so the system can determine which one to automatically adjust.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Changes behavior of OpportunityLineItem calculations when a line item has child schedule
rows for the Quantity value. When enabled, if the rollup quantity changes, then the
quantity rollup value is multiplied against the sales price to change the total price. Product2
flag must be set to true.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Date when the product revenue will be recognized and the product quantity will be shipped.

**•** Opportunity Close Date—ServiceDate is ignored.

**•** Product Date—ServiceDate is used if not `null.`

**•** Schedule Date—ServiceDate is used if not `null` and there are no revenue
schedules present for this line item, that is, there are no OpportunityLineItemSchedule
records with a field Type value of Revenue that are children of this record.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number indicating the sort order selected by the user. Client applications can use this to
match the sort order in Salesforce.

**Type**
currency

**Properties**
Filter, Nillable, Sort


-----

```
TotalPrice
UnitPrice

##### Usage

```

**Description**
Difference between standard and discounted pricing. Converted currency amounts when
the opportunity's currency is different from the user's currency.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
This field is available only for backward compatibility. It represents the total price of the
OpportunityLineItem.

If you don’t specify UnitPrice, this field is required. If you specify Discount and
`Quantity, this field or UnitPrice` is required. When updating these records, you can
change either this value or the `UnitPrice, but not both at the same time.`

This field is nillable, but you can’t set both TotalPrice and UnitPrice to null in the
same update request. To insert the TotalPrice via the API (given only a unit price and
the quantity), calculate this field as the unit price multiplied by the quantity. This field is
read-only if the opportunity line item has a revenue schedule. If the opportunity line item
doesn’t have a schedule or only has a quantity schedule, this field can be updated.

**Type**
currency

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
The unit price for the opportunity line item. In the Salesforce user interface, this field’s value
is calculated by dividing the total price of the opportunity line item by the quantity listed for
that line item. Label is Sales Price.

This field or TotalPrice is required. You can’t specify both.

If you specify Discount and Quantity, this field or TotalPrice is required.


An Opportunity can have associated OpportunityLineItem records only if the Opportunity has a Pricebook2. An OpportunityLineItem
must correspond to a Product2 that is listed in the opportunity's Pricebook2. For information about inserting OpportunityLineItem for
an opportunity that doesn’t have an associated Pricebook2 or any existing line items, see Effects on Opportunities.

This object is defined only for orgs with products enabled as a feature. If the products feature isn’t enabled, this object doesn’t appear
in the `describeGlobal()` call, and you can’t use describeSObjects() or query the OpportunityLineItem object.

[For a visual diagram of the relationships between OpportunityLineItem and other objects, see the Product & Price Book diagram on](https://architect.salesforce.com/diagrams/template-gallery/sales-cloud-product-price-book-data-model)
Salesforce Architect .


-----

Note:

**•** If the multicurrency option is enabled, the CurrencyIsoCode field is present. It can’t be modified, and is always set to
the value of the CurrencyIsoCode of the parent Opportunity.

**•** If customizable product schedules are enabled, you can use custom fields in default schedules and customize their layout. But
if you’ve applied validation rules or Apex triggers, they’re bypassed when they’re first inserted.

##### Effects on Opportunities

Opportunities with associated OpportunityLineItem records are affected in the following ways:

**•** Creating an OpportunityLineItem increments the Opportunity Amount value by the `TotalPrice` of the OpportunityLineItem.
Additionally, inserting an OpportunityLineItem increments the `ExpectedRevenue` on the opportunity by the TotalPrice
times the opportunity Probability.

**•** The Opportunity `Amount` becomes a read-only field when the opportunity has line items. The API ignores any attempt to update
this field on an opportunity with line items. Update requests aren’t rejected, but the updated value is ignored.

**•** You can’t update the PricebookId field or the CurrencyIsoCode field on the opportunity if line items exist. The API rejects
any attempt to update these fields on an opportunity with line items.

**•** When you create or update an OpportunityLineItem, the API verifies that the line item corresponds to a PricebookEntry in the
Pricebook2 that is associated with the opportunity. If the opportunity doesn’t have an associated Pricebook2, the API automatically
sets the price book on the opportunity if the line item corresponds to a PricebookEntry in an active Pricebook2, and if the PricebookEntry
has a `CurrencyIsoCode` field that matches the CurrencyIsoCode field of the opportunity. If the Pricebook2 isn’t active
or the `CurrencyIsoCode` fields do not match, an error is returned.

**•** The Opportunity HasOpportunityLineItem field is set to true when an OpportunityLineItem is inserted for that Opportunity.

**•** When OpportunityLineItem records are directly deleted, they aren’t sent to the recycle bin and can’t be undeleted. The
```
  getDeleted() call shows deleted OpportunityLineItem records until they’re purged, which is usually within the same day or

```
the next day.

**•** In Lightning, the ListPrice, Name, and ProductCode fields aren’t populated before insert because their values are computed
after the OpportunityLineItem.Product2Id value is saved. To access a value from these fields, use an After Insert trigger.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunityLineItemChangeEvent on page 67 (API version 60.0)**
Change events are available for the object.

SEE ALSO:

OpportunityLineItemSchedule
