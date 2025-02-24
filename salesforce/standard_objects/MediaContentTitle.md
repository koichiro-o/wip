#### MediaContentTitle

Stores details about an event or show that may be broadcast on TV or radio channels. This object is available in API version 54.0 and
later.

This is referenced while creating scheduled program records for the Channel Master setup.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AvailableLanguages
Description
Genre
LastReferencedDate

```

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
Captures the language of the Media content.

Possible values are:

**•** `English`

**•** `Hindi`

**•** `German`

**•** `French`

**•** `Spanish`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description for the Media Content Title.

**Type**
multipicklist

**Properties**
Create, Filter, Nillable, Restricted picklist, Update

**Description**
Specifies genre of the Media Content.

Possible values are:

**•** `Documentary`

**•** `Soap Opera`

**•** `Sitcom`

**•** `Movie`

**•** `News`

**•** `Comedy`

**•** `Sci-Fi`

**•** `Thriller`

**Type**
dateTime


-----

```
LastViewedDate
Name
NumberOfEpisodes

##### Associated Objects

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
The name of the media content title.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Each of the separate installments into which a serialized story or radio or television program
is divided.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[MediaContentTitleFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[MediaContentTitleHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[MediaContentTitleOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[MediaContentTitleShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.


-----
