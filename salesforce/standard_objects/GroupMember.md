#### GroupMember

Represents a User or Group that is a member of a public group.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
GroupId
UserOrGroupId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Group.

This is a relationship field.

**Relationship Name**
Group

**Relationship Type**
Lookup

**Refers To**
Group

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the User or Group that is a direct member of the group.

This field is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

##### Usage

If your group contains more than 10,000 members, for improved performance, you can adjust group membership using the GroupMember
API object instead of the group's detail page in Setup. You can also adjust membership using the public group's access summary or user
access policies in Setup.

A record exists for every User or Group who is a direct member of a public group whose `Type` field is set to Regular. User records that
are indirect members of Regular public groups aren't listed as group members. A User can be an indirect member of a group if he or
she is in a UserRole above the direct group member in the hierarchy, or if he or she is a member of a group that is included as a subgroup
in that group.

If you attempt to create a record that matches an existing record, the system simply returns the existing record.

SEE ALSO:

Overview of Salesforce Objects and Fields
