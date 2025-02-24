#### PartnerNetworkSyncLog

Represents the Org Sync Log tab in Salesforce, where Salesforce administrators can track the replication of record inserts and updates
being performed in Organization Sync. The Connection Detail page for the replication connection also displays the Org Sync Log’s twenty
most recent entries, and provides a link to the log.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

```

-----

##### Special Access Rules

The Org Sync Log tab can only be added in organizations where Organization Sync has been enabled. To add the tab to the Salesforce
user interface, users must also have the “Manage Connections” user permission.

##### Fields

```
ConnectionEvent
ConnectionId
Description
EntityType
Error

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The action being replicated to the partner organization, such as a record insertion.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the Salesforce to Salesforce replication connection in which the
replication event succeeded or failed.

**Type**
textarea

**Properties**
Nillable

**Description**
A description of the replication event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of record being inserted or updated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The code used to describe the replication failure or success.


-----

```
LocalRecord
Status
