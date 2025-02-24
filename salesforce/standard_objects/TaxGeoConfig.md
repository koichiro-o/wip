#### TaxGeoConfig

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Apex namespace prefix of the API used for the tax engine. In a packaging context, a
namespace prefix is a one to 15-character alphanumeric identifier that distinguishes your
package and its contents from packages of other developers on AppExchange.


Represents a tax configuration associated with a GeoCountry. This object is available in API version 57.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The TaxGeoConfig object is available if B2B Commerce or D2C Commerce is enabled.

##### Fields

```
GeoCountryId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The GeoCountry associated with the TaxGeoConfig.

This field is a relationship field.

**Relationship Name**
GeoCountry

**Relationship Type**
Lookup

**Refers To**
GeoCountry


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId
RoundingStrategyType

```

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

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the TaxGeoConfig.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The owner of the TaxGeoConfig record. By default, the asset owner is the user who created
the record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
picklist


-----

**Properties**
Create, Defaulted on create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Specifies the tax rounding strategy associated with the TaxGeoConfig.

Possible values are:

**•** `Rounding Down`

**•** `Rounding Off`

**•** `Rounding Up`

The default value is `Rounding Off.`

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**TaxGeoConfigShare on page 66**
Sharing is available for the object.

SEE ALSO:

GeoCountry
