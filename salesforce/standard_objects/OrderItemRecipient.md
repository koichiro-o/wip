#### OrderItemRecipient


**Description**
Numerical rank used to apply promotions in the correct order.

This field is available in API version 52.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Total amount of the adjustment, inclusive of tax. This amount is equal to Amount +
TotalTaxAmount.

This field is available in API version 49.0 and later.

**Type**
currency

**Properties**
Filter, Nillable, Sort

**Description**
Tax on the Amount.


Represents a site, employee, or other entity for which services are being ordered. This includes essential details such as the recipient's
name, contact information, and the specific site or location where the services will be provided. This object is available in API version
62.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

```

-----

##### Fields

**Field**
```
BroadbandConnectionType
LastReferencedDate
LastViewedDate
MaxDownloadSpeed
MaxUploadSpeed
Name

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the broadband connection that's available at the address.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is null, this
record might only have been referenced (LastReferencedDate) and not viewed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum download speed available at the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The maximum upload speed available at the address.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort


-----

```
OrderId
RecipientType
ServiceAddrValidationDate
Service Account

```

**Description**
The name of the customer's site or location.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The order associated with the recipient.

This field is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Master-detail

**Refers To**
Order (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of recipient of the order.

Possible values are:

**•** `Location`

**•** `Subscriber`

The default value is `Location.`

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the address was validated.

**Type**
entityid

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ServiceAddrValidationMsg
ServiceAddrValidationResult
ServiceAddress
ServiceCity
ServiceCountry

```

**Description**
Reference to the Account Entity where the product is used, serviced, or installed.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The message sent after the validation of the address.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the status of the address validation.

Possible values are:

**•** `Fail`

**•** `Partial Success`

**•** `Success`

The default value is `Success.`

**Type**
address

**Properties**
Filter

**Description**
The address where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ServiceGeocodeAccuracy
ServiceLatitude
ServiceLongitude
ServicePostalCode

```

**Description**
The country where the recipient receives the order.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the accuracy level of the geocoded address coordinates.

Possible values are:

**•** `Address`

**•** `Block`

**•** `City`

**•** `County`

**•** `ExtendedZip—Extended Zip`

**•** `NearAddress—Near Address`

**•** `Neighborhood`

**•** `State`

**•** `Street`

**•** `Unknown`

**•** `Zip`

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The latitude of the location where the recipient receives the order.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the recipient receives the order.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update


-----

```
ServiceState
ServiceStreet
ServiceabilityCheckDate
ServiceabilityData
SiteName

```

**Description**
The postal code of the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the recipient receives the order.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street where the recipient receives the order

**Type**
dateTime

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The date and time when the serviceability check was done.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The information about serviciability, such as broadband connection, download, and upload
speeds available at the address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The name of the customer's site or location.


-----

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[OrderItemRecipientChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[OrderItemRecipientFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[OrderItemRecipientHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[OrderItemRecipientOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[OrderItemRecipientShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
