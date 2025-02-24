### Get an Image from a Rich Text Area Field

Use the sObject Rich Text Image Get resource to retrieve an image from a rich text area field. In this example, we retrieve an image from
a custom rich text field of a Lead record called `LeadPhotoRichText__c. We assume that an image has already been uploaded`
to this field.

#### Obtain the Image Reference ID

Before you can retrieve the image with a request, you must first obtain the `refid` from the rich text field. Use the sObject Rows on
page 149 resource to retrieve the field information for the Lead record.
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Lead/00Q112222233333
 -H "Authorization: Bearer token"

```
Here’s an example of abridged output from the request.
```
{
   "attributes": {
     "type": "Lead",
     "url": "/services/data/v51.0/sobjects/Lead/00Q112222233333"
   },
   "Id": "00Q112222233333",
   "IsDeleted": false,
   "MasterRecordId": null,
   "LastName": "Smith",
   "FirstName": "John",
   ...
   "LeadPhotoRichText__c": "<img alt=\"johnSmithPhoto\"
src=\"https://MyDomainName.documentforce.com/servlet/rtaImage?eid=a005e000007Dksm&amp;feoid=00N5e00000djU6Y&amp;refid=0EM5e000000B9LQ\"></img>"
}

```
You can see from the LeadPhotoRichText__c field that the `refid` of the image is `0EM5e000000B9LQ. Use this value in the next`
step to retrieve the image.


-----

#### Retrieve the Image

Use the Lead record ID, rich text field name, and image `refid` to retrieve the image. The response returns the image as encoded data
with the same file type as it was uploaded with. Save the returned data as an image file with the appropriate file type using the --output
`filename` parameter.
```
curl
https://MyDomainName.my.salesforce.com/services/data/v62.0/sobjects/Lead/00Q112222233333/richTextImageFields/LeadPhotoRichText__c/0EMR00000000A8V
 -H "Authorization: Bearer token" --output "LeadPhoto.jpeg"
