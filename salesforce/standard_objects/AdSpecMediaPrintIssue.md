#### AdSpecMediaPrintIssue

Ad Specification Media Print Issue is a bridge entity that links the relationship between the Ad Space Specification and the Media Print
Issue entities. This object is available in API version 57.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdSpaceSpecificationId
MediaPrintIssueId
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the ID of an Ad Space specification

This field is a relationship field.

**Relationship Name**
AdSpaceSpecification

**Relationship Type**
Lookup

**Refers To**
AdSpaceSpecification

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the ID of an issue of the publication.

This field is a relationship field.

**Relationship Name**
MediaPrintIssue

**Relationship Type**
Lookup

**Refers To**
MediaPrintIssue

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Represents the name of the issue for the publication.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdSpecMediaPrintIssueChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdSpecMediaPrintIssueFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdSpecMediaPrintIssueHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdSpecMediaPrintIssueOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdSpecMediaPrintIssueShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
