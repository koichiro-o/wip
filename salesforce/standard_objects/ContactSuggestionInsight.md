#### ContactSuggestionInsight

Represents a suggestion for a new contact record. Available in API versions 45.0 and later.

##### Supported Calls
```
describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
To add or decline contact suggestions, users need a Sales Cloud Einstein license and edit access on accounts. As of the Spring ’20 release,
Pardot and Sales Engagement users no longer have access to this object.

##### Fields

```
AccountId

```

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the related account.


-----

```
Address
City
ContactTitle
Country
CreatedRecordId
CurrencyIsoCode

```

**Type**
address

**Properties**
Filter, Nillable

**Description**
The address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The city of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The title of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The country of the suggested contact.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the created contact record.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort


-----

```
Division
Email
FirstName
GeocodeAccuracy
LastName

```

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
The division of the suggested contact.

**Type**
email

**Properties**
Filter, Group, Nillable, Sort

**Description**

The email address of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The first name of the suggested contact.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Accuracy level of the geocode for the address. See Compound Field
Considerations and Limitations for details on geolocation compound fields.

Note: This field is available in the API only.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The last name of the suggested contact.


-----

```
LastOperationUserId
LastReferencedDate
LastViewedDate
Latitude
Longitude
Phone

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who last performed a related operation.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related
to this record, or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last viewed this record or list view. If this
value is null, the user might have only accessed this record or list view
(LastReferencedDate) but not viewed it.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with Longitude to specify the precise geolocation of an
address.

**Type**
double

**Properties**
Filter, Nillable, Sort

**Description**
Used in conjunction with `Latitude to specify the precise geolocation of an`
address.

**Type**
phone


-----

```
PostalCode
RationaleLabel
State
Status
Street

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The phone number of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The postal code of the suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The reason why this entry is a suggested contact.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The state of the suggested contact.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The status of the suggested contact. Possible values include:

**•** New

**•** Pending

**•** Added

**•** Declined

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort


-----

**Description**
The street of the suggested contact.

##### Usage

This object is read-only and isn’t supported in workflows, triggers, process builder, or Visualforce pages.
