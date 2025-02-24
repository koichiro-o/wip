#### StampAssignment

Represents assignment of a User Specialty to a user. This object is available in API version 39.0 and later.

Assign a User Specialty to users. This label appears beneath their profile photo.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
StampId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The unique id generated when creating a user specialty.

This is a relationship field.

**Relationship Name**
Stamp

**Relationship Type**
Lookup

**Refers To**
Stamp


-----

```
SubjectId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The id for the user getting the User Specialty label.

This is a relationship field.

**Relationship Name**
Subject

**Relationship Type**
Lookup

**Refers To**
User

