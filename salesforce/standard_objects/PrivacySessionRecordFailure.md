#### PrivacySessionRecordFailure

Represents error messages encountered during policy job executions in Privacy Center. This object is available in API version 59.0 and
later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
This object is available for users with the Privacy Center license and the Manage Privacy Center Policies user permission.

##### Fields

```
ErrorMessage
ErrorType
Name
OwnerId

```

**Type**
textarea

**Properties**
Nillable

**Description**
The description of the error encountered during the policy job execution.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of error encountered during the policy job execution.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Represents the job session record. This is a serialized, automatically generated number field.

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
PrivacyObjectSessionId
RecordIdNumber

##### Associated Objects

```

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
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the object in the policy job session.

This field is a relationship field.

**Relationship Name**
PrivacyObjectSession

**Relationship Type**
Lookup

**Refers To**
PrivacyObjectSession

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that failed to be processed by the policy job.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**PrivacySessionRecordFailureOwnerSharingRule on page 64**
Sharing rules are available for the object.

**PrivacySessionRecordFailureShare on page 66**
Sharing is available for the object.


-----
