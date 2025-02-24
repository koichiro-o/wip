#### ServiceReportLayout

Represents a service report template in field service.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Field Service must be enabled. All users with Field Service Standard user permission can view the ServiceReportLayout object via the
API.

##### Fields

```
DeveloperName
Language
LastViewedDate

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name of the service report template.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the service report template uses.

**Type**
dateTime


-----

```
MasterLabel
TemplateType

##### Associated Objects

```

**Properties**
Filter, Nillable, Sort

**Description**
The date the service report template was last viewed.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the service report template. For example, Maintenance Report
Template.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the service report template. Available in API version 46.0 and later.

Possible values are:

**•** `DigitalForm`

**•** `ServiceReport`

The default value is `ServiceReport.`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ServiceReportLayoutChangeEvent on page 67**
Change events are available for the object. Available in API version 55.0 and later.
