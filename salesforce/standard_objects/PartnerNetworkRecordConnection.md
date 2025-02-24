#### PartnerNetworkRecordConnection

Represents a record shared between Salesforce organizations using Salesforce to Salesforce.


-----

##### Supported Calls
```
create(), query()

 Special Access Rules

```
As of Winter ’21 and later, only authenticated internal and external users can access this object.

##### Fields

```
ConnectionId
EndDate
LocalRecordId
ParentRecordId
PartnerRecordId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required. ID of the connection a record is shared with.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date that sharing of the record was stopped.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the shared record.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the parent record of the shared record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
RelatedRecords
SendClosedTasks
SendEmails
SendOpenTasks
StartDate
Status

```

**Description**
ID of the shared record in the connection's organization.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort

**Description**
A comma-separated list of API names for child records to be shared with a parent
record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Forwards closed tasks related to the shared record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Sends an email notifying the connection's representative that you have forwarded
the record to them. Only new recipients of a record will receive a notification email.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Forwards open tasks related to the shared record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date that the shared record was accepted.

**Type**
picklist


-----

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the shared record. One of the following values:

**•** `Active (received)`

**•** `Active (sent)`

**•** `Connected`

**•** `Inactive`

**•** `Inactive (converted)`

**•** `Inactive (deleted)`

**•** `Pending (sent)`

##### Usage

When you create a PartnerNetworkRecordConnection, you forward a record to a connection.

Note: Attempting to forward a record from an object to which the connection is not subscribed results in an `Invalid`
`Partner Network Status` error.

When you delete a PartnerNetworkRecordConnection, you stop sharing a record with a connection.

**•** To share a record, use the following fields: `LocalRecordID and` `ConnectionId`

**•** To share a child of a parent record, use the following fields: `LocalRecordID,` `ConnectionId, and` `ParentRecordID`

**•** To share a child of a parent record and its child records, use the following fields: `LocalRecordID,` `ConnectionId,`
```
  ParentRecordID, and RelatedRecords

```
If the organization does not have Salesforce to Salesforce enabled, the PartnerNetworkRecordConnection object is not available, and
you can’t access it using the API.

SEE ALSO:

PartnerNetworkConnection
