#### Topic

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the time slot being tracked. The history is displayed on the detail page for
this record.


Represents a topic on a Chatter post or record. This object is available in API version 28.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), search(), update(), upsert()

 Fields

```
```
Description
ManagedTopicType
Name

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Description of the topic.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of managed topic. Values are:

**•** `Content`

**•** `Featured`

**•** `Navigational`

This field is available in API version 44.0 and later.

**Type**
string


-----

```
NetworkId
TalkingAbout

##### Usage

```

**Properties**
Create, Filter, Group, idLookup, Sort, Update

Note: You can change only the spacing and capitalization of a topic
name with the update property.

**Description**
Name of the topic.

**Type**
reference

**Properties**
Create, Filter, Nillable, Sort

**Description**
Identifier of the Experience Cloud site to which the topic belongs. This field is
available only if digital experiences is enabled in your org.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Number of people talking about the topic over the last two months, based on
factors such as topic additions and comments on posts with the topic.


Use this object to query a specific topic or to get a list of all topics, even those used solely in private groups and on records, and the
number of people talking about them.

Use this object to create, edit, or delete topics. To create a topic, you must have the Create Topics permission. To edit a topic, you must
have the Edit Topics permission. To delete a topic, you must have the Delete Topics or Modify All Data permission.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**TopicFeed (API version 29.0)**
Feed tracking is available for the object.
