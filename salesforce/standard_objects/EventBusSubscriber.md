#### EventBusSubscriber

Represents a trigger, process, or flow that’s subscribed to a platform event or a change data capture event. Doesn’t include CometD or
Pub/Sub API subscribers.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
EventBusSubscriber is read only and can only be queried. As of Summer ’20 and later, only your Salesforce org's internal users can access
this object.

##### Fields

```
ExternalId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
IsPartitioned
LastError
Name
Position
Retries

```

**Description**
The ID of the subscriber. For example, the trigger ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the platform event Apex trigger is configured with parallel subscriptions
[(true) or not (false). The default value is false. See Platform Event Processing at Scale](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_ps.htm)
[with Parallel Subscriptions for Apex Triggers in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_ps.htm)

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error message that the last thrown EventBus.RetryableException contains.
This field applies to Apex triggers only. Available in API version 43.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subscribed item, such as the trigger or process name. If the subscribed
item’s name is “Process”, at least one flow Pause element is subscribed to the event.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last event that the subscriber processed.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
Status
Tip
Topic

```

**Description**
The number of times the trigger was retried due to throwing the
```
  EventBus.RetryableException. This field applies to Apex triggers only. Available

```
in API version 43.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Indicates the status of the subscriber. Can be one of these values:

**•** `Error— The subscriber was disconnected and stopped receiving published events.`
A trigger reaches this state when it exceeds the number of maximum retries with the
```
   EventBus.RetryableException. Trigger assertion failures and unhandled

```
exceptions don’t cause the error state. We recommend limiting the retries to fewer than
nine times to avoid reaching this state. When you fix and save the trigger, or for a
managed package trigger, if you redeploy the package, the trigger resumes automatically
from the tip, starting from new events. Also, you can resume a trigger subscription in
the subscription detail page that you access from the platform event page.

**•** `Repartitioning—The system is in the process of modifying the trigger's parallel`
subscription configuration.

**•** `Running—The subscriber is actively listening to events. If you modify the subscriber,`
the subscription continues to process events.

**•** `Suspended—The subscriber is disconnected and can’t receive events because a`
Salesforce admin suspended it or due to an internal error. You can resume a trigger
subscription in the subscription detail page that you access from the platform event
page. To resume a process, deactivate it and then reactivate it. If you modify the
subscriber, the subscription resumes automatically from the tip, starting from new events.

[For more information, see View and Manage an Event’s Subscribers on the Platform Event’s](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm)
[Detail Page in the Platform Events Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.platform_events.meta/platform_events/platform_events_get_subscribers_apex.htm)

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The replay ID of the last published event.

Note: For high-volume platform events and change events, the value for Tip isn’t
available and is always -1.

**Type**
string


-----

```
Type

##### Usage

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subscription channel that corresponds to a platform event or change event.
For a platform event, the topic name is the event name appended with `__e, such as`
```
  MyEvent__e. For a change event, the topic is the name of the change event, such as
  AccountChangeEvent.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subscriber type (ApexTrigger). If the subscriber is a process or flow Pause element,
the type is blank.


Use EventBusSubscriber to query details about subscribers to a platform event. You can get all subscribers for a particular event by
filtering on the `Topic` field, as follows.
```
SELECT ExternalId, Name, Position, Status, Tip, Type
FROM EventBusSubscriber
WHERE Topic='Low_Ink__e'
