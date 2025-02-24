#### QuoteLineItemRecipient

Represents a site, employee, or other entity for which services are being quoted. This could include details such as the recipient's name,
contact information, associated site or location, and any specific requirements or preferences for the quoted services. This object is
available in API version 62.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
BroadbandConnectionType

```

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
MaxDownloadSpeed
MaxUploadSpeed
Name

```

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

**Description**
The name of the customer's site or location.


-----

```
QuoteId
RecipientType
ServiceAddrValidationDate
Service Account

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The quote associated with the recipient.

This field is a relationship field.

**Relationship Name**
Quote

**Relationship Type**
Master-detail

**Refers To**
Quote (the master object)

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the type of recipient of the service.

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

**Description**
Reference to the Account Entity where the product is used, serviced, or installed.


-----

```
ServiceAddrValidationMsg
ServiceAddrValidationResult
ServiceAddress
ServiceCity
ServiceCountry

```

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
The address where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The city where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The country where the recipient receives the service.


-----

```
ServiceGeocodeAccuracy
ServiceLatitude
ServiceLongitude
ServicePostalCode

```

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
The latitude of the location where the recipient receives the service.

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The longitude of the location where the recipient receives the service.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The postal code of the address.


-----

```
ServiceState
ServiceStreet
ServiceabilityCheckDate
ServiceabilityData
SiteName

##### Associated Objects

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The state where the recipient receives the service.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The street where the recipient receives the service.

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


This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**[QuoteLineItemRecipientChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[QuoteLineItemRecipientFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[QuoteLineItemRecipientHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[QuoteLineItemRecipientOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[QuoteLineItemRecipientShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
