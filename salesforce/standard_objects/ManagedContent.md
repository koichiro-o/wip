#### ManagedContent

Represents managed content in a Salesforce CMS workspace for use in an Experience Cloud site or a channel. The ManagedContent
object represents the complete instance of a managed content record. It provides a consistent identifier for the managed content so
that variants of the content item can be created over time. This object is available in API version 56.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```

-----

##### Special Access Rules

`ManagedContent` is available when the Digital Experiences app is enabled.

##### Fields

```
ApiName
AuthoredManagedContentSpaceId
ContentKey

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**

The unique API name of the Salesforce CMS content. Name requirements:

**•** must be 80 characters or fewer

**•** must begin with a letter

**•** can contain only underscores and alphanumeric characters

**•** can't include spaces

**•** can't end with an underscore

**•** can't contain two consecutive underscores

This field is available in API version 62.0 and later.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The Salesforce CMS workspace ID where the content resides.

This field is a relationship field.

**Relationship Name**
AuthoredManagedContentSpace

**Relationship Type**
Lookup

**Refers To**
ManagedContentSpace

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
Unique identifier of the content.


-----

```
ContentTypeFullyQualifiedName
Name
PrimaryLanguage

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

In a CMS workspace, the `ContentTypeFullyQualifiedName` for each standard
content type is:

**•** News: `news`

**•** Image: `cms_image`

**•** Document: `cms_document`

In both CMS workspaces and enhanced CMS workspaces, the
`ContentTypeFullyQualifiedName` for a custom content type is the same as the
developer name of the custom content type.

This field is available in API version 62.0 and later.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the Salesforce CMS content. When you view this content in a CMS workspace,
`Name` is the title of the latest content version. In an enhanced CMS workspace, `Name` is
the title of the content in the workspace’s default language.

This field is available in API version 58.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The default language of the Salesforce CMS workspace where the content resides.


-----

##### Usage

When you create or add content in a Salesforce CMS workspace, the content is uniquely identified by the Salesforce CMS workspace, a
content key, and a default language. `ManagedContent` can be queried through the public sObject API. Use this object to create
and retrieve information for a specific managed content.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ManagedContentChangeEvent on page 67 (API version 62.0)**
Change events are available for the object.
