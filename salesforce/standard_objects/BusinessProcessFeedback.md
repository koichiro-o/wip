#### BusinessProcessFeedback

Setup object that stores information about the survey and the question associated with each stage in a customer lifecycle map. Customer
lifecycle maps are used to track the scores provided by customers across their lifecycle using Salesforce Surveys. This object is reserved
for internal use, and is available in API version 49.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
ActionName
ActionParam
ActionType

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the survey used to gather feedback.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Name of the question used to gather feedback.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
BusinessProcessDefinitionId

```

**Description**
Method of collecting feedback.

Possible value is:

**•** `PHONE_CALL`

**•** `SURVEY`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
Unique identifier of the stage associated with the survey and question.

