#### EmailDomainFilter

```

**Properties**
Filter, Nillable, Sort

**Description**
Read-only field. The percentage of visitors who clicked a link contained in an email

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of prospects who loaded the images in the HTML version of
the email. The Unique Opens category counts each recipient only one time, even if the
prospect loaded images more than once.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The total number of prospects that have clicked the link to unsubscribe or
opted out of all emails in the Email Preference Center. They are removed from future email
sends.

**Type**
int

**Properties**
Defaulted on create, Filter, Group, Nillable, Sort

**Description**
Read-only field. The number of times a prospect clicked a link in the email. This metric doesn’t
include multiple clicks of the same link.


Represents a filter that determines whether an email relay is restricted to a specific list of domains. This object is available in API version
43.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Special Access Rules

You must have the “Email Administration,” “Customize Application,” and “View Setup” user permissions to use this object.

You must create an email relay in Setup or through the EmailRelay object before you can use the `EmailDomainFilter` object.

##### Fields

```
EmailRelayId
FromDomain
IsActive
PriorityNumber

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of the EmailRelay record.

This is a relationship field.

**Relationship Name**
EmailRelay

**Relationship Type**
Lookup

**Refers To**
EmailRelay

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the sender domains
(FromDomain) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether the email domain filter is active (true) or not (false). Use
this field to enable or disable the email domain filter.

**Type**
int


-----

```
ToDomain

##### Usage

```

**Properties**
Create, Filter, Group, idLookup, Nillable, Sort, Update

**Description**

Indicates the order in which the email domain filter is processed. Filters are
evaluated in ascending order. The priority number must be unique. If this field
is left blank, it is assigned the next available number and is processed last.
Processing stops after the first matching filter is applied.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**

Restricts the email relay to send emails based on the recipient domains
(ToDomain) listed in this field. This field is optional, accepts a list of
comma-separated values, and supports the wildcard character.


Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
