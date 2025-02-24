#### ApexLog

```

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
How long it takes (in milliseconds) to prepare and execute the query and to retrieve the
query results.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who’s using Salesforce services through the UI or the API. For example:
```
  00530000009M943.

```

Represents a debug log containing information about a transaction, including information about Apex, Visualforce, and workflow and
validation rules. This object is available in API version 19.0 and later.

##### Supported Calls
```
delete(), describeSObjects(), query(), retrieve()

 Fields

```
```
Application

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
This value depends on the client type that triggered the log.

**•** For API clients, this value is the client ID.


-----

```
DurationMilliseconds
Location
LogLength
LogUserId

```


**•** For browser clients, this value is `Browser.`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Duration of the transaction in milliseconds.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies the location of the origin of the log. Values are:

**•** `Monitoring—Log is generated as part of debug log monitoring. These types of logs`
are maintained for seven days or until a user deletes them.

**•** `SystemLog—Log is generated from the Developer Console. These types of logs are`
maintained for 24 hours or until the user clears them.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Length of the log in bytes.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the user whose actions triggered the debug log.

This is a polymorphic relationship field.

**Relationship Name**
LogUser

**Relationship Type**
Lookup

**Refers To**
User


-----

```
Operation
Request
RequestIdentifier
StartTime
Status

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the operation that triggered the debug log, such as APEXSOAP, Apex Sharing
```
  Recalculation, and so on.

```
**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Request type. Values are:

**•** `API—Request came from the API`

**•** `Application—Request came from the Salesforce user interface`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique identifier of the request that triggered the debug log. Use this request identifier
to correlate multiple debug logs triggered by the same request.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Start time of the transaction.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Status of the transaction. This value is either `Success, or the text of an unhandled Apex`
exception.


-----

##### Usage

You can read information about this object, as well as delete it, but you can't update or insert it.

SEE ALSO:

ApexClass

ApexTrigger

_[Developer Guide: Apex Developer Guide](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/)_
