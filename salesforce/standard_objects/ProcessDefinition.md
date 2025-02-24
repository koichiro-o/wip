#### ProcessDefinition

Represents the definition of a single approval process.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), search()

```
Portal and communities users with the Customer Community Plus and Partner Community licenses can access this object. All users in
org with approvals enabled have read access to ProcessDefinition.

##### Fields

```
Description

```

**Type**
textarea


-----

```
DeveloperName
LockType
Name
State

```

**Properties**
Filter, Nillable, Sort

**Description**
A description of this process, with a maximum of 3,000 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique process name, used internally.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of lock applied to the record being approved. When a record is in the approval
process, it’s always locked, and only an administrator can edit it. However, the currently
assigned approver can also be allowed to edit the record.

**•** Total

**•** Admin

**•** Owner

**•** Workitem

**•** Node

**•** none

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The external name of the process; the name seen by users.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The current state of this process.

**•** Active


-----

```
TableEnumOrId
Type

##### Usage

```


**•** Inactive

**•** Obsolete

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Specifies the object associated with the approval process, such as Account or Contact.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this process.

**•** Approval Process—Used to control the action taken for a record.

**•** State-based Process—Used internally to track various control processes, such as for
developing Salesforce Knowledge articles.


Use this object to read the description of an approval process. The definition is read-only.
