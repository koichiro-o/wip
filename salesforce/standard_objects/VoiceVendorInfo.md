#### VoiceVendorInfo

Represents information about the Service Cloud Voice or Sales Dialer provider’s vendor.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Spring ’20 and later, only your Salesforce org's internal users can access this object.

##### Fields

```
CorporateNumber
IsActive
LocalPresenceDefaultNumber
TenantConfigVersion

```

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The standard number that users can choose to display when making outgoing
calls.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Specifies whether the vendor is active or not.

**Type**
phone

**Properties**
Filter, Group, Nillable, Sort

**Description**
The default routing number that’s available for incoming local presence calls.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
VendorAccountKey
VendorProviderName
VendorType
