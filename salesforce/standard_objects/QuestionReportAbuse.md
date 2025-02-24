#### QuestionReportAbuse

Represents a user-reported abuse on a Question in a Chatter Answers zone. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Name
QuestionId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Question from which the user reported abuse.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Reason

##### Usage

```

**Description**
The ID of the Question from which the user reported abuse.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Question, such as `Spam,` `Hateful, or`
```
  Inappropriate.

```

Use this object to track user-reported abuse on questions created in a Chatter Answers zone.
