#### LoginGeo

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The category of user license.

Possible values are:

**•** `CsnOnly—Users whose access to the application is limited to Chatter. This user type`
includes Chatter Free and Chatter moderator users.

**•** `CspLitePortal—CSP Lite Portal license. Users whose access is limited because`
they’re organization customers and access the application through a customer portal or
an Experience Cloud site.

**•** `CustomerSuccess—Customer Success license. Users whose access is limited`
because they’re organization customers and access the application through a customer
portal.

**•** `Guest—Users whose access is limited so that your customers can view and interact`
with your site without logging in.

**•** `PowerCustomerSuccess—Power Customer Success license. Users whose access`
is limited because they’re organization customers and access the application through a
customer portal. Users with this license type can view and edit data they directly own
or data owned by or shared with users below them in the customer portal role hierarchy.

**•** `PowerPartner—Power Partner license. Users whose access is limited because they’re`
partners and typically access the application through a partner portal or site.

**•** `SelfService—Users whose access is limited because they’re organization customers`
and access the application through a self-service portal.

**•** `Standard—Standard user license. This user type also includes Salesforce Platform`
and Salesforce Platform One user licenses, and admins for this org.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The username that’s used for login.


Represents the geographic location of the user’s IP address for a login event. Due to the nature of geolocation technology, the accuracy
of geolocation fields (for example, country, city, postal code) may vary. This object is available in API version 34.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

Only users with Manage Users permissions can access this object.

##### Fields

```
City
Country
CountryIso
Latitude
LoginTime

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ISO 3166 code for the country where the user’s IP address is physically located. For more
[information, see Country Codes - ISO 3166](http://www.iso.org/iso/country_codes.htm)

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The latitude where the user’s IP address is physically located.

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
Time of the login attempt, in GMT time zone.


-----

```
Longitude
PostalCode
Subdivision

##### Usage

```

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
The longitude where the user’s IP address is physically located.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code where the user’s IP address is physically located. This value is not localized.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The name of the subdivision where the user’s IP address is physically located. In the U.S., this
value is usually the state name (for example, Pennsylvania). This value is not localized.


The API allows you to do many powerful queries. A few examples are:

**Sample Query** **Query String**

Query showing the country for a login event, where `SELECT Country FROM LoginGeo WHERE Id =`
`Id=LoginGeoId` from AuthSession `'0LE###############'`

Query showing the city and postal code for a login event, where `SELECT City, PostalCode FROM LoginGeo WHERE`
`Id=LoginGeoId` from LoginHistory `Id = '0SO###############'`
