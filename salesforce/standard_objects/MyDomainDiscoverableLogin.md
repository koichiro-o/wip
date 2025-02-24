#### MyDomainDiscoverableLogin

Represents configuration settings when the My Domain login page type is Discovery. Login Discovery provides an identity-first login
experience, where the login page contains the identifier field only. Based on the identifier entered, a handler determines how to
authenticate the user. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field Name**
```
ApexHandlerId
DeveloperName
ExecuteApexHandlerAsId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the Apex handler that contains the Discovery authentication logic.

This is a relationship field.

**Relationship Name**
ApexHandler

**Relationship Type**
Lookup

**Refers To**
ApexClass

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the handler. Requires Manage User permission.

This is a relationship field.

**Relationship Name**
ExecuteApexHandlerAs


-----

```
Language
MasterLabel
UsernameLabel

```

**Relationship Type**
Lookup

**Refers To**
User

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the MasterLabel.

Possible values are:

**•** `da` (Danish)

**•** `de` (German)

**•** `en_US (English)`

**•** `es (Spanish)`

**•** `es_MX (Spanish - Mexican)`

**•** `fi (Finnish)`

**•** `fr` (French)

**•** `it (Italian)`

**•** `ja (Japanese)`

**•** `ko` (Korean)

**•** `nl_NL (Dutch)`

**•** `no (Norwegian)`

**•** `pt_BR (Portuguese - Brazilian)`

**•** `ru (Russian)`

**•** `sv (Swedish)`

**•** `th` (Thai)

**•** `zh_CN (Chinese - Simplified)`

**•** `zh_TW (Chinese - Traditional)`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the action link group template.

**Type**
string


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Login prompt on login page when the My Domain login page type is Discovery.
It supports localization with custom labels.

##### Usage

Use this object to access the My Domain Login Discovery Page, which is a login page type that prompts users to identity themselves
with an email address, phone number, or custom identifier. My Domain Login Discovery performs an interview-based login process,
where users are first prompted to provide identity and then authenticated. For example, users receive a verification code that they enter
to complete the login process.
