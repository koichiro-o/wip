#### QuoteLineRelationship

Describes the relationship between quote line items, such as items in a bundle. When you create a QuoteLineRelationship object, it’s
immutable: it can’t be edited or removed. This object is available in API version 58.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Subscription Management is enabled.


-----

##### Fields

**Field**
```
AssociatedQuantScaleMethod
AssociatedQuoteLineId
AssociatedQuoteLinePricing

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
How to scale the quantity of the associated quote line, relative to the main quote line. If this
field has a non-null value, you can't edit the associated quote line's quantity.

Possible values are:

**•** `Constant— The associated quote’s line quantity remains the same in relation to the`
main quote line’s quantity. For example, the main quote line has a quantity of one and
the associated quote line has a quantity of one. If you increase the quantity of the main
quote line to two, the associated quote line’s quantity remains at one.

**•** `Proportional— The associated order’s item quantity increases or decreases based`
on the main quote line’s quantity. For example, the main quote line has a quantity of
one and the associated quote line has a quantity of two. If you increase the quantity of
the main quote line to two, the associated quote line’s quantity increases to four.

The default value is `Proportional.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the associated quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle
component.

**Relationship Name**
AssociatedQuoteLine

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how the associated quote line item is priced relative to the main quote line item.


-----

```
AssociatedQuoteLineRole
LastReferencedDate
LastViewedDate
MainQuoteLineId

```

Possible values are:

**•** `IncludedInBundlePrice— The associated quote line’s cost is $0 because it’s`
included in the bundle’s price.

**•** `NotIncludedInBundlePrice— The associated quote line has a cost because`
it’s not included in the bundle’s price.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Describes the position of the associated quote line item in the relationship.

Possible values are:

**•** `BundleComponent—The associated quote line item is part of a bundle.`

**•** `SetComponent—The associated quote line item is part of a set.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for example, through
a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate), but
not viewed it.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of the main quote line item.

This field is a relationship field. In a bundle relationship, this quote line is the bundle parent.


-----

```
MainQuoteLineRole
Name
ProductRelationshipTypeId
QuoteId

```

**Relationship Name**
MainQuoteLine

**Relationship Type**
Lookup

**Refers To**
QuoteLineItem

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Indicates the position of the main quote line item in the relationship.

Possible values are:

**•** `Bundle—The main quote line item is the bundle parent.`

**•** `Set—The main quote line item is the set parent.`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the quote line relationship.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique identifier of record that describes the relationship between the main and
associated quote lines.

This field is a relationship field.

**Relationship Name**
ProductRelationshipType

**Relationship Type**
Lookup

**Refers To**
ProductRelationshipType

**Type**
reference


-----

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the quote to which the main and associated quote lines belong.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**QuoteLineRelationshipChangeEvent**

Change events are available for the object.

**QuoteLineRelationshipFeed**

Feed tracking is available for the object.

**QuoteLineRelationshipHistory**

History is available for tracked fields of the object.

**QuoteLineRelationshipOwnerSharingRule**

Sharing rules are available for the object.

**QuoteLineRelationshipShare**

Sharing is available for the object.
