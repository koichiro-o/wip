#### Community (Zone)

Represents a zone that contains Idea or Question objects.

Note: Starting with the Summer ’13 release, Chatter Answers and Ideas communities were renamed to zones. In API version 28,
the API object label has changed to `Zone, but the API type is still` `Community.`

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CanCreateCase
DataCategoryName

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether users can ask private questions in the zone using Chatter Answers.

**Type**
string


-----

```
Description
HasChatterService
IsActive
IsPublished
Name

```

**Properties**
Filter, Nillable, Group, Sort

**Description**
The data category associated with the zone.

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Text description of the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether Chatter Answers is available in the zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is active or inactive. An idea or question can only be posted to
an active zone.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the zone is available in portals.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the zone.


-----

```
NetworkId

##### Usage

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Experience Cloud site that this zone is associated with. This field is available only if
digital experiences is enabled in your org. This field is available in API version 63.0 and later.


Use this object to create a zone in Ideas, Chatter Answers, or Answers. Zones help organize ideas and questions into logical groups and
are shared by the Ideas, Answers, and Chatter Answers.
