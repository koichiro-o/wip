### sObjects Suggested Articles by ID

```
When you enter an article ID, you can retrieve records that offer similar information as the ID you entered. This resource is available in
REST API version 30.0 and later.

Salesforce Knowledge must be enabled in your organization. The user must have the “View Articles” permission enabled. The articles
suggested include only the articles the user can access, based on the data categories and article types the user has permissions to view.


-----

Articles are suggested based on a relevance algorithm. The `suggestedArticles` resource is designed to get the IDs of articles
relevant to a case, work order, or work order line item. It’s intended to be used with other services that than use the IDs to get article
data for display.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/sObject/ID/suggestedArticles?language=articleLanguage

```
**Formats**
JSON, XML

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
None required

**Request parameters**

```
articleTypes

```

Optional. Three-character ID prefixes indicating the desired article types. You can specify
multiple values for this parameter in a single REST call, by repeating the parameter
name for each value.For example, articleTypes=ka0&articleTypes=ka1.


`categories` Optional. The name of the data category group and the data category API name (not
category title) for desired articles. The syntax is
```
                 categories={"Group":"Category"}. Characters in the URL might need

```
to be encoded. For example:
```
                  categories=%7B%22Regions%22%3A%22Asia%22%2C%22
                  Products%22%3A%22Laptops%22%7D

```
The same data category group can’t be specified more than one time. However, you
can specify multiple data category group and data category pairs. For example,
```
                 categories={"Regions":"Asia","Products":"Laptops"}.

```
```
description

```

Text of the description. Valid only for new records without an existing ID and required
if subject is null. Article suggestions are based on common keywords in the subject,
description, or both.


`language` Required. Language that the article is written in.

`limit` Optional. Specifies the maximum number of suggested articles to return.

`publishStatus` Optional. The article’s publication status. Valid values:

**•** `Draft–Not published`

**•** `Online–Published in Salesforce Knowledge`

**•** `Archived`


-----

```
subject

```

Text of the subject. Valid only for new records without an existing ID and required if
`description` is null. Article suggestions are based on common keywords in the
subject, description, or both.


`topics` Optional. The topic of returned articles. For example:
```
                  topics=outlook&topics=email.

```
`validationStatus` Optional. The validation status of returned articles.

#### Example

**Example Response Body**
```
  [ {
   "attributes" : {
    "type" : "KnowledgeArticleVersion",
    "url" : "/services/data/v62.0/sobjects/KnowledgeArticleVersion/ka0D00000004CcQ"
   "Id" : "ka0D00000004CcQ"
  }, {
   "attributes" : {
    "type" : "KnowledgeArticleVersion",
    "url" : "/services/data/v62.0/sobjects/KnowledgeArticleVersion/ka0D00000004CXo"
   },
   "Id" : "ka0D00000004CXo"
  } ]
