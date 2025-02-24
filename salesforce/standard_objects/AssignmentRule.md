#### AssignmentRule

Represents an assignment rule associated with a Case or Lead.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), search()

 Special Access Rules

```
**•** This object is read only. Assignment rules are created, configured, and deleted in the user interface.


-----

**•** Customer Portal users can’t access this object.

##### Fields

```
 Active
 Name
 SobjectType

##### Usage

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this assignment rule is active (true) or not (false).

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of this assignment rule.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type of assignment rule—Case or Lead.


Before creating or updating a new Case or Lead, a client application can query (by name) the AssignmentRule to obtain the ID of the
assignment rule to use, and then assign that ID to the `assignmentRuleId` field of the AssignmentRuleHeader. The
AssignmentRuleHeader can be set using either SOAP API or REST API.

Assignment rules can also be specified when creating or upserting Case or Lead objects via the Bulk API or the Bulk 2.0 API.

SEE ALSO:

Overview of Salesforce Objects and Fields
