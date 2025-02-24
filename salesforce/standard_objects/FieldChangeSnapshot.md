#### FieldChangeSnapshot

Use this virtual object to learn which opportunities' close dates changed during the specified time period. This object is available in API
version 52.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
To use FieldChangeSnapshot, set up historical trend reporting for opportunities in your org. You must also have the Pipeline Inspection
user permission and the Pipeline Inspection setting enabled.


-----

##### Fields

**Field**
```
CurrentValueDateOnly
FieldName
ParentId
ValidFrom
ValidTo

```

**Type**
date

**Properties**
Filter, Group, Nillable

**Description**
The current value of a date field on the opportunity.

**Type**
string

**Properties**
Filter, Group

**Description**
The name of the field to get the change history for. Possible values are:

**•** `CloseDate`

**Type**
reference

**Properties**
Filter, Group

**Description**
The ID of the opportunity to get the change history for.

This is a relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
dateTime

**Properties**
Filter

**Description**
The date and time that specifies the beginning of the time period.

**Type**
dateTime


-----

**Properties**
Filter

**Description**
The date and time that specifies the end of the time period.

##### Usage

Use FieldChangeSnapshot to learn about the first change made to the specified opportunity during the specified time period. Subsequent
changes are not returned.

Example: Suppose that last week you changed an opportunity's close date to June 1, 2021. Assuming the opportunity had the
ID '006R0000XXXXXXXXXX', the following query would return the `CurrentValueDateOnly` of June 1, 2021:
```
   Select CurrentValueDateOnly from FieldChangeSnapshot where ParentID =
   '006R0000XXXXXXXXXX' and FieldName = 'CloseDate' and ValidTo = LAST_WEEK AND ValidFrom
   = LAST_WEEK and CurrentValueDateOnly < 2021-07-01
