#### Knowledge__DataCategorySelection

Represents a data category that classifies an article. This object is available in API version 39.0 and later.

Note: By default, the prefix for this object name is `Knowledge` and that is the value shown in this reference. However, this
prefix can be modified by changing the Object Name for the Knowledge__kav object in Object Manager.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Lightning Knowledge must be enabled in your org.

##### Fields

```
DataCategoryGroupName
DataCategoryName
ParentId

```

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category group which has categories associated with the article.

**Type**
datacategorygroupreference

**Properties**
Create

**Description**
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the article associated with the data category selection.


-----

##### Usage

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use this object to query and manage article categorization in your organization. Client applications can create
a categorization for an article with a Draft status. They can also delete and query article categorizations.

Note: When using this object to classify an article, you can't select both a category (for example USA) and one of its descendants
(California) or ascendant categories (North America). In this case, only the first category is selected.
