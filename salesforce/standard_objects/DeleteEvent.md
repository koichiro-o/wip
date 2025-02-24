#### DeleteEvent

```

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the account being managed.

This is a relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**
Account


Represents a record that has been soft deleted. Search on this object was available in API version 48.0, then removed in API version 50.0.

DeleteEvent is a read-only object. You can't create, update, or delete it directly. To create a DeleteEvent record, soft delete a record of
[another type, like an Account. To remove a DeleteEvent record, use the emptyRecycleBin() API or hard delete the corresponding Record.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/sforce_api_calls_emptyrecyclebin.htm)

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
DeletedById

```

**Type**
reference

**Properties**
Filter, Group, Sort


-----

```
DeletedDate
Record
RecordName
SobjectName

```

**Description**
The ID of the user who deleted the record.

This is a relationship field.

**Relationship Name**
DeletedBy

**Relationship Type**
Lookup

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the record was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the record that was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the record that was deleted.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of record that was deleted, for example, Account.


-----
