#### PrivacyJobSession

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the Privacy Hold Reason.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the owner of the account associated with this customer.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


Represents the status of past, ongoing, and scheduled policy jobs in Privacy Center. This object is available in API version 59.0 and later.

This object is Read-only.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.


-----

##### Fields

**Field**
```
CreationDate
CurrentObject
EndTime
FailureLog
JobStartType

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the object that the policy job is currently processing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job finished executing.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of why the policy job failed to execute.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
How the policy job session was started.

Possible values are:

**•** `manual`

**•** `scheduled`


-----

```
JobStatus
Name
OptionsProcessingFailed
OptionsTraversalComplete
OptionsTraversalFailed

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Represents the status of the policy job session.

Possible values are:

**•** `cancelled`

**•** `completed`

**•** `failures`

**•** `inactive`

**•** `running`

**•** `running_next`

**•** `scheduled`

**•** `suspended`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session failed to process the records with the deletion or masking
rules in the policy.

**Type**
boolean

**Properties**
Filter

**Description**
Indicates that the policy job session successfully captured the records targeted by the filters
in the policy.

**Type**
boolean


-----

```
OwnerId
PolicyDescription
PolicyName
PolicyType

```

**Properties**
Filter

**Description**
Indicates that the policy job session failed to capture the records targeted by the filters in
the policy.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the owner of the account associated with this customer.

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
The description of the policy the job session is associated with.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the policy the job session is associated with.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of policy the job session is associated with.

Possible values are:


-----

```
PrivacyPolicyDefinitionId
PrivacyRtbfRequestId
ScheduledTime
SerializedPolicy

```


**•** `datamanagement—Data Management.`

**•** `datamask—This policy type is reserved for future use.`

**•** `rtbf— Right to Be Forgotten.`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the policy the job session is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyPolicyDefinition

**Relationship Type**
Lookup

**Refers To**
PrivacyPolicyDefinition

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the Right to Be Forgotten request the policy job is executing for.

This field is a relationship field.

**Relationship Name**
PrivacyRtbfRequest

**Relationship Type**
Lookup

**Refers To**
PrivacyRTBFRequest

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session is scheduled to run.

**Type**
textarea


-----

```
StartTime

##### Associated Objects

```

**Properties**
Nillable

**Description**
The serial ID of a snapshot of the policy the job session is for. A snapshot of the policy is taken
to maintain consistent metadata for the policy the job is for, in case changes are made to
the policy while the job is executing.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time the policy job session started executing.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacyJobSessionOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PrivacyJobSessionShare on page 66**
Sharing is available for the object.
