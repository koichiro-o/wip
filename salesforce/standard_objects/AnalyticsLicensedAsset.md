#### AnalyticsLicensedAsset

Represents a licensed Analytics asset. In this context, Analytics is CRM Analytics, Sonic, or Mulesoft Data Path. Available in API version
52.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ConsumerNamespace
LicenseType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The consumer namespace for the asset. The possible values are:

**•** `Industries`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The license type for the asset. The possible values are:

**•** `Aqs (Analytics Query Service)`

**•** `Cdp` (Data Cloud)

**•** `DataPipelineQuery` (Data Pipeline Query)

**•** `EinsteinAnalytics` (CRM Analytics)

**•** `MulesoftDataPath` (Mulesoft DataPath)

**•** `Sonic (Salesforce Data Pipelines)`

The default value is `EinsteinAnalytics.`

