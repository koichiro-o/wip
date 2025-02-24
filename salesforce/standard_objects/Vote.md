#### Vote

Represents a vote that a user has made on a Knowledge Article, Idea, or Reply.

Note: In API version 16.0 and earlier, SOQL queries on the Vote object only return votes for the Idea object. Starting in API version
17.0, SOQL queries return votes for both Idea and Reply.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

Voting on Knowledge articles is available only when Knowledge is enabled.

##### Fields

```
IsDeleted
LastModifiedById
LastModifiedDate

```

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
reference

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
ID of the user most recently associated with this vote.

**Type**
dateTime

**Properties**
Defaulted on create, Filter, Sort

**Description**
The datetime when this vote was last modified.


-----

```
ParentId
Type

```

**Type**
reference

**Properties**
Group, Sort, Create, Filter

**Description**
ID of the Knowledge Article, Idea, or Reply associated with this vote.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Idea, IdeaComment, KnowledgeArticle, Solution

**Type**
picklist

**Properties**
Group, Sort, Create, Filter, Restricted picklist, Update

**Description**
Picklist that indicates the type of vote. The value Up indicates that the vote is a user's positive
endorsement of the associated idea or reply. The value `Down` indicates that the vote is a
user's negative endorsement of the associated idea or reply.


Note: If you are importing Vote data into Salesforce and need to set the value for an audit field, such as CreatedDate, contact
Salesforce. Audit fields are automatically updated during API operations unless you request to set these fields yourself..

##### Usage

For Knowledge Articles, one vote record is inserted per user per Knowledge Article. Voting for another article version overrides the vote
for the previous version.

In version 12.0 and later, use this object to track the votes that users made on ideas. For more information on ideas, see “Understand
and Work with Ideas” in the Salesforce Help .

In version 17.0 and later, you must filter using the following syntax when querying this object in a SOQL query: ParentId = single
```
ID, Parent.Type = single Type, Id = single ID, or Id IN (list of IDs). See Comparison Operators in the

```
[Salesforce SOQL and SOSL Reference Guide for a sample query.](https://developer.salesforce.com/docs/atlas.en-us.254.0.soql_sosl.meta/soql_sosl/)

A SOQL query must filter using one of the following Parent or Id clauses.

**•** `ParentId = [single ID]`

**•** `Parent.Type = [single type]`

**•** `Id = [single ID]`


-----

**•** `Id IN = [list of IDs]`

SEE ALSO:

Idea

IdeaComment
