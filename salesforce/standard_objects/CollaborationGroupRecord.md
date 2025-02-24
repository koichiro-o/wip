#### CollaborationGroupRecord

Represents the records associated with Chatter groups.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
CollaborationGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Chatter group.

This is a relationship field.

**Relationship Name**
CollaborationGroup

**Relationship Type**
Lookup


-----

```
NetworkId
RecordId

##### Associated Objects

```

**Refers To**
CollaborationGroup

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. The ID of the Experience Cloud site that the group belongs to. Available from API
version 34.0.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the record associated with the Chatter group.

This is a polymorphic relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**
Account, Campaign, Case, Contact, Contract, Lead, Opportunity


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CollaborationGroupRecordChangeEvent (API version 62.0)**
Change events are available for the object.
