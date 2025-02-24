#### ContactPointAddress

Represents a contact’s billing or shipping address, which is associated with an individual or person account. This object is available in
API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Fields

```
```
ActiveFromDate
ActiveToDate

```

**Type**
date

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address became active.

**Type**
date


-----

```
Address
AddressFirstName
AddressLastName
AddressMiddleName
AddressType

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The date when the contact’s address is no longer active.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The full address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name associated with the address.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Last name associated with the address.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Middle name associated with the address.

This field is available in API version 57.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
BestTimeToContactEndTime
BestTimeToContactStartTime
BestTimeToContactTimezone
City
CompanyName

```

**Description**
Indicates the type of address.

Possible values are:

**•** `Billing`

**•** `Shipping`

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latest time to contact the individual.

**Type**
time

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The earliest time to contact the individual.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The timezone applied to the best time to contact the individual.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Company name associated with the address.

This field is available in API version 57.0 and later.


-----

```
ContactPointPhoneId
Country
GeocodeAccuracy

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Represents the primary phone number associated with this address.

This is a relationship field.

**Relationship Name**
ContactPointPhone

**Relationship Type**
Lookup

**Refers To**
ContactPointPhone

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address country.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The level of accuracy of a location’s geographical coordinates compared with its physical
address. A geocoding service typically provides this value based on the address’s latitude
and longitude coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip`

**•** `NearAddress`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`


-----

```
IsDefault
IsPrimary
IsThirdPartyAddress
LastReferencedDate
LastViewedDate

```


**•** `Zip`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s address is the preferred method of communication (true)
or not (false). The default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether a contact’s address is their primary address (true) or not (false). The
default value is `false.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the address is associated with a third party (true) or not (false). The
default value is `false.`

This field is available in API version 57.0 and later.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last referenced a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, it’s
possible that this record was referenced (LastReferencedDate) and not viewed.


-----

```
Latitude
Longitude
Name
OwnerId
ParentId

```

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Longitude to specify the precise geolocation of the address. Acceptable values
are numbers between –90 and 90 with up to 15 decimal places.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with Latitude to specify the precise geolocation of the address. Acceptable values
are numbers between –180 and 180 with up to 15 decimal places.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Required. The name of the contact point address record.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The ID of the account’s owner associated with this contact.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
PhoneNumber
PostalCode
PreferenceRank
State
Street

```

**Description**
The ID of the contact’s parent record. Only an individual or account can be a contact’s parent.

This is a polymorphic relationship field.

**Relationship Name**
Parent

**Relationship Type**
Lookup

**Refers To**
Account, Individual

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number associated with the address.

This field is available in API version 57.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address postal code.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Preference rank when there are multiple contact point addresses.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address state.

**Type**
textarea


-----

```
UsageType

##### Associated Objects

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Specify the usage type of this address. For instance, whether it’s a work address or a home
address.

Possible values are:

**•** `Home`

**•** `Inactive`

**•** `Temporary`

**•** `Work`


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**ContactPointAddressChangeEvent**

Change events are available for the object.

**ContactPointAddressHistory**

History is available for tracked fields of the object.

**ContactPointAddressShare**

Sharing is available for the object.
