#### AsyncOperationLog

Represents an async operations log containing progress and status information about external synchronizations to the Omnichannel
Inventory service. This object is available in API version 51.0 and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
search(), undelete()

 Special Access Rules

```
This object is only available in Omnichannel Inventory orgs.

##### Fields

```
AsyncOperationNumber
Description
Error
ExternalReference

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The auto-generated number assigned to the operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the operation.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message for the operation. Applies only if the operation has an error.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort


-----

```
FinishedAt
LastStatusUpdateAt
RelatedRecordId
Request
Response

```

**Description**
The unique external reference ID per type.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation finished.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the status of the operation was last updated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The related record ID for the async request. This field is available in API version 60.0 and later.

This field is a polymorphic relationship field.

**Relationship Name**
RelatedRecord

**Relationship Type**
Lookup

**Refers To**
Asset, OrderItemSummary

**Type**
textarea

**Properties**
Nillable

**Description**
The request sent to the external service.

**Type**
textarea


-----

```
StartedAt
Status
Type

```

**Properties**
Nillable

**Description**
The full response from the external service.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the operation started.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the operation.

Possible values are:

**•** `Completed`

**•** `Error`

**•** `In Progress`

**•** `New`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of operation that is being tracked.

Possible values are:

**•** `CancelAsset—This value is available in API version 60.0 and later.`

**•** `CreateAsset—This value is available in API version 60.0 and later.`

**•** `LocationManagement`

**•** `OrderSummaryAdjustmentAggregate`


-----
