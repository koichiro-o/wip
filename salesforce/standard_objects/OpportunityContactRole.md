#### OpportunityContactRole

Represents the role that a Contact plays on an Opportunity.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), update(), upsert()

 Fields

```
```
ContactId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
ID of an associated Contact. The API applies user access rights to the associated Opportunity
for this object, but not to the associated Contact. The API may return rows from a query on
this object that include this field’s values for contacts to which the user does not have
sufficient access rights. It may also return values for this field for contacts that have been


-----

```
CurrencyIsoCode
Division
IsDeleted
IsPrimary

```

deleted. In either case, the client must perform a query on the contact table for this field’s
value to determine whether the Contact is accessible to the user and has not been deleted.

This is a relationship field.

**Relationship Name**
Contact

**Relationship Type**
Lookup

**Refers To**
Contact

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
Available only for orgs with the multicurrency feature enabled. Contains the ISO code for
any currency allowed by the org. This field is available in API version 47.0.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Restricted picklist, Sort

**Description**
A logical segment of your organization's data. For example, if your company is organized
into different business units, you could create a division for each business unit, such as “North
America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the record has been moved to the Recycle Bin (true) or not (false).
The `IsDeleted` flag is usable only when the parent record is deleted to the recycle bin,
and not when the `OpportunityContactRole` record is deleted directly. Label is
**Deleted.**

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update


-----

```
 OpportunityId
 Role

##### Usage

```

**Description**
Indicates whether the associated Contact plays the primary role on the Opportunity (true)
or not (false). Each Opportunity has only one primary contact. Label is Primary.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. ID of an associated Opportunity. This field is non-nullable, and it cannot be updated.
You must provide a value for this field when creating new records. You can’t change it after
it has been created.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Name of the role played by the associated Contact on the Opportunity, such as Business
User or Decision Maker.


Use the Opportunity Contact Role object to manage information about contacts and roles related to opportunities. Records of this type
appear in the user interface in the Opportunity Contact Role related list and on the Opportunity detail page.

Although allowed, we do not recommend that you create multiple relationships between the same Opportunity and a Contact.

##### Associated Objects

This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.


-----

**OpportunityContactRoleChangeEvent (API version 45.0)**
Change events are available for the object.

SEE ALSO:

Overview of Salesforce Objects and Fields
