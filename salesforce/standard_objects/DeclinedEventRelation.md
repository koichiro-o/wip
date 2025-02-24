#### DeclinedEventRelation

Represents event participants (invitees or attendees) with the status Declined for a given event.This object is available in API versions
29.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
EventId
RelationId
RespondedDate

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the event.

This is a relationship field.

**Relationship Name**
Event

**Relationship Type**
Lookup

**Refers To**
Event

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the ID of the invitee.

This is a polymorphic relationship field.

**Relationship Name**
Relation

**Relationship Type**
Lookup

**Refers To**
Calendar, Contact, Lead, User

**Type**
dateTime


-----

```
Response
Type

##### Usage

```

**Properties**
Filter, Nillable, Sort

**Description**
Indicates the most recent date and time when the invitee declined an invitation
to the event.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the content of the response field. Label is `Comment.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates whether the invitee is a user, lead or contact, or resource.


**Query invitees who have declined an invitation to an event**
```
  SELECT eventId, type, response FROM DeclinedEventRelation WHERE eventid='00UTD000000ZH5LA'

```
SEE ALSO:

AcceptedEventRelation

UndecidedEventRelation
