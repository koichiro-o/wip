### Working with Approval Processes and Process Rules

The examples in this section use REST API resources to work with approval processes and process rules.

IN THIS SECTION:

Get a List of All Approval Processes
Use the Process Approvals resource to get information about approvals.

Submit a Record for Approval
Use the Process Approvals resource to submit a record or a collection of records for approval. Each call takes an array of requests.

Approve a Record
Use the Process Approvals resource to approve a record or a collection of records. Each call takes an array of requests. The current
user must be an assigned approver.

Reject a Record
Use the Process Approvals resource to reject a record or a collection of records. Each call takes an array of requests. The current user
must be an assigned approver.

Bulk Approvals
Use the Process Approvals resource to do bulk approvals. You can specify a collection of different Process Approvals requests to have
them all executed in bulk.

Get a List of Process Rules
Use the Process Rules resource to get information about process rules.

Get a Particular Process Rule
Use the Process Rules resource and specify thesObjectName and workflowRuleId of the rule you want to get the metadata
for.

Trigger Process Rules
Use the Process Rules resource to trigger process rules. All rules associated with the specified ID will be evaluated, regardless of the
evaluation criteria. All IDs must be for records on the same object.

#### Get a List of All Approval Processes

Use the Process Approvals resource to get information about approvals.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/approvals/ -H
  "Authorization: Bearer token"

```
**Example request body**
none required

**Example JSON response body**


-----

#### Submit a Record for Approval

Use the Process Approvals resource to submit a record or a collection of records for approval. Each call takes an array of requests.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/approvals/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d @submit.json"

```
**Example request body** `submit.json` **file**

In the following example, the record "001D000000I8mIm" is submitted for approval process "PTO_Request_Process" by skipping its
entry criteria on behalf of submitter "005D00000015rZy."
```
  {
  "requests" : [{
  "actionType": "Submit",
  "contextId": "001D000000I8mIm",
  "nextApproverIds": ["005D00000015rY9"],
  "comments":"this is a test",
  "contextActorId": "005D00000015rZy",
  "processDefinitionNameOrId" : "PTO_Request_Process",
  "skipEntryCriteria": "true"}]
  }

```
**Example JSON response body**
```
  [ {
   "actorIds" : [ "005D00000015rY9IAI" ],
    "entityId" : "001D000000I8mImIAJ",
    "errors" : null,
    "instanceId" : "04gD0000000Cvm5IAC",
    "instanceStatus" : "Pending",
    "newWorkitemIds" : [ "04iD0000000Cw6SIAS" ],
    "success" : true } ]

#### Approve a Record

```
Use the Process Approvals resource to approve a record or a collection of records. Each call takes an array of requests. The current user
must be an assigned approver.

**Example usage**


-----

**Example request body** `approve.json` **file**
```
  {
   "requests" : [{
    "actionType" : "Approve",
    "contextId" : "04iD0000000Cw6SIAS",
    "nextApproverIds" : ["005D00000015rY9"],
    "comments" : "this record is approved"}]
  }

```
**Example JSON response body**
```
  [ {
   "actorIds" : null,
   "entityId" : "001D000000I8mImIAJ",
   "errors" : null,
   "instanceId" : "04gD0000000CvmAIAS",
   "instanceStatus" : "Approved",
   "newWorkitemIds" : [ ],
   "success" : true
  } ]

#### Reject a Record

```
Use the Process Approvals resource to reject a record or a collection of records. Each call takes an array of requests. The current user
must be an assigned approver.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/approvals/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d @reject.json"

```
**Example request body** `reject.json` **file**
```
  {
   "requests" : [{
    "actionType" : "Reject",
    "contextId" : "04iD0000000Cw6cIAC",
    "comments" : "This record is rejected."}]
  }

```
**Example JSON response body**


-----

#### Bulk Approvals

Use the Process Approvals resource to do bulk approvals. You can specify a collection of different Process Approvals requests to have
them all executed in bulk.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/approvals/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d @bulk.json"

```
**Example request body** `bulk.json` **file**
```
  {
   "requests" :
   [{
    "actionType" : "Approve",
    "contextId" : "04iD0000000Cw6r",
    "comments" : "approving an account"
    },{
    "actionType" : "Submit",
    "contextId" : "001D000000JRWBd",
    "nextApproverIds" : ["005D00000015rY9"],
    "comments" : "submitting an account"
    },{
    "actionType" : "Submit",
    "contextId" : "003D000000QBZ08",
    "comments" : "submitting a contact"
    }]
  }

```
**Example JSON response body**


-----

#### Get a List of Process Rules

Use the Process Rules resource to get information about process rules.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/ -H
  "Authorization: Bearer token"

```
**Example request body**
none required

**Example JSON response body**
```
  {
   "rules" : {
    "Account" : [ {
      "actions" : [ {
       "id" : "01VD0000000D2w7",
       "name" : "ApprovalProcessTask",
       "type" : "Task"
      } ],
      "description" : null,
      "id" : "01QD0000000APli",
      "name" : "My Rule",
      "namespacePrefix" : null,
      "object" : "Account"
    } ]
   }
  }

#### Get a Particular Process Rule

```
Use the Process Rules resource and specify thesObjectName and `workflowRuleId` of the rule you want to get the metadata
for.

**Example usage**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/Account/01QD0000000APli
   -H "Authorization: Bearer token"

```
**Example request body**
none required

**Example JSON response body**


-----

#### Trigger Process Rules

Use the Process Rules resource to trigger process rules. All rules associated with the specified ID will be evaluated, regardless of the
evaluation criteria. All IDs must be for records on the same object.

**Example usage**
```
  curl https://MyDomainName.my.salesforce.com/services/data/v62.0/process/rules/ -H
  "Authorization: Bearer token" -H "Content-Type: application/json" -d @rules.json"

```
**Example request body** `rules.json` **file**
```
  {
   "contextIds" : [
    "001D000000JRWBd",
    "001D000000I8mIm",
    "001D000000I8aaf"]
  }

```
**Example JSON response body**
```
  {
   "errors" : null,
   "success" : true
  }
