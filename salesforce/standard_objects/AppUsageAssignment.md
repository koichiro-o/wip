#### AppUsageAssignment

Provides application context for a record. A record can have different allowed actions or different related objects when it’s created for
different applications. For example, a Revenue Lifecycle Management order has a related `RevenueLifecycleManagement`
AppUsageAssignment, so Salesforce knows it can create assets for that order. Available in API version 50.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
AppUsageType
Name
RecordId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The application context for the record. Allowed values are determined by the available
licenses. For example, the `RevenueLifecycleManagement` and `BuyNow`
AppUsageTypes are available with the Subscription Management license.

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
Autogenerated name for the AppUsageAssignment.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The record that the AppUsageAssignment provides context for. For example, the order
record.

This is a relationship field.

**Relationship Name**
Record

**Relationship Type**
Lookup

**Refers To**

**•** Order in API version 58.0 and later

**•** Asset, Contract, Quote in API version 59.0 and later

**•** WebCart in API version 60.0 and later

**•** OrderSummary in API version 61.0 and later

```
Article Type__DataCategorySelection

```
A data category selection represents a data category that classifies an article. This object is available in API version 19.0 and later.


-----

This object can be used to associate an article with data categories from a data category group or to query the category selections for
an article.

The object name is variable and has a syntax of Article Type__DataCategorySelection, where Article Type is the Object
`Name` for the article type associated with the article. For example, Offer__DataCategorySelection represents the association
between the `Offer` article type and its data categories. Every article is associated with an article type.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), getDeleted(), retrieve()

 Special Access Rules

```
Knowledge must be enabled in your org. Not available in Lightning Knowledge. Users can only access, create or delete data category
selection visible to their role, permission set, or profile. If a user has partial visibility on an article's categorization, only the visible categories
are returned.

##### Fields

```
DataCategoryGroupName
DataCategoryName
ParentId

```

**Type**

DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category group which has categories associated with the article.

**Type**

DataCategoryGroupReference

**Properties**
Create

**Description**
Unique name of the data category associated with the article.

**Type**
reference

**Properties**
Create, Filter

**Description**
ID of the article associated with the data category selection.


-----

##### Usage

Every article in Salesforce Knowledge can be categorized. A data category selection represents a category that has been selected to
classify an article. You can use the `Article Type__DataCategorySelection object to query and manage article categorization in`
your org. Client applications can create a categorization for an article with a Draft status. They can also delete and query article
categorizations.

Note: When using Article Type__DataCategorySelection to classify an article, you can't select both a category (for example
USA) and one of its descendants (California) or ascendant categories (North America). In this case, only the first category is selected.

Answers zones use QuestionDataCategorySelection to classify questions.

##### SOQL Sample

The following SOQL query returns the data category selections used to classify the article whose ID is `ka0D000000005ApIAI.`
```
SELECT Id,DataCategoryName, ParentId
     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```
This clause only returns category unique names. To retrieve category labels use the following clause:
```
SELECT Id,toLabel(DataCategoryName), ParentId
     FROM Offer__DataCategorySelection WHERE ParentId='ka0D000000005ApIAI'

```
Tip: You can also use relationship queries to retrieve categorizations from an article type.

SEE ALSO:

QuestionDataCategorySelection
