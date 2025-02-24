#### OpportunityContactRoleSuggestionInsight

Represents a suggestion for a new opportunity contact role. Available in API versions 45.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getDeleted(), query(), retrieve()

 Special Access Rules

```
To add or decline opportunity contact role suggestions, users need a Sales Cloud Einstein license, edit access on opportunities, and read
or edit access on contacts. As of the Spring ’20 release, Pardot and Sales Engagement users no longer have access to this object.

##### Fields

```
ContactId
CreatedRecordId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related contact record.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created opportunity contact role record.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Division
LastOperationUserId
LastReferencedDate
LastViewedDate
OpportunityId

```

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the suggested opportunity contact role.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who last performed a related operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record indirectly, for
example, through a list view or related record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, it’s possible that the user only accessed this record or list view
(LastReferencedDate), but not viewed it.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related opportunity.


-----

```
RationaleLabel
Role
Status

##### Usage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this is a suggested opportunity contact role.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of the suggested opportunity contact role.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the suggested contact. Possible values include:

**•** New

**•** Pending

**•** Added

**•** Declined


This object is read-only and isn’t supported in workflows, triggers, or process builder.
