#### QueueSobject

Represents the mapping between a queue Group and the types associated with the queue, including custom objects.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

A queue is a Group whose `Type` is `Queue. To create a Group, you must have the Manage Users permission.`

##### Fields

```
 QueueId
 SobjectType

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of a queue.

This field is a relationship field.

**Relationship Name**
Queue

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
A list of object types that can be associated with the queue specified by the `QueueId.`


Use this object to associate a queue with the sObject that can be associated with the queue, including custom objects.

Warning: You can't update or insert more than 18 queues at once when using the Bulk API.

SEE ALSO:

Overview of Salesforce Objects and Fields


-----
