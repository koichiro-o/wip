#### AdServerUser

Captures the mapping of a user with an ad server. This object is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdServerId
AdServerUserIdentifier

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Captures the ad server to which the user is mapped.

This is a relationship field.

**Relationship Name**
AdServerId__r

**Relationship Type**
Lookup

**Refers To**
AdServer

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Captures the publisher's Contact and User Id sent during Order creation. This is equivalent
of TraffickerId in GAM.


-----

```
AdServerUserProperties
LastReferencedDate
LastViewedDate
Name
OwnerId

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The custom properties of the ad server user.

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
and LastReferenceDateis not null, the user accessed this record or list view indirectly.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the ad server user.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the ad server user.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


-----

```
Type
UserId

##### Associated Objects

```

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Describes the user persona as per the ad server definition.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specifies the user for which the ad server mapping is created.

This is a relationship field.

**Relationship Name**
UserId__r

**Relationship Type**
Lookup

**Refers To**
User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdServerUserChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdServerUserFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdServerUserHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdServerUserOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdServerUserShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
