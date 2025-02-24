#### TaskRelation

Represents the relationship between a task and a lead, contacts, and other objects related to the task. If Shared Activities is enabled, this
object doesn’t support triggers, workflow, or data validation rules. This object is available in API version 24.0 and later.

TaskRelation is only available if you’ve enabled Shared Activities in your organization.

TaskRelation allows the following relationships:

**•** A task can be related to one lead or up to 50 contacts.

**•** A task can also be related to one account, asset, campaign, case, contract, opportunity, product, solution, or custom object.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), queryAll(),
retrieve()

 Fields

```
```
AccountId
IsWhat
RelationId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the Account ID of the relation.

For information on IDs, see ID Field Type.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the relation is an Account, Opportunity, Campaign, Case, other
standard object, or a custom object. Value is `false` if `RelationId is a`
contact or lead and `true` otherwise.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Indicates the WhatId or WhoId in the relationship. For more information, see
```
  Task.

```
For information on IDs, see ID Field Type.


-----

```
TaskId

##### Usage

```
**See contacts associated with a task**
```
  public void
     String soqlQuery =
    QueryResult qResult =
    try {
       TaskRelation relation1 =
    }catch
       ce.printStackTrace();
     }
   }

##### Associated Objects

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Represents the ID of the associated Task.

For information on IDs, see ID Field Type.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaskRelationChangeEvent (API version 44.0)**
Change events are available for the object.

SEE ALSO:

Task

TaskWhoRelation
