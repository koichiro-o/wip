#### CommerceEntitlementPolicyShare

Represents the entitlement rule for sharing products and prices with users other than the owner. This object is available in API version
49.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.


-----

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
The CommerceEntitlementPolicyShare object is available only if the B2B Commerce license is enabled.

##### Fields

```
AccessLevel
ParentId
RowCause

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Possible values are:

**•** `All—Owner`

**•** `Edit—Read/Write`

**•** `Read—Read Only`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the parent entitlement policy.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

Possible values are:

**•** `CompliantCollaboration—Compliant Data Sharing`

**•** `GuestParentImplicit—Associated guest user sharing`

**•** `GuestPersonImplicit—Associated Guest User Sharing`

**•** `GuestRule—Guest User Sharing Rule`

**•** `ImplicitChild—Account Sharing`


-----

```
UserOrGroupId

```


**•** `ImplicitParent—Associated record owner or sharing`

**•** `ImplicitPerson—Person Contact`

**•** `Manual—Manual Sharing`

**•** `Owner`

**•** `Rule—Sharing Rule`

**•** `SurveyShare—Survey Sharing Rule`

**•** `Team—Sales Team`

**•** `Territory—Territory Assignment Rule`

**•** `Territory2AssociationManual—Territory Manual`

**•** `Territory2Forecast—Territory assignment for forecasting and reporting`

**•** `TerritoryManual—Territory Manual`

**•** `TerritoryRule—Territory Sharing Rule`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The unique ID of the associated user or buyer group.

