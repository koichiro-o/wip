#### PrivacyObjectSession

Represents the status of each object being processed in past, ongoing, and scheduled policy jobs in Privacy Center. This object is available
in API version 59.0 and later.

See the status of each object as a policy executes. For example, if a Data Management policy includes an Account object and a Contact
object, then a PrivacyObjectSession record is created for each object.

Each object in a policy has five potential queues to enter. The first queue captures and stores records targeted by the policy filters. If the
first queue run fails to capture every record, then the object goes through three retry attempts to capture the remaining records. The
fifth queue stores the record IDs of any records that weren’t captured in any of the four attempts.

This object is Read-only.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.


-----

##### Fields

**Field**
```
CurrentEntity
Name
ObjectFailureLog
ObjectStatus
OwnerId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object in the policy.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
textarea

**Properties**
Nillable

**Description**
This field is reserved for later use.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The policy execution status for the object.

Possible values are:

**•** `processing_completed`

**•** `processing_failed`

**•** `processing_ongoing`

**•** `processing_pending`

**•** `traversal_completed`

**•** `traversal_failed`

**•** `traversal_ongoing`

**Type**
reference


-----

```
PolicyNode
Position
PrivacyJobSessionObjectId

```

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with the customer that the policy was executed
for.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the object in the serialized policy. This field associates the object session in the
policy execution with the coordinating object in the Privacy Center policy.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents a record’s position in the batch queue for the object being processed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyJobSessionObject

**Relationship Type**
Lookup

**Refers To**
PrivacyJobSession


-----

```
ProcessType
ProcessedFailures
ProcessedSuccesses
ProcessedTotal
Processor

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of action being executed on the object in the policy.

Possible values are:

**•** `delete`

**•** `mask`

**•** `retry_delete`

**•** `retry_mask`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution failed to process.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records the policy execution successfully processed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records processed in the policy job.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the deletion, masking, or traversal processor executing the policy job.


-----

```
Queue
QueueLength
RecordsAffected
Retry
TraversalEndTime
TraversalStartTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is reserved for later use.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of records in the queue to be processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of records processed by the policy job.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The queue number of the retry session after a failed policy execution attempt. Each attempt
to retry the policy execution is put into a retry queue.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The end time of the record-capturing phase for the object session.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
UniqueConstraint

##### Associated Objects

```

**Description**
The start time of the record-capturing phase for the object session.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
For internal use only.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyObjectSessionOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PrivacyObjectSessionShare on page 66**
Sharing is available for the object.
