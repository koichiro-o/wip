#### ManagedContentVariant

Represents a variant of a managed content item. This object is available in API version 56.0 and later.

Managed content variants are associated with a `ManagedContent object. The managed content and variants are counted as one`
content record in your Salesforce org.

For example, say you have a managed content item of content type News and a default language of English. When you translate the
News content into other languages such as Spanish, Japanese, and French, a managed content variant for each language is created.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

 Special Access Rules

```
`ManagedContentVariant` is available when the Digital Experiences app is enabled.


-----

##### Fields

**Field**
```
ContentTypeFullyQualifiedName
IsPublished
Language
ManagedContentId

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The fully qualified name of the content type of this CMS content. In an enhanced CMS
workspace, the `ContentTypeFullyQualifiedName` for each standard content
type is:

**•** News: `sfdc_cms__news`

**•** Image: `sfdc_cms__image`

**•** Document: `sfdc_cms__document`

The ContentTypeFullyQualifiedName for a custom content type is the same as
the developer name of the custom content type.

This field is available in API version 62.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the managed content variant is published to a channel.

The default value is `false.`

This field is calculated.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Language of the variant.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Globally unique identifier for the managed content item.

This field is a relationship field.


-----

```
ManagedContentKey
ManagedContentVariantStatus
Name
UrlName

```

**Relationship Name**
ManagedContent

**Relationship Type**
Lookup

**Refers To**
ManagedContent

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Globally unique identifier for managed content that associates with the managed content
variant.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Publication status of the managed content.

Possible values are:

**•** `Draft`

**•** `Published`

**•** `Revised`

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Name of the managed content variant.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL name of the managed content variant.


-----

```
VariantType

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Type of variant.

Possible value is:

**•** `Content`


Managed content variants are associated with a `ManagedContent object. The managed content and managed content variants`
are counted as one content record in your Salesforce org.

`ManagedContentVariant` can be queried through the public sObject API. Use this object to retrieve information for a specific
content in a certain language and format of a managed content.
