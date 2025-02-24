#### ReplyReportAbuse

Represents a user-reported abuse on a Reply in a Chatter Answers zone. This object is available in API version 24.0 and later.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Name
Reason
ReplyId

##### Usage

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the Reply from which the user reported abuse.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The reason the user reported abuse on the Reply, such as `Spam,` `Hateful, or`
```
  Inappropriate.

```
**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the Reply from which the user reported abuse.


Use this object to track user-reported abuse on replies created in a Chatter Answers zone.


-----
