#### PresenceUserConfigProfile

Represents a configuration that determines the settings that are assigned to presence users who are assigned to a specific profile.
User-level configurations override profile-level configurations. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), query(), update(), retrieve()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
PresenceUserConfigId
ProfileId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
If an individual user is also assigned a presence configuration through the
PresenceUserConfigProfile, this configuration will override that.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the profile that’s associated with this presence configuration. A profile can be
associated with only one presence configuration.

