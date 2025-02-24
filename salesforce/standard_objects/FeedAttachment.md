#### FeedAttachment

Represents an attachment to a feed item, such as a file attachment or a link. Use FeedAttachment to add various attachments to one
feed item. This object is available in API version 36.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), idEnabled(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** You can read, create, update, or delete a FeedAttachment only if you have the corresponding access to the associated FeedItem.

**•** Inline images aren’t creatable, updatable, or deletable through SOAP API.

##### Fields

```
FeedEntityId
RecordId
Title
Type

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the associated feed entity that contains this attachment.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The ID of the record that this feed attachment contains. For inline images,
`RecordId` is a ContentDocument ID. For content attachments, RecordId
is a ContentVersion ID, For feed items, `RecordId` is a FeedItem ID.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The title of this feed attachment. When Type is `Link, Title` value is the
label for the attachment link. Otherwise, Title value isn’t used.

**Type**
picklist


-----

```
Value

##### Usage

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of this feed attachment. Valid values are:

**•** 0 `Content—A content attachment.`

**•** 1 `InlineImage—An inline image. The system creates an inline image`
attachment when an image is added to the body of the associated FeedItem.
You can’t add an inline image directly using FeedAttachment.

**•** 2 `Link—A link.`

**•** 3 FeedEntity—A feed entity, for example, a post that is shared. Available
in API version 39 and later in Lightning Experience.

**•** 4 ChatterExtension—a Rich Publisher App that’s integrated with the
Chatter publisher.

**•** 5 `Record—A record.`

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The string value of this FeedAttachment. This field is optional. If the feed
attachment is a Link FeedAttachment, the value is the link URL string.



**•** This Apex example shows how to add an attachment to a Lead using API version 36.0 and later. First, post a feed item.
```
  //create and insert post
  FeedItem post = new FeedItem();
  post.Body = 'HelloThere';
  post.ParentId = 'ID_OF_LEAD_ENTITY';
  post.Title = 'FileName';
  insert post;

```
Then insert the attachment.
```
  //create and associate a content attachment to the post
  FeedAttachment feedAttachment = new FeedAttachment();
  feedAttachment.FeedEntityId = post.Id;
  feedAttachment.RecordId = 'ID_OF_CONTENT_VERSION';
  feedAttachment.Title = 'FileName';
  feedAttachment.Type = 'CONTENT';
  insert feedAttachment;

```
**•** You can create only one link attachment (FeedAttachment of type `Link) per feed item.`


-----

**•** If the feed item type is one of the following, you can add content or link feed attachments to a FeedItem.

**–** `AdvancedTextPost`

**–** `TextPost`

**–** `ContentPost`

**–** `LinkPost`

**–** `QuestionPost`

**•** When a `FeedAttachment` is added or removed from a feed item, Salesforce updates the type of the feed item to its most
appropriate value, as follows.

**–** If all content feed attachments are removed from a feed item of type ContentPost, the type of this feed item is updated to
```
   TextPost.

```
**–** Conversely, if a content feed attachment is added to a feed item of type TextPost, the type of this feed item is updated to
```
   ContentPost.

```
**–** If all link feed attachments are removed from a feed item of type LinkPost, the type of this feed item is updated to TextPost.

**–** Conversely, if a link feed attachment is added to a feed item of type TextPost, the type of this feed item is updated to
```
   LinkPost.

```
**–** The type of all other feed items, such as `QuestionPost` or `AdvancedTextPost` feed items, doesn’t change when any
feed attachments are added or removed.

**–** If a content feed attachment is added to a feed item of type `LinkPost, the feed item type is updated to` `ContentPost.`

**–** If all content attachments are removed from a feed item of type `ContentPost, but there's also a link attachment, the feed`
item type is updated to `LinkPost.`

**•** Users without administrator privileges can’t retrieve a FeedAttachment by its ID in a SOQL query. They can retrieve attachments by
specifying the associated FeedEntityId, as follows:
```
  SELECT Id FROM FeedAttachment WHERE FeedEntityId = 'some_feedItem_id'

```
**•** Alternatively, retrieve attachments by using a SOQL query on FeedItem with a subquery on the FeedAttachments child relationship,
as follows.
```
  SELECT Body, (SELECT RecordId, Title, Type, Value FROM FeedAttachments)
  FROM FeedItem
  WHERE Id = 'some_feedItem_id'

```
**•** FeedAttachment is not a triggerable object. You can access feed attachments in FeedItem update triggers by retrieving them through
[a SOQL query. For a trigger example, and to learn about trigger considerations for FeedAttachment, see Triggers for Chatter Objects](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/apexcode/apex_triggers_fields_not_updated_chatter.htm)
in the Apex Developer Guide.
