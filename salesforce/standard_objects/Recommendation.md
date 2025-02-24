#### Recommendation

```
Represents the recommendations surfaced as offers and actions for Einstein Next Best Action. This object is available in API version 45.0
and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Special Access Rules

```
You must have the Modify All Data or Manage Next Best Action Recommendations user permission to create and edit recommendations.

##### Fields

```
AcceptanceLabel

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label that appears as the accept option on the surfaced recommendation. Maximum size is
80 characters.


-----

```
ActionReference
Description
ExternalId
ImageId
IsActionActive

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Flow referenced for this recommendation. Label is Action.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Text description of the recommendation. Maximum size is 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Stores an identifier for the recommendation source, such as product, so Einstein can group
all responses for a given recommendation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Image referenced by this recommendation. Label is Image.

This is a relationship field.

**Relationship Name**
Image

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
LastReferencedDate
LastViewedDate
Name
NetworkId
RecommendationKey
RejectionLabel

```

**Description**
Indicates whether the flow referenced in the Action field is active (true) or not (false). Read
only.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the recommendation was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the recommendation. Maximum size is 80 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Experience Cloud site associated with the recommendation (if applicable).

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Track responses to a recommendation when it doesn’t have an ID. Maximum size is 255
characters.

**Type**
string


-----

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label that appears as the reject option on the surfaced recommendation. Maximum size is
80 characters.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**RecommendationChangeEvent (API version 48.0)**
Change events are available for the object.
