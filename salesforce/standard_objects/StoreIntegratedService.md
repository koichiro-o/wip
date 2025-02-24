#### StoreIntegratedService

Represents an association between an integration and a store. This object is available in API version 49.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Special Access Rules

```
The StoreIntegratedService object is available only if the B2B Commerce license is enabled.

##### Fields

```
Integration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
ServiceProviderType
StoreId

```

**Description**
Required. The integration ID.

Possible values are:

**•** If the integration is a RegisteredExternalService:

**–** The ID of the RegisteredExternalService OR

**–** [ServiceProviderType]__[DeveloperName]

**•** ServiceProviderType: Price, Inventory, Tax, or Shipment

**•** DeveloperName of RegisteredExternalService

**•** If the integration is a PaymentGateway:

**–** The ID of the PaymentGateway

**•** If the integration is a Flow:

**–** [ServiceProviderType]__[NamespacePrefix]__[ApiName]

**–** If NamespacePrefix is null, it’s [ServiceProviderType]__[ApiName]

**•** ServiceProviderType: Flow

**•** ApiName and NamespacePrefix of FlowDefinitionView

**•** If the integration is the Salesforce Standard pricing:

**–** [ServiceProviderType]__B2B_STOREFRONT__StandardPricing

**•** ServiceProviderType: Price

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. The type of integration service provider.

Possible values are:

**•** `Flow`

**•** `Inventory`

**•** `Payment`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Type**
reference


-----

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. The unique ID for the store.
