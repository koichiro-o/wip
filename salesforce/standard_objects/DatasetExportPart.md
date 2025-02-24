#### DatasetExportPart

Represents a dataset exported from CRM Analytics. When a dataset is exported, the data is converted into a .csv file and the schema is
stored in a separate JSON file. These files are stored in two objects: DatasetExport and DatasetExportPart. DatasetExportPart contains
parts of the .csv file.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
CompressedDataFileLength
DataFile

```

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.

**Type**
base64


-----

```
 DataFileLength
 DatasetExportId
 Owner
 PartNumber

##### Usage

```

**Description**
Contains a part of the dataset data from the generated .csv file. Maximum size is 32 MB.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
This field is required when a record in an object contains a BLOB (binary large object) field.
In the DataExportPart object, DataFile is the BLOB field.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the parent record that the part record is associated with.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
User ID of the owner, as specified in the `userId parameter in the export node of the`
dataflow that created the record. Only the specified owner can read the content of the record.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Used with the DatasetExportId to uniquely identify the data part. Parts are assembled
sequentially based on their numbers.


This object is used with the DatasetExport object for exporting data from a dataset in CRM Analytics for use in Einstein Discovery. An
export is initiated using the export node in an Analytics dataflow.

SEE ALSO:

DatasetExport


-----
