#### AdSpaceGroupMember

Defines the association of an Ad Space Specification record with an Ad Space Group record. This object is available in API version 54.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
AdSpaceGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the group type ad space specificaton that the ad space specification group member
is a part of.

This is a relationship field.

**Relationship Name**
AdSpaceGroupId__r

**Relationship Type**
Master-detail

**Refers To**
AdSpaceSpecification (the master object)


-----

```
AdSpaceGroupMemberNameId
LastReferencedDate
LastViewedDate
Name

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID the ad space specification that's part of the relared ad space group.

This field is a relationship field.

**Relationship Name**
AdSpaceGroupMemberName

**Refers To**
AdSpaceSpecification

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
The name of the ad space group member.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdSpaceGroupMemberChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.


-----

**[AdSpaceGroupMemberFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdSpaceGroupMemberHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdSpaceGroupMemberOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdSpaceGroupMemberShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
