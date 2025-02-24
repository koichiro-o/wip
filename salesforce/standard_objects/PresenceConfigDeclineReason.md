#### PresenceConfigDeclineReason

Represents the settings for a decline reason that a presence user provides when declining work. This object is available in API version
37.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), update(), query(), retrieve()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

As of Spring ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
PresenceDeclineReasonId
PresenceUserConfigId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the PresenceDeclineReason record.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the PresenceUserConfig record where the decline reasons are added.

