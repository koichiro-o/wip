#### AdBuyServerAccount

Represents a user account in the buy side platform. The user can send RFPs to the seller and can accept, reject, or review proposals. For
example, Buyer account. Every proposal in the Ad server requires both buyer and seller account details. This object is available in API
version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Account.

This field is a relationship field.

**Relationship Name**
Account


-----

```
AccountIdentifier
Name
OwnerId
Type

```

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Unique account ID in the buy side platform.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of user account in the buy side platform.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of Account.

Possible values are:

**•** `Buyer`


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdBuyServerAccountChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdBuyServerAccountFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdBuyServerAccountHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdBuyServerAccountOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdBuyServerAccountShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
