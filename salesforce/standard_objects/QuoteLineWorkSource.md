#### QuoteLineWorkSource

Represents an association between a quote and work sources, such as assets, quote line items, order products, or work type groups. This
object is available in API version 63.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AssetId
OrderItemId
QuoteId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Asset

**Refers To**
Asset

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The order product associated with the quote work source.

This field is a relationship field.

**Relationship Name**
OrderItem

**Refers To**
OrderItem

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
Quote


-----

```
QuoteLineItemId
WorkTypeGroupId

```

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the quote work source.

This field is a relationship field.

**Relationship Name**
QuoteLineItem

**Refers To**
QuoteLineItem

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The quote associated with the work source

This field is a relationship field.

**Relationship Name**
WorkTypeGroup

**Refers To**
WorkTypeGroup

