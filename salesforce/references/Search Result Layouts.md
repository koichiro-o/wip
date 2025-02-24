### Search Result Layouts

Returns search result layout information for the objects in the query string. For each object, this call returns the list of fields displayed on
the search results page as columns, the number of rows displayed on the first page, and the label used on the search results page.

This call supports bulk fetch for up to 100 objects in a query.

#### Syntax

**URI**
```
  /services/data/vXX.X/search/layout/?q=commaDelimitedObjectList

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```

-----

**Response format**

**Property** **Type** **Description**

`field` String Object and field name formatted with a

period separating. For example:
```
                                   Account.Name.

```
`format` String The type of date field, such as the date only

or date and time. Only date related types
are specified; otherwise, `null.`

`label` String Name as it appears to users

`name` String API name

#### Example

See Get Search Result Layouts for Objects.
