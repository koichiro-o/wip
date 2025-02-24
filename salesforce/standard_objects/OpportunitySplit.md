#### OpportunitySplit

OpportunitySplit credits one or more opportunity team members with a portion of the opportunity amount. This object is available in
API version 16.0 and later for pilot customers, and version 28.0 and later for others.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
ArchivedTerritoryName
HasOpportunityLineItemSplit

```

**Type**
String

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the associated territory that’s on an archived territory model. If the
OpportunityLineItemSplit isn’t associated with a territory on an archived territory
model, the field value is null. This field is available in API version 62.0 and later.

**Type**
boolean


-----

```
OpportunityId
Split
SplitAmount
SplitNote

```

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only. Indicates whether the opportunity split has a split on the opportunity
line item level (true) or not (false).

The default value is `false. This field is available in API version 58.0 and later.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the opportunity for which the split is being created.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Read-only. Automatically generated number identifying the split within the
opportunity.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Monetary amount of the split.

Label is `Split Amount.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SplitOwnerId
SplitPercentage
SplitTypeId

```

**Description**
Enter any notes or comments about the split. The character limit is 255.

Label is `Split Note.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The opportunity owner.

This field is a relationship field.

**Relationship Name**
SplitOwner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
percent

**Properties**
Create, Filter, Sort, Update

**Description**
Split percentage that this team member receives. If the split type is validated to
a 100% total, this number can range from 0 to 100. If the total isn’t validated, this
number can range from 0 to 1,000.

Label is `Split (%).`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Auto-generated, numeric ID for the split type defined by the OpportunitySplitType
object. This field is available in API version 28 and later.

If this field is blank, the system automatically specifies the default split type for
the opportunity amount, which is validated to 100%.

This field is a relationship field.

**Relationship Name**
SplitType


-----

```
Territory2Id

##### Usage

```

**Relationship Type**
Lookup

**Refers To**
OpportunitySplitType

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the associated territory. This field is a relationship field, and is available in
API version 62.0 and later.

**Relationship Name**
Territory2

**Relationship Type**
Lookup

**Refers To**
Territory2


Use the OpportunitySplit object to manage splits for an opportunity.

If you change the opportunity owner using the API, the old owner remains on the opportunity team with either Read-only access, or
the level of access specified in your organization-wide defaults.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**OpportunitySplitChangeEvent (API version 48.0)**
Change events are available for the object.

**OpportunitySplitHistory on page 62 (API version 59.0)**
History is available for tracked fields of the object.
