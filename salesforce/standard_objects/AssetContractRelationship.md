#### AssetContractRelationship

Represents a relationship between an asset and a contract. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
This object is available in Enterprise, Unlimited, and Developer Editions of Revenue Cloud.

##### Fields

```
AssetId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the asset related to the contract.

This field is a relationship field.

**Relationship Name**
Asset

**Relationship Type**
Lookup

**Refers To**
Asset


-----

```
ContractId
EndDate
LastReferencedDate
LastViewedDate
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the contract related to the asset.

This field is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The end date and time of the relationship between contract and asset.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view. The associated UI label is Last Modified Date.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user accessed this record or list view (LastReferencedDate) but didn’t view it.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
StartDate

##### Associated Objects

```

**Description**
The auto-generated number assigned to AssetContractRelationship. (Read Only)

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The start date and time of the relationship between contract and asset.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AssetContractRelationshipFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AssetContractRelationshipHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.
