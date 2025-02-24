#### OrgMetricScanResult

Represents data or an item associated with a feature’s results in a Salesforce Optimizer evaluation. For example, for the Custom Field
Limit feature, an OrgMetricScanResult object represents an object flagged for approaching the custom field limit. This object is available
in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in orgs where Salesforce Optimizer is enabled. Requires the Modify All Data and Customize Application user
permissions.

##### Fields

```
Date
Flags
ItemStatus

```

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date associated with an item in a feature’s Optimizer evaluation.

**Example**
For the Unsupported Browsers feature, `Date` indicates the date that the user last logged
in with an unsupported browser.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The flags associated with an item in a feature’s Optimizer evaluation.

**Example**
For the API Versions feature, `Flags` indicates the API version of an object that Optimizer
evaluates as outdated.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update


-----

```
Name
Object
OrgMetricScanSummaryId

```

**Description**
The recommended action for an item in a feature’s Optimizer evaluation.

Possible values are:

**•** `Action Required`

**•** `Immediate Action Required`

**•** `No Action Required`

**•** `Not Currently Enabled`

**•** `Review Required`

**•** `Unable to Analyze`

The default value is `No Action Required.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the item in a feature’s Optimizer evaluation, such as an object name.

**Example**
For the Unassigned Roles feature, `Name` refers to the name of the unassigned role.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The object ID associated with the item in a feature’s Optimizer evaluation.

For the Release Update feature only, `Object` indicates the release that the update is
scheduled for.

**Example**
For the Unused Reports feature, `Object` refers to the ID of the unused report.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The feature’s OrgMetricScanSummary ID from the most recent Optimizer run.

This field is a relationship field.

**Relationship Name**
OrgMetricScanSummary


-----

```
Profile
Quantity
Type
Url

```

**Relationship Type**
Master-detail

**Refers To**

OrgMetricScanSummary on page 3708 (the master object)

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The profile ID associated with the item in a feature’s Optimizer evaluation.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A quantity associated with the item in a feature’s Optimizer evaluation.

**Example**
For the Custom Field Limits feature, `Quantity` indicates the total number of fields on an
object that approaches the custom field limit.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The type of item or data in a feature’s Optimizer evaluation.

**Example**
For the Unsupported Browsers feature, `Type` indicates the unsupported browser and
platform used.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL associated with the item in a feature’s Optimizer evaluation.

**Example**
For the Unassigned Page Layouts feature, the URL represents a link to the unassigned layout.


-----

```
User

```
SEE ALSO:


**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The user ID or username associated with the item in a feature’s Optimizer evaluation. For
the Release Update feature only, User indicates the name of the release update that requires
review.

**Example**
For the User Logins feature, `User` indicates the username of a user who hasn’t recently
logged in.


_[Salesforce Help: Improve Your Implementation with Salesforce Optimizer](https://help.salesforce.com/s/articleView?id=sf.optimizer_introduction.htm&language=en_US&type=5)_
