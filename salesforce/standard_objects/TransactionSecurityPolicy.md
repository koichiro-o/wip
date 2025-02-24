#### TransactionSecurityPolicy

Represents a transaction security policy definition.

This object is available in API version 42.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ActionConfig

```

**Type**
textarea

**Properties**
Create, Update


-----

```
ApexPolicyId
BlockMessage
CustomEmailContent

```

**Description**
Describes the action to take when the matching Transaction Security policy is triggered. Also
indicates the type of notifications selected and the ID of the intended recipient. The recipient
must be active and assigned the Modify All Data and View Setup user permissions. Multiple
actions can be taken. The actions available depend on the `Event Type` field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the Apex `TxnSecurity.PolicyCondition` or
```
  TxnSecurity.EventCondition interface for this policy.

```
**Type**
string

**Properties**
Create,Filter, Nillable, Sort, Update

**Description**
The custom message sent to a user when a policy blocks their action. Used in Real-Time
Event Monitoring only. Maximum of 1000 characters. This field is null when the default
message option is selected in the UI. Available only when EventName is set to ApiEvent,
```
  ListViewEvent, BulkApiResultEventStore, or ReportEvent. Available

```
in API version 49.0 and later.

Include org- or policy-specific information in your custom message, such as the name of the
responsible administrator or the business unit. Be careful about what you include. Too much
information on how the policy was designed. can aid a malicious user.

Two-factor authentication (2FA) isn’t supported in Lightning Experience, so events like
`ListView` and `ReportEvent` are upgraded to Block in Lightning.

Custom messages aren’t translatable.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The administrator-created custom email content sent when a policy is triggered. Used in
Real-Time Event Monitoring only. Maximum of 1333 characters. This field is null when the
Custom Email Content setting is selected in the UI but no message content is entered. This
field is available in API version 54.0 and later.

Custom messages aren’t translatable.


-----

```
Description
DeveloperName
EventName

```

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description entered for this policy.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The API, or program name, for this policy.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Real-Time Event Monitoring only. Indicates the name of the event the policy monitors.
Valid values are:

**•** `ApiEvent—Tracks these user-initiated read-only API calls:` `query(),`
```
   queryMore(), and count(). Captures API requests through SOAP API and Bulk

```
API for the Enterprise and Partner WSDLs. Tooling API calls and API calls originating from
a Salesforce mobile app aren’t captured.

**•** `ApiAnomalyEventStore—Tracks anomalies in how users make API calls.`
ApiAnomalyEventStore is an object that stores the event data of ApiAnomalyEvent.
This object is available in API version 50.0 and later.

**•** `BulkApiResultEventStore—Tracks when a user downloads the results of a`
Bulk API request. `BulkApiResultEventStore` is a big object that stores the
event data of `BulkApiResultEvent. This object is available in API version 50.0`
and later.

**•** `CredentialStuffingEventStore—Tracks when a user successfully logs into`
Salesforce during an identified credential stuffing attack. Credential stuffing refers to
large-scale automated login requests using stolen user credentials.This value is available
in API 49.0 and later.

**•** `FileEventStore—Tracks when a user downloads, previews, or uploads a file.`
FileEventStore is a big object that stores the event data of FileEvent. This object is available
in API version 57.0 and later.


-----

```
EventType
ExecutionUserId

```


**•** `GuestUserAnomalyEventStore—Tracks data access anomalies that are caused`
by guest user permission misconfiguration. GuestUserAnomalyEventStore is an object
that stores the event data of GuestUserAnomalyEvent.This object is available in API
version 60.0 and later.

**•** `ListViewEvent—Tracks when users access data with list views using Lightning`
Experience, Salesforce Classic, or the API. It doesn’t track list views of Setup entities.

**•** `LoginEvent—LoginEvent tracks the login activity of users who log in to Salesforce.`

**•** `PermissionSetEventStore—Tracks changes to permission sets and permission`
set groups.

**•** `ReportAnomalyEventStore—Tracks anomalies in how users run or export`
reports, including unsaved reports. This value is available in API 49.0 and later.

**•** `ReportEvent—Tracks when reports are run in your org.`

**•** `SessionHijackingEventStore—Tracks when unauthorized users gain`
ownership of a Salesforce user’s session with a stolen session identifier. To detect such
an event, Salesforce evaluates how significantly a user’s current browser fingerprint
diverges from the previously known fingerprint using a probabilistically inferred
significance of change. This value is available in API 49.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Used in Legacy Transaction Security only. Indicates the type of event the policy monitors.
Valid values are:

**•** `AccessResource—Notifies you when the selected resource has been accessed.`

**•** `AuditTrail—Reserved for future use.`

**•** `DataExport—Notifies you when any API query is made, such as from the Data Loader`
API client, or when a Report export occurs.

**•** `Entity—Notifies you on use of an object type such as an authentication provider or`
chatter post.

**•** `Login—Notifies you when a user logs in.`

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. The ID of an active user who is assigned the Modify
All Data and View Setup user permissions. As of Summer '20, Legacy Transaction Security is
a retired feature in all Salesforce orgs.


-----

```
MasterLabel
NamespacePrefix
ResourceName
State

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The policy’s name.

Important: Where possible, we changed noninclusive terms to align with our
company value of Equality. We maintained certain terms to avoid any effect on
customer implementations.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
`namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Used in Legacy Transaction Security only. A resource used to narrow down the conditions
under which the policy triggers. For example, with a `DataExport event, you can select`
a resource Lead to specifically monitor export activity occurring on your Lead entities. The
resources available depend on the `EventType` field.

As of Summer '20, Legacy Transaction Security is a retired feature in all Salesforce orgs.

**Type**
picklist


-----

```
Type

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates whether the policy is active. Valid values are:

**•** `Disabled`

**•** `Enabled`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of validation that the policy uses. The valid values are:

**•** `CustomApexPolicy— Created with Apex editor.`

**•** `CustomConditionBuilderPolicy— Created with Condition Builder`

.

