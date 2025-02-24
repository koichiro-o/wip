#### DomainSite

Read-only junction object that joins the Site and Domain objects. This object is available in API version 26.0 and later.

To access this object, Salesforce Sites, Digital Experiences, or Site.com must be enabled. `DomainSite` contains records for domains
that serve your Experience Cloud sites only when enhanced domains are deployed. The system-managed site hostnames for those


-----

Experience Cloud sites end in `.my.site.com. This object doesn’t contain records for legacy domains that serve Experience Cloud`
sites with hostnames that end in `.force.com.`

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
**•** Customer Portal users can’t access this object.

**•** To view this object, you must have either the View Setup and Configuration or Manage Custom Domains permission.

**•** Site.com Publisher users have read-only API access to the Domain and DomainSite objects.

##### Fields

```
DomainId
PathPrefix
SiteId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**

The ID of the associated Domain.

This is a relationship field.

**Relationship Name**
Domain

**Relationship Type**
Lookup

**Refers To**
Domain

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Shows where a site’s root exists on a domain. Can only be set for custom Web
addresses. Always begins with a `/.`

**Type**
reference

**Properties**
Filter, Group, Sort


-----

**Description**

The ID of the associated Site.

This is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

##### Usage

Use this read-only object to query or retrieve information about your sites.
