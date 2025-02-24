#### ExtlRecShrRecordMap

Represents the lead or opportunity being mapped between a partner and vendor for Partner Connect. This object is available in API
version 62.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
ExtlRecShrCnctId
ExtlRecord
InboundStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the external record share connection.

This field is a relationship field.

**Relationship Name**
ExtlRecShrCnct

**Refers To**
ExtlRecShrCnct

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the lead or opportunity record on the external system.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of imports and updates received.

Possible values are:

**•** `ImportSuccess`

**•** `ImportConctExtlRecError`

**•** `UpdateSuccess`

**•** `UpdateFieldMapError`

**•** `UpdateConctExtlRecError`

**•** `UpdateUnknownError`


-----

```
InternalRecordId
IsImported
LastModifiedSent
Name
OutboundStatus

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the lead or opportunity record on the internal system.

This field is a polymorphic relationship field.

**Relationship Name**
InternalRecord

**Relationship Type**
Master-detail

**Refers To**
Lead, Opportunity (the master object)

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record originated on the internal system (true) or external system
(false).

The default value is `false.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Timestamp of the last record update between the vendor and partner. This field doesn’t
capture when the result is received.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
For internal use only.

**Type**
picklist


-----

```
UniqueRecordKey

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of exports, updates, and results received.

Possible values are:

**•** `ExportSuccess`

**•** `ExportInProgress`

**•** `ExportSuccessSkipped`

**•** `ExportSuccessPartial`

**•** `ExportPublishFieldMapError`

**•** `ExportSubscribeFieldMapError`

**•** `ExportPublishEventError`

**•** `ExportPublishUnknownError`

**•** `ExportSubscribeUnknownError`

**•** `ExportPublishConnectionError`

**•** `UpdateInProgress`

**•** `UpdateInProgressUpdateSuccess`

**•** `UpdatePublishFieldMapErrorUpdateSubscribeRecordNotFound`

**•** `UpdatePublishFieldMapError`

**•** `UpdateSubscribeFieldMapError`

**•** `UpdatePublishConnectionError`

**•** `UpdatePublishEventError`

**•** `UpdatePublishUnknownError`

**•** `UpdateSubscribeUnknownError`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Record key used internally for indexing. If IsImported is false, then this field contains
the `InternalRecordId` value. If `IsImported` is `true, this field contains the`
`ExtlRecord` value.

This field is a calculated field.


-----
