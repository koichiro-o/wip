#### DatasetExport

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExport acts as the header
and includes the JSON schema.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CompressedMetadataLength
Metadata

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
base64

**Properties**
Nillable

**Description**
Contains the JSON schema that describes the data in the CSV. This schema includes column
metadata such as type, format, and defaultValue.


-----

```
MetadataLength
Owner
PublisherInfo
PublisherType
Status

```

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExport object, Metadata is the BLOB field.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
User ID of the owner, as specified in the `userId parameter in the export node of the`
dataflow that created the record. Only the specified owner can read the content of the record.

**Type**
string

**Properties**
Filter, idLookup, Sort

**Description**
Identifies the export record to facilitate searching when a user has multiple export records.
By default, this column is set to the ID of the dataflow that generated the export record,
concatenated with the name of the specific export node. PublisherInfo is unique within your
organization.

Note: A dataflow can have multiple export nodes.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Target of the export, as specified in the `target parameter in the export node of the`
dataflow that created the record. The value must be `EinsteinDiscovery.`

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Status of the export. The possible values are:


-----

**•** New

**•** InProgress

**•** Completed

**•** Canceled

**•** Failed

Note: The content of the Metadata field can be downloaded when the status is
Completed.

##### Usage

This object is used with the DatasetExportPart object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery.
An export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

DatasetExportPart
