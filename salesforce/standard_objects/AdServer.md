#### AdServer

Stores and delivers advertising content onto various platforms. This object is available in API version 54.0 and later.

An ad server is the ad technology that enables the management, serving, and tracking of an ad or internal promotion on media properties.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AdServerApplicationName
AdServerNetworkIdentifier
AdServerProperties
AllowedAdPriorityTypes
LastReferencedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Arbitrary string identifying the publisher's application.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Identifies the associated publisher's network.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The custom properties of an ad server.

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
Stores the available Ad Types for the selected Ad Server.

Possible values are:

**•** `Standard`

**•** `Sponsorship`

The picklist is dynamic. More values can be added dynamically.

**Type**
dateTime


-----

```
LastViewedDate
Name
NamedCredentialReference
OwnerId

```

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
The name of the ad server.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores names of the credential references, which hold the authentication details associated
with the AdServer record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the ad server.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdServerHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdServerOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdServerShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
