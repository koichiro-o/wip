#### SocialPersona

Represents a snapshot of a contact's profile on a social network such as Facebook or Twitter. This object is available in API version 22.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AreWeFollowing
AuthorLabels
AvatarUrl

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a Salesforce social account is following the social persona or
not.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Comma-separated list of author type tags.

**Type**
string


-----

```
Bio
ExternalId
ExternalPictureURL
Followers
Following

```

**Properties**
Nillable

**Description**
Retrieves the user's social network avatar. It's a read-only field and you can't
specify or update its value.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Biography of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona on the social network.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL to the picture of the social persona on the social network.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of followers that the social persona has.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of people that the social persona is following.


-----

```
InfluencerScore
IsBlacklisted
IsDefault
IsFollowingUs
IsVerified
LastReferencedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 score describing the influence of the social persona. No longer used.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is blacklisted or not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona supplies the default avatar image that’s
displayed on the contact or account.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is following a Salesforce social account or
not.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether the social persona is verified or not.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
ListedCount
MediaProvider
MediaType
Name
NumberOfFriends

```

**Description**
Date and time when the social persona was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date and time when the social persona was last viewed.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Radian6 field. No longer used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Social network type of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the social persona.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
NumberOfTweets
ParentId
ProfileType
ProfileUrl

```

**Description**
Number of friends that the social persona has.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Number of tweets made by the social persona.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the contact parent record for the social persona.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Contact, Lead, SocialPost

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Type of profile. Values are:

**•** `Person`

**•** `Page`

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
URL for the profile.


-----

```
Provider
R6SourceId
RealName
SourceApp
TopicType

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Social network, such as Facebook or Twitter, of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the social persona in Social Studio.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Real name of the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Salesforce product that created the social persona.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of topic, such as keyword or managed.


The fields on a SocialPersona object don’t provide real-time data. They provide a snapshot of information from the last time Salesforce
collected a post from the social persona. Many of the Radian6-related fields are no longer accurate or used.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SocialPersonaHistory (API version 26.0)**
History is available for tracked fields of the object.
