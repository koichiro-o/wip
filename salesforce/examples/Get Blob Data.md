### Get Blob Data

Use the sObject Blob Get resource to get blob data for a given record. To get blob data, a record with blob data must exist in Salesforce.

Only certain standard objects have blob fields, such as Attachment, ContentNote, ContentVersion, Document, Folder, and Note.

Note: The sObject Blob Get resource isn’t compatible with Composite API requests, because it returns binary data instead of data
in JSON or XML formats. Instead, make individual sObject Blob Get requests to retrieve blob data.

The following example gets the blob data for the Document record that was created in Insert or Update Blob Data on page 75.

#### Example for retrieving blob data from a Document record
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Document/015D0000000N3ZZIA0/body
 -H "Authorization: Bearer token"

```
**Example request body**
none required

**Example response body**
Document body content is returned in binary form. The response content type isn’t JSON or XML since the returned data is binary.
You can save the returned binary data to a file to store and access it.

SEE ALSO:

Insert or Update Blob Data
