#### UserPrioritizedRecord

Represents records that Pipeline Inspection, Account Intelligence, Contact Intelligence, and Lead Intelligence users flag as important for
tracking in pipeline and intelligence views and filters. This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
update(), upsert()

 Special Access Rules

```
To use UserPrioritizedRecord in Pipeline Inspection and the Account Intelligence, Contact Intelligence, and Lead Intelligence views,
enable the Pipeline Inspection user permission and the Pipeline Inspection setting.

##### Fields

```
OwnerId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who marked this record as important.

This field is a polymorphic relationship field.


-----

```
TargetId
TargetKeyPrefix

##### Associated Objects

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the target object that is marked as important. Supported objects include:

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

This field is a polymorphic relationship field.

**Relationship Name**
Target

**Relationship Type**
Lookup

**Refers To**

**•** Account

**•** Contact

**•** Lead

**•** Opportunity

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The key prefix of the target object that is marked as important.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**UserPrioritizedRecordOwnerSharingRule on page 64**
Sharing rules are available for the object.

**UserPrioritizedRecordShare on page 66**
Sharing is available for the object.
