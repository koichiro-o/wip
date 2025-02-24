#### MobileSettingsAssignment

Represents the assignment of a particular field service mobile settings configuration to a user profile. This object is available in API version
41.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout()—available in API version 51.0 and later, describeSObjects(), query(),
retrieve(), update(), upsert()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
FieldServiceMobileSettingsId
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of a set of field service mobile settings.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the profile to associate with the set of field service mobile settings.

