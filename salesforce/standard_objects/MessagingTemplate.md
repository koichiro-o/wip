#### MessagingTemplate

Represents a Messaging template used to send pre-formatted messages. This object is available in API version 47.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), search(),
update(), upsert()

 Fields

```
```
Description
DeveloperName
Language
MasterLabel
Message

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API name for the Messaging template.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the Messaging template.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The label of the Messaging template.

**Type**
textarea

**Properties**
Create, Update


-----

**Description**
The body text of the Messaging template.
