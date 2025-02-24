### Parameterized Search

Executes a simple REST search using parameters instead of a SOSL clause. Indicate parameters in the URI with the GET method. Or, use
the POST method to create complex searches in a request body.

#### Search with Parameters in the URI

Get search results using simple URI parameters instead of using SOSL. Make basic queries without defining a large SOSL query. Use this
API when you have a basic use case to cover, replacing FIND `searchString` IN ALL FIELDS by just including the search string in the
URI. This resource is available in REST API version 36.0 and later.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/parameterizedSearch/?q=searchString

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Required Global Parameters**

**Name** **Description**

`q` A search string that is properly URL-encoded.

Note: SOSL clauses aren’t supported.

Available in version 36.0 and later.

**Optional Global Parameters**

|Name|Type|Description|
|---|---|---|
|dataCategory|string|Single value. If an organization uses Salesforce Knowledge articles or answers, dataCategory filters all search results based on one data category. For example, dataCategory=GlobalCategory__c below NorthAmerica__c. When using dataCategories, specify a Salesforce Knowledge article or answer type with sobject and all the required parameters. For example:|
|||q=tourism&sobject=KnowledgeArticleVersion&KnowledgeArticleVersion.where= language='en_US'+and+publishStatus='online'&KnowledgeArticleVersion.fields= id,title&dataCategory=Location__c+Below+North_America__c|
|||If you require multiple dataCategory filters, use dataCategories with the POST method.|
|defaultLimit|string|Single value. The maximum number of results to return for each sobject (GET) or sobjects (POST) specified. The maximum defaultLimit is 2000. At least one sobject must be specified. GET example: defaultLimit=10&sobject=Account&sobject=Contact. When an sobject limit is specified using sobject.limit=value, such as Account.limit=10, this parameter is ignored for that object.|


-----

|Name|Type|Description|
|---|---|---|
|division|string|Single value. Filters search results based on the division field. For example in the GET method, division=global. Specify a division by its name rather than ID. All searches within a specific division also include the global division.|
|fields|string|Comma-separated list of one or more fields to return in the response for each sobject specified. At least one sobject must be specified at the global level. For example: fields=id&sobject=Account&sobject=Contact. The global fields parameter is overridden when sobject are specified using sobject.fields=field names. For example, Contact.fields=id,FirstName,LastName would override the global setting of just returning the id. If unspecified, then the search results contain the IDs of records matching all fields for the specified object. Functions The following optional functions can be used within the fields parameter. • toLabel: Translates response field value into the user’s language. For example, Lead.fields=id,toLabel(Status). This function requires extra setup. • convertCurrency: Converts response currency fields to the user’s currency. For example, Opportunity.fields=id,convertCurrency(Amount). This function requires extra setup. Multi-currency must be enabled in your org. • format: Applies localized formatting to standard and custom number, date, time, and currency fields. For example, Opportunity.fields=id,format(Amount). Aliasing is supported in fields for toLabel, convertCurrency, and format. In addition, aliasing is required when the query includes the same field multiple times. For example, Opportunity.fields=id,format(Amount) AliasAmount|
|in|string|Scope of fields to search. If you specify one or more scope values, the fields are returned for all found objects. Use one of the following values: • ALL • NAME • EMAIL • PHONE • SIDEBAR This clause doesn't apply to articles, documents, feed comments, feed items, files, products, and solutions. If any of these objects are specified, the search isn’t limited to specific fields; all fields are searched.|


-----

|Name|Type|Description|
|---|---|---|
|metadata|string|Specifies if metadata should be returned in the response. No metadata is returned by default. To include metadata in the response, use the LABELS value, which returns the display label for the fields returned in search results. For example: ?q=Acme&metadata=LABELS|
|netWorkIds|string|Filters search results by a comma-separated list. A network ID represents the Experience Cloud site ID.|
|offset|string|Single value. The starting row offset into the result set returned. The maximum offset is 2000. Only one sobject can be specified when using this parameter.|
|overallLimit|string|Single value. The maximum number of results to return across all sobject parameters specified. The maximum overallLimit is 2000.|
|pricebookId|string|Single value. Filters product search results by a price book ID for only the Product2 object. The price book ID must be associated with the product that you’re searching for. For example, ?q=laptop&sobject=product2&pricebookId=01sxx0000002MffAAE|
|snippet|string|The target length (maximum number of snippet characters) to return in Salesforce Knowledge article, case, case comment, feed, feed comment, idea, and idea comment search results. The snippet parameter displays contextual excerpts and highlights the search term for each article in the search results. Snippet results are used to differentiate matches to the search term in article search results. The target length can be from 50 to 1000 characters. Snippet and highlights are generated from email, text, and text area (long and rich) fields. Snippets aren’t displayed for partially matching searches or if the user doesn’t have access to the field that contains the snippet. Snippets are only displayed when 20 or fewer results are returned on a page. At least one of the following sobject values must be specified. • To search a specific article type, use the article type name with the suffix __kav. • To search all article types, use KnowledgeArticleVersion. • To search case, case comment, feed, feed comment, idea, and idea comment types, use Case, CaseComment, FeedItem, FeedComment, Idea, and IdeaComment. For example, q=tourism&sobject=Case&snippet=500.|
|sobject|string|Objects to return in the response. Must be a valid object type. You can use multiple sobject values, such as sobject=Account&sobject=Contact. If unspecified, then the search results contain the IDs of all objects.|


-----

|Name|Type|Description|
|---|---|---|
|spellCorrection|boolean|Specifies whether spell correction is enabled for a user’s search. When set to true, spell correction is enabled for searches that support spell correction. The default value is true. For example: q=Acme&sobject=Account&Account.fields=id&spellCorrection=true|
|updateTracking|string|Specifies a value of true to track keywords that are used in Salesforce Knowledge article searches only. If unspecified, the default value of false is applied.|
|updateViewStat|string|Specifies a value of true to update an article’s view statistics. Valid only for Salesforce Knowledge article searches. If unspecified, the default value of false is applied.|

```
sobject-level Parameters

```
The following optional parameters can be used with the `sobject parameter in a GET method to further refine search results.`
These settings would override any settings specified at the global level.

The format is sobject.parameter, such as Account.fields. An sobject must be specified to use these parameters,
for example, `sobject=Account&Account.fields=id,name.`

|Name|Type|Description|
|---|---|---|
|fields|string|Comma-separated list of one or more fields to return in the response. For example, KnowledgeArticleVersion.fields=id,title.|
|limit|string|Specifies the maximum number of rows that are returned for the sobject. For example, Account.limit=10.|
|orderBy|string|Controls the field order of the results using the following syntax orderBy = field {ASC|DESC} [NULLS_{FIRST|LAST}] For example: Account.orderBy=Name • ASC: ascending. Default. • DESC: descending. • NULLS_FIRST: Null records at the beginning of the results. Default. • NULLS_LAST: Null records at the end of the results.|
|where|string|Filter search results for this object by specific field values. For example, Account.where = conditionExpression. Here the conditionExpression of the WHERE clause uses the following syntax: fieldExpression [logicalOperator fieldExpression2 ... ]. Add multiple field expressions to a condition expression by using logical and comparison operators. For example, KnowledgeArticleVersion.where=publishstatus='online' and language='en_US'.|


-----

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/parameterizedSearch/?q=Acme&sobject=Account&Account.fields=id,name&Account.limit=10

#### Search with Parameters in the Request Body

```
Search by defining parameters in the request body Access advanced search that offers more control over how the search query executes.
It also allows you to filter using several DataCategories, networks (sites), orderBy constraints, and filters. This resource is available in REST
API version 36.0 and later.

##### Syntax

**URI**
```
  /services/data/vXX.X/parameterizedSearch/

```
**Formats**
JSON, XML

**HTTP methods**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Required Global Parameters**

**Name** **Description**

`q` A search string that is properly URL-encoded.

Note: SOSL clauses aren’t supported.

Available in version 36.0 and later.

**Optional Global Parameters**

|Name|Type|Description|
|---|---|---|
|dataCategories|dataCategoriesFilter[]|If an organization uses Salesforce Knowledge articles or answers, filter all search results based on one or more data categories. When using dataCategories, specify a Salesforce Knowledge article or answer type with sobjects and the required parameters. For example:|
|||{ "q":"Acme", "fields":["id", "title"], "sobjects":[{"name":"KnowledgeArticleVersion",|


-----

|Name|Type|Description|
|---|---|---|
||||
|||"where":"language='en_US' and publishstatus='draft'"}], "dataCategories":[ {"groupName" : "location__c", "operator":"below", "categories":["North_America__c"]} ] }|
||||
|defaultLimit|string|Single value. The maximum number of results to return for each sobject (GET) or sobjects (POST) specified. The maximum defaultLimit is 2000. At least one sobject must be specified. GET example: defaultLimit=10&sobject=Account&sobject=Contact. When an sobject limit is specified using sobject.limit=value, such as Account.limit=10, this parameter is ignored for that object.|
|division|string|Single value. Filters search results based on the division field. For example in the GET method, division=global. Specify a division by its name rather than ID. All searches within a specific division also include the global division.|
|fields|string[]|Array of one or more fields to return in the response for each sobjects specified. At least one sobjects must be specified at the global level. For example:|
|||{ "q":"Acme", "fields":["Id", "Name", "Phone"], "sobjects":[{"name": "Account"}, {"name": "Contact", "fields":["Id", "FirstName", "LastName"]}, {"name": "Lead"}] }|
|||The global fields parameter is overridden when sobjectsFilter[] fields are specified. Such as, in the previous example, Id, FirstName, and LastName is returned for Contact instead of the global fields of Id, Name and Phone. If unspecified, then the search results contain the IDs of records matching all fields for the specified object. Functions The following optional functions can be used within the fields parameter.|


-----

|Name|Type|Description|
|---|---|---|
|||• toLabel: Translates response field value into the user’s language. This function requires extra setup. For example: { ... "sobjects":[ {"name": "Lead", "fields":["Id", "toLabel(Status)"]}, ... } • convertCurrency: Converts response currency fields to the user’s currency. This function requires extra setup. Multi-currency must be enabled in the org. For example: { ... "sobjects":[ {"name": "Opportunity", "fields":["Id", "convertCurrency(Amount)"]}] ... } • format: Applies localized formatting to standard and custom number, date, time, and currency fields. For example: { ... "sobjects":[ {"name": "Opportunity", "fields":["Id", "format(Amount)"]}] ... } Aliasing is supported within fields for toLabel, convertCurrency, and format. In addition, aliasing is required when the query includes the same field multiple times. For example:|
|||{ ... "sobjects":[ {"name": "Opportunity", "fields":["Id", "format(Amount) AliasAmount"]}] ... }|
||||
|in|string|Scope of fields to search. If you specify one or more scope values, the fields are returned for all found objects. Use one of the following values: • ALL • NAME • EMAIL • PHONE • SIDEBAR|


-----

|Name|Type|Description|
|---|---|---|
|||This clause doesn't apply to articles, documents, feed comments, feed items, files, products, and solutions. If any of these objects are specified, the search isn’t limited to specific fields; all fields are searched.|
|metadata|string|Specifies if metadata should be returned in the response. No metadata is returned by default. To include metadata in the response, use the LABELS value, which returns the display label for the fields returned in search results. For example: ?q=Acme&metadata=LABELS|
|netWorkIds|string[]|Filters search results by an array. A network ID represents the Experience Cloud site ID.|
|offset|string|Single value. The starting row offset into the result set returned. The maximum offset is 2000. Only one sobject can be specified when using this parameter.|
|overallLimit|string|Single value. The maximum number of results to return across all sobject parameters specified. The maximum overallLimit is 2000.|
|pricebookId|string|Single value. Filters product search results by a price book ID for only the Product2 object. The price book ID must be associated with the product that you’re searching for. For example, ?q=laptop&sobject=product2&pricebookId=01sxx0000002MffAAE|
|snippet|string|The target length (maximum number of snippet characters) to return in Salesforce Knowledge article, case, case comment, feed, feed comment, idea, and idea comment search results. The snippet parameter displays contextual excerpts and highlights the search term for each article in the search results. Snippet results are used to differentiate matches to the search term in article search results. The target length can be from 50 to 1000 characters. Snippet and highlights are generated from email, text, and text area (long and rich) fields. Snippets aren’t displayed for partially matching searches or if the user doesn’t have access to the field that contains the snippet. Snippets are only displayed when 20 or fewer results are returned on a page. At least one of the following sobject values must be specified. • To search a specific article type, use the article type name with the suffix __kav. • To search all article types, use KnowledgeArticleVersion. • To search case, case comment, feed, feed comment, idea, and idea comment types, use Case, CaseComment, FeedItem, FeedComment, Idea, and IdeaComment. For example, q=tourism&sobject=Case&snippet=500.|


-----

|Name|Type|Description|
|---|---|---|
|sobjects|sobjectsFilter[]|Objects to return in the response. Must contain valid object types. Use with the required parameters. For example:|
|||{ "q":"Acme", "fields":["id", "title"], "sobjects":[{"name":"Solution__kav", "where":"language='en_US' and publishstatus='draft'"}, {"name":"FAQ__kav", "where":"language='en_US' and publishstatus='draft'"}] }|
|||If unspecified, then the search results contain the IDs of all objects.|
|spellCorrection|boolean|Specifies whether spell correction is enabled for a user’s search. When set to true, spell correction is enabled for searches that support spell correction. The default value is true. For example: q=Acme&sobject=Account&Account.fields=id&spellCorrection=true|
|updateTracking|string|Specifies a value of true to track keywords that are used in Salesforce Knowledge article searches only. If unspecified, the default value of false is applied.|
|updateViewStat|string|Specifies a value of true to update an article’s view statistics. Valid only for Salesforce Knowledge article searches. If unspecified, the default value of false is applied.|


`dataCategoriesFilter[]` **Parameters**
Parameters must be specified in the order presented in the table (groupName, `operator,` `categories).`

|Name|Type|Description|
|---|---|---|
|groupName|string|The name of the data category group to filter by.|
|operator|string|Valid values: • ABOVE • ABOVE_OR_BELOW • AT • BELOW|
|categories|string[]|The name of the categories to filter by.|


-----

`sobjectsFilter[]` **Parameters**

**Name** **Type** **Description**

`fields` string[]

`limit` string

`name` string Name of the

`orderBy` string

For example:
```
            {
            ...
            ...
            }

```
**•** `ASC`

**•** `DESC`

**•**

**•**

`where` string

For example,

##### Example

**Example Request Body**

|Name|Type|Description|
|---|---|---|
|fields|string[]|Array of one or more fields to return in the response for the sobject.|
|limit|string|Specify the maximum number of rows that are returned for the sobject.|
|name|string|Name of the sobject to return in the response.|
|orderBy|string|Controls the field order of the results using the following syntax "orderBy" : "field {ASC|DESC} [NULLS_{FIRST|LAST}]" For example:|
|||{ ... "sobjects":[ {"name": "Account", "fields":["Id", "name"], "orderBy": "Name DESC Nulls_last"}] ... }|
|||• ASC: ascending. Default. • DESC: descending. • NULLS_FIRST: Null records at the beginning of the results. Default. • NULLS_LAST: Null records at the end of the results.|
|where|string|Filter search results for this object by specific field values. For example, where : conditionExpression. Here the conditionExpression of the WHERE clause uses the following syntax: fieldExpression [logicalOperator fieldExpression2 ... ]. Add multiple field expressions to a condition expression by using logical and comparison operators.|


-----
