#### KnowledgeArticleVersionHistory

Enables read-only access to the full history of an article. This object is available in API version 25.0 and later.

[Knowledge__VersionHistory is derived from this object. To access this derived object, turn on field history tracking for Knowledge objects.](https://help.salesforce.com/articleView?id=tracking_field_history_for_custom_objects.htm&type=5&language=en_US)

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

```
You can also enable `delete()` [in API version 42.0 and later. See Enable delete of Field History and Field History Archive.](https://help.salesforce.com/articleView?id=000321814&type=1&mode=1&language=en_US)


-----

##### Special Access Rules

Knowledge must be enabled in your org. This object respects field, entity, and record-level security. You must have at least “Read”
permission on the article type or the field to access its history. For data category security, Salesforce determines access based on the
categorization of the online version of an article. If there’s no online version, then security is applied based on the archived version,
followed by the security of the draft version.

##### Fields

```
DataType
EventType
FieldName
Language

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of data that is tracked in the history table. This field is available in API
version 50.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of event that is tracked in the history table.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**

Name of the tracked field.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The language that the article is written in, such as `French` or `Chinese`
```
  (Traditional). Querying or searching articles in SOSL requires that you

```
specify the `Language` field in the WHERE clause. The language must be the
same for all article types.


-----

```
NewValue
OldValue
ParentId
ParentSobjectType
VersionId
VersionNumber

```

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

The new value of the field that was changed.

**Type**
anyType

**Properties**
Nillable, Sort

**Description**

The most recent value of the field before it was changed.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the article.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of object that contains the field.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**

The ID assigned to a version of the article.

This is a polymorphic relationship field.

**Type**
int

**Properties**
Filter, Group, Sort


-----

**Description**
The number assigned to a version of an article. This field is available in API version
24.0 and later.

##### Usage

Use this object to query events in the history of an article. For example, you can retrieve the number of edits a particular user has made
to an article, how many times the article has been published, and so on.
