#### InvoiceDocument

Tracks and displays the status of documents generated for invoices. Invoice documents are available in the related lists of invoice entity
records. This object is available in API version 61.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Fields

```
```
ContentDocumentId
DateGenerated
DocumentGenerationProcessId

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the generated PDF document.

This field is a relationship field.

**Relationship Name**
ContentDocument

**Refers To**
ContentDocument

**Type**
date

**Properties**
Filter, Group, Nillable, Sort

**Description**
The date on which the PDF is generated.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the entity that contains the information used to create the PDF invoice.

This field is a relationship field.

**Relationship Name**
DocumentGenerationProcess

**Refers To**
DocumentGenerationProcess


-----

```
DocumentNumber
ErrorMessage
InvoiceId
Status

```

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the generated document.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Errors that occur during PDF generation.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the invoice entity to which the invoice document is attached.

This field is a relationship field.

**Relationship Name**
Invoice

**Relationship Type**
Master-detail

**Refers To**
Invoice (the master object)

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the PDF generation process.

Possible values are:

**•** `Blocked`

**•** `Cancelled`

**•** `Failure`

**•** `Pending`

**•** `Success`


-----
