#### SurveyPage

Represents a page, such as the title page or a question page, in a survey.

##### Supported Calls
```
getDeleted(), getUpdated(), query(), retrieve()

```
Note: You can’t define custom fields for the SurveyPage object using the Object Manager.

##### Fields

```
DeveloperName
Name

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique API name of this SurveyPage object.

**Type**
string


-----

```
SurveyVersionId

##### Associated Objects

```

**Properties**
Filter, Group, idLookup, Sort

**Description**
The name of the survey page that appears in the UI.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The version of the survey that the page belongs to.


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**SurveyPageChangeEvent on page 67**
Change events are available for the object.
