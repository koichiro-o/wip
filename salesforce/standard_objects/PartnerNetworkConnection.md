#### PartnerNetworkConnection

Represents a Salesforce to Salesforce connection between Salesforce organizations.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Winter ’21 and later, only authenticated internal and external users can access this object.


-----

##### Fields

**Field**
```
AccountId
ConnectionName
ConnectionStatus
ConnectionType

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Account associated with this connection.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
A descriptive name for the connection. Limit: 295 characters.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the Salesforce to Salesforce connection. The picklist includes the following
values:

**•** `Sent`

**•** `Received`

**•** `Pending`

**•** `Accepted`

**•** `Rejected`

**•** `Inactive`

**•** `Disconnecting`

**•** `ConnectionSuspended`

**•** `SubscribeInProgress`

**•** `UsersInitialSync`

**•** `BulkSyncMetadata`

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
ContactId
IsSyncAuditFields
IsSyncMetadata
IsSyncUsers

```

**Description**
The type of Salesforce to Salesforce connection. The picklist includes the following
values:

**•** `Standard`

**•** `Replication`

This field is available in API version 30.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the Contact associated with this connection.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether audit fields are synced between the primary and secondary
organization in a replication connection. This field is available in API version 32.0 and
later, and is only accessible in Salesforce organizations where Organization Sync is
enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether supported types of metadata are synced from the primary to the
secondary organization in a replication connection. This field is available in API version
33.0 and later, and is only accessible in Salesforce organizations where Organization
Sync is enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether users with standard Salesforce user licenses are synced between
the primary and secondary organization in a replication connection. This field is


-----

```
PrimaryContactId
ReplicationRole
ResponseDate

##### Usage

```

available in API version 35.0 and later, and is only accessible in Salesforce organizations
where Organization Sync is enabled.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the User associated with this connection.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The role of this Salesforce organization in the replication connection. The picklist
includes the following values:

**•** `Primary`

**•** `Secondary`

This field is available in API version 30.0 and later, and is only accessible in Salesforce
organizations where Organization Sync is enabled.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the connection was accepted or rejected.


Represents Salesforce to Salesforce standard and replication connections. This object is referenced by all objects that have been shared
with other organizations, enabling you to determine which connections shared a record with you. If the organization does not have
Salesforce to Salesforce enabled, the PartnerNetworkConnection object is not available, and you can’t access it via the API.

SEE ALSO:

PartnerNetworkRecordConnection
