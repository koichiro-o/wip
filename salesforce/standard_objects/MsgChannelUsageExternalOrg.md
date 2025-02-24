#### MsgChannelUsageExternalOrg

Represents the Enterprise ID (EID) and Business Unit (MID) for Marketing Cloud connections in a Unified Messaging channel. This object
is available in API version 60.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ExternalOrgIdentifier

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The Enterprise ID (EID) of a Marketing Cloud connection.


-----

```
ExternalSubOrgIdentifier
MessagingChannelUsageId

##### Usage

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The Business Unit (MID) of a Marketing Cloud connection.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The associated MessagingChannelUsage record, which must have a DeploymentType of MJ
(referring to Marketing Cloud Journey Builder).

This field is a relationship field.

**Relationship Name**
MessagingChannelUsage

**Relationship Type**
Lookup

**Refers To**
MessagingChannelUsage


MsgChannelUsageExternalOrg records apply only to MessagingChannelUsage records related to Marketing Cloud.

Only one MsgChannelUsageExternalOrg record can exist for each MessagingChannelUsage record with a DeploymentType of `MJ.`
MsgChannelUsageExternalOrg records are created when an admin enters the EID and MID for a Marketing Cloud application in Unified
Messaging Setup and then clicks Connect.

The data saved in a MsgChannelUsageExternalOrg record is used for making a connection to Marketing Cloud. If an admin disconnects
a Marketing Cloud application in Unified Messaging Setup, the saved EID and MID are used during deprovisioning.
