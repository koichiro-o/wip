#### CampaignMemberStatus

One or more member status values defined for a campaign.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.


-----

You can't delete a CampaignMemberStatus if that status is designated as the default status or if the status is currently used in a Campaign.

##### Fields

```
CampaignId
HasResponded
IsDefault
IsDeleted
Label

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the campaign associated with this member status.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is equivalent to “Responded” (true) or not (false). Beginning
with API version 39.0, at least one `CampaignMemberStatus` on each campaign must
have a `hasResponded` value of `true.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether this status is the default status (true) or not (false). Beginning with
API version 39.0, there must be a default CampaignMemberStatus defined for every campaign.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
string

**Properties**
Filter, Sort

**Description**
Label for the status in the picklist. Limited to 765 characters.


-----

```
 SortOrder

##### Usage

```

**Type**
int

**Properties**
Filter, Group, Sort, Update

**Description**
Unique number order where this campaign member status appears in the picklist.


Use this object to create picklist items for the member status in a campaign.

This object is defined only for those organizations that have the marketing feature and valid marketing licenses. In addition, the object
is accessible only to those users that are enabled as marketing users. If the organization does not have the marketing feature or valid
marketing licenses, this object does not appear in a `describeGlobal() call, and you can't use` `describeSObjects()` or
`query()` with the CampaignMember object.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**CampaignMemberStatusChangeEvent (API version 46.0)**
Change events are available for the object.

SEE ALSO:

Campaign

CampaignMember
