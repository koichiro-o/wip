#### ActiveFeatureLicenseMetric

Represents the number of active, assigned, and purchased feature licenses in the org. This object is available in API version 52.0 and
later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ActiveUserCount
AssignedUserCount
FeatureType

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license who have logged in within the last 30 days.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number of users assigned this feature license.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of feature license.

Possible values are:

**•** `AvantgoUser—AvantGo User`

**•** `ChatterAnswersUser—Chatter Answers User`


-----

```
MetricsDate
TotalLicenseCount

```


**•** `InteractionUser—Flow User`

**•** `JigsawProspectingUser—Data.com User`

**•** `KnowledgeUser—Knowledge User`

**•** `LiveAgentUser—Chat User`

**•** `MarketingUser—Marketing User`

**•** `MobileUser—Apex Mobile User`

**•** `OfflineUser—Offline User`

**•** `SFContentUser—Salesforce CRM Content User`

**•** `SiteforceContributorUser—Site.com Contributor User`

**•** `SiteforcePublisherUser—Site.com Publisher User`

**•** `SupportUser—Service Cloud User`

**•** `WirelessUser—Wireless User`

**•** `WorkDotComUserFeature—WDC User`

**Type**
date

**Properties**
Filter, Group, Sort

**Description**
Date that feature license metrics were collected.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of feature licenses in the organization.

