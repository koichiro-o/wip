#### ObjectDataImport

Represents the data import status of one or more object records. This object is available in API version 57.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Fields

```
```
EndDate
FileName
ObjectDataImportNumber

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time (in UTC) when the data import finished.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Optional. If the data import was from a comma-delimited file (CSV), the name of the file. The
maximum length is 120 characters.

**Type**
string


-----

```
OwnerId
PrimaryObject
Result
Status

```

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
An auto-generated number identifying the data import.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who owns the data import status record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The name of the primary object being imported. For example, Lead. This value is usually
provided programmatically. The maximum length is 120 characters.

**Type**
textarea

**Properties**
Nillable

**Description**
The JSON response of the data object import result, including error messages.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The processing status of the data object import.

Possible values are:


-----

```
Type

##### Associated Objects

```


**•** `Completed`

**•** `In Progress`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of data import, such as from a comma-delimited file or through a connector.

Possible values are:

**•** `CSV Async`

**•** `CSV Sync`

**•** `External Record Import—A record imported or updated by Partner Connect`
[between a partner and vendor system. To see this field, enable Partner Connect. See Set](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)
[Up Partner Connect as a Partner in Salesforce Help. Available in API version 62.0 and later.](https://help.salesforce.com/s/articleView?id=sf.prm_pc_setup_partner_parent.htm&language=en_US)

**•** `One time Connector`


This object has these associated objects. If the API version isn’t specified, they’re available in the same API versions as this object. Otherwise,
they’re available in the specified API version and later.

**ObjectDataImportOwnerSharingRule on page 64**
Sharing rules are available for the object.

**ObjectDataImportShare on page 66**
Sharing is available for the object.
