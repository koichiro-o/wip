#### CustomFieldDisplayValue

Stores variation details for the product attribute item view. This object is available in API version 63.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
CustomFieldDisplayValue is available only if the B2B or D2C Commerce license is enabled.


-----

##### Fields

**Field**
```
Color
CurrencyIsoCode
CustomFieldDisplayId
Name
PickListApiValue

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The color variation in hexadecimal value format, for example `#FF0000.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The currency ISO code allowed by the organization. Possible value is:

**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the custom field display that this variation is associated with.

This field is a relationship field.

**Relationship Name**
CustomFieldDisplay

**Refers To**
CustomFieldDisplay

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
Name of the custom field display value.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update


-----

**Description**
The API name of the color variation picklist value, for example, `red_c.`

##### Usage

This object only gets populated when display type in the CustomFieldDisplay object is ColorSwatch.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as
CustomFieldDisplayValue.

**CustomFieldDisplayValueChangeEvent on page 67**
Change events are available for the object.

**CustomFieldDisplayValueFeed on page 54**
Feed tracking is available for the object.

**CustomFieldDisplayValueHistory on page 62**
History is available for tracked fields of the object.
