#### UserProvisioningLog

Represents messages generated during the process of provisioning users for third-party applications. This object is available in API version
33.0 and later.

Some messages for this object are generated automatically by Salesforce, and others are created by the developers of the user provisioning
plugin. Developers can use this object to log messages from the flow associated with the user provisioning process or the Apex plugin
that calls the target system. Administrators can use this object as a log of all user provisioning activity and as a troubleshooting tool if
desired behavior is missing. This object is available as a custom report type.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), undelete(), update(), upsert()

 Fields

```
```
Details
ExternalUserId
ExternalUsername
Name

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The value of this field depends on the log entry. For example, if the target system returns an
error, the error message may be recorded in this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The unique identifier for the user in the target system.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The username set in the target system for the associated user account.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
OwnerId
Status
UserId
UserProvisioningRequestId

```

**Description**
The unique name for this object.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Salesforce ID of the Group or User who owns this object.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The status of the user provisioning request. Based on the context of the log, it can contain
different values, such as an HttpStatusCode.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Salesforce ID of the user making the request.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique identifier for the user provisioning request.

This is a relationship field.

**Relationship Name**
UserProvisioningRequest


-----

**Relationship Type**
Lookup

**Refers To**
UserProvisioningRequest
