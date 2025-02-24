#### CallTemplate

```


**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The static name of the call outcome.


Represents a call script for users to read when making calls.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
Description
HtmlBody
LastReferencedDate

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The description of the call script.

**Type**
textarea

**Properties**
Nillable

**Description**
The body content of the call script.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastViewedDate
Name
OwnerId
TemplateType
TotalCalls

```

**Description**
The time stamp that indicates when the current user last viewed a record that is related to
this CallTemplate.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The time stamp that indicates when the current user last viewed this CallTemplate. If this
value is null, this record might have been only referenced (LastReferencedDate) and
not viewed.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the call script.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the call script.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of call template.

Possible values are:

**•** `Text`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
TotalCallsCallBackLater
TotalCallsLeftVoicemail
TotalCallsMeaningfulConnect
TotalCallsNotInterested
TotalCallsUncategorized
TotalCallsUnqualified

```

**Description**
The total number of calls that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Call Back Later call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Left Voicemail call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Meaningful Connect call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total Not Interested call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total uncategorized call results that use the CallTemplate.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The total Unqualified call results that use the CallTemplate.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CallTemplateChangeEvent (API version 48.0)**
Change events are available for the object.
