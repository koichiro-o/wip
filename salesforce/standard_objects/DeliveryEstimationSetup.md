#### DeliveryEstimationSetup

Shows the configuration options for the commerce delivery service offered through a web store or sales channel. Includes settings such
as delivery location group, channel, fulfillment types, and default fulfillment time. This object is available in API version 61.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
The DeliveryEstimationSetup object is available only if the B2B Commerce or D2C Commerce license is enabled.

##### Fields

```
ChannelId
DefaultBusinessHoursId
DefaultPickupTime

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the web store or sales channel associated with the delivery estimation configuration.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID for the default business hours.

This is a relationship field.

**Relationship Name**
DefaultBusinessHours

**Refers To**
BusinessHours

**Type**
time

**Properties**
Create, Filter, Sort, Update

**Description**
Default pickup time.


-----

```
DefaultProcessingTime
DefaultProcessingTimeUnit
ExternalReference
isEnabled
LastReferencedDate

```

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Default processing time.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Default processing time unit. Possible values are:

**•** `Hours`

**•** `Days`

**•** `Weeks`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Unique code, reference, or identifier for the delivery estimation configuration record used
by external systems. Can be the name of the web store or sales channel associated with the
configuration to ensure a unique ID within the organization.

For example, `DefaultWebstore123.`

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the given delivery estimation configuration is active.

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
LastSyncedById
LastSyncedDate
LastSyncedMessage
LastViewedDate
LocationGroupId

```

**Description**
The date when the record was last modified. Its label in the user interface is `Last`
```
  Modified Date.

```
**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
User ID of who performed the last sync for this delivery estimation configuration. This field
is available in API version 62.0 and later.

This is a relationship field.

**Relationship Name**
LastSyncedBy

**Refers To**
User

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Date the delivery estimation configuration was last synced. This field is available in API version
62.0 and later.

**Type**
textarea

**Properties**
Nillable

**Description**
Message that occurred during the last sync. This field is available in API version 62.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Last time the delivery estimation configuration was viewed.

**Type**
reference


-----

```
Name
OwnerId

```
ServiceRegion


**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents a group of Omnichannel Inventory locations.

This is a relationship field.

**Relationship Name**
LocationGroup

**Refers To**
LocationGroup

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the delivery estimation setup configuration.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the user who currently owns this DeliveryEstimationSetup object. Default value is the
user logged in to the API to perform the create.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Refers To**
Group, User

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
An org's commerce delivery service provisioning region (North America, Europe, or Asia)
that's set when Delivery Estimation is enabled in the Order Management app. It can't be
changed. If the field is empty, provisioning hasn't occurred yet. Available in API version 63.0
and later.


-----

```
SyncStatus
