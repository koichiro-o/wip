#### AdServerAccount

Captures the mapping of an account with an Ad Server. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AdServerAdvertiserIdentifier
AdServerId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Captures the AdvertiserID in the Ad Server.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the AdServer ID for which the mapping is created.

This is a relationship field.

**Relationship Name**
AdServerId__r

**Relationship Type**
Lookup


-----

```
AdvertiserId
Name
Type

##### Associated Objects

```

**Refers To**
AdServer

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Specifies the Advertiser account mapped to the Ad Server.

This is a relationship field.

**Relationship Name**
AdvertiserId__r

**Relationship Type**
Master-detail

**Refers To**
Account (the master object)

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Ad server account.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The account type as per the Ad server definition.

Possible values are:

**•** `Advertiser`

**•** `Agency`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdServerAccountChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.


-----

**[AdServerAccountFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdServerAccountHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdServerAccountOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdServerAccountShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
