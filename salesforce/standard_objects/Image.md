#### Image

Represents the details of an image. This object is available in API version 47.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
 AlternateText
 CapturedAngle
 ContentDocumentId
 ImageClass

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Accessibility text to explain the image in words.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Angle at which the image was captured.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Unique identifier of the content document where image is stored.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The image category.

Possible values are:

**•** `FOOD`

**•** `LOGOS`

**•** `OBJECTS`


-----

```
ImageClassObjectType
ImageViewType
IsActive
LastReferencedDate
LastViewedDate

```


**•** `SCENES`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of image. Used in Einstein Object Detection to identify whether the image is used
to detect objects or build a model.

Possible values are:

**•** `DETECTION—Actual Image`

**•** `FEEDBACK`

**•** `TRAINING`

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Orientation of the image.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if an image is active. The default value is False. An active image can be used for
building or updating a model in Einstein Object Detection.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date on which the image was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort


-----

```
Name
OwnerId
Title
Url

```

**Description**
The date on which the image was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Name of the record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Unique identifier of the record owner.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Title of the image.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Public URL of the image file.


-----
