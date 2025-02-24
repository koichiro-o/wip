#### VendorCallCenterStatusMap

Stores a mapping between a call center vendor agent status and a Salesforce presence status for an associated call center. This object
is available in API version 54.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, Omni-Channel and Service Cloud Voice must be enabled.

##### Fields

```
CallCenterId
ExternalStatus
ServicePresenceStatusId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Reference to a call center.

This is a relationship field.

**Relationship Name**
CallCenter

**Relationship Type**
Lookup

**Refers To**
CallCenter

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Status value to set for the call center vendor agent.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**
Reference to a presence status that can be assigned to a service channel.

This is a relationship field.

**Relationship Name**
ServicePresenceStatus

**Relationship Type**
Lookup

**Refers To**
ServicePresenceStatus
