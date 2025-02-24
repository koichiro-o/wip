### Record Count

Lists information about object record counts in your organization.

This resource is available in REST API version 40.0 and later for API users with the “View Setup and Configuration” permission. The returned
record count is a cached snapshot in time that may not accurately represent the number of records in the object at the time of the
request.

The record count value is updated automatically at variable time intervals, and there are no fixed schedules for these updates. It doesn’t
include the following types of records:

**•** Deleted records in the recycle bin

**•** Archived records

**•** Associated objects such as ChangeEvent, Feed, History, OwnerSharingRule, and Share objects

To get an accurate count, use the SOQL query `SELECT count() FROM sObject. Results are limited to records visible to the`
user executing the query.

#### Syntax

**URI**
```
  /services/data/vXX.X/limits/recordCount?sObjects=objectList

```

-----

**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

**Parameter**
```
  sObjects

```
**Response body**

Record Count Response Body

#### Example

**Example Request**
```
  curl
  https://MyDomainName
   -H "Authorization: Bearer token"

```
**Example Response Body**


A comma-delimited list of object names. If a listed object isn’t found in the org, it’s
ignored and not returned in the response.

This parameter is optional. If this parameter isn’t provided, the resource returns record
counts for all objects in the org.


#### Record Count Response Body

Describes the result of a Record Count request.


-----

##### Record Count Results

**Properties**

**Name** **Type** **Description**

`sObjects` Record Count sObject Collection of sObject record count results. The order of objects in the
Result[] collection is not guaranteed to match the order of objects in the request.

**JSON example**
```
  {
    "sObjects" : [ {
     "count" : 3,
     "name" : "Account"
    }, {
     "count" : 10,
     "name" : "Contact"
    } ]
  }

##### Record Count sObject Result

```
**Properties**

**Name** **Type** **Description**

`count` Integer The number of records for the object in the org. This is an approximate
count and does not include soft-deleted or archived records.

`name` String The name of the object.

**JSON example**
```
  {
    "count" : 10,
    "name" : "Contact"
  }
