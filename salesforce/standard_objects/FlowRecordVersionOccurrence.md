#### FlowRecordVersionOccurrence

Represents an instance of a recurring flow that runs on a schedule. For example, a flow that runs weekly on Wednesdays creates an
occurrence each time it runs. This object is available in API version 60.0 and later.

##### Supported Calls
```
describe(), read()

 Fields

```
```
Entries
Errors
ErrorDetail
Exits
FlowRecordId

```

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of entries for this occurrence.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of errors for this occurrence.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A description of the error. This field is available in API version 63.0 and later.

**Type**
integer

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The number of exits for this occurrence.

**Type**
string


-----

```
FlowRecordVersionId
ProgressStatus

```

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated flow record.

**Type**
string

**Properties**
Filter, Group, Query, Retrieve, Sort

**Description**
The ID of the associated version of the flow record.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The running status of the flow interview.

Valid values are:

**•** `Canceled`

Specifies a flow interview that was deactivated by a user. The flow doesn’t process
previously added records and no additional records are added to this flow.

**•** `Completed`

Indicates a flow interview that is complete. No additional records are eligible to
be processed in this flow.

**•** `Error`

Indicates a flow interview that has been deactivated because it encountered an
error. When the error occurs, the error details are emailed to up to 5 users with
the Manage Flows permission who most recently logged into Salesforce.

**•** `Finishing`

Indicates a flow interview that was deactivated by a user, but is finishing records
previously added that are eligible to run to completion. No additional records are
added to this flow.

**•** `InProgress`

Indicates a flow interview that is running or ready to run.

**•** `PreparingData`

Indicates a flow interview that is preparing the resources it requires to run. This
process can take up to 2 hours.


-----

```
ScheduledDate
Stopped
