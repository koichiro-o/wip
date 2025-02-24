#### OauthCustomScope

Represents a permission defining the protected data that a connected app can access from an external entity when Salesforce is the
OAuth authorization provider.

An OAuth custom scope tells an external entity about a connected app’s permissions to access protected data. The OAuth custom scope
that you create in your Salesforce org corresponds to the same custom scope defined in your external entity, and assigned to the resource.

For example, you define an Order Status custom scope in your external entity that allows access to customer order status data in your
order system’s API. In Salesforce, you create an OAuth custom scope that you also name Order Status. You assign this custom scope to
the connected app requesting access to the order status API. When the external entity receives the connected app’s request to access
a customer’s order status, it validates the connected app’s access token and Order Status scope. With a successful validation, the app
can access the customer order status information in the order system’s API.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
You must have the “Manage Connected Apps” permission to access this object.

##### Fields

```
Description

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The description of the permission provided to the connected app by the scope.
The custom scope’s description must be unique, can only include alphanumeric
characters, and can be up to 60 characters long.

You can enter a custom label in place of a description. An advantage of using a
custom label is that you can maintain reusable text in a single location and
[translate the text into multiple languages. See Custom Labels.](https://help.salesforce.com/articleView?id=cl_about.htm&language=en_US)

Note: The description formatting requirements that apply to custom
scopes also apply to custom labels.


-----

```
DeveloperName
IsPublic
Language
MasterLabel
NamespacePrefix

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Use when referring to the OAuth custom scope from a program. This label must
be unique, and can include only alphanumeric characters and underscores.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the object is included in the connected app’s OpenID Connect
[discovery endpoint. For more information, see OpenID Connect Discovery](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)
[Endpoint.](https://help.salesforce.com/articleView?id=remoteaccess_using_openid_discovery_endpoint.htm&language=en_US)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Indicates the default language defined for the developing org.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The master label for the custom scope record. This label must be unique, and
can include only alphanumeric characters and underscores.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix for an OAuth custom scope that's been installed as part
of a second-generation managed package. If the custom scope isn't packaged,
this value is empty. This field is available in API version 61.0 and later.


-----
