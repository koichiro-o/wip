### Process Approvals

```
Accesses all approval processes. Can also be used to submit a particular record if that entity supports an approval process and one has
already been defined. Records can be approved and rejected if the current user is an assigned approver.

IN THIS SECTION:

Get Process Approvals
Gets a list of all approval processes. This resource is available in REST API version 30.0 and later.

Submit, Approve, or Reject Process Approvals
Submits a particular record if that entity supports an approval process and one has already been defined. Records can be approved
and rejected if the current user is an assigned approver. This resource is available in REST API version 30.0 and later.


-----

Return HTTP Headers for Process Approvals
Returns only the headers that are returned by sending a GET request to the process approvals resource. This gives you a chance to
see returned header values of the GET request before retrieving the content. This resource is available in REST API version 30.0 and
later.

#### Get Process Approvals

Gets a list of all approval processes. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/approvals/

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

**Example**
See Get a List of All Approval Processes..

#### Submit, Approve, or Reject Process Approvals

Submits a particular record if that entity supports an approval process and one has already been defined. Records can be approved and
rejected if the current user is an assigned approver. This resource is available in REST API version 30.0 and later.

When using a POST request to do bulk approvals, the requests that succeed are committed and the requests that don’t succeed send
back an error.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/approvals/

```
**Formats**
JSON, XML

**HTTP methods**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required


-----

**Request body**
The request body contains an array of process requests that contain the following information:

**Name** **Type** **Description**

`actionType` string Represents the kind of action to take: `Submit,` `Approve, or` `Reject.`

`contextActorId` ID The ID of the submitter who’s requesting the approval record.

`contextId` ID The ID of the item that is being acted upon.

`comments` string The comment to add to the history step associated with this request.

`nextApproverIds` ID[] If the process requires specification of the next approval, the ID of the user to be
assigned the next request.

`processDefinitionNameOrId` string The developer name or ID of the process definition.

`skipEntryCriteria` boolean Determines whether to evaluate the entry criteria for the process (true) or not
(false) if the process definition name or ID isn’t null. If the process definition name

or ID isn’t specified, this argument is ignored, and standard evaluation is followed
based on process order. By default, the entry criteria isn’t skipped if it’s not set
by this request.

**Response body**
The response contains an array of process results that contain the following information:

**Name** **Type** **Description**

`actorIds` ID[] IDs of the users who are currently assigned to this approval step.

`entityId` ID The object being processed.

`errors` Error[] The set of errors returned if the request failed.

`instanceId` ID The ID of the ProcessInstance associated with the object submitted for processing.


`instanceStatus` string


The status of the current process instance (not an individual object but the entire
process instance). The valid values are “Approved,” “Rejected,” “Removed,” or
“Pending.”


`newWorkItemIds` ID[] Case-insensitive IDs that point to ProcessInstanceWorkitem items (the set of
pending approval requests)

`success` boolean `true` if processing or approval completed successfully.

##### Example

**•** See Submit a Record for Approval.

**•** See Approve a Record.

**•** See Reject a Record.

**•** See Bulk Approvals.


-----

#### Return HTTP Headers for Process Approvals

Returns only the headers that are returned by sending a GET request to the process approvals resource. This gives you a chance to see
returned header values of the GET request before retrieving the content. This resource is available in REST API version 30.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/process/approvals/

```
**Formats**
JSON, XML

**HTTP methods**
HEAD

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**
None required

##### Example

**Example Request**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/approvals/ -H
  "Authorization: Bearer token"

```
**Example Response Body**
```
  HTTP/1.1 200 OK
  Date: Mon, 21 Nov 2022 22:56:26 GMT
