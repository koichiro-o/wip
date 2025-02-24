#### BriefcaseAssignment

Represents the assignment of a briefcase definition to selected users and user groups. This object is available in API version 50.0 and
later.

Use this object to assign selected records for users and groups to view offline. Briefcase objects are available in orgs that have Briefcase
Builder and Field Service enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
BriefcaseId
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the briefcase definition. Label is Briefcase Definition ID.

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the user or group requiring access to the briefcase. Label is User or Group
**ID.**

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**BriefcaseAssignmentChangeEvent (API version 55.0)**
Change events are available for the object.
