#### EmailTemplateMonthlyMetric

Represents the monthly engagement metrics for an email template. This object is available in API version 53.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Sales Engagement must be enabled.

##### Fields

```
AllEmailsBouncedCount
AllEmailsDeliveredCount
AllEmailsHardBouncedCount
AllEmailsLinkClickedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this email template in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AllEmailsNotDeliveredCount
AllEmailsOpenedCount
AllEmailsOutOfOfficeCount
AllEmailsRepliedCount
AllEmailsSentCount

```

**Description**
The number of emails containing a link clicked by the recipient for this email template in
the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails not delivered for this email template in the month. This field is available
in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this email template in the month.

This is a calculated field.


-----

```
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount
AllEmailsUntrackedSentCount
DeliveredRecipientCount
DeliveredRecipientRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this email template in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were successfully delivered an email for this email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. This field is available
in API version 54.0 and later.

This is a calculated field.


-----

```
EmailTemplateId
HardBounceTrackableSends
HrdBncTrackableRecipientSends
IsLocked
LinkClickTrackableSends

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related email template.

This is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. This field is available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. This field is
available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record is locked or not.

The default value is 'false'.

**Type**
int


-----

```
LinkClkTrackableRecipientSends
MayEdit
Month
MonthInt
OooTrackableRecipientSends

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking for the email template in the month. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking for the email template in
the month. This field is available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the monthly metric record can be edited or not.

The default value is 'false'.

**Type**
date

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


-----

```
OpenTrackableRecipientSends
OpenTrackableSends
OutOfOfficeTrackableSends
RecipientReplies
RecipientSends

```

**Description**
The number of recipients who received an email with out-of-office tracking for the email
template in the month. Out-of-office tracking requires Inbox. This field is available in API
version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email for this email template in the
month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
RecipientsHardBounced
RecipientsOutOfOffice
RecipientsSoftBounced
ReplyTrackableRecipientSends
ReplyTrackableSends

```

**Description**
The number of unique email recipients for this email template in the month. This field is
available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email for this email template in the month.
Hard bounces can mean that the recipient's email address doesn't exist or is misspelled. This
field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that responded with an out-of-office reply for the email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email for the email template in the month.
A soft bounce often indicates a temporary issue with the recipient's email server, such as a
full inbox. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with reply tracking for this email template
in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
SftBncTrackableRecipientSends
SoftBounceTrackableSends
SomeEmailsDeliveredCount
SomeEmailsDeliveredRate
TrackableRecipientSendHrdBncRt

```

**Description**
The number of emails sent with reply tracking for the email template in the month. This field
is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking for the email
template in the month. This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking for the email template in the month.
This field is available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients for the email template in the month. This field is available in API version
54.0 and later.

This is a calculated field.

**Type**
percent


-----

```
TrackableRecipientSendOooRate
TrackableRecipientSendReplyRt
TrackableRecipientSendSftBncRt
TrackableSendHardBounceRate

```

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced for the email template in the month. This field is available in API version 54.0 and
later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients for the email template in the month. This field is available in API
version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced for the email template in the month. This field is available in API version 54.0
and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


-----

```
TrackableSendLinkClickRate
TrackableSendOpenRate
TrackableSendOutOfOfficeRate
TrackableSendReplyRate

```

**Description**
The percentage of emails sent with hard bounce tracking that hard bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with link tracking that had link clicks for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by the recipient for the
email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
for the email template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with reply tracking that received replies for the email template
in the month. This field is available in API version 54.0 and later.

This is a calculated field.


-----

```
TrackableSendSoftBounceRate
UniqueEmailsLinkClickedCount
UniqueEmailsOpenedCount
UniqueEmailsRepliedCount

```

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with soft bounce tracking that soft bounced for the email
template in the month. This field is available in API version 54.0 and later.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by unique recipients for the email template in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an email you sent was opened by a unique recipient for the email
template in the month. When you send a list email, this field increments each time a recipient
opens the received email.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies from unique recipients for the email template in the month.

