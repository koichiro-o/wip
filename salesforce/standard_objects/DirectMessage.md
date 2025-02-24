#### DirectMessage

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The ID of the saved payment method record.

**Relationship Name**
SavedPaymentMethod

**Relationship Type**
Lookup

**Refers To**
SavedPaymentMethod

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Defines the state of the digital wallet as a payment source.

Possible values are:

**•** `Active—Customers can make payments with the digital wallet.`

**•** `Canceled—The digital wallet can no longer be used for payments. This status can’t`
be changed.

**•** `InActive—The digital wallet can’t be used for payments until a user changes its`
status to Active.


Represents a direct message conversation between multiple users in Chatter. This object is available in API version 38.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve(), update()

 Special Access Rules

```
You must have the Manage Chatter Messages and Direct Messages permission enabled to access the DirectMessage object.


-----

##### Fields

**Field**
```
 Name
 Subject

##### Usage

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort, Update

**Description**
A default value that isn’t visible to users.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort, Update

**Description**
Subject of the overall direct message conversation.


DirectMessage is an object used by Salesforce to control DirectMessage conversations. It represents a record of a direct message
conversation, but doesn’t include conversation data, such as posts or comments. It is most frequently used to moderate direct message
data in order to meet data compliance regulations.
