#### DigitalSignature

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Sync status of the delivery estimation setup configuration.

Possible values are:

**•** `Deleting`

**•** `Deprovisioned`

**•** `Error`

**•** `None`

**•** `Synced`

**•** `Syncing`

The default value is `NONE. This field is available in API version 62.0 and later.`


Represents a signature captured on a service report in field service.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()

 Special Access Rules

```
Field Service must be enabled.

##### Fields

```
DigitalSignatureNumber

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the signature.


-----

```
DocumentBody
DocumentContentType
DocumentLength
DocumentName
ParentId

```

**Type**
base64

**Properties**
Create

**Description**
The captured signature image.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The data type of the captured signature. Possible values are:

**•** `audio/ogg`

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
The length of the captured signature.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The name of the captured signature image.

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Place
SignatureType
SignedBy

```

**Description**
ID of the service appointment, work order, or work order line item that the service
report is generated for.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
AuthorizationFormConsent, Order, ServiceAppointment, WorkOrder,
WorkOrderLineItem

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The place where the report was signed.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort

**Description**
The role of the person signing the service report. Your org comes with one
signature type, Default. A service report template can only contain one
signature per type. If you plan to collect multiple signatures on service reports,
create additional values for the Signature Type field.

Create at least one value for every role that might need to sign a service report.
For example, `Technician, Customer, Supervisor, or Supplier. If`
some service reports will be signed by multiple people in one role—for example,
all technicians present at an appointment—create numbered types:
```
  Technician 1, Technician 2, and so forth.

```
Note: You can create up to 1,000 signature types. You can’t delete
signature types, but you can deactivate them so they can’t be used in
service report templates. When you deactivate a type, it still appears on
service report templates that used it, but you can’t use it on new service
report templates.

**Type**
string


-----

```
SignedDate

##### Usage

```

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The name of the person signing.

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort

**Description**
The date and time of the signing.


Add signature blocks to service report templates to determine which signatures need to be gathered on reports that use the template.
Service report templates can contain up to 20 signatures, and each signature must use a different Signature Type. For example, create
a standard service report template that contains a customer signature and a technician signature.

[To learn more about digital signatures, see Guidelines for Using Signatures on Service Reports.](https://help.salesforce.com/articleView?id=fs_signature_guidelines.htm&language=en_US)

##### Associated Objects

This object has the following associated objects. Unless noted, they’re available in the same API version as this object.

**DigitalSignatureChangeEvent (Available in API version 57.0)**
Change events are available for the object.
