#### ActionCdncStpMonthlyMetric

Represents the monthly engagement metrics for an action cadence step. This object is available in API version 49.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Sales Engagement must be enabled.

##### Fields

```
ActionCadenceStepId
AllCallsCallBackLater
AllCallsLeftVoicemail

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related action cadence step.

This is a relationship field.

**Relationship Name**
ActionCadenceStep

**Relationship Type**
This is an overview-detail relationship field, where ActionCadenceStep is the master object.

**Refers To**
ActionCadenceStep

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Left Voicemail.


-----

```
AllCallsMeaningfulConnect
AllCallsNotInterested
AllCallsUncategorized
AllCallsUnqualified
AllEmailsBouncedCount
AllEmailsDeliveredCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this step with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AllEmailsHardBouncedCount
AllEmailsLinkClickedCount
AllEmailsNotDeliveredCount
AllEmailsOpenedCount
AllEmailsOutOfOfficeCount
AllEmailsRepliedCount

```

**Description**
The number of successfully delivered emails for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails containing a link clicked by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were bounced for all recipients on the email. Bounced emails
aren’t marked as delivered. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails opened by the recipient for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out-of-office reply for this step in the month.

**Type**
int


-----

```
AllEmailsSentCount
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount
AllEmailsUntrackedSentCount
AllTotalCallsCount

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails replied to for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with engagement tracking enabled for this step in the month.
Available in API version 51.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent without engagement tracking for this step in the month. Available
in API version 51.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
DeliveredRecipientCount
DeliveredRecipientRate
HardBounceTrackableSends
HasTemplateAssigned
HrdBncTrackableRecipientSends

```

**Description**
The total number of calls with all call results for this step in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that were successfully delivered an email. Available in API version
54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of unique recipients that received an email you sent. Available in API version
54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with hard bounce tracking. Available in API version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this step has an associated email template or call script. Available in API
version 52.0 and later.

The default value is 'false'.

**Type**
int


-----

```
IsCompoundMetric
LinkClickTrackableSends
LinkClkTrackableRecipientSends
Month

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with hard bounce tracking. Available in API
version 54.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
When true, indicates that this metric represents engagement for a combination of the action
cadence step and a single email template. The value is true for all action cadence steps
created in Summer ’21 and later.

When false, indicates that the metric represents engagement for the action cadence step
and all email templates used on the step. The value is false for all action cadence steps created
in Spring ’21 and earlier. The default value is 'false'.

Available in API version 52.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with link click tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with link tracking. Available in API version
54.0 and later.

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
The month in which the engagement occurred.


-----

```
MonthInt
OooTrackableRecipientSends
OpenTrackableRecipientSends
OpenTrackableSends
OutOfOfficeTrackableSends
RecipientReplies

```

**Type**
int

**Properties**
Filter, Group, idLookup, Sort

**Description**
The month in which the engagement occurred, in `yyyymm` format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with out-of-office tracking. Out-of-office
tracking requires Inbox. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with open tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with open tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with out-of-office tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
RecipientSends
RecipientsHardBounced
RecipientsOutOfOffice
RecipientsSoftBounced
ReplyTrackableRecipientSends

```

**Description**
The number of unique recipients who replied to an email. Available in API version 54.0 and
later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique email recipients. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that hard-bounced an email. Hard bounces can mean that the
recipient's email address doesn't exist or is misspelled. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that responded with an out-of-office reply. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients that soft-bounced an email. A soft bounce often indicates a
temporary issue with the recipient's email server, such as a full inbox. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ReplyTrackableSends
SftBncTrackableRecipientSends
SoftBounceTrackableSends
SomeEmailsDeliveredCount
SomeEmailsDeliveredRate

```

**Description**
The number of recipients who received an email with reply tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with reply tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who received an email with soft bounce tracking. Available in API
version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent with soft bounce tracking. Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of sent emails that were successfully delivered to at least one of its recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of sent and tracked emails that were successfully delivered to at least one
of their recipients. Available in API version 54.0 and later.


-----

```
TemplateId
TrackableRecipientSendHrdBncRt
TrackableRecipientSendOooRate
TrackableRecipientSendReplyRt

```

This field is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the email template or call script associated with this step. Available in API version
52.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
Template

**Relationship Type**
Lookup

**Refers To**
CallTemplate, EmailTemplate

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with hard bounce tracking that hard
bounced. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with out-of-office tracking that received out-of-office replies
from unique recipients. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort


-----

```
TrackableRecipientSendSftBncRt
TrackableSendHardBounceRate
TrackableSendLinkClickRate
TrackableSendOpenRate

```

**Description**
The percentage of emails sent with reply tracking that received replies from unique recipients.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to unique recipients with soft bounce tracking that
soft-bounced. Available in API version 54.0 and later.

This field is a calculated field.

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
54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent with open tracking that were opened by the recipient. Available
in API version 54.0 and later.

This field is a calculated field.


-----

```
TrackableSendOutOfOfficeRate
TrackableSendReplyRate
TrackableSendSoftBounceRate
UniqueEmailsLinkClickedCount
UniqueEmailsOpenedCount

```

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

**Description**
The percentage of emails sent with reply tracking that received replies. Available in API
version 54.0 and later.

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
The number of unique recipients who clicked a link in an email for this step in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened an email for this step in the month.


-----

```
UniqueEmailsRepliedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to an email for this step in the month.

