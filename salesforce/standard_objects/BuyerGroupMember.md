#### BuyerGroupMember

Represents a member of a buyer group. This object is available in API version 55.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout, describeSObjects(), getDeleted(), getUpdated(), query,
retrieve(), undelete(), update(), upsert()

 Special Access Rules

```
The BuyerGroupMember object is available only if the Commerce Buyer and Entitlements Integrator permission is granted.

##### Fields

```
BuyerGroupId
BuyerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the buyer group to which the member belongs.

`BuyerGroupId` is a relationship field.

**Relationship Name**
BuyerGroup

**Relationship Type**
Lookup

**Refers To**
BuyerGroup

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the account or guest buyer profile.

`BuyerId` is a polymorphic relationship field.


-----

```
Name
OwnerId

```

**Relationship Name**
Buyer

**Relationship Type**
Lookup

**Refers To**
Account, GuestBuyerProfile

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The name of the buyer group member.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, idLookup, Sort

**Description**
The ID of the member group or user.

`OwnerId` is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User

