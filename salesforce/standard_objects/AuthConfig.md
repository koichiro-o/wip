#### AuthConfig

Represents authentication options for My Domain and Experience Cloud site login pages. This object is available in API version 32.0 and
later.

The fields for this object control the options that display on the login page of an org. By default, you have a My Domain and corresponding
login page. If you use Digital Experiences, you can also set up a login page for each of your Experience Cloud sites.

**•** Logging in with a username and password

**•** Using SAML for single sign-on

**•** Authentication provider logins from a third-party service, such as Facebook or Twitter

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
You must have “View Setup and Configuration” permission to view the settings.

##### Fields

```
AuthOptionsAuthProvider

```

**Type**
boolean

**Properties**
Filter


-----

```
AuthOptionsCertificate
AuthOptionsSaml
AuthOptionsUsernamePassword
DeveloperName

```

**Description**

If `true, at least one Auth. Provider is selected to show up on the login page,`
and this object has child AuthConfigProvider objects for each provider.

**Type**
boolean

**Properties**
Filter

**Description**

If `true, certificate-based login displays on the My Domain login page.`

**Type**
boolean

**Properties**
Filter

**Description**

If `true, at least one SAML configuration is selected to show up on the login`
page. If the organization has only one SAML configuration, this value indicates
whether that configuration is selected to show up on the login page. If the
organization has multiple SAML configurations, see the child AuthConfigProvider
objects for each configuration.

**Type**
boolean

**Properties**
Filter

**Description**

If `true, the login option for a username and password appears on the login`
page.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The name of the domain created using My Domain or, for an Experience Cloud
site, a concatenated string of site name_site prefix.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.


-----

```
IsActive
Language
MasterLabel
NamespacePrefix

```

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Whether this configuration is in use.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The language for the organization.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The text that’s used to identify the Visualforce page in Setup.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, NamespacePrefix is set to the namespace
prefix of the org for all objects that support it, unless an object is in an installed
managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the
Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.


-----

```
Type
Url
