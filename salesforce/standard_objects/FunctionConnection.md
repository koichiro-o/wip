#### FunctionConnection

Represents a connection between an org and Salesforce Functions. This object is available in API version 52.0 and later.

In API version 53.0, the name of this object was changed from SfFunctionsConnection to FunctionConnection.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), undelete(),
update(), upsert()

 Fields

```
```
Error
FunctionsAccountLoginOrg
FunctionsAccountName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The error string, if any, for the connection between the org and Salesforce Functions.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce Functions account login org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
FunctionsAccountUuid
Sequence
Status

##### Usage

```

**Description**
The Salesforce Functions account name.

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The unique Salesforce Functions account UUID. This is a generated ID that is not in Salesforce
object ID format.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, Sort

**Description**
Sequence number for the record.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The status of the connection between the org and Salesforce Functions.

Possible values are:

**•** `Attempted`

**•** `None`

**•** `TrustedBiDirection`

**•** `TrustedUniDirection`

The default value is 'None'. `TrustedBiDirection` indicates the connection is fully
established.


FunctionConnection is not intended for direct use and should be treated as a read-only object that represents the current connection
information between your org and Salesforce Functions. To create and manage connections between your org and Salesforce Functions
[use the steps and commands described in the Salesforce Functions developer documentation.](https://developer.salesforce.com/docs/platform/functions/guide/index.html)

FunctionConnection is not supported in Trialforce templates or org snapshots.


-----
