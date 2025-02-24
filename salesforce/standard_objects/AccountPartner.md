#### AccountPartner

This object represents a partner relationship between two Account records. An AccountPartner record is created automatically when a
Partner record is created for a partner relationship between two accounts. An AccountPartner record is also created automatically
between an account and an opportunity’s account when a Partner record is created between an account and an opportunity.

Note: This object is completely distinct from and independent of Account records that have been enabled for the partner portal.


-----

##### Supported Calls
```
create(), delete(), describeLayout()describeSObjects(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
AccountFromId
AccountToId
IsPrimary

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the main Account in the partner relationship.

This is a relationship field.

**Relationship Name**
AccountFrom

**Relationship Type**
Lookup

**Refers To**
Account

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


-----

```
OpportunityId
ReversePartnerId
Role

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the AccountPartner is the primary partner of an opportunity (true).
When there are no corresponding Opportunity Partner records, the value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the opportunity in a partner relationship.

This is a relationship field.

**Relationship Name**
Opportunity

**Relationship Type**
Lookup

**Refers To**
Opportunity

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
ID of the reciprocal AccountPartner record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
The UserRole that the partner Account has on the main Account. For example, Consultant
or `Distributor.`


##### Creating an Account-Account Partner Relationship

When you create a partner relationship between two accounts (when you create a Partner record and specify the AccountFromId),
the API automatically creates two AccountPartner records, one for the forward relationship and one for the reverse. For example, if you
create a Partner relationship with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId, the API`
automatically creates two AccountPartner records:


-----

**•** The forward relationship AccountPartner with “Acme, Inc.” as the AccountFromId and “Acme Consulting” as the AccountToId.

**•** The reverse relationship AccountPartner with “Acme Consulting” as the AccountFromId and “Acme, Inc.” as the AccountToId.

**•** The value of the Role field in the reverse relationship AccountPartner is set to the PartnerRole record ReverseRole value associated
with the value of the `Role` field in the forward relationship AccountPartner.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

Partner

OpportunityPartner
