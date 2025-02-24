### sObject Rich Text Image Get

```
Gets the specified image data from a specific rich text area field in a given record. To get an image, you must have a record with an image
uploaded to a rich text area field.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/id/richTextImageFields/fieldName/contentReferenceId

```
**Formats**
Binary data

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

**Parameter** **Description**

`sObjectName` Indicates the name of the standard object of the record.

`id` The ID of the object.

`fieldName` The name of the rich text area field.

```
contentReferenceId

```

The reference ID that uniquely identifies an image within a rich text area field.

You can obtain the reference by retrieving information for the object. The description
shows the contents of the rich text area field. For example:


-----

The `refid` parameter of the image (0EMRM00000002Ip in this example) is the
```
                   contentReferenceId.

#### Example

```
For an example of retrieving the blob data from a rich text area field, see Get an Image from a Rich Text Area Field on page 74.

SEE ALSO:

[Object Reference for the Salesforce Platform](https://developer.salesforce.com/docs/atlas.en-us.252.0.object_reference.meta/object_reference/)
