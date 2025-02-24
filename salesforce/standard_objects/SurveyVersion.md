#### SurveyVersion

Represents a version of a survey.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search()

```
Note: You can’t define custom fields for the SurveyVersion object using the Object Manager.

##### Fields

```
BrandingSetId

```

**Type**
reference


-----

```
Description
IsTemplate
LastReferencedDate
LastViewedDate
Name

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the branding set associated with the survey version.

**Type**
textarea

**Properties**
Nillable

**Description**
The description of this survey version.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the survey version is a template. Template surveys are
automatically shared with all users in your Salesforce org.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the current user last viewed a record related to the survey
version.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed the survey version.

**Type**
string

**Properties**
Filter, Group, Sort

Filter, Group, Sort

Filter, Group, idLookup, Sort


-----

```
SurveyId
SurveyStatus
VersionNumber

##### Associated Objects

```

**Description**
The name of the survey that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the survey associated with the survey version.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the survey. Possible values include:

**•** `Active`

**•** `Draft`

**•** `Obsolete`

**•** `InvalidDraft`

**Type**
int

**Properties**
Filter, Group, Sort

**Description**
The version number of the survey.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyVersionChangeEvent on page 67**
Change events are available for the object.
