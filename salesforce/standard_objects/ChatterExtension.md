#### ChatterExtension

Represents a Rich Publisher App that’s integrated with the Chatter publisher. This object is available in API version 41.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
CompositionComponentEnumOrId
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The ID of the composition component for the Rich Publisher App. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of your custom Rich Publisher App. This field requires a value.


-----

```
DeveloperName
ExtensionName
HeaderText
HoverText
IconId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the developer who is responsible for the app.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of your extension. This field requires a value.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show in the header of your app composer. Header text is required for Lightning
type extensions.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The text to show when a user mouses over your extension’s icon. Mouse-over text is required
for Lightning type extensions.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The icon to show in the Chatter publisher. Use an existing file asset ID from your org. This
field requires a value.

This is a relationship field.


-----

```
IsProtected
Language
MasterLabel
NamespacePrefix
RenderComponentEnumOrId

```

**Relationship Name**
Icon

**Relationship Type**
Lookup

**Refers To**
ContentAsset

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
An auto-generated value. It currently has no impact.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language used for this instance of the `ChatterExtension. This field requires a`
value.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the `ChatterExtension` object. This field requires a value.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The prefix to use for the extension’s namespace.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
Type

```

**Description**
The rendering component of the Rich Publisher App that you provide. It’s comprised of the
`lightning:availableForChatterExtensionRenderer` interface. This field
requires a value.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Describes the type of the extension. Currently, the only value supported is `Lightning.`
Included to allow for other possible types in the future.

