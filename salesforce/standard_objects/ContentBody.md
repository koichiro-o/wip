#### ContentBody

```

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language for this document. This field defaults to the user's language unless the org is
multi-language enabled. Specifies the language of the labels returned. The value must be a
valid user locale (language and country), such as `de_DE` or `en_GB. For more information`
on locales, see the `Language` field on the CategoryNodeLocalization object.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The label for the asset file. This internal label doesn’t get translated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```

Represents the body of a file in Salesforce CRM Content or Salesforce Files. This object is available in API version 40.0 and later.

##### Supported Calls
```
describeSObjects()

 Special Access Rules

```
Cannot be queried, inserted, updated, or deleted directly.


-----

##### Fields

**Field**
```
Id

##### Usage

```

**Type**
ID

**Properties**
, Filter, Group, idLookup, Sort

**Description**
ID of the file body.


ContentBody is intended for internal Salesforce use. If you need to access the file content body, please use ContentVersion.
