#### WorkAccess


**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the product that is represented by the `WishlistItem.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the parent `Wishlist` of this `WishlistItem.`


Used to grant or restrict user access to give badge definitions. Each badge definition record must have one WorkAccess record.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Additional Considerations and Related Objects

```
WorkAccess is not available through Schema Builder and is not customizable. A WorkAccess record is required for users to Give
BadgeDefinitions. If a WorkAccess record is not created, BadgeDefinitions will not be available to users.

The sharing of WorkAccess records is through WorkAccessShare. For each WorkBadgeDefinition record, you must create both a WorkAccess
record (per WorkBadgeDefinition) and WorkAccessShare records for sharing to users or groups.

##### Fields

```
AccessType

```

**Type**
picklist


-----

```
OwnerId
ParentId

##### Associated Objects

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Define the type of Access given to user (“Give”).

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID for owner of Access record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Salesforce unique ID for BadgeDefinition record associated with this Access record.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
WorkBadgeDefinition


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**WorkAccessChangeEvent (API version 62.0)**
Change events are available for the object.

**WorkAccessOwnerSharingRule**

Sharing rules are available for the object.


-----

The original WDC feature is unavailable as of Spring ’22. This object isn’t available as of API version 54.0. For more information, see
[Phased WDC (legacy Work.com) Feature Retirement.](https://help.salesforce.com/s/articleView?id=000356306&type=1&language=en_US)

**WorkAccessShare**

Sharing is available for the object.
