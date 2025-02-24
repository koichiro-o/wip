#### OrderDeliveryMethod

Shows the customizations and options that a buyer selected for their delivery method. This object is available in API version 48.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To access Commerce Orders entities, your org must have a Salesforce Order Management license. Commerce Orders entities are available
only in Lightning Experience.


-----

##### Fields

**Field**
```
 Carrier
 ClassOfService
 Description
 IsActive
 LastReferencedDate
 LastViewedDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier that the buyer chose for their delivery method. Developers must add values to
this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The carrier class of service that the buyer chose for their delivery method. Developers must
add values to this field.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the delivery method.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Assign new delivery groups to active delivery methods.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime


-----

```
Name
OwnerId
ProductId
ReferenceNumber
ShippingCarrierMethod

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Default name of this record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The user who owns an order delivery method record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Optional. This product represents a delivery charge order product for a delivery using this
delivery method. For example, you could create a product that represents an overnight
express charge and assign it to an overnight express delivery method.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Reference number for an external delivery method.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

**Description**
Optional. A specific shipping service provided by a shipping carrier, such as Ground, 2Day,
and NextDay. Depends on the range of transit times available for each carrier.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderDeliveryMethodChangeEvent (API version 62.0)](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**
Change events are available for the object.
