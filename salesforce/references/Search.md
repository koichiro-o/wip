### Search

```
Executes the specified SOSL search. The search string must be URL-encoded.

[For more information on SOSL see the SOQL and SOSL Reference.](http://www.salesforce.com/us/developer/docs/soql_sosl/index_Left.htm)

#### Syntax

**URI**
```
  /services/data/vXX.X/search/?q=SOSL_searchString

```
**Formats**
JSON, XML

**HTTP Method**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Parameters**

**Parameter** **Description**

`q` A SOSL statement that is properly URL-encoded.


-----

#### Example

See Search for a String on page 66.
