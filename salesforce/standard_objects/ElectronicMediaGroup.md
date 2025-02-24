#### ElectronicMediaGroup

Represents the type of media that you can associate with a product or category.This object is available in API version 49.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
You must have the B2B Commerce license and a CMS workspace to access a web store.

##### Fields

```
CurrencyIsoCode
Description
DeveloperName

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

The default value is `USD.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the store.

**Type**
string

**Properties**
Filter, Group, Sort


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
UsageType

```

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

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
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the media group.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the ElectronicMediaGroup object. For external routing, allows the
object to be used in the Streaming API to listen to events whenever a ElectronicMediaGroup
record is created, modified, or deleted.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

**Description**
Possible values are:

**•** `Attachment`

**•** `Banner`

**•** `Listing`

**•** `Standard`

**•** `Tile`
