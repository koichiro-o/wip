#### TenantSecurityNotificationRule

Stores an alert configured in the Security Center Alerts feature to notify recipients of changes made to security settings. For more
[information, see Create Alerts for Security Changes. This object is available to Security Center subscribers in API version 53.0 and later.](https://help.salesforce.com/s/articleView?id=sf.security_center_create_alerts.htm&type=5&language=en_US)

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is read/write.


-----

##### Fields

**Field**
```
MetricsType
Name
NotificationRuleIdentifier
NotificationType
Operator
RecipientEmails

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of data being collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the metric for which data is being collected.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The ID of the alert that was triggered. This field is unique within your organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The type of notification used for the alert. The options are:

**•** `Email`

**•** `In-App`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The operator for the change that triggered the alert. For example, greater than.

**Type**
textarea


-----

```
RuleName
Status
Threshold
TriggerType
Version

```

**Properties**
Create, Nillable, Update

**Description**
The email addresses for the recipients of the alert details.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the custom alert that triggered the notification. This field is unique within your
organization.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The status of the alert setting. The options are:

**•** `Active`

**•** `Draft`

**•** `Inactive`

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The threshold value that triggered the alert.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of trigger used for the alert. The values are:

**•** `Always`

**•** `On Change`

**Type**
int


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The version number of the custom alert.

##### Associated Objects

This object has these associated objects. If the API version isn’t specified, it’s available in the same API versions as this object. Otherwise,
it’s available in the specified API version and later.

**TenantSecurityNotificationRuleChangeEvent on page 67**
Change events are available for the object.

**TenantSecurityNotificationRuleFeed on page 54**
Feed tracking is available for the object.

**TenantSecurityNotificationRuleHistory on page 62**
History is available for tracked fields of the object.

**TenantSecurityNotificationRuleOwnerSharingRule on page 64**
Sharing rules are available for the object.

**TenantSecurityNotificationRuleShare on page 66**
Sharing is available for the object.
