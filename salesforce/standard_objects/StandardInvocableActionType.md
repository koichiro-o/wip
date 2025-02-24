#### StandardInvocableActionType

Represents a collection of fields to set up granular user permissions for access to a standard invocable action in Flow Builder. This object
is available in API version 60.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Marketing Cloud Growth edition and the Manage Flow user permission or View Flows user permission are required.

##### Fields

```
DeveloperName

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The developer name and namespace combination of the invocable action. This combination
must be unique.


-----

```
Language
MasterLabel
Namespace

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The language code of the invocable action. For a full list of supported languages and their
[codes, see Supported Languages. This field is available in API version 60.0 and later.](https://help.salesforce.com/s/articleView?id=sf.faq_getstart_what_languages_does.htm&language=en_US)

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label for the invocable action. This display value is the internal label that doesn’t get
translated. This field is available in API version 60.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace of the invocable action. Enter a value only if you’re using the invocable action
in Flow Builder or with Apex.

