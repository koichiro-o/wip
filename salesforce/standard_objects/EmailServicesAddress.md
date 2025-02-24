#### EmailServicesAddress

An email service address.

Each email service has one or more email addresses to which users can send messages for processing. An email service only processes
messages it receives at one of its addresses.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.


-----

##### Fields

**Field**
```
AuthorizedSenders
DeveloperName
EmailDomainName
FunctionId

```

**Type**
textarea

**Properties**
Create, Filter, Nillable, Sort, Update

**Description**
Configures the email service address to only accept messages from the email addresses or
domains listed in this field. If the email service address receives a message from an unlisted
email address or domain, the email service performs the action specified in the
`AuthorizationFailureAction` field of its associated email service. Leave this field
blank if you want the email service address to receive email from any email address.

**Type**
string

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
The name of the object in the API. This name can contain only underscores and alphanumeric
characters and must be unique in your org. It must begin with a letter, not include spaces,
not end with an underscore, and not contain two consecutive underscores. This 25-character
field must be unique among other EmailServicesAddress records under the same
EmailServiceFunction parent.

In managed packages, this field prevents naming conflicts on package installations. This field
is automatically generated, but you can supply your own value if you create the record using
the API. With this field, a developer can change the object’s name in a managed package
and the changes are reflected in a subscriber’s organization.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no `DeveloperName` is specified, performance might be slow
while Salesforce generates one for each record.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
A read only field you can query that contains the system-generated domain part of this email
service address. The system generates a unique domain-part for each email service address
to ensure that no two email service addresses are identical.

**Type**
reference


-----

```
IsActive
LocalPart
RunAsUserId

```

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the email service for which the email service address receives messages.

This is a relationship field.

**Relationship Name**
Function

**Relationship Type**
Lookup

**Refers To**
EmailServicesFunction

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this object is active (true) or not (false).

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
The local-part of the email service address. The local-part of the address is the string that
comes before the @ symbol.

For the local-part of a Salesforce email address, all alphanumeric characters are valid, plus
the following special characters:
```
  ! # $ % & amp; ' * / = ? ^ _ + - ` { | } ~,

```
The dot character (.) is also valid as long as it's not the first or last character.

Email addresses aren’t case-sensitive.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The username of the user whose permissions the email service assumes when processing
messages sent to this address.


-----

##### Usage

This object supports the email services feature, which allows you to create automated processes that use Apex classes to process the
contents, headers, and attachments of inbound email. For example, you can create an email service that automatically creates contact
records based on contact information in messages.

SEE ALSO:

EmailServicesFunction
