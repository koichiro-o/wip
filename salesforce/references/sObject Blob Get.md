### sObject Blob Get

Gets the specified blob field from an individual record and returns it as binary data. Only certain standard objects have blob fields, such
as Attachment, ContentNote, ContentVersion, Document, Folder, and Note.

Note: The sObject Blob Get resource isn’t compatible with Composite API requests, because it returns binary data instead of data
in JSON or XML formats. Instead, make individual sObject Blob Get requests to retrieve blob data.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/blobField

```
**Formats**
Binary data

**HTTP Method**
GET


-----

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**
none required

#### Example

For an example of retrieving blob data from a Document, see Get Blob Data on page 81.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
