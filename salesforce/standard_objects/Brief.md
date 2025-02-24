#### Brief

Represents a marketing brief. A brief contains information that’s used for positioning and grounding a marketing campaign. This object
is available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
CurrencyIsoCode
Description
KeyMessage
LastReferencedDate
LastViewedDate

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency type for the brief.

Possible values are:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the brief.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The main idea or message that you want to deliver to your customers through the campaign
that’s associated with the brief.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last referenced by a campaign.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the brief was last viewed.


-----

```
Name
TargetAudience

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the brief.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A description of the characteristics of the audience that you want to reach through the
campaign that’s associated with this brief.

