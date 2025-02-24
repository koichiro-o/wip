#### AuthorizationFormText

Represents an authorization form’s text and language settings. This object is available in API version 46.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available if Data Protection and Privacy is enabled.

##### Fields

```
AuthorizationFormId
ContentDocumentId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. The ID of the associated authorization form record.

This is a relationship field.

**Relationship Name**
AuthorizationForm

**Relationship Type**
Lookup

**Refers To**
AuthorizationForm

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the ContentDocument that provides the authorization form’s text.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup


-----

```
DetailAuthorizationFormText
FullAuthorizationFormUrl
LastReferencedDate
LastViewedDate
Locale

```

**Refers To**
ContentDocument

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A detailed version of the authorization form.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The URL where the full text of the authorization form is located.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, it’s possible that this record was referenced (LastReferencedDate)
and not viewed.

**Type**

picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. Locale and LocaleSelection have the same
function.


-----

```
LocaleSelection
Name
SummaryAuthFormText

##### Associated Objects

```

Note: `Locale` can contain custom values not included in the picklist
if added before version 47.0.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code that control the language of the
authorization form text. Locale and LocaleSelection have the same
function.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the authorization form text.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A shortened version of the authorization form that is displayed to the user.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AuthorizationFormTextChangeEvent (API version 61.0)**
Change events are available for the object.

**AuthorizationFormTextHistory**

History is available for tracked fields of the object.
