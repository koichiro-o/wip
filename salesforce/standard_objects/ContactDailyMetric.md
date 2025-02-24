#### ContactDailyMetric

Represents the daily engagement metrics for a contact. This object is available in API version 52.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

Sales Engagement must be enabled.

##### Fields

**Field**
```
AllCallsCallBackLater
AllCallsLeftVoicemail
AllCallsMeaningfulConnect
AllCallsNotInterested
AllCallsUncategorized

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Call Back Later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Left Voicemail.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Meaningful Connect.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Not Interested.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with no call result specified.


-----

```
AllCallsUnqualified
AllEmailsBouncedCount
AllEmailsDeliveredCount
AllEmailsDeliveredRate
AllEmailsHardBouncedCount
AllEmailsOutOfOfficeCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of calls in the day for this contact with the call result Unqualified.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total of hard and soft bounced emails for this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of successfully delivered emails for this contact in the day.

This is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of tracked emails sent that were successfully delivered to this contact. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of hard bounced emails for this contact in the day.

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
The number of emails that triggered an out of office reply for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact in the day.

This is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails soft bounced for this contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact without engagement tracking enabled in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total number of calls to this contact with all call results in the day.

This is a calculated field.


-----

```
ContactId
DailyCutOffTimeStamp
Date
DateInt
HardBounceTrackableSends

```

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

**Refers To**
Contact

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The time of day when each 24-hour metrics period starts and ends.

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
The number of emails sent to this contact with hard bounce tracking.


-----

```
InboundEngagementsCount
LinkClickTrackableSends
OpenTrackableSends
OutOfOfficeTrackableSends
OutboundEngagementsCount

```

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of inbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `UniqueEmailsOpenedCount,`
```
  UniqueEmailsRepliedCount, and UniqueEmailsLinkClickedCount.

```
Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with link click tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with open tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with out-of-office tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort


-----

```
ReplyTrackableSends
SoftBounceTrackableSends
TrackableSendHardBounceRate
TrackableSendLinkClickRate

```

**Description**
The number of outbound engagements for this contact in the day. This field is a calculated
field. The value is the sum of `AllTotalCallsCount` and
```
  AllEmailsDeliveredCount.

```
Available in API version 58.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with reply tracking.

Available in API version 54.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of emails sent to this contact with soft bounce tracking.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with hard bounce tracking that hard bounced.
This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with link tracking that had link clicks. This field
is a calculated field.

Available in API version 54.0 and later.


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
recipient. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with out-of-office tracking that received
out-of-office replies. This field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with reply tracking that received replies. This
field is a calculated field.

Available in API version 54.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of emails sent to this contact with soft bounce tracking that soft bounced.
This field is a calculated field.

Available in API version 54.0 and later.

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
The number of individual emails in which the contact clicked a link in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails opened by the contact in the day.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of individual emails replied to by the contact in the day.

