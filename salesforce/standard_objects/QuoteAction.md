#### QuoteAction

Indicates the type of sales transaction that’s being quoted; for example, a renewal sale. This object is available in API version 59.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available in orgs with Subscription Management or Revenue Cloud. It’s also available in Industries Automotive and Industries
Field Service.


-----

##### Fields

**Field**
```
LastReferencedDate
LastViewedDate
Name
QuoteId
SourceAssetId

```

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
the user accessed this record or list view indirectly, but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name given to the quote action.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote related to this quote action.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Lookup

**Refers To**
Quote

**Type**
reference


-----

```
Type

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The asset changed by this sales transaction. For example, if the quote action is a quantity
amendment, this field contains the ID of the asset that’s amended.

This field is a relationship field.

**Relationship Name**
SourceAsset

**Relationship Type**
Lookup

**Refers To**
Asset

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of sales transaction that the related quote is for.

Valid values are:

**•** `Add`

**•** `Amend`

**•** `Cancel`

**•** `No Change`

**•** `Renew`

