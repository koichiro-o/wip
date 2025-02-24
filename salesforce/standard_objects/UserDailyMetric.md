#### UserDailyMetric

```


**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

ID of the UserCustomBadge.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**

The translated text for the UserCustomBadge. Label is Translation Text.


Represents the daily engagement metrics for a user. This object is available in API version 52.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Sales Engagement must be enabled.

##### Fields

```
AllCallsCallBackLater

```

**Type**
int


-----

```
AllCallsLeftVoicemail
AllCallsMeaningfulConnect
AllCallsNotInterested
AllCallsUncategorized
AllCallsUnqualified
AllEmailsBouncedCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this user with the call result Unqualified.

**Type**
int


-----

```
AllEmailsDeliveredCount
AllEmailsHardBouncedCount
AllEmailsNotDeliveredCount
AllEmailsOutOfOfficeCount
AllEmailsSentCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this user in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this user in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount
AllEmailsUntrackedSentCount
AllTotalCallsCount
DailyCutOffTimeStamp

```

**Description**
The number of emails sent by this user in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this user in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls by this user with all call results in the day.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.


-----

```
Date
DateInt
HardBounceTrackableSends
LinkClickTrackableSends
OpenTrackableSends
OutOfOfficeTrackableSends

```

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The date on which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The date on which the engagement occurred, in yyyymmdd format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 53.0 and later.


-----

```
RecipientReplies
RecipientSends
ReplyTrackableRecipientSends
ReplyTrackableSends
SoftBounceTrackableSends
SomeEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who responded to an email. Available in API version 53.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who were sent an email. Available in API version 53.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with reply tracking. Available in API version
53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
SomeEmailsDeliveredRate
TrackableRecipientSendReplyRt
TrackableSendHardBounceRate
TrackableSendLinkClickRate

```

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This is a calculated field.


-----

```
TrackableSendOpenRate
TrackableSendOutOfOfficeRate
TrackableSendReplyRate
TrackableSendSoftBounceRate
UniqueEmailsLinkClickedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
UniqueEmailsOpenedCount
UniqueEmailsRepliedCount
UserId

##### Associated Objects

```

**Description**
The number of unique recipients who clicked a link in an email sent by the user on the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by the user on the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by the user on the day.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserDailyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserDailyMetricShare on page 66**
Sharing is available for the object.


-----
