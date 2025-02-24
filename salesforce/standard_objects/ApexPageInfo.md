#### ApexPageInfo

Represents metadata about a single Visualforce page. This object is available in API version 48.0 and later.

##### Supported Calls
```
describeSObjects(), query()

 Special Access Rules

```
As of Summer '20 and later, this object can only be accessed by users who can view a particular Visualforce page, and users with the
View Setup and Configuration permission.

##### Fields

```
ApexPageId
ApiVersion

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
ID for the Visualforce page.

**Type**
double


-----

```
Description
DurableId
IsAvailableInTouch
IsShowHeader
MasterLabel

```

**Properties**
Filter, Sort

**Description**
The API version for the page. Every page has an API version specified at creation. If the API
version is less than 15.0 and ApiVersion is not specified, ApiVersion defaults to
```
  15.0.

```
**Type**
textarea

**Properties**
Filter, Nillable, Sort

**Description**
Description of the Visualforce page.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
For internal use only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates if Visualforce tabs associated with the Visualforce page can be used in the Salesforce
app (true) or not (false). The default value is `false.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The showHeader value for the Visualforce page. This will be “unknown” if the Visualforce
page uses an expression to compute `showHeader. The default value is` `true.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Name
NameSpacePrefix

##### Usage

```

**Description**
The text used to identify the Visualforce page in the Setup area of Salesforce.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Developer name of the Visualforce page.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition org that creates
a managed package has a unique namespace prefix. Limit: 15 characters. You can refer to a
component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, the namespace prefix is set to the namespace prefix of the
org for all objects that support it.

Note: If an object is in an installed managed package, the object has the
namespace prefix of the installed managed package. This field’s value is the
namespace prefix of the Developer Edition org of the package developer.

**•** In non-Developer Edition orgs, `NamespacePrefix` is only set for objects that are
part of an installed managed package. Objects outside of an installed managed package
do not have a namespace prefix.


Use ApexPageInfo to query limited metadata about Visualforce pages. Some of this metadata corresponds to settings for a Visualforce
page available in Visualforce Pages. To access Visualforce Pages, from Setup, in the Quick Find box, enter Custom Code. Then,
select Visualforce Pages. Other values are only available via API. Use ApexPageInfo [in Visualforce pages to add custom content that](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_apexpage.htm)
extends the base Salesforce application functionality.

Users can only query `ApexPageInfo` records if they can display the associated Visualforce page, or if they have the View Setup &
Configuration permission. Allow users to view Visualforce pages by modifying their user profile or assigning permission sets.
