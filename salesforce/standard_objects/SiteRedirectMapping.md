#### SiteRedirectMapping

Represents a site redirect from an external site to an Experience Cloud site. This object is available in API version 52.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
This object is available only if Digital Experiences is enabled for your org and Create and Set Up Experiences is enabled.

##### Fields

```
Action
IsActive

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
The type of the redirect.

Possible values are:

**•** `Permanent`

**•** `Temporary`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the redirect is enabled.

Default value is `false.`


-----

```
IsDynamic
SiteId
Source
Target

##### Usage

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a redirect rule is dynamic.

Default value is `false. This field is available in API version 57.0 and later.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the site for the redirect.

This field is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the site you want to redirect.

**Type**
url

**Properties**
Create, Filter, Sort

**Description**
The URL of the Experience Cloud site you want to users to visit.


If you build a new site on Experience Cloud but you also have an old site on a different platform, ensure that users visit the new site. Use
SiteRedirectMapping to redirect users from the external site to the Experience Cloud site.


-----
