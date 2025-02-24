#### OpportunityPartner

This object represents a partner relationship between an Account and an Opportunity. An OpportunityPartner record is created
automatically when a Partner record is created for a partner relationship between an account and an opportunity.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve()

```

-----

##### Special Access Rules

Customer Portal users can't access this object.

##### Fields

```
AccountToId
IsPrimary
OpportunityId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the partner Account in the partner relationship.

This is a relationship field.

**Relationship Name**
AccountTo

**Relationship Type**
Lookup

**Refers To**
Account

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the account is the opportunity’s primary partner (true) or not (false).
Label is Primary.

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the Opportunity that is in the partner relationship.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity


-----

```
ReversePartnerId
Role

```

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the reciprocal OpportunityPartner record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The UserRole that the Account has on the Opportunity. For example, `Reseller` or
```
  Manufacturer.

```

##### Creating an Account-Opportunity Partner Relationship

When you create a partner relationship between an account and an opportunity (when you create a Partner record and specify the
`OpportunityId` field), the API automatically creates two OpportunityPartner records, one for the forward relationship and one for
the reverse.

**•** The value of the Partner field `AccountToId` maps to the value of the OpportunityPartner field `AccountToId.`

**•** The values of the OpportunityId, Role, and IsPrimary fields in both the Partner and OpportunityParnter records are the
same.

**•** If you set the `IsPrimary` value to 1 (true) upon insert of a new OpportunityPartner, the `IsPrimary` value is automatically
set to 0 (false) for any existing primary partners for that opportunity.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

Partner

AccountPartner
