#### TenantSecurityNotification

Stores information about notifications that were triggered in Security Center as a function of the Alerts feature. For more information,
[see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 54.0 and later.](https://help.salesforce.com/s/articleView?id=sf.security_center_create_alerts.htm&type=5&language=en_US)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read-only.


-----

##### Fields

**Field**
```
MetricCount
MetricIdentifier
MetricsType
Name
NotificationDate
NotificationType

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The metric count that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the type of metric that was counted.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The metric for which the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the triggered notification rule.

**Type**
dateTime

**Properties**
Create, Filter, Sort, Update

**Description**
The date and time that the notification was sent.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

```
Operator
RecipientEmails
RuleName
Tenant
TenantName
Threshold

```

**Description**
The type of notification sent. For example, a Chatter feed or push notification.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The quantity of metrics used to measure.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The email addresses of the recipients who receive security notifications.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the notification rule.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the tenant for which the notification was triggered.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The org name of the tenant for which the notification was triggered.

**Type**
int

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update


-----

```
TriggerType

##### Associated Objects

```

**Description**
The threshold value that triggered the notification.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger that set off the notification. For example, a security change was made.


This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityNotificationFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityNotificationHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityNotificationOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityNotificationShare on page 66**
Sharing is available for the object.
