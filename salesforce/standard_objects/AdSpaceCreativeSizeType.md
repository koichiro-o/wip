#### AdSpaceCreativeSizeType

Each Ad Space Creative Size Type defines the compatibility of an Ad Space with an Ad Creative Size Type. This object is available in API
version 54.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AdCreativeSizeTypeId
AdSpaceSpecificationId
AppearanceOrder

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference to the Ad Creative SizeType record.

This is a relationship field.

**Relationship Name**
AdCreativeSizeTypeId__r

**Relationship Type**
Lookup

**Refers To**
AdCreativeSizeType

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Reference to the AdSpace Specification record.

This is a relationship field.

**Relationship Name**
AdSpaceSpecificationId__r

**Relationship Type**
Master-detail

**Refers To**
AdSpaceSpecification (the master object)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of creative to be served by the Ad server.


-----

Possible values are:

**•** `picklist`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdSpaceCreativeSizeTypeFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdSpaceCreativeSizeTypeHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.
