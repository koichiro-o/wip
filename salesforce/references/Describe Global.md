### Describe Global

Lists the available objects and the associated metadata. This resource returns both custom and standard objects.

In addition, it provides the org encoding, as well as the maximum batch size permitted in queries. For more information on encoding,
[see Internationalization and Character Sets.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api.meta/api/implementation_considerations.htm#sforce_api_other_internationalization)

You can use the `If-Modified-Since` or `If-Unmodified-Since` header with this resource. If you use the
`If-Modified-Since` header and no available object’s metadata has changed since the provided date, a 304 Not Modified
status code is returned with no response body.

Note: The If-Modified-Since and If-Unmodified-Since headers check for more than object-specific metadata
changes. They also check for org-wide events, such as changes to permissions, profiles, or field labels.

#### Syntax

**URI**
```
  /services/data/vXX.X/sobjects/

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
If-Modified-Since
If-Unmodified-Since

```

An optional header specifying a date and time. The request returns records that have
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z. For example:`
```
If-Modified-Since: Mon, 30 Nov 2020 08:34:54 MST.

```
An optional header specifying a date and time. The request returns records that haven’t
been modified after that date and time.

The format is `EEE, dd MMM yyyy HH:mm:ss z. For example:`
```
If-Unmodified-Since: Mon, 30 Nov 2020 08:34:54 MST.

```

-----

#### Example

See Get a List of Objects.

SEE ALSO:

Conditional Request Headers
