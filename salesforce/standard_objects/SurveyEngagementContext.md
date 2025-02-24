#### SurveyEngagementContext

Represents the context based on which a survey invitation was sent or a survey response was received. This object is available in API
version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

```
Note: You can’t define custom fields for the SurveyEngagementContext object using the Object Manager.

##### Fields

```
ContextType

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context type based on which the survey invitation was sent or the response was received.


-----

```
ContextValue
Name
OwnerId
SurveyInvitationId
SurveyResponseId

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Context based on which the survey invitation was sent or the response was received.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the record's owner.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey invitation.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the survey response.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyEngagementContextShare**

Sharing is available for the object.


-----
