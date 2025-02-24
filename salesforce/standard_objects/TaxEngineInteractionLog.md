#### TaxEngineInteractionLog

A record of a communication with an external tax engine following a tax calculation request. This object is available in API version 55.0
and later.

##### Supported Calls
```
delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete()

 Special Access Rules

```
This object is available when Subscription Management is enabled in your org.

##### Fields

```
Description
DocumentCode
EffectiveDate

```

**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Optional user-defined description for providing more information about the tax engine
interaction log.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Document code of the transaction for which the tax engine integration log was captured.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
InteractionHttpStatusCode
InteractionType
LastReferencedDate
LastViewedDate
ReferenceEntity

```

**Description**
The date that the tax engine request takes effect. This date is available for reference and
bookkeeping only and doesn’t have any impact on tax calculation.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The HHTP result code of the external callout made to a third-party tax engine provider. Refer
to your third-party tax engine provider’s documentation for details about the specific codes
returned.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of request made to the tax engine. In Subscription Management Summer
‘22, only `CalculateTax` is supported.

Possible values are:

**•** `CalculateTax`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
string


-----

```
RequestBody
RequestContentType
RequestLength
RequestName
ResponseBody

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The record on which tax was calculated.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API request.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the type of data passed in the request. For example, `application/html` or
```
  text/csv.

```
**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the request body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the request.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the content of the tax calculation API response.


-----

```
ResponseContentType
ResponseLength
ResponseName
ResultCode
TaxEngineId

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Shows the method used to deliver the tax calculation API response, such as
`application/html` or `text/vnd.salesforce.quip-template.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The character length of text within the response body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the response from the tax engine.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The code describing the result of the request.

Possible values are:

**•** `AdapterException—The Apex adapter interface for the tax provider threw an`
exception.

**•** `Success—The request was successful.`

**•** `TaxEngineError—An error occurred while processing the request. See the log for`
details.

**•** `ValidationError—A validation error occurred. Check that the request is complete`
and valid.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort


-----

```
TaxEngineInteractionLogNumber
