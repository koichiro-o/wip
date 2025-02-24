#### SalesChannel

```
Represents the origin of an order. For example, a web storefront, physical store, marketplace, or mobile app. If you integrate Salesforce
Order Management with Salesforce B2C Commerce, set up a SalesChannel corresponding to each Site in your B2C Commerce
implementation. This object is available in API version 48.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is only available in Salesforce Order Management orgs.

##### Fields

```
Description
ExternalChannelNumber
LastReferencedDate

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of the SalesChannel.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
External system identifier for the SalesChannel.

**Type**
dateTime


-----

```
LastViewedDate
OwnerId
SalesChannelName
Type

```

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. A null value can mean that
this record has only been referenced (LastReferencedDate) and not viewed.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the user who currently owns this SalesChannel. Default value is the user logged in
to the API to perform the create.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the SalesChannel.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Type of the SalesChannel. Each Type corresponds to one Type Category. You can customize
the Type picklist to represent your business processes, but the Type Category picklist is fixed
because some order processing is based on those values. If you customize the Type picklist,
include at least one value for each Type Category. This field is available in API version 53.0
and later.

Default values are:

**•** `B2B`

**•** `B2C`

**•** `Other`


-----

```
TypeCategory

##### Associated Objects

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Type Category of the SalesChannel. Each Type Category corresponds to one or more Types.
This field isn’t visible in the UI. This field is available in API version 53.0 and later.

Possible values are:

**•** `B2B`

**•** `B2C`

**•** `Other`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SalesChannelChangeEvent (API version 62.0)**
Change events are available for the object.

SEE ALSO:

Order

OrderSummary
