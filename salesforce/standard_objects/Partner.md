#### Partner

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort

**Description**
The type of app used by the participant, such as messaging, chatbot, live_message, agent.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The role of this participant in the conversation, such as System, Agent, Chatbot, EndUser,
Supervisor, or Router.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subject of this participant in the conversation.


Represents a partner relationship between two Account records or between an Opportunity record and an Account record.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.


-----

##### Fields

**Field**
```
AccountFromId
AccountToId
IsPrimary

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if `OpportunityId` is null. ID of the main account in a partner relationship
between two accounts. Specifying this field when creating a Partner record creates two
AccountPartner records, one for each direction of the relationship. If you specify the
`OpportunityId` field, you can’t specify this field as well.

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
Required. ID of the Partner Account related to either an opportunity or an account. You must
specify this field when creating an Opportunity Partner or an Account Partner record.

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
Valid for Opportunity Partners only.


-----

```
OpportunityId
ReversePartnerId
Role

```

Indicates that the account is the primary partner for the opportunity. Only one account can
be marked as primary for an opportunity. If you set this field to 1 (true) upon insert of a
new opportunity partner, this field is automatically set to 0 (false) for any other primary
partners for that opportunity.

Label is Primary.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
Required if AccountFromId is null. ID of the opportunity in a partner relationship between
an account and an opportunity. Specifying this field when creating a record creates an
OpportunityPartner record. If you specify the AccountFromId field, you can’t also specify
this field.

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
ID of the reciprocal Parnter record in a partner relationship.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
UserRole that the account has toward the related opportunity or account, such as consultant
or distributor.


-----

##### Roles

In the Salesforce user interface, system administrators can set up the valid role values and their corresponding reverse role values in the
PartnerRole object. Each account in the relationship is assigned a `Role` (such as `Consultant` or `Distributor) designating`
that account’s role toward the related account or opportunity.

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

##### Creating an Account-Account Partner Relationship

When you create a partner relationship between two accounts (when you create a Partner record and specify the AccountFromId),
the API automatically creates two AccountPartner records, one for the forward relationship and one for the reverse. For example, if you
create a Partner relationship with “Acme, Inc.” as the `AccountFromId` and “Acme Consulting” as the `AccountToId, the API`
automatically creates two AccountPartner records:

**•** The forward relationship AccountPartner with “Acme, Inc.” as the AccountFromId and “Acme Consulting” as the AccountToId.

**•** The reverse relationship AccountPartner with “Acme Consulting” as the AccountFromId and “Acme, Inc.” as the AccountToId.

**•** The value of the `Role` field in the reverse relationship AccountPartner is set to the PartnerRole record `ReverseRole` value
associated with the value of the `Role` field in the forward relationship AccountPartner.

This mapping allows the API to manage the records and their relationships efficiently.

SEE ALSO:

AccountPartner

OpportunityPartner

UserRole

PartnerRole
