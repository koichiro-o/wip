#### ActivityMetric

Represents activities that were added to Salesforce automatically by Einstein Activity Capture and manually by users.

This object is available in API version 45.0.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Unless otherwise noted, Einstein Activity Capture and Activity Metrics must be enabled.

##### Fields

```
BaseId

```

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, idLookup, Sort


-----

```
BaseType
FirstCallDateTime
FirstEmailDateTime
InactiveDays
LastActivityDateLastModDate

```

**Description**
The ID of the record that the activities apply to.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The entity that corresponds to the BaseId

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the first call was made. This field is available only to Sales Engagement
users. Einstein Activity Capture and Activity Metrics aren’t required.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the first email was sent. This field is available only to Sales
Engagement users. Einstein Activity Capture and Activity Metrics aren’t required.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Indicates the number of days since the most recent activity was completed. This field is
derived from the Last Activity Date field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastActivityDateTime field was last modified.


-----

```
LastActivityDateTime
LastCallDateLastModDate
LastCallDateTime
LastEmailDateLastModDate
LastEmailDateTime
LastEmailReceivedDateTime

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent activity was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastCallDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent call was made through Sales Dialer or Inbox.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastEmailDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent or received.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was received.


-----

```
LastEmailSentDateTime
LastEventDateLastModDate
LastEventDateTime
LastTaskDateLastModDate
LastTaskDateTime
NextActivityDateLastModDate

```

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent email was sent.

Available in API version 54.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastEventDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the most recent event was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Indicates when the LastTaskDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date when the last task was completed.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
NextActivityDateTime

##### Usage

```

**Description**
Indicates when the NextActivityDateTime field was last modified.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Indicates the date of the next scheduled task or event. Only open tasks in the future are
included.


Use this object to see data about sales activities that were added to Salesforce manually and by Einstein Activity Capture. Activity Metric
fields are derived from your activity data. For example, the Inactive Days field indicates the number of days since the most recent activity
was completed. Create a trigger that notifies a user when there isn’t any activity on an account for a certain amount of time.
