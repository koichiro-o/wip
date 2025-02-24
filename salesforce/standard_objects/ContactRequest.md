#### ContactRequest

Represents a customer’s request for support to get back to them about an issue. This object is available in API version 45.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), undelete(), update(), upsert()

 Fields

```
```
IsCallback

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Determines how a voice call callback is handled after an agent accepts the callback
work item.

If set to `true, when an agent accepts the work item, the Omni-Channel utility`
doesn’t immediately dial the callback phone number. Instead, the agent can
determine how to handle the call. For example, after the agent accepts the work
item, they can view the callback details, transfer the call, or contact the end user
at another phone number. If the agent makes a call by using click-to-dial, the
call appears as a Callback call in the Omni-Channel utility.

If set to `false, when the agent accepts the work item in the Omni-Channel`
utility, the contact request is opened. The agent can review callback details. If


-----

```
LastReferencedDate
LastViewedDate
Name
OwnerId

```

they call with click-to-dial, the call appears as an Outbound call in the
Omni-Channel utility.

The default value is `false. Available in API version 60.0 and later.`

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed a record related to this
record.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The timestamp for when the current user last viewed this record. If this value is
null, this record might only have been referenced (LastReferencedDate)
and not viewed.

**Type**
string

**Properties**
Autonumber, Defaulted on create, Filter, idLookup, Sort

**Description**
The contact request number.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the Salesforce record that owns the request.

This is a polymorphic relationship field.

**Relationship Name**
Owner

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

```
PreferredChannel
PreferredPhone
RequestDescription
RequestReason

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The channel the customer selected as their preferred method of communication
in the contact request flow. For example:

**•** Phone

**Type**
phone

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The phone number the customer provided when requesting help in the contact
request flow.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
The description of the customer’s issue that they provided when requesting help
in the contact request flow.

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Sort, Update

**Description**
The reason the customer provided when requesting help in the contact request
flow. These values are customizable in Object Manager. The default values are:

**•** Account

**•** Billing

**•** Case

**•** General

**•** Order

**•** Other

**•** Product


-----

```
Status
WhatId
WhoId

```

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The status of the contact request. For example:

**•** Abandoned

**•** Attempted

**•** Contacted

**•** New

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce record the contact request is related to, such as an account,
case, opportunity, or work order.

This is a polymorphic relationship field.

**Relationship Name**
What

**Relationship Type**
Lookup

**Refers To**
Account, Case, Opportunity, WorkOrder

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
ID of the Salesforce contact record the contact request is related to, such as a
contact, lead, or user.

This is a polymorphic relationship field.

**Relationship Name**
Who

**Relationship Type**
Lookup

**Refers To**
Contact, Lead, User


-----

##### Usage

Contact request records are created when a customer fills out an online form. This form is created using a flow that uses the type
```
ContactRequestFlow. There’s a guided setup experience to create this flow on the Customer Contact Requests page in Setup.

```
You then add the flow to an Experience Cloud site using either the Flows component or the Contact Request Button & Flow component.

Contact Request works in Experience Cloud sites, whether they require authentication or not. Make sure that your users have the Run
Flows permission, including your Guest User profile. Without this permission, members won’t see the button or the form to submit
contact requests.

By default, all Standard User and System Administrator profiles have access to the object. Make sure that your users profiles, like service
agents, have at least read access on the contact request object.

You can create queues for contact requests and route them with Omni-Channel.

##### Associated Objects

This object has the following associated objects. Unless noted, they are available in the same API version as this object.

**ContactRequestOwnerSharingRule**

Sharing rules are available for the object.

**ContactRequestShare**

Sharing is available for the object.

SEE ALSO:

_[Salesforce Help: Set Up and Manage Contact Requests](https://help.salesforce.com/articleView?id=contact_request.htm&language=en_US)_
