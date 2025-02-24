#### FunctionInvocationRequest

Represents invocation information for a Salesforce Function. This object is available in API version 51.0 and later.

When a Salesforce Function is invoked using the Apex `functions.Function` invoke methods, a FunctionInvocationRequest
record is created that contains information on the status and results of the invocation.

##### Supported Calls
```
delete(), describeSObjects(), getDeleted(), getUpdated(), query(), undelete(), update()

 Fields

```
```
CallbackStatus
ExecutionTime
ExtendedResponse

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the callback for asynchronous invocations. This field is new in API version 52.0.

Possible values are:

**•** `Completed`  - Not used for the Salesforce Functions beta.

**•** `Enqueued`  - The Function has completed (either successfully or unsuccessfully), and
the callback has been enqueued for asynchronous execution in the Salesforce org.

**•** `Failed`  - Not used for the Salesforce Functions beta.

**•** `PendingResponse`  - The Function has not yet completed, so the callback has not
been called yet.

The default value is 'PendingResponse'.

**Type**
long

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
The execution time of the Function in milliseconds.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
JSON object with additional information about the result of the Function execution.


-----

```
FunctionName
InvokingNamespacePrefix
NamespacePrefix
OwnerId

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the Function that was invoked. This name is case-sensitive and uses the format
“project name-function name”

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Prefix of the namespace that invokes the function. A namespace can invoke the global
function using an installed package via Apex.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. This object is available in API version
53.0 and later. Each Developer Edition org that creates a managed package has a unique
namespace prefix. Limit: 15 characters. You can refer to a component in a managed package
by using the `namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Filter, Group, Sort, Update

**Description**
The owner of the FunctionInvocationRequest.

This is a polymorphic relationship field.


-----

```
ResponseBody
ResponseContentType
ResponseLength
ResponseName
ResponseUncompressedLength

```

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
base64

**Properties**
Nillable, Update

**Description**
Response body of the invoked Function.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Content type of the response body of the invoked Function. For example, the content type
could be application/json, text/csv, or various other values depending on what
the Function returned.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Length of the response body.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Name of response, not currently used.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort, Update


-----

```
StackTrace
Status

##### Usage

```

**Description**
Uncompressed length of the Function response, if the response content was compressed.

**Type**
textarea

**Properties**
Nillable, Update

**Description**
If there was an error invoking the function, this field contains the Function stack trace.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Status of the invoked Function. Functions that are invoked asynchronously can be in a queued
`InProgress` state before they are invoked.

Possible values are:

**•** `Dispatched`  - Not used for the Salesforce Functions beta.

**•** `Error`  - The Function failed to execute due to either an error starting the Function, or
an error while the Function was running.

**•** `FunctionInProgress`  - The Function invocation has been sent to the Salesforce
Functions compute environment, and is running.

**•** `InProgress`  - The Function invocation request has been enqueued.

**•** `New`  - The Function invocation request has been created, but not enqueued yet.

**•** `Success`  - The Function has completed execution. For status on whether the callback
has been called, see the CallbackStatus field.

The default value is 'New'.


Treat FunctionInvocationRequest records as read-only records used to get information about a specific Function invocation. To invoke
Functions, use the Apex `functions.Function` class invoke methods.

FunctionInvocationRequest is not supported in Trialforce templates or org snapshots.
