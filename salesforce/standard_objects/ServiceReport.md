#### ServiceReport

```

include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

Only users with View DeveloperName OR View Setup and Configuration permission can
view, group, sort, and filter this field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the presence status.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The label of the presence status.


Represents a report that summarizes a work order, work order line item, or service appointment.

The fields that appear on a service report are determined by its service report template. Service reports can be signed by the customer
and shared as a PDF.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()update( )

 Special Access Rules

```
Field Service must be enabled.


-----

##### Fields

**Field Name**
```
ContentVersionDocumentId
DocumentBody
DocumentContentType
DocumentLength
DocumentName

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the service report version, used for storage.

**Type**
base64

**Properties**
Create, Nillable

**Description**
The report output. DocumentBody can’t be retrieved via REST API.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of data used for the report output.. Possible values are:

**•** `audio/ogg`

**•** `text/calendar`

**•** `video/3gpp2`

**•** `video/3gpp`

**•** `image/avif`

**•** `text/calendar`

**•** `audio/x-caf`

**•** `image/webp`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The length of the report output.

**Type**
string


-----

```
DocumentTemplate
IsSigned
ParentId
ServiceReportLanguage

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the report output, always set to Service Report.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The template used to generate service documents for the Document Builder
feature.

Important: DocumentTemplate is different from Template. The
document template needs to reference a flexipage that is of type

`serviceDocument` and must target the object used to generate the
service document. For example, you can't use an Account flexipage for a
service report tied to a work order.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the service report contains one or more signatures. This field
isn’t supported for Document Builder.

Tip: Add this field to the Service Reports related list on work orders, work
order line items, and service appointments.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the service appointment, work order, or work order line item that the
service report summarizes. For example, if you click Create Service Report on
a service appointment, this field lists the service appointment’s record ID.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Restricted picklist


-----

```
ServiceReportNumber
Status
Template

```

**Description**
The language used for the service report. The language is selected in the
`ServiceReportLanguage` field on the associated work order. If the work
order doesn’t specify a service report language, the report is translated in the
default language in Salesforce of the person generating the report.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
An auto-generated number identifying the service report.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The status of the service report. Available in API version 53.0 and later.

Possible values are:

**•** `Completed`

**•** `Failed`

**•** `Generating`

**•** `In Progress`

**•** `None`

**•** `Queued`

The default value is `None.`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The service report template used to generate the service report.

Note: If the person creating the service report doesn’t have access to
certain objects or fields that are included in the service report template,
those fields aren’t visible in the report they create.


-----

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ServiceReportChangeEvent on page 67**
Change events are available for the object. Available in API version 55.0 and later.

**ServiceReportHistory**

History is available for tracked fields of the object.
