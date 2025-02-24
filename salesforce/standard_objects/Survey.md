#### Survey

Represents a survey.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

```
Note: You can’t define custom fields for the Survey object using the Object Manager.

##### Fields

```
ActiveVersionID
Description
DeveloperName
IsPartialSaveEnabled

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the survey version currently activated.

**Type**
string

**Properties**
Nillable

**Description**
The description of the survey. This field isn’t visible in the UI.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The survey’s unique API name.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether to save the partial responses for the survey (true) or not
(false).

The default value is `false.`


-----

```
LastReferencedDate
LastViewedDate
LatestVersionId
Name
NamespacePrefix

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the most recent version of this survey.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the survey that appears in the UI. This field is read-only from API
version 50.0.

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


-----

```
OwnerId
SurveyType
TotalVersionsCount

##### Associated Objects

```

installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user who created the survey.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Type of the survey. The default value is Survey.

Possible values are:

**•** `ASSESSMENT — Survey type for sales enablement teams. Available from`
API version 58.0 and later.

**•** `BASIC — Survey with a question page with like or dislike, long text, multiple`
selection, NPS, rating, short text, and single selection questions, and without
inserted participant responses, display logic, and page branching logic.

**•** `SURVEY — Survey with all the available features.`

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The number of versions of the survey.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**SurveyChangeEvent on page 67**
Change events are available for the object.

**SurveyFeed (API version 42.0)**
Feed tracking is available for the object.


-----

**SurveyOwnerSharingRule**

Sharing rules are available for the object.

**SurveyShare**

Sharing is available for the object.
