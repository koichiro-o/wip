### Recently Viewed Items

```
Gets the most recently accessed items that were viewed or referenced by the current user. Salesforce stores information about record
views in the interface and uses it to generate a list of recently viewed and referenced records, such as in the sidebar and for the
auto-complete options in search.


-----

This resource only accesses most recently used item information. If you want to modify the list of recently viewed items, you must update
recently viewed information directly by using a SOQL Query with a FOR VIEW or `FOR REFERENCE` clause.

Note: The API response filters and displays recent records based on the permissions of the token or session ID user.

**URI**
```
  /services/data/vXX.X/recent

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

```
  limit

#### Example

```

An optional limit that specifies the maximum number of records to be returned. If this
parameter is not specified, the default maximum number of records returned is the
maximum number of entries in RecentlyViewed, which is 200 records in total.



**•** For an example of retrieving a list of recently viewed items, see View Recently Viewed Records on page 81.

**•** For an example of setting records as recently viewed, see Mark Records as Recently Viewed on page 82.
