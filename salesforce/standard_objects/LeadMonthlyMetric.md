#### LeadMonthlyMetric

Represents the monthly engagement metrics for a lead. This object is available in API version 52.0 and later.

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
The number of calls in the month for this lead with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Not Interested.


-----

```
AllCallsUncategorized
AllCallsUnqualified
AllEmailsBouncedCount
AllEmailsDeliveredCount
AllEmailsDeliveredRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this lead with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this lead in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this lead in the month.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this lead. This field
is a calculated field.

This is a calculated field.

Available in API version 54.0 and later.


-----

```
AllEmailsHardBouncedCount
AllEmailsOutOfOfficeCount
AllEmailsSentCount
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount
AllEmailsUntrackedSentCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
AllTotalCallsCount
HardBounceTrackableSends
LeadId
LinkClickTrackableSends

```

**Description**
The number of emails sent to this lead without engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this lead with all call results in the month.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with hard bounce tracking.

Available in API version 54.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related lead.

This is a relationship field.

**Relationship Name**
Lead

**Relationship Type**
Lookup

**Refers To**
Lead

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with link click tracking.

Available in API version 54.0 and later.


-----

```
Month
MonthInt
OpenTrackableSends
OutOfOfficeTrackableSends
ReplyTrackableSends
SoftBounceTrackableSends

```

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

**Description**
The number of emails sent to this lead with open tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with out-of-office tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with reply tracking.

Available in API version 54.0 and later.

**Type**
int


-----

```
TrackableSendHardBounceRate
TrackableSendLinkClickRate
TrackableSendOpenRate
TrackableSendOutOfOfficeRate

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this lead with soft bounce tracking.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with link tracking that had link clicks. This field is
a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with open tracking that were opened by the
recipient. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.


-----

```
TrackableSendReplyRate
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
The percentage of emails sent to this lead with reply tracking that received replies. This field
is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this lead with soft bounce tracking that soft bounced. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails in which the lead clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the lead in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the lead in the month.


-----
