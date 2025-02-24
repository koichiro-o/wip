#### UserMonthlyMetric

Represents the monthly engagement metrics for a user. This object is available in API version 52.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Sales Engagement must be enabled.

##### Fields

```
AllCallsCallBackLater
AllCallsLeftVoicemail
AllCallsMeaningfulConnect
AllCallsNotInterested

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Meaningful Connect.

**Type**
int


-----

```
AllCallsUncategorized
AllCallsUnqualified
AllEmailsBouncedCount
AllEmailsDeliveredCount
AllEmailsHardBouncedCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this user with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails sent by this user in the month.


-----

```
AllEmailsLinkClickedCount
AllEmailsNotDeliveredCount
AllEmailsOpenedCount
AllEmailsOutOfOfficeCount
AllEmailsRepliedCount
AllEmailsSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that were undelivered for all recipients on the email. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this user in the month.

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
DeliveredRecipientCount

```

**Description**
The number of emails sent by this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user that soft bounced in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent by this user without engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls with all call results for this user in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received an email. Available in API version 53.0
and later.

This is a calculated field.


-----

```
DeliveredRecipientRate
HardBounceTrackableSends
HrdBncTrackableRecipientSends
LinkClickTrackableSends
LinkClkTrackableRecipientSends
Month

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients who successfully received an email. Available in API
version 53.0 and later.

This is a calculated field.

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
The number of recipients who were sent an email with hard bounce tracking. Available in
API version 53.0 and later.

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
The number of recipients who were sent an email with link click tracking. Available in API
version 53.0 and later.

**Type**
date


-----

```
MonthInt
OooTrackableRecipientSends
OpenTrackableRecipientSends
OpenTrackableSends
OutOfOfficeTrackableSends

```

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with out-of-office tracking. Available in
API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email with open tracking. Available in API version
53.0 and later.

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
RecipientsHardBounced
RecipientsOutOfOffice
RecipientsSoftBounce
ReplyTrackableRecipientSends

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
The number of email recipients who were sent an email that hard bounced. Available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who responded with an out-of-office reply. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent an email that soft bounced. Available in API version
54.0 and later.

**Type**
int


-----

```
ReplyTrackableSends
SftBncTrackableRecipientSends
SoftBounceTrackableSends
SomeEmailsDeliveredCount
SomeEmailsDeliveredRate

```

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
The number of recipients who were sent an email with soft bounce tracking. Available in
API version 53.0 and later.

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

**Description**
The number of emails that were successfully delivered to at least one recipient on the email.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


-----

```
TrackableRecipientSendHrdBncRt
TrackableRecipientSendOooRate
TrackableRecipientSendReplyRt
TrackableRecipientSendSftBncRt

```

**Description**
The percentage of emails that were successfully delivered to at least one recipient on the
email. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients who hard bounced an email with hard bounce tracking.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that resulted in out-of-office replies
from unique recipients. This field is a calculated field. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that soft
bounced.

This field is a calculated field. Available in API version 54.0 and later.


-----

```
TrackableSendHardBounceRate
TrackableSendLinkClickRate
TrackableSendOpenRate
TrackableSendOutOfOfficeRate
TrackableSendReplyRate

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced. Available in
API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks. Available in API version
53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by a recipient. Available
in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


-----

```
TrackableSendSoftBounceRate
UniqueEmailsLinkClickedCount
UniqueEmailsOpenedCount
UniqueEmailsRepliedCount
UserId

```

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced. Available in API
version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who clicked a link in an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email sent by this user in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email sent by this user in the month.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related user.


-----

This is a relationship field.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**UserMonthlyMetricOwnerSharingRule**

Sharing rules are available for the object.

**UserMonthlyMetricShare on page 66**
Sharing is available for the object.
