### Support Knowledge with REST API

Knowledge Support REST APIs allow both authorized and guest users to retrieve the user’s visible data categories and their associated
articles. This resource is available in REST API version 38.0 and later.

Authenticated users need the `UserProfile.apiEnabled` permission, Knowledge enabled in the organization, read rights on
the article type, and any other knowledge specific permission or preference that controls visibility to articles.

Guest users need the `Guest Access to the Support API` preference enabled on the relevant Site, Knowledge enabled in
the organization, and read rights on the article type and article channel that controls the visibility for guest users.

#### Syntax

**URI**
```
  /services/data/vXX.X/support

```
**Method**
GET

**Formats**
JSON, XML

**Authentication**
```
  Authorization: Bearer token

#### Example

```
**Example Response Body**
```
  {
  "dataCategoryGroups" : "/services/data/vXX.X/support/dataCategoryGroups",
  "knowledgeArticles" : "/services/data/vXX.X/support/knowledgeArticles"
  :
  }

```
IN THIS SECTION:

Data Category Groups
Get data category groups that are visible to the current user. This resource is available in REST API version 38.0 and later.

Data Category Detail
Gets data category details and the child categories by a given category. This resource can be used in API version 38.0 and later.


-----

Articles List
Get a page of online articles for the given language and category through either search or query. This resource is available in REST
API version 38.0 and later.

Articles Details
Gets all online article fields, accessible to the user. This resource is available with article IDs in REST API version 38.0 and later, and
this resource is available with article URL names in version 44.0 and later.

#### Data Category Groups

Get data category groups that are visible to the current user. This resource is available in REST API version 38.0 and later.

Salesforce Knowledge must be enabled in your organization. This resource can be used in API version 38.0 and later. Use the language
[code format used in Which Languages Does Salesforce Support?.](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)

Only the user’s visible data categories are returned. A user might be able to see several sub trees in the category group, therefore, the
top categories that are visible to the user in each group are returned.

##### Syntax

**URI**
```
  /services/data/vXX.X/support/dataCategoryGroups

```
**Method**
GET

**Formats**
JSON, XML

**Authentication**
```
  Authorization: Bearer token

```
**HTTP headers**
**Accept: Optional. Can be either** `application/json` or `application/xml.`

**Accept-language: Optional. Language to translate the categories. Any ISO-639 language abbreviation, and an ISO-3166 country**
code subtag in the HTTP Accept-Language header. Only one language accepted. If no language specified, the non-translated labels
are returned.

**Input:**

string `sObjectName: Required.` `KnowledgeArticleVersion` only.

boolean `topCategoriesOnly: Optional. Defaults to true`

**•** True returns only the top level categories.

**•** False returns the entire tree.

Note: All the input parameters are case-sensitive.

**Output:**
A list of the active data category groups that are visible to the current user in the site context. Returns id, name, label, and their top
level categories or the entire data category group tree that are visible to the current user. The labels must be translated to the given
language if they are available.

**•** **Data Category Group List**


-----

This payload lists the active root Data Category Groups that can be used in other requests to return the data categories and
articles related to it.
```
    {
      "categoryGroups": [ Data Category Group, ....],
    }

```
Note: Returns only the active groups that are associated to the given entity (by `sObjectName). Only`
`KnowledgeArticleVersion` is supported.

**•** **Data Category Group**

This represents an individual data category group, and its root category.
```
    {
      "name": String, // the unique name of the category group
      "label": String, // returns the translated version if it is available
      "objectUsage" : String, // currently only "KnowledgeArticleVersion" is available.
      "topCategories": [ Data Category Summary, ....]
    }

```
**•** **Data Category Summary**

This provides a summary of data category information. The Summary and Detail responses share common properties, with the
goal of providing only as much information as is necessary from associated resources.
```
    {
      "name": String, // the unique name of the category
      "label": String, // returns the translated version if it is available
      "url": URL, // the url points to the data category detail API
    "childCategories": [ Data Category Summary, ....] // null if topCategoriesOnly is
    true
    }

```
Note: The URL property is a pre-calculated path to the unique resource representing this data category, in this case it is
a Data Category Detail API.

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/support/dataCategoryGroups?sObjectName=KnowledgeArticleVersion
   -H "Authorization: Bearer token"

```
**Example Response Body**


-----

#### Data Category Detail

Gets data category details and the child categories by a given category. This resource can be used in API version 38.0 and later.

[Salesforce Knowledge must be enabled in your organization. Use the language code format used in Which Languages Does Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)
_[Support?.](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)_

##### Syntax

**URI**
```
  /services/data/vXX.X/support/dataCategoryGroups/group/dataCategories/category

```
**Method**
GET

**Formats**
JSON, XML

**Authentication**
```
  Authorization: Bearer token

```
**HTTP headers**
**Accept: Optional. Can be either** `application/json` or `application/xml.`

**Accept-language: Optional. Language to translate the categories. Any ISO-639 language abbreviation, and an ISO-3166 country**
code subtag in the HTTP Accept-Language header. Only one language accepted. If no language specified, the non-translated labels
are returned.

**Input:**

string `sObjectName: Required.` `KnowledgeArticleVersion` only.

**Output:**
Details of the category and a list of child categories (name, label, etc.).

**•** **Data Category Detail**


-----

Used for situations where the hierarchical representation of data categories is important. The child property contains a list of
child data categories.
```
    {
      "name": String, // the unique name of the category
      "label": String, // returns the translated version if it is available
      "url": URL,
      "childCategories": [ Data Category Summary, ....],
    }

```
Note: If the category isn’t visible to the current user the return is empty.

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/support/dataCategoryGroups/Doc/dataCategories/All?sObjectName=KnowledgeArticleVersion
   -H "Authorization: Bearer token"

```
**Example Response Body**
```
  {
   "childCategories" : [ {
    "childCategories" : null,
    "label" : "Help",
    "name" : "Help",
    "url" :
  "/services/data/v62.0/support/dataCategoryGroups/Doc/dataCategories/Help?sObjectName=KnowledgeArticleVersion"
   }, {
    "childCategories" : null,
    "label" : "QA",
    "name" : "QA",
    "url" :
  "/services/data/v62.0/support/dataCategoryGroups/Doc/dataCategories/QA?sObjectName=KnowledgeArticleVersion"
   } ],
   "label" : "All",
   "name" : "All",
   "url" :
  "/services/data/v62.0/support/dataCategoryGroups/Doc/dataCategories/All?sObjectName=KnowledgeArticleVersion"
  }

#### Articles List

```
Get a page of online articles for the given language and category through either search or query. This resource is available in REST API
version 38.0 and later.


-----

##### Syntax

**URI**
```
  /services/data/vXX.X/support/knowledgeArticles

```
**Method**
GET

**Formats**
JSON, XML

**Authentication**
```
  Authorization: Bearer token

```
**HTTP headers**
**Accept: Optional. Can be either** `application/json` or `application/xml.`

**Accept-language: Required. The article must be an active language in the user’s organization**

**•** If the language code isn’t valid, an error message is returned: “The language code is not valid or not supported by Knowledge.”

**•** If the language code is valid, but not supported by Knowledge, then an error message is returned: “Invalid language code. Check
that the language is included in your Knowledge language settings."

**Input:**

string `q: Optional, Performs an SOSL search. If the query string is null, empty, or not given, an SOQL query runs.`

The characters `?` and `*` are used for wildcard searches. The characters `(,` `), and` `"` are used for complex search terms. See
[https://developer.salesforce.com/docs/atlas.en-us.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_find.htm.](https://developer.salesforce.com/docs/atlas.en-us.252.0.soql_sosl.meta/soql_sosl/sforce_api_calls_sosl_find.htm)

string `channel: Optional, defaults to user’s context. For information on channel values, see Valid` `channel` values.

**•** **App: Visible in the internal Salesforce Knowledge application**

**•** **Pkb: Visible in the public knowledge base**

**•** **Csp: Visible in the Customer Portal**

**•** **Prm: Visible in the Partner Portal**

string `categories` in map json format `{“group1”:”category1”,”group2”:”category2”,...} )`

Optional, defaults to None. Category group must be unique in each group:category pair, otherwise you get
```
  ARGUMENT_OBJECT_PARSE_ERROR. There is a limit of three data category conditions, otherwise you get
  INVALID_FILTER_VALUE.

```
string `queryMethod values are:` `AT, BELOW, ABOVE, ABOVE_OR_BELOW. Only valid when categories are specified,`
defaults to ABOVE_OR_BELOW.

string `sort: Optional, a sortable field name` `LastPublishedDate, CreatedDate, Title, ViewScore. Defaults`
to `LastPublishedDate` for query and relevance for search.

Note: When sorting on `ViewScore` it is only available for query, not search, and no pagination is supported. You only get
one page of results.

string `order: Optional, either ASC or DESC, defaults to DESC. Valid only when sort is valid.`

integer `pageSize: Optional, defaults to 20. Valid range 1 to 100.`

integer `pageNumber : Optional, defaults to 1.`

**Output:**
A page of online articles in the given language and category visible to the current user.

**•** **Article Page**


-----

A page of articles. The individual entries are article summaries so the size can be kept at a minimum.
```
  {
    "articles": [ Article Summary, … ], // list of articles
      "currentPageUrl": URL, // the article list API with current page number
       "nextPageUrl": URL, // the article list API with next page number,
      which can be null if there are no more articles.
      "pageNumber": Int // the current page number, starting at 1.
    }

```
Note: The API supports paging. Each page of responses includes a URL to its page, as well as the URL to the next page
of articles.

Note: if the user input parameter has the default value, the API does not show this parameter in either
`currentPageUrl` or `nextPageUrl.`

**•** **Article Summary**

A summary of an article used in a list of article responses. It shares similar properties to the Article Detail representation, as one
is a superset of the other.
```
  {
      "id": Id, // articleId
      "articleNumber": String,
     "articleType": String, // apiName of the article type, available in API v44.0
   and later
      "title": String,
      "urlName": String, // available in API v44.0 and later
      "summary": String,
      "url": URL, // to the Article Detail API
      "viewCount": Int, // view count in the interested channel
     "viewScore": double (in xxx.xxxx precision), // view score in the interested
   channel.
      "upVoteCount": int, // up vote count in the interested channel.
      "downVoteCount": int, // down vote count in the interested channel.
      "lastPublishedDate": Date // last publish date in ISO8601 format
      "categoryGroups": [ Data Category Group, …. ]}

```
The “url” property always points to the Article Details resource endpoint. For information on valid channel values, see the channel
parameter description

**•** **Data Category Group**

An individual data category group, its root category, and a list of selected data categories in the group.
```
  {
      "groupName": String, // the unique name of the category group
      "groupLabel": String, // returns the translated version
      "selectedCategories": [ Data Category Summary, … ]
    }

```
**•** **Data Category Summary**

Provides a summary of data category information. The Summary and Detail responses share common properties.


-----

Note: The outputs of Data Category Group and Data Category Summary in Article List API are different from the Data
Category Groups API.

##### Example

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/support/knowledgeArticles?sort=ViewScore&channel=Pkb&pageSize=3
    HTTP Headers:
       Content-Type: application/json; charset=UTF-8
       Accept: application/json
       Accept-Language: en-US

```
**Example Response Body**


-----

##### Usage

Salesforce Knowledge must be enabled in your organization. This resource can be used in API version 38.0 and later. The Custom File
[Field is not supported because it returns a link to a binary stream. Use the language code format used in Which Languages Does Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)
_[Support?.](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)_

##### Valid channel Values

**•** When using the options string `channel, where the matching articles are visible, the following values are valid.`

**–** `App–Visible in the internal Salesforce Knowledge application`

**–** `Pkb–Visible in the public knowledge base`

**–** `Csp–Visible in the Customer Portal`

**–** `Prm–Visible in the Partner Portal`

**•** If `channel` isn’t specified, the default value is determined by the type of user.

**–** `Pkb` for a guest user

**–** `Csp` for a Customer Portal user

**–** `Prm` for a Partner Portal user

**–** `App` for any other type of user

**•** If `channel` is specified, the specified value may be used to retrieve articles.

**–** For guest, Customer Portal, and Partner Portal users, if the specified channel is other than the channel accessible to the user, an
error is returned.

**–** For all users other than guest, Customer Portal, and Partner Portal users, the specified channel value is used.


-----

#### Articles Details

Gets all online article fields, accessible to the user. This resource is available with article IDs in REST API version 38.0 and later, and this
resource is available with article URL names in version 44.0 and later.

Salesforce Knowledge must be enabled in your organization. This resource can be used in API version 38.0 and later. The Custom File
[Field is not supported because it returns a link to a binary stream. Use the language code format used in Which Languages Does Salesforce](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)
_[Support?.](https://help.salesforce.com/apex/HTViewHelpDoc?id=faq_getstart_what_languages_does.htm&language=en_US)_

A lookup custom field is visible to guest users depending on the lookup entity type. For example, User is visible, but Case and Account
are not visible. Following standard fields are not visible to a guest user, even if they are in the layout:

**•** archivedBy

**•** isLatestVersion

**•** translationCompletedDate

**•** translationImportedDate

**•** translationExportedDate

**•** versionNumber

**•** visibleInInternalApp

**•** visibleInPKB

**•** visibleToCustomer

**•** visbileToPartner

##### Valid channel Values

**•** When using the options string `channel, where the matching articles are visible, the following values are valid.`

**–** `App–Visible in the internal Salesforce Knowledge application`

**–** `Pkb–Visible in the public knowledge base`

**–** `Csp–Visible in the Customer Portal`

**–** `Prm–Visible in the Partner Portal`

**•** If `channel` isn’t specified, the default value is determined by the type of user.

**–** `Pkb` for a guest user

**–** `Csp` for a Customer Portal user

**–** `Prm` for a Partner Portal user

**–** `App` for any other type of user

**•** If `channel` is specified, the specified value may be used to retrieve articles.

**–** For guest, Customer Portal, and Partner Portal users, if the specified channel is other than the channel accessible to the user, an
error is returned.

**–** For all users other than guest, Customer Portal, and Partner Portal users, the specified channel value is used.

##### Syntax

**Method**
GET


-----

**Formats**
JSON, XML

**Authentication**
```
  Authorization: Bearer token

```
**Endpoint**
```
  /services/data/vXX.X/support/knowledgeArticles/articleId_or_articleUrlName

```
**HTTP headers**
**Accept: Optional. Can be either** `application/json` or `application/xml.`

**Accept-language: Required. The article must be an active language in the user’s organization**

**•** If the language code isn’t valid, an error message is returned: “The language code is not valid or not supported by Knowledge.”

**•** If the language code is valid, but not supported by Knowledge, then an error message is returned: “Invalid language code. Check
that the language is included in your Knowledge language settings."

**Input:**

string `channel: Optional, defaults to user’s context. For information on channel values, see Valid` `channel` Values.

**•** **App: Visible in the internal Salesforce Knowledge application**

**•** **Pkb: Visible in the public knowledge base**

**•** **Csp: Visible in the Customer Portal**

**•** **Prm: Visible in the Partner Portal**

boolean `updateViewStat: Optional, defaults to true. If true, API updates the view count in the given channel as well as the`
total view count.

boolean `isUrlName: Optional, defaults to false. If true, indicates that the last portion of the endpoint is a URL name instead of an`
article ID. Available in API v44.0 and later

**Output:**
The detailed fields of the article, if the article is online and visible to the current user.

**•** **Article Detail**

Full detail of an article, with complete metadata and layout-driven fields used for display of an article. It includes all the same
properties as an Article Summary representation.


-----

**•** **User Summary**
```
    {
         "id": String
         "isActive": boolean // true/false
         "userName": String // login name
         "firstName": String
         "lastName": String
         "email": String
         "url": String // to the chatter user detail url:
    /services/data/vXX.X/chatter/users/{userId}, for guest user, it will return null.
         }

```
**•** **Article Field**

An individual field of article information, which is listed in an Article Detail in the order required by the administrator’s layout.
```
    {
         "type": Enum, // see the Notes
         "name": String, // In API v43.0 and earlier, the developer name. In
    API v44.0 and later, the API name.
         "label": String, // label
         "value": String,
         }

##### Example

```
**Example Request**


-----

**Example Response Body**


-----

##### Usage
