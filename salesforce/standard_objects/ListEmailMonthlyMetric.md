#### ListEmailMonthlyMetric

Represents the monthly engagement metrics for a single list email. This object is available in API version 49.0 and later.

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

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard and soft bounces that were triggered for this list email in the month.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who successfully received this list email in the month.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total hard bounces that were triggered for this list email in the month.


-----

```
AllEmailsLinkClickedCount
AllEmailsOpenedCount
AllEmailsOutOfOfficeCount
AllEmailsRepliedCount
AllEmailsSentCount
AllEmailsSoftBouncedCount

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of link clicks by the recipients of this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who opened this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of out-of-office replies that were triggered for this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of replies to this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients to whom this list email was sent in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The total soft bounces that were triggered for this list email in the month.


-----

```
HardBounceTrackableSends
LinkClickTrackableSends
ListEmailId
Month
MonthInt

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with hard bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with link click tracking in the month.
Available in API version 53.0 and later.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related list email.

This field is a relationship field.

**Relationship Name**
ListEmail

**Relationship Type**
Lookup

**Refers To**
ListEmail

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


-----

```
OpenTrackableSends
OutOfOfficeTrackableSends
ReplyTrackableSends
SoftBounceTrackableSends
TrackableSendHardBounceRate

```

**Description**
The month in which the engagement occurred, in yyyymm format.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with open tracking in the month.
Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with out-of-office tracking in the
month. Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with reply tracking in the month.
Available in API version 53.0 and later.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of recipients who were sent this list email with soft bounce tracking in the
month. Available in API version 53.0 and later.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with hard bounce tracking, resulted
in a hard bounce in the month. Available in API version 54.0 and later.


-----

```
TrackableSendLinkClickRate
TrackableSendOpenRate
TrackableSendOutOfOfficeRate
TrackableSendReplyRate
TrackableSendSoftBounceRate

```

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who clicked on a link in this list email that was sent with link
click tracking in the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients who opened this list email that was sent with open tracking in
the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom the list email, sent with out-of-office tracking, resulted
in an out-of-office reply in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with reply tracking, resulted in a
reply in the month. Available in API version 53.0 and later.

This field is a calculated field.

**Type**
percent


-----

```
UniqueEmailsLinkClickedCount
UniqueEmailsOpenedCount
UniqueEmailsRepliedCount

```

**Properties**
Filter, Nillable, Sort

**Description**
The percentage of recipients for whom this list email, sent with soft bounce tracking, resulted
in a soft bounce in the month. Available in API version 54.0 and later.

This field is a calculated field.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who clicked a link in this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who opened this list email in the month.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of unique recipients who replied to this list email in the month.

