#### QuoteDocument

Represents a quote in document format. Available in API version 18.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
ContentVersionDocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID for the document’s version.


-----

```
CurrencyIsoCode
Discount
Document
GrandTotal
Name
QuoteId

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Restricted picklist

**Description**
Available only for organizations with the multicurrency feature enabled.

Contains the ISO code for any currency allowed by the organization. If the
organization has multicurrency and a Pricebook2Id specified on the quote,
then the currency value of this field must match the currency of the
PricebookEntry objects that are associated with any quote line items it has.

**Type**
percent

**Properties**
Filter, Nillable, Sort

**Description**
The discount for the quote used in the document.

**Type**
base64

**Properties**
Create, Nillable

**Description**
The binary data of the document stored in the QuoteDocument object.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Grand total for the quote used in the document.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Name of the quote document.

**Type**
reference


-----

**Properties**
Create, Filter, GroupSort

**Description**
ID for the quote used for the document.

##### Usage

Use the QuoteDocument object to store a document that can be used to present the quote information to the customer.

SEE ALSO:

Quote

QuoteLineItem
