#### ContactMonthlyMetric

Represents the monthly engagement metrics for a contact. This object is available in API version 52.0 and later.

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

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Call Back Later.


-----

```
AllCallsLeftVoicemail
AllCallsMeaningfulConnect
AllCallsNotInterested
AllCallsUncategorized
AllCallsUnqualified
AllEmailsBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with no call result specified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the month for this contact with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the month.


-----

```
AllEmailsDeliveredCount
AllEmailsDeliveredRate
AllEmailsHardBouncedCount
AllEmailsOutOfOfficeCount
AllEmailsSentCount

```

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this contact in the month.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails that triggered an out of office reply for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the month.

This is a calculated field.


-----

```
AllEmailsSoftBouncedCount
AllEmailsTrackedSentCount
AllEmailsUntrackedSentCount
AllTotalCallsCount
ContactId

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the
month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the month.

This is a calculated field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related contact.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup


-----

```
HardBounceTrackableSends
LinkClickTrackableSends
Month
MonthInt
OpenTrackableSends

```

**Refers To**
Contact

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with hard bounce tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking. Available in API version
54.0 and later.

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
The number of emails sent to this contact with open tracking. Available in API version 54.0
and later.


-----

```
OutOfOfficeTrackableSends
ReplyTrackableSends
SoftBounceTrackableSends
TrackableSendHardBounceRate
TrackableSendLinkClickRate

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking. Available in API version
54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking. Available in API version 54.0
and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with soft bounce tracking. Available in API version
54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. Available
in API version 54.0 and later.

This field is a calculated field.


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
The percentage of emails sent to this contact with open tracking that were opened by the
recipient. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with reply tracking that received replies.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
UniqueEmailsOpenedCount
UniqueEmailsRepliedCount

```

**Description**
The number of individual emails in which the contact clicked a link in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the contact in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the month.

