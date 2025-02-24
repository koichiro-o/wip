#### SvcCatalogRequest

```

**Description**
Allows the Service Catalog Builder to control whether the flow is displayed to users within
the Service Catalog.

Possible values are:

**•** `Deprecated`

**•** `Draft—Default`

**•** `PendingChanges`

**•** `Published`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The business type for which the Service Catalog is used. Available in API version 57.0 and
later.

Possible values are:

**•** `CustomerService`

**•** `Employee—Default`

**•** `FinancialServices`

**•** `Industry`


Represents a request made by a user using the Service Catalog. Catalog builders use this object to report on Service Catalog activity.
This object is available in API version 53.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
To access this object, get the Service Catalog Access permission set license, Employee Productivity Starter license, or Employee Productivity
Plus add-on license.


-----

##### Fields

**Field**
```
CatalogItemDescription
CatalogItemName
CatalogItemVersion
ClosedDate
CurrencyIsoCode

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description for the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the catalog item.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Version for the catalog item.

This is a calculated field. Available in API version 58.0 and later.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the request was closed. This field is automatically populated when
`IsClosed` is 'true'.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
ISO code of the currency. Must be one of the valid alphabetic, three-letter currency ISO codes
defined by the ISO 4217 standard, such as USD, GBP, or JPY. Must be unique within your
organization. Default value is `USD-U.S. Dollar.`


-----

```
FlowInterviewGuid
IsClosed
ItemFlowVersion
LastReferencedDate
LastViewedDate

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique GUID associated with the automation that was executed as part of the catalog item.
Available in API version 60.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the request has been resolved. This field is automatically checked when
`ClosedDate` is populated.

The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Version for the item flow.

This is a calculated field.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
the user might have only accessed this record or list view (LastReferencedDate) but
not viewed it.


-----

```
Name
OwnerId
Status
SubmitterId

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The Service Catalog request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID for the owner record.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service catalog request. Available in API version 60.0 and later.

Possible values are:

**•** `CompletedExecution—Default`

**•** `CreatedRequest`

**•** `StartedExecution`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID for the submitter record.

This is a relationship field.


-----

```
SvcCatalogItemDefinitionId
TargetCustomerId

```

**Relationship Name**
Submitter

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The catalog item that was used to create this request.

This is a relationship field.

**Relationship Name**
SvcCatalogItemDefinition

**Relationship Type**
Lookup

**Refers To**
SvcCatalogItemDef

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The customer ID that the request was submitted for. For example, when an agent runs a
catalog item for a given contact, the contact is represented by the TargetCustomerId.
Available in API version 61.0 and later.

This is a polymorphic relationship field.

**Relationship Name**
TargetCustomer

**Relationship Type**
Lookup

**Refers To**
Contact, User

