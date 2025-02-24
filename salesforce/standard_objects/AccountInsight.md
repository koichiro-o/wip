#### AccountInsight

Represents an individual insight (a key business development) related to an account record.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To see an insight related to a specific account, users need a Sales Cloud Einstein license and access to the account record. As of the
Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

##### Fields

```
AccountId
ActualHeardWithinDays
CompetitorName
ContactName

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the related account record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field has been deprecated as of API version 45.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
ContactTitle
CurrencyIsoCode
Division
ExpectedHeardWithinDays
LastHeard
LastReferencedDate

```

**Description**
This field is not in use as of API version 46.0.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is not in use as of API version 46.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the related record.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Reserved for future use.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Reserved for future use.

**Type**
dateTime


-----

```
LastViewedDate
NumberOfNewsArticles
Rationale
Title
TrendType

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of news articles related to insights of type M&A activity
```
  detected, Company is expanding, and Leadership changes.

```
**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The explanation for an insight, providing more background information and
details that are specific to the org.

**Type**
string

**Properties**
Filter, Group, Nillable

**Description**
The title of the insight.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort


-----

```
Type

##### Usage

```

**Description**
The trend type of the insight. Possible values include:

**•** Negative

**•** Positive

**•** Informational

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of insight. Possible values include:

**•** M&A activity detected

**•** Company is expanding

**•** Leadership changes


This object is read-only and isn’t supported with workflows, triggers, or process builder.
