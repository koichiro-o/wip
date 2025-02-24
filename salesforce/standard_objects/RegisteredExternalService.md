#### RegisteredExternalService

Represents a registered external service used for checkout integrations by data integrators. This object is available in API version 49.0
and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
The RegisteredExternalService object is available only if the B2B Commerce license is enabled.

##### Fields

```
ConfigUrl

```

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to the configuration page for the integration.


-----

```
Description
DeveloperName
DocumentationUrl
ExtensionPointName

```

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Description of the external service provider.

This field is available in API version 59.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization.

Note: Only users with View DeveloperName OR View Setup and Configuration
permission can view, group, sort, and filter this field.

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Link to documentation for the registered external service.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
This field is available in API version 55.0 and later. Name of an extension point.

Possible values are:

**•** `Commerce_Domain_Cart_Calculate`

**•** `Commerce_Domain_Checkout_CreateOrder`

**•** `Commerce_Domain_Inventory_CartCalculator`

**•** `Commerce_Domain_Inventory_Service`

**•** `Commerce_Domain_OrderManagement_Product`


-----

```
ExternalServiceProviderId
ExternalServiceProviderType

```


**•** `Commerce_Domain_Pricing_CartCalculator`

**•** `Commerce_Domain_Pricing_Service`

**•** `Commerce_Domain_Promotions_CartCalculator`

**•** `Commerce_Domain_Promotions_ShippingCalculator`

**•** `Commerce_Domain_Shipping_CartCalculator`

**•** `Commerce_Domain_Shipping_SplitShipment`

**•** `Commerce_Domain_Tax_CartCalculator`

**•** `Commerce_Domain_Tax_Service`

**•** `Commerce_Endpoint_Account_Address`

**•** `Commerce_Endpoint_Account_Addresses`

**•** `Commerce_Endpoint_Cart_Item—This field value is available in API version`
62.0 and later.

**•** `Commerce_Endpoint_Cart_ItemCollection—This field value is available`
in API version 62.0 and later.

**•** `Commerce_Endpoint_Catalog_Product`

**•** `Commerce_Endpoint_Catalog_Products`

**•** `Commerce_Endpoint_Search_ProductSearch`

**•** `Commerce_Endpoint_Search_Products`

**•** `Commerce_Endpoint_Search_ProductsByCategory`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of an Apex class functioning as a provider. The Apex class can either implement one
of the following interfaces:

**•** sfdc_checkout.CartInventoryValidation

**•** sfdc_checkout.CartPriceCalculations

**•** sfdc_checkout.CartShippingCharges

**•** sfdc_checkout.CartTaxCalculations

[or the Apex class can extend one of the base classes for an extension. See Available Extensions.](https://developer.salesforce.com/docs/commerce/salesforce-commerce/guide/available-extensions.html)

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of external service provider. For an extension, you set the type to `Extension,`
and you specify an `extensionPointName. For example, for a Pricing Cart Calculator`


-----

```
IconUri
IsApplication
Language

```

extension, you specify `Commerce_Domain_Pricing_CartCalculator` as the
```
  extensionPointName. For an integration, you set the type to one of the other possible

```
values, such as `Price, and you omit` `extensionPointName.`

Possible values are:

**•** `Extension` (this value is available in API version 55.0 and later)

**•** `Inventory`

**•** `Price`

**•** `Promotions` (this value is available in API version 53.0 and later)

**•** `Shipment`

**•** `Tax`

**Type**
url

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
URI of icon for the extension provider.

This field is available in API version 59.0 and later.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates if the extension provider is contained within a managed package.

The default value is `false.`

This field is available in API version 59.0 and later.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The combined language and locale ISO code, which controls the language for labels displayed
in an application.

Possible values are:

**•** `da—Danish`

**•** `de—German`

**•** `en_US—English`

**•** `es—Spanish`


-----

```
MasterLabel
NamespacePrefix

```


**•** `es_MX—Spanish (Mexico)`

**•** `fi—Finnish`

**•** `fr—French`

**•** `it—Italian`

**•** `ja—Japanese`

**•** `ko—Korean`

**•** `nl_NL—Dutch`

**•** `no—Norwegian`

**•** `pt_BR—Portuguese (Brazil)`

**•** `ru—Russian`

**•** `sv—Swedish`

**•** `th—Thai`

**•** `zh_CN—Chinese (Simplified)`

**•** `zh_TW—Chinese (Traditional)`

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The primary label for the registered external service.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that aren’t Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.


-----
