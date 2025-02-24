#### QuestionDataCategorySelection

A data category selection represents a data category that classifies a question.

This object can be used to associate a question with a data category from a data category group or to query the categorization for a
question.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To create, read or update data category selection, you must have create, read or update permission on the categorized question. Users
who can update question can also delete its category selection. Users who can create questions can only select categories visible to
their role.

##### Fields

```
DataCategoryGroupName

```

**Type**

DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category group which has a category associated with
the question.


-----

```
DataCategoryName
ParentId

##### Usage

```

**Type**

DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category associated with the question.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the question associated with the data category selection.


Every question can be categorized in a data category. You can use the QuestionDataCategorySelection object to query and manage
question categorization. Client applications can create categorization for a question. They can also delete, query, and retrieve question
categorization.

Warning: Even though the API lets you select more than one category for QuestionDataCategorySelection, the Answers tab only
supports one data category selection for questions. Selecting multiple categories through QuestionDataCategorySelection may
result in unexpected behavior in the Answers tab, such as losing your multiple selections. You should only select one data category
when using QuestionDataCategorySelection.

##### Sample Code—Java

In the following example, the `selectCategory method adds a category to a question data category selection. The`
`retrieveCategorySelections` method returns all the categories from a question data category selection.


-----

Salesforce Knowledge uses a similar object for article data category selection. See Article Type__DataCategorySelection for SOQL
examples using this object.

SEE ALSO:

Article Type__DataCategorySelection
