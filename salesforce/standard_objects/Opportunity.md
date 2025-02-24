#### Opportunity

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
(Read-Only) An auto-generated number identifying the operating hours holiday.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the operating hours that’s related to the holiday indicated in the HolidayId field.

This is a relationship field.

**Relationship Name**
OperatingHours

**Relationship Type**
Lookup

**Refers To**
OperatingHours


Represents an opportunity, which is a sale or pending deal.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
AccountId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the account associated with this opportunity.

This is a relationship field.


-----

```
ActivityMetricId
ActivityMetricRollupId
AgeInDays

```

**Relationship Name**
Account

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric.

This field is a relationship field.

**Relationship Name**
ActivityMetric

**Refers To**
ActivityMetric

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
When Einstein Activity Capture with Activity Metrics is enabled, the ID of the related activity
metric rollup.

This field is a relationship field.

**Relationship Name**
ActivityMetricRollup

**Refers To**
ActivityMetricRollup

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the opportunity was created, calculated by the current date minus
the created_date field. This field is available in API version 52.0 and later if you enabled
Pipeline Inspection.


-----

```
Amount
CampaignId
CloseDate
ConnectionReceivedId

```

**Type**
currency

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Estimated total sale amount. For opportunities with products, the amount is the sum of the
related products. Any attempt to update this field, if the record has products, will be ignored.
The update call will not be rejected, and other fields will be updated as specified, but the
Amount will be unchanged.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Campaign. This field is defined only for those organizations that have the
campaign feature Campaigns enabled. The User must have read access rights to the
cross-referenced Campaign object in order to create or update that campaign into this field
on the opportunity.

This is a relationship field.

**Relationship Name**
Campaign

**Relationship Type**
Lookup

**Refers To**
Campaign

**Type**
date

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Date when the opportunity is expected to close.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that shared this record with your organization. This
field is available if you enabled Salesforce to Salesforce.


-----

```
ConnectionSentId
ContactId
ContractId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the PartnerNetworkConnection that you shared this record with. This field is available
if you enabled Salesforce to Salesforce. This field is supported using API versions earlier than
15.0. In all other API versions, this field’s value is null. You can use the new
PartnerNetworkRecordConnection object to forward records to connections.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the contact associated with this opportunity, set as the primary contact. Read-only field
that is derived from the opportunity contact role, which is created at the same time the
opportunity is created. This field can only be populated when it’s created, and can’t be
updated. To update the value in this field, change the `IsPrimary` flag on the
OpportunityContactRole associated with this opportunity. Available in API version 46.0 and
later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the contract that’s associated with this opportunity.

This is a relationship field.

**Relationship Name**
Contract

**Relationship Type**
Lookup

**Refers To**
Contract

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
Description
ExpectedRevenue
ExportStatus
Fiscal

```

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

If the organization has multicurrency and a Pricebook2 is specified on the opportunity (that
is, the Pricebook2Id field is not blank), then the currency value of this field must match
the currency of the PricebookEntry records that are associated with any opportunity line
items it has.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Text description of the opportunity. Limit: 32,000 characters.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field that is equal to the product of the opportunity `Amount` field and the
```
  Probability. You can’t directly set this field, but you can indirectly set it by setting the

```
`Amount` or `Probability` fields.

**Type**
picklist

**Properties**
Filter, Restricted picklist, Sort

**Description**
Derived field for the record map for Partner Connect. The export status of this opportunity
to the partner’s connected org. To see this field, enable Partner Connect and add the Export
Vendor Records to an Authorized Partner Org user permission to the cosell export user. See
[Set Up Partner Connect as a Vendor in Salesforce Help. Available in API version 62.0 and later.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
If fiscal years are not enabled, the name of the fiscal quarter or period in which the opportunity
`CloseDate` falls. Use YYY Q format, for example, '2006 1' for first quarter of 2006.


-----

```
FiscalQuarter
FiscalYear
ForecastCategory
ForecastCategoryName

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal quarter. Valid values are 1, 2, 3, or 4.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the fiscal year, for example, 2006.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Restricted picklist field. It is implied, but not directly controlled, by the `StageName` field.
You can override this field to a different value than is implied by the `StageName` value.
The values of this field are fixed enumerated values. The field labels are localized to the
language of the user performing the operation, if localized versions of those labels are
available for that language in the user interface.

In API version 12.0 and later, the value of this field is automatically set based on the value of
the ForecastCategoryName and can’t be updated any other way. The field properties
Create, Defaulted on create, Nillable, and Update are not available in version 12.0.

Possible values are:

**•** `BestCase`

**•** `Closed`

**•** `Forecast`

**•** `MostLikely`

**•** `Omitted`

**•** `Pipeline`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
HasOpenActivity
HasOpportunityLineItem
HasOverdueTask

```

**Description**
The name of the forecast category. It is implied, but not directly controlled, by the
`StageName` field. You can override this field to a different value than is implied by the
`StageName` value. Available in API version 12.0 and later.

Possible values are:

**•** `Best Case`

**•** `Closed`

**•** `Commit`

**•** `Most Likely`

**•** `Omitted`

**•** `Pipeline`

**Type**
boolean

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an open event or task (true) or not (false). Available
in API version 35.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether the opportunity has associated line items. A value of
`true` means that Opportunity line items have been created for the opportunity. An
opportunity can have opportunity line items only if the opportunity has a price book. The
opportunity line items must correspond to PricebookEntry objects that are listed in the
opportunity Pricebook2. However, you can insert opportunity line items on an opportunity
that does not have an associated Pricebook2. For the first opportunity line item that you
insert on an opportunity without a Pricebook2, the API automatically sets the
`Pricebook2Id` field, if the opportunity line item corresponds to a PricebookEntry in an
active Pricebook2 that has a `CurrencyIsoCode` field that matches the
`CurrencyIsoCode` field of the opportunity. If the Pricebook2 is not active or the
`CurrencyIsoCode` fields do not match, then the API returns an error. You can’t update
the `Pricebook2Id` or `PricebookId` fields if opportunity line items exist on the
Opportunity. You must delete the line items before attempting to update the
`PricebookId` field.

**Type**
boolean


-----

```
IqScore
IsClosed
IsDeleted
IsExcludedFromTerritory2Filter

```

**Properties**
Defaulted on create, Group,

**Description**
Indicates whether an opportunity has an overdue task (true) or not (false). Available in
API version 35.0 and later.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The likelihood, measured on a scale of 1 to 99, that an opportunity will be won. Einstein
Opportunity Scoring must be enabled. Available in API version 41.0 and later. Label is
**Opportunity Score.**

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Directly controlled by `StageName. You can query and filter on this field, but you can’t`
directly set it in a create, upsert, or update request. It can only be set via StageName. Label
is Closed.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Used for Filter-Based Opportunity Territory Assignment (Pilot in Spring ’15 / API version 33).
Indicates whether the opportunity is excluded (True) or included (False) each time the
APEX filter is executed.


-----

```
IsPriorityRecord
IsSplit
IsWon
LastActivityDate
LastActivityInDays

```

**Type**
boolean

**Properties**
Defaulted on create, Group

**Description**
Shows whether the user has marked the opportunity as important (True) or not (False).
The default value is `false. Available in API version 53.0 and later.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Read-only field that indicates whether credit for the opportunity is split between opportunity
team members. Label is `IsSplit. This field is available in versions 14.0 and later for`
organizations that enabled Opportunity Splits during the pilot period.

Warning: This field should not be used. However, it’s documented for the benefit
of pilot customers who find references to `IsSplit` in code.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Directly controlled by `StageName. You can query and filter on this field, but you can’t`
directly set the value. It can only be set via `StageName. Label is Won.`

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
Value is one of the following, whichever is the most recent:

**•** Due date of the most recent event logged against the record.

**•** Due date of the most recently closed task associated with the record.

**Type**
int

**Properties**
Aggregate, Filter, Group, Nillable, Sort


-----

```
LastAmountChangedHistoryId
LastCloseDateChangedHistoryId
LastReferencedDate

```

**Description**
The number of days since the last completed event or task for the record, calculated by the
current date minus the `last_activity` field. If the `last_activity` field is null,
this field is null. This field is available in API version 52.0 and later if you enabled Pipeline
Inspection.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Amount field was last updated in Winter ’21 or later. Information includes the date and time
of the change and the user who made the change. Available in API version 50.0 and later.

This is a relationship field.

**Relationship Name**
LastAmountChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the OpportunityHistory record that contains information about when the opportunity
Close Date field was last updated in Winter ’21 or later. Information includes the date and
time of the change and the user who made the change. Available in API version 50.0 and
later.

This is a relationship field.

**Relationship Name**
LastCloseDateChangedHistory

**Relationship Type**
Lookup

**Refers To**
OpportunityHistory

**Type**
datetime


-----

```
LastStageChangeDate
LastStageChangeInDays
LastViewedDate
LeadSource

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
datetime

**Properties**
Aggregate, Filter, Nillable, Sort

**Description**
The date of the last change made to the `Stage` field on this opportunity record. This field
is available in API version 52.0 and later.

**Type**

**int**

**Properties**
Aggregate, Filter, Group, Nillable, Sort

**Description**
The number of days since the last change was made to the Stage field on the opportunity
record, calculated by the current date minus the `last_stage_change_date` field. If
the `last_stage_change_date` is null, then this field contains the value for
```
  AgeInDays. This field is available in API version 52.0 and later if you enabled Pipeline

```
Inspection.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Source of this opportunity, such as Advertisement or Trade Show.


-----

```
Name
NextStep
OwnerId
PartnerAccountId

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. A name for this opportunity. Limit: 120 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of next task in closing opportunity. Limit: 255 characters.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the User who has been assigned to work this opportunity.

If you update this field, the previous owner's access becomes Read Only or the access specified
in your organization-wide default for opportunities, whichever is greater.

If you have set up opportunity teams in your organization, updating this field has different
consequences depending on your version of the API:

**•** For API version 12.0 and later, sharing records are kept, as they are for all objects. (All
previous opportunity team members are kept on the opportunity team.)

**•** For API version before 12.0, sharing records are deleted. (All previous opportunity team
members are removed from the opportunity team.)

**•** For API version 16.0 and later, users must have the “Transfer Record” permission in order
to update (transfer) account ownership using this field.

This is a relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference


-----

```
Pricebook2Id
PricebookId
Probability

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the partner account for the partner user that owns this opportunity. Available if Partner
Relationship Management is enabled or if digital experiences is enabled and you have partner
portal licenses.

Note: If you are uploading opportunities using API version 15.0 or earlier, and one
of the opportunities in the batch has a partner user as the owner, the `Partner`

`Account` field on all opportunities in the batch is set to that partner user’s account
regardless of whether the partner user is the owner. In version 16.0, the `Partner`
`Account` field is set to the appropriate account for the partner user that owns the
opportunity. If the owner of the opportunity is not a partner user, this field remains
empty.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
ID of a related Pricebook2 object. The `Pricebook2Id` field indicates which Pricebook2
applies to this opportunity. The Pricebook2Id field is defined only for those organizations
that have products enabled as a feature. You can specify values for only one field
(Pricebook2Id or `PricebookId)—not both fields. For this reason, both fields are`
declared nillable.

This is a relationship field.

**Relationship Name**
Pricebook2

**Relationship Type**
Lookup

**Refers To**
Pricebook2

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Nillable, Update

**Description**
Unavailable as of version 3.0. As of version 8.0, the Pricebook object is no longer available.
Use the `Pricebook2Id` field instead, specifying the ID of the Pricebook2 record.

**Type**
percent


-----

```
PushCount
RecordTypeId
StageName

```

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Percentage of estimated confidence in closing the opportunity. It is implied, but not directly
controlled, by the `StageName` field. You can override this field to a different value than
what is implied by the `StageName.`

Note: If you're changing the Probability field through the API using a partner
WSDL call, or an Apex `before` trigger, and the value may have several decimal
places, we recommend rounding the value to a whole number. For example, the
following Apex in a `before` trigger uses the `round` method to change the field
value: `o.probability = o.probability.round();`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of times an opportunity’s close date has been pushed out by one calendar
month. For example, moving a close date from April to May counts as one push, but moving
from April 1 to April 30 doesn't count. The total is not decreased when the close date is
moved in. Available in API version 53.0 and later.

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
ID of the record type assigned to this object.

**Type**
picklist

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Current stage of this record. The `StageName` field controls several other fields
on an opportunity. Each of the fields can be directly set or implied by changing the
`StageName` field. In addition, the `StageName` field is a picklist, so it has additional
members in the returned describeSObjectResult to indicate how it affects the other fields.
To obtain the stage name values in the picklist, query the OpportunityStage object. If the
`StageName` is updated, then the ForecastCategoryName, IsClosed, IsWon,
and `Probability` are automatically updated based on the stage-category mapping.


-----

```
SyncedQuoteID
Territory2Id
TotalOpportunityQuantity
Type

```

**Type**
reference

**Properties**
Create, Filter, Nillable, Update

**Description**
Read only in an Apex trigger. The ID of the Quote that syncs with the opportunity. Setting
this field lets you start and stop syncing between the opportunity and a quote. The ID has
to be for a quote that is a child of the opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the territory that is assigned to the opportunity. Available only if Enterprise Territory
Management has been enabled for your organization.

Note: Users who have full access to an opportunity’s account can assign any territory
from the active model to the opportunity. Users who do not can assign only a territory
that is also assigned to the opportunity’s account. The same restriction applies to
territory assignments made via Apex in system mode.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Number of items included in this opportunity. Used in quantity-based forecasting.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of opportunity. For example, Existing Business or New Business. Label is Opportunity
**Type.**


Note: If you are importing Opportunity data and need to set the value for an audit field, such as `CreatedDate, contact`
Salesforce. Audit fields are automatically updated during API operations unless you request to set these fields yourself..


-----

##### Usage

Use the Opportunity object to manage information about a sale or pending deal. You can also sync this object with a child Quote. To
update an Opportunity, your client application needs “Edit” permission on opportunities. You can create, update, delete, and query
Attachment records associated with an opportunity via the API. To split credit for an opportunity among multiple opportunity team
members, use the OpportunitySplit object.

Client applications can also create or update opportunity objects by converting a Lead with `convertLead().`

Note: On opportunities and opportunity products, the workflow rules, validation rules, and Apex triggers fire when an update to
a child opportunity product or schedule causes an update to the parent record. This means your custom application logic is
enforced when there are updates to the parent record, ensuring higher data quality and compliance with your organization’s
business policies.

##### Sample Code—Java

This code starts the sync between an object and a child quote.
```
public void startQuoteSync() {
      Opportunity opp = new Opportunity();
      opp.setId(new ID("006D000000CpOSy"));
      opp.setSyncedQuoteId(new ID("0Q0D000000002OZ"));
  // Invoke the update call and save the results
  try {
    SaveResult[] saveResults = binding.update(new SObject[] {opp});
    // check results and do more processing after the update call ...
  }
  catch (Exception ex) {
    System.out.println("An unexpected error has occurred." + ex.getMessage());
    return;
 }
}

```
This code stops the sync between an object and a child quote.
```
public void stopQuoteSync() {
      Opportunity opp = new Opportunity();
      opp.setId(new ID("006D000000CpOSy"));
      opp.setFieldsToNull(new String[] {"SyncedQuoteId"} );
  // Invoke the update call and save the results
  try {
    SaveResult[] saveResults = binding.update(new SObject[] {opp});
    // check results and do more processing after the update call ...
  }
  catch (Exception ex) {
    System.out.println("An unexpected error has occurred." + ex.getMessage());
    return;
 }
}

##### Associated Objects

```
This object has these associated objects. Unless noted, they are available in the same API version as this object.


-----

**OpportunityChangeEvent (API version 44.0)**
Change events are available for the object.

**OpportunityFeed (API version 18.0)**
Feed tracking is available for the object.

**OpportunityHistory**

History is available for tracked fields of the object.

**OpportunityOwnerSharingRule**

Sharing rules are available for the object.

**OpportunityShare**

Sharing is available for the object.

##### Additional Considerations

If you are using `before triggers to set` `Stage` and `Forecast Category` for an opportunity record, the behavior is as follows:

**•** If you set `Stage` and `Forecast Category, the opportunity record contains those exact values.`

**•** If you set `Stage` but not `Forecast Category, the` `Forecast Category` value on the opportunity record defaults to
the one associated with trigger Stage.

**•** If you reset `Stage` to a value specified in an API call or incoming from the user interface, the `Forecast Category` value
should also come from the API call or user interface. If no value for Forecast Category is specified and the incoming Stage
is different than the trigger Stage, the Forecast Category defaults to the one associated with trigger Stage. If the trigger
`Stage and incoming` `Stage` are the same, the `Forecast Category` is not defaulted.

If you are cloning an opportunity with products, the following events occur in order:

**[1. The parent opportunity is saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)**

**[2. The opportunity products are saved according to the order of execution.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_triggers_order_of_execution.htm)**

Note: If errors occur on an opportunity product, you must return to the opportunity and fix the errors before cloning.

If any opportunity products contain unique custom fields, you must null them out before cloning the opportunity.

SEE ALSO:

OpportunityCompetitor

OpportunityHistory

OpportunityLineItem

OpportunityLineItemSchedule

OpportunityFieldHistory

Quote

QuoteLineItem

PartnerNetworkConnection
