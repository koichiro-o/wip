#### EmailRoutingAddress

An email address used for Email-to-Case. Email routing addresses store a unique email services address provided by Salesforce and
configuration options for emails received by this address.

##### Supported Calls
```
create(), describeSObjects(), delete(), update(), query(), retrieve(), upsert()

 Special Access Rules

```
To access this object, Email-to-Case must be enabled. Only admin users can access this object.

##### Fields

```
PersonalName

```

**Type**
string

**Properties**
Create, Filter, Sort, Update


-----

```
Address
EmailServicesAddress

```
SEE ALSO:

EmailServicesAddress


**Description**
The display name of the EmailRoutingAddress. Maximum size is 300 characters.

**Type**
email

**Properties**
Create, Filter, Sort, Update

**Description**
The email address to which your customers direct their questions. Emails are forwarded from
this address.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A unique, Salesforce-generated email address. This field value is read-only and can't be
modified. Emails are forwarded to this address.

