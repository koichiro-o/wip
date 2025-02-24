#### MediaPrintIssue

Represents the details of an issue with details such as issue name, date, advertising deadline about the publication. It is specific to Print
media channels in Ad Sales and is available periodically based on publication frequency. This object is available in API version 57.0 and
later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdvertisingDeadline
IssueDate
MediaChannelId

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Represents the date by which the user can request Ad products in the media plan for the
selected issue.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the date of the issue made publicly available.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the ID of the Media Channel.

This field is a relationship field.

**Relationship Name**
MediaChannel

**Relationship Type**
Lookup

**Refers To**
MediaChannel


-----

```
Name

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Represents the name of the issue for the publication made publicly available based on the
publication frequency.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[MediaPrintIssueChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[MediaPrintIssueFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[MediaPrintIssueHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[MediaPrintIssueOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[MediaPrintIssueShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
