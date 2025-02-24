#### OpportunityRelatedDeleteLog

Represents an audit log of the deletion of opportunity-related child records, such as opportunity team members, product splits, or
opportunity splits. This object is available in API version 59.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Fields

**Field**
```
CurrencyIsoCode
DataType
DeleteLog

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Available only when the multicurrency feature is enabled. Contains the ISO code for any
currency allowed by the organization.

When multicurrency is enabled, and a Pricebook2 is specified on the parent opportunity
(that is, the Pricebook2Id field isn’t blank on the opportunity record referenced by this
object’s `OpportunityId), then the value must match the currency of the`
`CurrencyIsoCode` field on the PricebookEntry records that are associated with this
object.

Possible values are:

**•** `AED—UAE Dirham`

**•** `CAD—Canadian Dollar`

**•** `INR—Indian Rupee`

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Data type of the field that was deleted.

Possible values are:

**•** `Double`

**•** `DynamicEnum`

**•** `EntityId`

**•** `StaticEnum`

**•** `Text`

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
FieldName
OpportunityId
Parent

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The name of the field that was deleted.

Possible values are:

**•** `OpportunityLineItemSplit.SplitOwnerId`

**•** `OpportunityLineItemSplit.SplitPercentage`

**•** `OpportunityLineItemSplit.SplitTypeId`

**•** `OpportunitySplit.SplitOwnerId`

**•** `OpportunitySplit.SplitPercentage`

**•** `OpportunitySplit.SplitTypeId`

**•** `OpportunityTeamMember.TeamMemberRole`

**•** `OpportunityTeamMember.UserId`

**•** `Product2.Name`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. ID of the associated opportunity.

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
Filter, Group, Nillable, Sort

**Description**
ID of the record that was deleted. Records with the same Parent text indicate that the value
shown in the Value field came from the same record that was previously deleted. Refer to
the FieldName field to see which field is being tracked.


-----

```
SobjectType
Value
