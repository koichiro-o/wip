#### Dashboard

Represents a dashboard, which shows data from custom reports as visual components. Access is read-only. This object is available in
API version 20.0 and later.

##### Supported Calls
```
describeSObjects(), describeLayout(), query(), retrieve(), search()

```

-----

##### Fields

**Field**
```
BackgroundDirection
BackgroundEnd
BackgroundStart
ChartTheme
ColorPalette

```

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the direction of the background fade. Available values are:

**•** `Top to Bottom`

**•** `Left to Right`

**•** `Diagonal (default value)`

Label is `Background Fade Direction.`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the ending fade color in hexadecimal. Label is Ending Color.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the starting fade color in hexadecimal. Label is Starting Color.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the background theme used for charts.

Possible values are:

**•** `dark—Dark Background`

**•** `light—Light Background`

**Type**
picklist


-----

```
DashboardResultRefreshedDate
DashboardResultRunningUser
Description

```

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Returns the color palette used for the dashboard.

Possible values are:

**•** `Default—Default Palette`

**•** `accessible—Mineral(Accessible) Palette`

**•** `bluegrass—Bluegrass Palette`

**•** `colorSafe—Color Safe Palette`

**•** `dusk—Dusk Palette`

**•** `earth—Lake Palette`

**•** `fire—Fire Palette`

**•** `gray—Gray Palette`

**•** `heat—Heat Palette`

**•** `justice—Wildflowers Palette`

**•** `nightfall—Nightfall Palette`

**•** `pond—Pond Palette`

**•** `sunrise—Sunrise Palette`

**•** `tropic—Ocean Palette`

**•** `unity—Aurora Palette`

**•** `water—Water Palette`

**•** `watermelon—Watermelon Palette`

**Type**
string

**Properties**
Nillable

**Description**
Returns the date on which the dashboard results were last refreshed.

**Type**
string

**Properties**
Nillable

**Description**
The user whose security settings were used to generate the dashboard results.

**Type**
string


-----

```
DeveloperName
FolderId
FolderName

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
Returns the description of the dashboard. Limit: 255 characters.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The unique name of the object in the API. This name can contain only
underscores and alphanumeric characters, and must be unique in your org. It
must begin with a letter, not include spaces, not end with an underscore, and
not contain two consecutive underscores. In managed packages, this field
prevents naming conflicts on package installations. With this field, a developer
can change the object’s name in a managed package and the changes are
reflected in a subscriber’s organization. Label is Dashboard Unique Name.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance may slow while Salesforce generates one for each
record.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Required. Returns the ID of the Folder that contains the dashboard. See Folder.

This is a relationship field.

**Relationship Name**
Folder

**Relationship Type**
Lookup

**Refers To**
Folder, User

**Type**
string

**Properties**
Filter, Nillable, Sort


-----

```
IsDeleted
LastReferencedDate
LastViewedDate
LeftSize

```

**Description**
Name of the folder that contains the dashboard. Available in API version 35.0
and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not
(false). Label is Deleted.

**Type**
datetime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
datetime

**Properties**
Filter, Nillable, Sort,

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the left column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


-----

```
MiddleSize
NamespacePrefix
RightSize

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Returns the size of the middle column of the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

Returns the size of the right column in the dashboard.

Available values are:

**•** `Narrow`

**•** `Medium`

**•** `Wide`


-----

```
RunningUserId
TextColor
Title
TitleColor
TitleSize

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Returns the ID of the running user specified for the dashboard.

If the dashboard was created in Lightning Experience and is configured to run
as the viewing user, it returns the user ID of the dashboard creator.

If the dashboard was created in Salesforce Classic and is configured to run as the
logged-in user, returns the user ID of the last specified running user.

This is a relationship field.

**Relationship Name**
RunningUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the body text color in hexadecimal. Label is Text Color.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Returns the title of the dashboard. Limit: 80 characters.

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
Returns the title text color in hexadecimal. Label is Title Color.

**Type**
int


-----

```
Type

##### Supported Query Scopes

```

**Properties**
Filter, Group, Sort

**Description**
Returns the title font size in points. Label is Title Size.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
Returns the dashboard type. Available values are:

**•** `SpecifiedUser—The dashboard displays data according to the access`
level of one specific running user.

**•** `LoggedInUser—The dashboard displays data according to the access`
level of the logged-in user.

**•** `MyTeamUser—The dashboard displays data according to the access level`
of the logged-in user, and managers can view dashboards from the point of
view of users beneath them in the role hierarchy.


Use these scopes to help specify the data that your SOQL query returns.

**allPrivate**
Records saved in all users’ private folders.

[Requires the user permission "Manage All Private Reports and Dashboards" and Enhanced Analytics Folder Sharing. If your organization](https://help.salesforce.com/HTViewHelpDoc?id=analytics_sharing_enable.htm&language=en_US)
was created after the Summer ’13 release, you already have Enhanced Analytics Folder Sharing. Available in API version 36.0 and
later.

**created**
Records created by the user running the query.

**everything**
All records except records saved in other users’ private folders.

**mine**
Records saved in the private folder of the user running the query.

##### Usage

Provides read-only access to the current values in the dashboard fields.


-----

##### Example: Dashboards in an Inactive User’s Private Folder

This SOQL query returns dashboards saved in a specific user’s private folder.
```
SELECT Id FROM Dashboard USING SCOPE allPrivate WHERE CreatedByID = ‘005A0000000Bc2deFG’

##### Associated Objects

```
This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**DashboardFeed**

Feed tracking is available for the object.

SEE ALSO:

DashboardTag

Report
