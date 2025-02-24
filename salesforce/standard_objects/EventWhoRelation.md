#### EventWhoRelation

Represents the relationship between an event and a lead or contacts. This derived object is a filtered version of the EventRelation on
page 2329 object; that is, IsParent is true and IsWhat is false. It doesn’t represent relationships to invitees or to accounts, opportunities,
or other objects. This object is available in API versions 29.0 and later.

EventWhoRelation allows a variable number of relationships: one lead or up to 50 contacts. Available only if you’ve enabled Shared
Activities for your organization.

Note: EventWhoRelation objects aren’t created for child events.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
EventId

```

**Type**
reference


-----

```
RelationId
Type

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the contacts or lead related to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the person related to the event is a contact or lead.


**Apex example that queries relations to a contact or lead**
```
  List<EventWhoRelation> whoRelations = [SELECT Id, Relation.Name FROM
  EventWhoRelation WHERE EventId = '00UD0000005zijD'];

```
SEE ALSO:

Event

EventRelation
