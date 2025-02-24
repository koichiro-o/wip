#### DuplicateRecordItem

Represents an individual record that’s part of a duplicate record set. Use this object to create custom report types.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, enable Duplicate Management. A Salesforce admin can grant access to any user with a Sales Cloud or CRM user
license.

##### Fields

```
DuplicateRecordSetId
Name

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The duplicate record set that the duplicate record item is assigned to.

This is a relationship field.

**Relationship Name**
DuplicateRecordSet

**Relationship Type**
Lookup

**Refers To**
DuplicateRecordSet

**Type**
string


-----

```
RecordId
