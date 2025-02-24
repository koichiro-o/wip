### sObject Get Updated

Retrieves the list of individual records that have been updated (added or changed) within the given timespan for the specified object.
This resource is available in REST API version 31.0 and later.

This resource is commonly used in data replication applications. Note these considerations:

**•** Results are returned for no more than 30 days previous to the day the call is executed.

**•** Your client application can replicate any objects to which it has sufficient permissions. For example, to replicate all data for your
organization, your client application must be logged in with “View All Data” access rights to the specified object. Similarly, the objects
must be within your sharing rules.

**•** There is a limit of 600,000 IDs returned from this resource. If more than 600,000 IDs are found, EXCEEDED_ID_LIMIT is returned.
You can correct the error by choosing start and end dates that are closer together.

**•** The call uses the `SystemModstamp` field to determine an object's add or change date. If `SystemModstamp` isn’t available,
the call uses `LastModifiedDate.`


-----

[See “Data Replication” in the SOAP API Developer Guide for additional details on data replication and data replication limits.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/)

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/updated/?start=startDateAndTime&end=endDateAndTime

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

**Parameter** **Description**

`start` Starting date/time (Coordinated Universal Time (UTC) time zone—not local— timezone)
of the timespan for which to retrieve the data. The API ignores the seconds portion of

the specified dateTime value (for example, 12:30:15 is interpreted as 12:30:00 UTC).
The date and time must be formatted as described in Valid Date and DateTime Formats.
The date/time value for `start` must chronologically precede `end. This parameter`
must be URL-encoded

`end` Ending date/time (Coordinated Universal Time (UTC) time zone—not local— timezone)
of the timespan for which to retrieve the data. The API ignores the seconds portion of

the specified dateTime value (for example, 12:35:15 is interpreted as 12:35:00 UTC).
The date and time must be formatted as described in Valid Date and DateTime Formats.
This parameter must be URL-encoded

**Response format**

**Property** **Type** **Description**

`ids` array Array of updated records that satisfy the start and end dates specified in the
request. Each entry contains the record ID.

`latestDateCovered` String ISO 8601 format timestamp (Coordinated Universal Time (UTC)—not local—
time zone) of the last date covered in the request.

#### Examples

For an example of getting a list of updated deleted items, see Get a List of Updated Records Within a Given Timeframe.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)


-----
