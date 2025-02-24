#### OmniSupervisorConfigProfile

Represents the supervisor profiles to which an Omni-Channel supervisor configuration applies. User-level configurations override
profile-level configurations. This object is available in API version 41.0 and later.


-----

##### Supported Calls
```
create(), delete(), query(), update(), retrieve()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
OmniSupervisorConfigId
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
A unique identifier for the Omni-Channel supervisor configuration.

This is a relationship field.

**Relationship Name**
OmniSupervisorConfig

**Relationship Type**
Lookup

**Refers To**
OmniSupervisorConfig

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
A unique identifier for the profile that’s associated with this Omni-Channel supervisor
configuration. A profile can be associated with only one Omni-Channel supervisor
configuration. This field is unique within your org.

This is a relationship field.

**Relationship Name**
Profile

**Relationship Type**
Lookup

**Refers To**
Profile


-----
