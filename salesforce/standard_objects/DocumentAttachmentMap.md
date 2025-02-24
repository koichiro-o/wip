#### DocumentAttachmentMap

Maps the relationship between an EmailTemplate and its attachment, which is stored as a Document.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Customer Portal users can’t access this object.


-----

##### Fields

**Field**
```
 DocumentId
 DocumentSequence
 ParentId

##### Usage

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the document that this object tracks.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Represents the order that the attachments will be included in the email defined by the
EmailTemplate specified by the `DocumentId. Label is Attachment Sequence. The first`
attachment is given a value of 0, and each subsequent attachment is given a value
incremented by 1.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the EmailTemplate parent. The attachment identified by `DocumentId` is attached
to the EmailTemplate specified in this field.


Use this object to map the relationship of an EmailTemplate to its attachments, and to specify the order of the attachments.

SEE ALSO:

EmailTemplate
