#### AdOpportunity

Represents an extension to the opportunity that stores campaign attributes specific to media ad sales. This object is available in API
version 59.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), undelete(), update(), upsert()

 Special Access Rules

```
This object is available only if the Media Cloud license is enabled.

##### Fields

```
BuyerId
CurrencyIsoCode

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Buyer.

This field is a relationship field.

**Relationship Name**
Buyer

**Relationship Type**
Lookup

**Refers To**
AdBuyServerAccount

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for organizations with the multicurrency feature enabled. Contains the ISO
code for any currency allowed by the organization.

Possible values are:

**•** `BRL—Brazilian Real`

**•** `CAD—Canadian Dollar`

**•** `EUR—Euro`


-----

```
DealType
Name
OpportunityId
OwnerId

```


**•** `USD—U.S. Dollar`

The default value is `USD.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The campaign type to be executed in the downstream ad server.

Possible values are:

**•** `Direct-sales`

**•** `Preferred (Non-Guaranteed)`

**•** `Programmatic Guaranteed`

The default value is `Direct-sales.`

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the ad opportunity.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Opportunity.

This field is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

**Description**
The ID of the user that owns this record.

This field is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**[AdOpportunityChangeEvent](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_change_event.htm)**

Change events are available for the object.

**[AdOpportunityFeed](https://developer.salesforce.com/docs/atlas.en-us.254.0.object_reference.meta/object_reference/sforce_api_associated_objects_feed.htm)**

Feed tracking is available for the object.

**[AdOpportunityHistory](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_history.htm)**

History is available for tracked fields of the object.

**[AdOpportunityOwnerSharingRule](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_ownersharingrule.htm)**

Sharing rules are available for the object.

**[AdOpportunityShare](https://developer.salesforce.com/docs/atlas.en-us.254.0.industries_reference.meta/industries_reference/sforce_api_associated_objects_share.htm)**

Sharing is available for the object.
