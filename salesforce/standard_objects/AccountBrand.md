#### AccountBrand

Represents the brand details of a Partner Account. This object is available in API version 43.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated() query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if digital experiences is enabled in your org and it has a Partner Community or Customer Community Plus
license.


-----

##### Fields

**Field**
```
AccountId
Address
City
CompanyName
Country
Email

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of the Account. This number is unique within your organization.

**Type**
address

**Properties**
Filter, Nillable

**Description**
The street address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the company associated with the account brand.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the account is physically located.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
GeocodeAccuracy
LastReferencedDate
LastViewedDate
Latitude
LogoId
LogoUrl

```

**Description**
Email address associated with the account.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist Sort, Update

**Description**
Stores data for accurate geocoded location.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
Most recent date viewed.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used along with `Longitude` to specify the precise geolocation of an address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the logo.

**Type**
url

**Properties**
Nillable,


-----

```
Longitude
Name
OwnerId
Phone
PostalCode
State

```

**Description**
URL of the logo. This field is available in API version 44.0 and later.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with `Latitude` to specify the precise geolocation of an address.

**Type**
string

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Required. Name of the account.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Required. ID of the Owner.

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Phone number.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code where the user’s IP address is physically located.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
Street
Website

##### Associated Objects

```

**Description**
The address state.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The address street.

**Type**
url

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Website for the Account Brand.


This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**AccountBrandOwnerSharingRule**

Sharing rules are available for the object.

**AccountBrandShare**

Sharing is available for the object.
