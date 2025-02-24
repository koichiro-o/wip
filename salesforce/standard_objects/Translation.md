#### Translation

```

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The access time of Salesforce services in GMT. For example,
```
  2020-01-20T19:12:26.965Z. Milliseconds are the most granular setting.

```
**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The time at which the Transaction Security event was generated in ISO8601-compatible
format. For example: 2015-07-27T11:32:59.555Z.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URI of the page that’s receiving the request. For example: `/home/home.jsp.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The 15-character ID of the user who’s using Salesforce services through the UI or the API.
For example: `00530000009M943.`


The Translation object represents the languages enabled for translation in your Salesforce org. This object is available in API version 47.0
and later.

##### Supported Calls
```
create(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

**•** Your organization must be using Enterprise, Performance, Unlimited, or Developer edition.

**•** To view this object, you must have the “View Setup and Configuration” permission.

**•** To use the `create(),` `update(), and` `upsert()` calls, Translation Workbench must be enabled in your org.

**•** To manage translations, Translation Workbench must be enabled in your org. Specify translators for each language through the
Translation Language Settings Setup page.

##### Fields

```
CanManage
IsActive
Language
