#### FeedRevision

Holds the revision history of a specific feed item or comment, including a list of attributes that changed for each revision. This object is
available in API version 34.0 and later.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Fields

**Field Name**
```
Action
EditedAttribute
FeedEntityId
IsDeleted
IsValueRichText

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Holds the type of modification to the underlying feed item or comment attribute.
`Action` can have the value `Changed.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Identifies the part of the feed item or comment which was modified. A single
revision can have many edited attributes.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Identifies the modified feed item or comment.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the record has been moved to the Recycle Bin (true) or not
(false). This field is a standard system field.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the feed item `Body` contains rich text. If you post a rich text
feed comment using SOAP API, set IsRichText to true and escape HTML
entities from the body. Otherwise, the post is rendered as plain text.

Rich text supports the following HTML tags:


-----

**•** `<p>`

**•** `<a>`

**•** `<b>`


Tip: Though the `<br>` tag isn’t supported, you can use
`<p>&nbsp;</p>` to create lines.

```
OriginNetworkId
Revision
Value

```


**•** `<code>`

**•** `<i>`

**•** `<u>`

**•** `<s>`

**•** `<ul>`

**•** `<ol>`

**•** `<li>`

**•** `<img>`

The `<img>` tag is accessible only through the API and must reference files
in Salesforce similar to this example: `<img`
```
   src="sfdc://069B0000000omjh"></img>

```
Note: In API version 35.0 and later, the system replaces special characters
in rich text with escaped HTML. In API version 34.0 and prior, all rich text
appears as a plain-text representation.

**Type**

reference

**Properties**

Filter, Group, Nillable, Sort

**Description**
The ID of the Experience Cloud site in which a user modified the feed item or
comment. This field is only available, if digital experiences is enabled for your
org.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The revision number of the feed item or comment.

**Type**
textarea

**Properties**
Nillable


-----

**Description**
Identifies the value of the `EditedAttribute` field before the update.

##### Usage

This object tracks the changes made to a feed item or feed comment and stores a list of attributes that changed for each revision.

**•** To query the FeedRevision object, users need the View All Data permission or supply a WHERE clause on the `FeedEntityId.`
