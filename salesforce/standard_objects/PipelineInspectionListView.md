#### PipelineInspectionListView

Represents a pipeline view, an intelligence view, or a saved filter. A pipeline view shows a set of opportunity records, based on specific
criteria. An intelligence view shows a set of account, lead, or contact records, based on specific criteria. This object is available in API
version 53.0 and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
To access this object, enable the Pipeline Inspection user permission and the Pipeline Inspection setting. To create and modify list views,
users must have the Create and Customize List Views permission. To create and modify public list views, users must have the Manage
Public List Views permission.

##### Fields

```
ChangePeriodLiteralType
ChangePeriodStartDate

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The date literal associated with the pipeline changes metrics group, used for filtering by a
custom time period.

Possible values are:

**•** `CUSTOM_DATE`

**•** `FOUR_WEEKS_AGO`

**•** `ONE_MONTH_AGO`

**•** `ONE_WEEK_AGO`

**•** `START_OF_THE_PERIOD`

**•** `THIS_MONTH`

**•** `THIS_WEEK`

**•** `THREE_MONTHS_AGO`

**•** `THREE_WEEKS_AGO`

**•** `TWO_MONTHS_AGO`

**•** `TWO_WEEKS_AGO`

**Type**
date


-----

```
DateLiteralType
EndDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The start date used when filtering by a custom time period for pipeline changes metrics and
forecast category metrics groups.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The date literal associated with the pipeline and intelligence views, used for filtering by the
close date, created date, or activity date.

Possible values are:

**Accounts** **Contacts &** **Opportunities**
**Leads**

`ALL_TIME` ** **
```
  CUSTOM_DATE

```
`DATE_NONE`  
`LAST_180_DAYS`  
`LAST_365_DAYS`  
`LAST_90_DAYS`  ```
  LAST_MONTH
  NEXT_FISCAL_QUARTER
  NEXT_MONTH
  NEXT_WEEK
  THIS_FISCAL_QUARTER
  THIS_MONTH
  THIS_WEEK

```
  - Available in API version 60.0 and later.

** Available on the "My Important" list views.

**Type**
date

|Col1|Accounts|Contacts & Leads|Opportunities|
|---|---|---|---|
|ALL_TIME||**|**|
|CUSTOM_DATE||||
|DATE_NONE *||||
|LAST_180_DAYS *||||
|LAST_365_DAYS *||||
|LAST_90_DAYS *||||
|LAST_MONTH||||
|NEXT_FISCAL_QUARTER||||
|NEXT_MONTH||||
|NEXT_WEEK||||
|THIS_FISCAL_QUARTER||||
|THIS_MONTH||||
|THIS_WEEK||||


-----

```
IsSystemManaged
ListViewId
MarketSegments
StartDate

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The end date used when filtering by a custom time period for close dates.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the system is managing changes to visibility and deletion of a pipeline
view (true) or not (false).

The default value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated ListView record. This field is unique within your organization.

This is a relationship field.

**Relationship Name**
ListView

**Relationship Type**
Lookup

**Refers To**
ListView

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The customer segments selected in the Prospecting Center view.

This field is available in API version 61.0 and later.

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
SummaryField
UserId
ViewType

```

**Description**
The start date used when filtering by a custom time period for close dates.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The opportunity field specified in a pipeline view to summarize pipeline inspection metrics.

Possible values are standard field names or custom field IDs for custom currency and number
fields.

**•** `Amount`

**•** `ExpectedRevenue`

**•** `TotalOpportunityQuantity`

**•** `custom_field_ID`

This field is available in API version 56.0 and later.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the user whose records you want to see by default in the list view. This field is a
relationship field.

This field is available in API version 58.0 and later.

**Relationship Name**
User

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The corresponding API name for the pipeline or intelligence view type.

Possible values are:

**•** `MY_ACCOUNTS–Available in API version 60.0 and later.`


-----

**•** `MY_CONTACTS`

**•** `MY_IMPORTANT_ACCOUNTS–Available in API version 60.0 and later.`

**•** `MY_IMPORTANT_CONTACTS`

**•** `MY_IMPORTANT_LEADS`

**•** `MY_IMPORTANT_OPPORTUNITIES`

**•** `MY_LEADS`

**•** `MY_PIPELINE`

**•** `MY_PROSPECTING_CENTER_ACCOUNTS–Available in API version`
```
                  61.0 and later.

##### Usage

```
Use this object to retrieve the metadata for a pipeline inspection view.
