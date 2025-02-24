#### ServiceChannelStatus

Represents the status that’s associated with a specific service channel. This object is available in API version 32.0 and later.


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
ServiceChannelId
ServicePresenceStatusId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the presence status that’s associated with the service channel that’s specified by
the `ServicePresenceChannelId.`

