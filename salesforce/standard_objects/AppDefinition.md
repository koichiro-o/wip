#### AppDefinition

Represents the metadata of an app and its navigation items. Metadata is returned only for apps that the current user can access. This
object is available in API version 43.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
Description
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The optional description of the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DurableId
HeaderColor
Id
IsLargeFormFactorSupported
IsMediumFormFactorSupported

```

**Description**
The developer name of the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A unique virtual Salesforce ID for the application.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The header color in the application. Specify the color with a hexadecimal code,
such as #0000FF for blue.

**Type**
ID

**Properties**
Defaulted on create, Filter, Group, idLookup, Sort

**Description**
A default Salesforce ID.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Large form factor is set in the CustomApplication
metadata.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Medium form factor is set in the CustomApplication
metadata.


-----

```
IsNavAutoTempTabsDisabled
IsNavPersonalizationDisabled
IsNavTabPersistenceDisabled
IsOmniPinnedViewEnabled
IsOverrideOrgTheme
IsSmallFormFactorSupported

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the navigation automatically creates temporary tabs settings.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether navigation personalization is disabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether workspace tabs are cleared for each new console session.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the Omni-Channel component is enabled in sidebar view. The
default is false.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to override the global theme for the org. When true, the color
scheme and logo that the user has set are used. When false, the global theme
for the org is used, even if the user has set a color scheme and logo.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

```
Label
LogoUrl
MasterLabel
NamespacePrefix
NavType

```

**Description**
Indicates whether the Small form factor is set in the CustomApplication
metadata.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The localized label value corresponding to the MasterLabel field.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logo URL of the application as selected by the admin.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The non-translated label entered when the application was created.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the application.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of navigation for the application. The value Standard is for Lightning
Experience. The value `Console` is for Salesforce console. A null value is for
Salesforce Classic.


-----

```
UiType
UtilityBar
