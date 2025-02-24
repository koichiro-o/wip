#### SiteIframeWhitelistUrl

Represents a list of external domains that you allow to frame your Salesforce site or Experience Cloud site pages. This object is available
in API version 44.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. Because changing
terms in our code can break current implementations, we maintained this object’s name.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** Customer Portal users can’t access this object.

**•** To view this object, you must have the “View Setup and Configuration” permission.

##### Fields

```
SiteId
Url

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the site to include in the inline frame.

This is a relationship field.

**Relationship Name**
Site

**Relationship Type**
Lookup

**Refers To**
Site

**Type**
string


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The domain allowed to frame your Salesforce site or Experience Cloud site page.
Accepts these formats: example, example.com, *example.com, and
https://example.com.
