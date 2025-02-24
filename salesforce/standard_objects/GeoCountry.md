#### GeoCountry

```


**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the object that owns the topic.

This field is a polymorphic relationship field.

**Relationship Name**
Parent

**Refers To**
GenAiPlannerDefinition, GenAiPlannerFunctionDef

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The only supported value is `Topic.`

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
A specific job description for a topic.


Represents a country. This object is available in API version 56.0 and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The GeoCountry object is available if B2B Commerce or D2C Commerce is enabled.

##### Fields

```
Description
IsoCode
LastReferencedDate
LastViewedDate

```

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A brief description of this record.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort

**Description**
Two-letter ISO code of the country as defined in the org’s State-Country picklist. This field is
unique within your organization

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed data in this record, a record related to
this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this value is null,
it's possible the user accessed data in this record or list view but didn't view it directly.


-----

```
Name
OwnerId

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
The name of the country that corresponds with the ISO code.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the GeoCountry record. By default, the asset owner is the user who created
the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**GeoCountryOwnerSharingRule on page 64**
Sharing rules are available for the object.

**GeoCountryShare on page 66**
Sharing is available for the object.

SEE ALSO:

GeoState

TaxGeoConfig
