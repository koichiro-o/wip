#### AuthConfigProviders

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The organization type for this object.

**•** `Org (includes custom domains)`

**•** `Community`

**•** `Site`

**•** Portal

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**

The login URL of the organization for this AuthConfig object. Each URL has only
one associated AuthConfig object.


Represents an authentication provider that’s configured in an organization. AuthConfigProviders is a child of the AuthConfig object. This
object is available in API version 32.0 and later.

This object links the authentication configuration for an organization to the Auth Provider through the AuthOptionsAuthProvider
[field of the AuthConfig object. The login page of a My Domain or Experience Cloud site can allow multiple SAML configurations and](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_objects_authconfig.htm)
multiple authentication providers. These configurations can be set to show up as buttons on the login page. Each configuration has an
AuthConfigProvider object. For more information about how to display these configurations on the login page, see these resources in
Salesforce Help.

**•** [My Domain: Add Identity Providers to the My Domain Login Page](https://help.salesforce.com/s/articleView?id=sf.domain_name_login_id_prov.htm&language=en_US)

**•** [Experience Cloud: Configure Your Login Page](https://help.salesforce.com/s/articleView?id=sf.external_identity_login_pages_configure.htm&language=en_US)

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
You must have “View Setup and Configuration” permission to view the settings.


-----

##### Fields

**Field Name**
```
AuthConfigId
AuthProviderId
