#### TopicAssignment

Represents the assignment of a topic to a specific feed item, record, or file. This object is available in API version 28.0 and later.

Administrators must enable topics for objects before users can add topics to records of that object type. Topics for most objects are
available in API version 30.0 and later. Topics for ContentDocument are available in API version 37.0 and later.


-----

##### Supported Calls
```
create(), describeSObjects(), delete(), getDeleted(), getUpdate(), query(), retrieve()

 Fields

```
```
EntityId
EntityKeyPrefix
EntityType

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the feed item, record, or file.

This is a polymorphic relationship field.

**Relationship Name**
Entity

**Relationship Type**
Lookup

**Refers To**
Account, Asset, Campaign, Case, Contact, ContentDocument, Contract, Event,
FeedItem, Lead, Opportunity, Order, ProductItem, ProductItemTransaction,
ProductRequest, ProductRequestLineItem, ProductRequired, ProductTransfer,
ResourceAbsence, ResourcePreference, ReturnOrder, ReturnOrderLineItem,
ServiceAppointment, ServiceResource, ServiceResourceSkill, ServiceTerritory,
ServiceTerritoryMember, Shift, Shipment, Solution, Task, WorkOrder,
WorkOrderLineItem

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The first three digits of the `EntityID` field, which identify the object type
(account, opportunity, etc). This read-only field is available in API version 32.0
and later.

Interface label is “Record Key Prefix,” which appears only in reports.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
NetworkId
TopicId

##### Usage

```

**Description**
The standard name for the object type (account, opportunity, etc). This read-only
field is available in API version 33.0 and later.

Note: Querying topic assignments for the ManagedContentVersion entity
type isn’t supported.

Interface label is “Object Type,” which appears only in reports.

Tip: In most cases, you should use this field rather than
```
    EntityKeyPrefix, which exists primarily to support older reports.

```
**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Identifier of the community to which the TopicAssignment belongs. This field is
available only if digital experiences is enabled in your org.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Identifier of the topic.

This is a relationship field.

**Relationship Name**
Topic

**Relationship Type**
Lookup

**Refers To**
Topic


Use this object to query the assignments of topics to feed items, records, or files. To assign or remove topics, you must have the “Assign
Topics” permission.

In SOQL `SELECT` syntax, this object supports nested semi-joins, allowing queries on Knowledge articles assigned to specific topics.
For example:


-----

No SOQL limit if logged-in user has “View All Data” permission. If not, do one of the following:

**•** Specify a LIMIT clause of 1,100 records or fewer.

**•** Filter on `Id` or `Entity` when using a `WHERE` clause with "=".

SEE ALSO:

Topic

FeedItem
