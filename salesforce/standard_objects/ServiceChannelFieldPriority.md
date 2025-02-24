#### ServiceChannelFieldPriority

Represents a secondary routing priority field-value mapping. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
[To access this object, Omni-Channel must be enabled.](https://help.salesforce.com/articleView?id=omnichannel_intro.htm&type=5&language=en_US)

##### Fields

```
Priority
ServiceChannelId
Value

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The priority number assigned to the mapped field value.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service channel.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The value of the SecRoutingPriorityField field defined in parent ServiceChannel.

