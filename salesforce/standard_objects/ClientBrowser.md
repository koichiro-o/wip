#### ClientBrowser

Represents a cookie added to the browser upon login, and also includes information about the browser application where the cookie
was inserted. This object is available in version 28.0 and later.

##### Supported Calls
```
describeSObjects(), delete(), query(), retrieve()

 Fields

```
```
FullUserAgent
LastUpdate
ProxyInfo

```

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Detailed information about the client (browser). For example, `Mozilla/5.0`
```
  (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.1)
  Gecko/2008070208 Firefox/3.0.1

```
**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Represents the last time the cookie was changed.

**Type**
string


-----

```
UsersId

##### Usage

```

**Properties**
Filter, Nillable, Sort

**Description**
The browser’s current proxy information.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User


At every login, the device the login request is from is checked against the known devices using ClientBrowser. A match means a cookie
was found on the browser that matches an entry in the ClientBrowser table, so the device is known. No match means that no matching
cookie was found, so the device is unknown, and the user is asked to confirm their identity.
