### sObject Relevant Items

```
Gets the current user’s most relevant items. Relevant items include records for objects in the user’s global search scope and also most
recently used (MRU) objects.

Relevant items include up to 50 of the most recently viewed or updated records for each object in the user’s global search scope.

Note: The user’s global search scope includes the objects the user interacted with most in the last 30 days, including objects the
user pinned from the search results page in the Salesforce Classic.

Then, the resource finds more recent records for each most recently used (MRU) object until the maximum number of records, which
is 2,000, is returned.


-----

This resource only accesses the relevant item information. Modifying the list of relevant items is not currently supported.

This resource is available in API version 35.0 and later.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/relevantItems

```
**Formats**
JSON

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

**Parameter** **Description**

`lastUpdatedId` Optional. Compares the entire current list of relevant items to a previous version, if
available. Specify the `lastUpdatedId` value returned in a previous response.

`sobjects` Optional. To scope the results to a particular object or set of objects, specify the name
for one or more sObjects.

Note: sObject names are case-sensitive.

```
sobject.lastUpdatedId

```

Optional. Compares the current list of relevant items for this particular object to a
previous version, if available. Specify the lastUpdatedId value returned in a
previous response.

Note: You can only specify this parameter for the sObjects specified in the
```
  sobjects parameter.

```

**Response header**
The response contains headers unique to this resource.

**Name** **Type** **Description**

`lastUpdatedId` string A unique code that can be used in subsequent calls to compare the
results for a complete result set with the results in this response list.


`newResultSetSinceLastQuery` boolean (true
or false)


If a response was previously requested for the current user, indicates
whether the current response matches the previous response, or the
one specified by a lastUpdatedId.


**Response body**
The response contains an array of records for each object returned, including the following information for each record.


-----

`apiName` string The object’s unique name, such as Account

`key` ID The first 3 characters of the sObject’s ID that indicates the object type.

`label` string The object’s plural label, such as Accounts.

`lastUpdatedId` string A unique code that can be used in subsequent calls to compare the
results for the new result set with the current results for this object.

`qualifiedApiName` string A unique external name for the sObject.

`recordIds` ID A comma-separated list of IDs for the matching records.

#### Example

See View Relevant Items.
