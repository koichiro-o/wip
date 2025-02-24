#### BackgroundOperationResult

Stores error messages generated when or importing data into big objects using Bulk API. This is a big object, available in API version
37.0 and later.


-----

Each instance of BackgroundOperationResult represents one error. The Message field stores the text of the error message.
The `ParentID` field stores the:

**•** Batch ID for the data import, in case of Bulk API

Bulk API validates data at the time of import, and generates an error message for the first occurrence of invalid data in any row of the
data file. The validation performed depends on the type of data being imported.

**•** **Text—The length of the input string must be less than or equal to the length of the corresponding text field in the target object.**

**•** **Number—The input data must be a number, whose scale and precision are compatible with the corresponding number field in**
the target object.

**•** **ID—The input data must be a valid 15- or 18-character ID.**

**•** **DateTime—The input data must be a valid dateTime value, in the approved format.**

**•** **Lookup—The lookup value must be a valid 15- or 18-character ID.**

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
CreatedById
CreatedDate
Data

```

**Type**
ID

**Properties**
Nillable

**Description**
The user ID of the user initiating the Bulk API request.

**Type**
dateTime

**Properties**
Defaulted on create

**Description**
The date and time at which the Bulk API request was made.

**Type**
string

**Properties**
Nillable

**Description**
The data that generated the error message. The total length is limited to 2,000
characters, and each column can occupy a maximum of 50 characters. Any data
exceeding those limits is truncated.


-----

```
Id
Message
MessageType
ParentId

##### Usage

```

**Type**
ID

**Properties**
Defaulted on create, idLookup

**Description**
The ID of the error message.

**Type**
string

**Properties**
Nillable

**Description**
The text of the error message.

**Type**
picklist

**Properties**
Nillable, Restricted picklist

**Description**
The type of error message. The possible values are: ERROR, WARNING, or INFO.

**Type**
reference

**Properties**
Filter, Sort

**Description**
The batch ID in Bulk API.


You can check for errors by querying the `BackgroundOperationResult` object. For example, this query returns details of all
errors in a data file imported using Bulk API, whose batch ID is `751xx000000006OAAQ.`
```
SELECT CreatedbyId, CreatedDate, Id, Message, MessageType, ParentId FROM
BackgroundOperationResult WHERE ParentId = “751xx000000006OAAQ”

```
Note: You can only view errors resulting from Bulk API requests that you initiated, unless you have the global permission to view
all data.
