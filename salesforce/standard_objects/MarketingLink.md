#### MarketingLink

Represents an Account Engagement marketing link record, either a custom redirect or a file, that has been synced to Salesforce. This
object is available in API version 42.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

```

-----

##### Special Access Rules

To access this object, your org must use Account Engagement and users need the CRM User or Sales User permission set.

##### Fields

```
CampaignId
LastReferencedDate
LastViewedDate
Name
TargetUrl

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID of the related campaign.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The timestamp that indicates when the current user last viewed a record that is
related to this marketing link.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

The date and time when the current user last viewed this record. If this value is
null, this record might only have been referenced (see
```
  LastReferencedDate) and not viewed.

```
**Type**
string

**Properties**
Filter, Group, Sort

**Description**

The name of the marketing link.

**Type**
url

**Properties**
Filter, Group, Sort


-----

```
TotalTrackedLinkClicks
Type
UniqueTrackedLinkClicks

##### Associated Objects

```

**Description**

The target URL of the marketing link.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The total number of clicks for the redirect. Includes clicks from visitors and
identified prospects. When a person clicks the link multiple times, each click is
counted in this number.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**

Specifies the type of marketing link record, either a custom redirect or file.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**

The number of unique clicks for the redirect. Includes clicks from visitors and
identified prospects. Only the first click is counted in this number.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MarketingFormEvent (API version 44.0)**
Change events are available for the object.

**MarketingLinkFeed**

Feed tracking is available for the object.
