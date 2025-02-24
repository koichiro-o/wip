#### ProductEntitlementTemplate

Represents predefined terms of customer support (Entitlement) that users can add to products (Product2).

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only Salesforce admins, users with access to the Case, Entitlement, or Work Order objects, and users with
the View Setup and Configuration permission can access this object.

##### Fields

```
EntitlementTemplateId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
Product2Id

##### Usage

```

**Description**
Required. ID of the entitlement template. Must be a valid ID.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of the Product2 associated with the entitlement template. Must be a
valid ID.


Use to query and manage entitlement templates.

SEE ALSO:

Entitlement
