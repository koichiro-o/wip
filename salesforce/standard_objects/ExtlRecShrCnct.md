#### ExtlRecShrCnct

Represents authentication data to make outbound calls to and inbound calls from an external system to publish events for Partner
Connect. This object is available in API version 62.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

```

-----

##### Special Access Rules

[To see this object, enable Partner Connect or Partner Connect for Vendors. See Set Up Partner Connect as a Partner and Set Up Partner](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Connect as a Vendor in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_vendor_parent.htm&language=en_US)

##### Fields

```
CnctName
CnctRole
CnctStatus
ExternalClientApplicationId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of the connection.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
System’s role in the connection.

Possible values are:

**•** `Partner`

**•** `Vendor`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Status of the connection.

Possible values are:

**•** `Disabled`

**•** `Enabled`

**•** `Error`

**•** `Pending`

**•** `Unknown`

**Type**
reference


-----

```
ExtlSystem
NamedCredentialId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of external client app representing your org’s connection to the external system.

This field is a relationship field.

**Relationship Name**
ExternalClientApplication

**Refers To**
ExternalClientApplication

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
ID of the external system.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the named credential.

This field is a relationship field.

**Relationship Name**
NamedCredential

**Refers To**
NamedCredential

