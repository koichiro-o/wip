#### CommSubscription

Represents a customer’s subscription preferences for a specific communication. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
DataUsePurposeId
IsDefault
 LastReferencedDate
 LastViewedDate
 Name
 OwnerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the data use purpose record associated with the communication subscription.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if this communication subscription is the default (true) or not (false). This field
has a default value of `false. Only one communication subscription record can be the`
default.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. Name of the communication subscription record.

**Type**
reference


-----

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account owner associated with this customer.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**CommSubscriptionChangeEvent (API version 61.0)**
Change events are available for the object.

**CommSubscriptionFeed**

Feed tracking is available for the object.

**CommSubscriptionHistory**

History is available for tracked fields of the object.

**CommSubscriptionOwnerSharingRule**

Sharing rules are available for the object.

**CommSubscriptionShare**

Sharing is available for the object.
