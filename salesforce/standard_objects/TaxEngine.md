#### TaxEngine

A tax engine represents both an instance of a tax engine provider as well as the merchant credentials for that specific instance. When
Subscription Management calculates tax on an order item, it sends a request through Subscription Management Tax Calculation API to
an external tax engine. The Salesforce tax engine record contains information passed to the external tax engine, such as This object is
available in API version 55.0 and later.

The merchant credentials are stored in a named credential record in Salesforce. The named credential record is referenced in the tax
engine object’s Merchant Credentials field.

The tax adapter Apex class ID is stored in the tax engine provider. When a user calls Calculate Tax API, Subscription Management interacts
with the external tax provider using the adapter class and the named credentials.

The tax engine address and seller code from the TaxEngine record are also used in the interaction.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available when Subscription Management or Commerce Subscriptions is enabled. If your org has Subscription Management
and Commerce Subscriptions enabled, then Subscription Management takes precedence.

##### Fields

```
Description
ExternalReference

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
The description of the tax engine provider and merchant credential.

**Type**
string


-----

```
LastReferencedDate
LastViewedDate
MerchantCredentialId
SellerCode

```

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**
Shows information about the external platform used for the tax engine.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp when the current user last accessed this record, a record related to this record,
or a list view.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Looks up to the merchant credential setup entity in Salesforce. CommerceTax Tax Calculation
API sends this information to the external tax engine for use in the tax calculation process.

This field is a relationship field.

**Relationship Name**
MerchantCredential

**Relationship Type**
Lookup

**Refers To**
NamedCredential

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update


-----

```
Status
TaxEngineAddress
TaxEngineCity
TaxEngineCountry
TaxEngineGeocodeAccuracy

```

**Description**
Seller code of the transaction for which the tax engine integration log was captured.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Shows the status of the tax engine.

Possible values are:

**•** `Active—This tax engine is available for use.`

**•** `Inactive—This tax engine isn't available for use.`

**Type**
address

**Properties**
Filter

**Description**
[The compound form of the tax engine address. Read-only. See Address Compound Fields](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_address.htm)
for details on compound address fields. Used in case the request doesn’t contain a Ship To
address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 40 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum size is 80 characters.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update


-----

```
TaxEngineLatitude
TaxEngineLongitude
TaxEngineName
TaxEnginePostalCode
TaxEngineProviderId

```

**Description**
[Accuracy level of the geocode for the tax engine address. See Compound Field Considerations](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)
[and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLongitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –90 and 90 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
double

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Used with TaxEngineLatitude to specify the precise geolocation of a tax engine address.
Acceptable values are numbers between –180 and 180 with up to 15 decimal places. See
[Compound Field Considerations and Limitations for details on geolocation compound fields.](https://developer.salesforce.com/docs/atlas.en-us.254.0.api.meta/api/compound_fields_limitations.htm#compound_fields_limitations)

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The name of the tax engine.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Postal code maximum size is 20 characters.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The Id of the tax engine provider.


-----

```
TaxEngineState
TaxEngineStreet
TaxPrvdAccountIdentifier
Type

```

This field is a relationship field.

**Relationship Name**
TaxEngineProvider

**Relationship Type**
Lookup

**Refers To**
TaxEngineProvider

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. State maximum size is 80 characters.

**Type**
textarea

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Details for the tax engine address. Maximum of 255 characters.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique identifier of the external tax provider’s account. This field is only available if
Commerce Subscriptions is enabled for your org. Available in API version 63.0 and later.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Specifies the tax engine used to calculate tax. This field is only available if Commerce
Subscriptions is enabled for your org. Available in API version 63.0 and later.

Possible values are:

**•** `CommerceTaxExtension—Commerce Tax Extension`

**•** `RevenueCloudTaxExtension—Revenue Cloud Tax Extension`

**•** `StandardTaxEngine—Standard Tax Extension`


-----

**•** `StripeNative—Stripe Native`
