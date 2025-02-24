#### UserRecordAccess

Represents a user’s access to a set of records. This object is read only and is available in API version 24.0 and later. This object doesn’t
consider whether a user’s access is blocked by a restriction rule.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
HasAllAccess
HasDeleteAccess
HasEditAccess
HasTransferAccess
HasReadAccess

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user can share the record.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has delete access to the record (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has edit access to the record (true) or not (false).

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has transfer access to the record (true) or not (false).

**Type**
boolean


-----

```
MaxAccessLevel
RecordId
UserId

##### Usage

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether a user has read access to the record (true) or not (false).

**Type**
picklist

**Properties**
Group, Nillable, Restricted picklist, Sort

**Description**
Indicates a user’s maximum level of access to a record.

Valid values are:

**•** `None`

**•** `Read`

**•** `Edit`

**•** `Delete`

**•** `Transfer`

**•** `All`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
ID of the record.

**Type**
reference

**Properties**
Filter, Group

**Description**
ID of the user.


Use this object to query a user’s access to records. You can only query records of objects listed on the Sharing Settings Setup page. You
can’t create, delete, or update any records using this object.

[Note: UserRecordAccess doesn’t consider whether a user’s access is blocked due to a restriction rule. If a user’s access is blocked](https://developer.salesforce.com/docs/atlas.en-us.254.0.restriction_rules.meta/restriction_rules/restriction_rules_about.htm)
even though query results state that they should have access, check to see if a restriction rule on the object prevents the user’s
access.


-----

Up to 200 record IDs can be queried. You can include an `ORDER BY` clause for any field that is being selected in the query.

The following sample query returns the records, whether the queried user has read and transfer access to each record, and the user’s
maximum access level to each record.
```
SELECT RecordId, HasReadAccess, HasTransferAccess, MaxAccessLevel
   FROM UserRecordAccess
   WHERE UserId = [single ID]
   AND RecordId = [single ID] //or Record IN [list of IDs]

```
The following query returns the records to which a queried user has read access.
```
SELECT RecordId
   FROM UserRecordAccess
   WHERE UserId = [single ID]
   AND RecordId = [single ID] //or Record IN [list of IDs]
   AND HasReadAccess = true

```
Using API version 30.0 and later, UserRecordAccess is a foreign key on the records. You can’t filter by or provide the `UserId` or
`RecordId` fields when using this object as a lookup or foreign key. The previous sample queries can be run as:
```
SELECT Id, Name, UserRecordAccess.HasReadAccess, UserRecordAccess.HasTransferAccess,
UserRecordAccess.MaxAccessLevel
    FROM Account
SELECT Id, Name, UserRecordAccess.HasReadAccess
    FROM Account

```
SOQL restrictions:

**•** When the running user is querying a user's access to a set of records, records that the running user doesn’t have read access to are
filtered out of the results.

**•** When filtering by UserId and RecordId only, you must use SELECT RecordId and optionally one or more of the access
level fields:HasReadAccess, HasEditAccess, HasDeleteAccess, HasTransferAccess, and HasAllAccess.
You can include `MaxAccessLevel.`

**•** When filtering by `UserId,` `RecordId, and an access level field, you must use` `SELECT RecordId` only.

SEE ALSO:

_[Developer Guide: Restriction Rules](https://developer.salesforce.com/docs/atlas.en-us.254.0.api_meta.meta/api_meta/meta_sharingrules.htm)_
