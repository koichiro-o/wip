#### SiteDomain

SiteDomain is a read-only object, and a one-to-many replacement for the Site.TopLevelDomain field. This object is available in API version
21.0, and has been deprecated as of API version 26.0. In API version 26.0 and later, use the Domain and DomainSite objects instead.

To access this object, Digital Experiences, Salesforce Sites, or Site.com must be enabled.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the View Setup and Configuration permission.

##### Fields

```
Domain

```

**Type**
url

**Properties**
Filter, Sort


-----

```
SiteId
DomainType

##### Usage

```

**Description**
The branded custom Web address within the global namespace identified by
this domain's type. In the Domain Name System (DNS) global namespace, this
field is the custom Web address that you registered with a third-party domain
name registrar. The custom Web address can be used to access the site of this
domain.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the associated Site.

**Type**
picklist

**Properties**
Filter, Group, Sort, Nillable

**Description**
The global namespace that this custom Web address belongs to. This value is
set to DNS for custom Web addresses in the global DNS. This field is available in
version 24.0 of the API.


Use this read-only object to query the domains that are associated with each site in your organization.
