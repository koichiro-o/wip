#### LiveChatBlockingRule

Represents a rule for blocking chat visitors’ IP addresses from starting new chats with agents. This object is available in API version 34.0
and later.

##### Supported Calls
```
create(), delete(), query(), update(), retrieve()

 Special Access Rules

```
To create a new rule, you must be logged in with the “Customize Application” permission or as a system administrator.

##### Fields

```
Description
DeveloperName

```

**Type**
string

**Properties**
Create, Nillable

**Description**
The description of the blocking rule—for example, the reason why the given IP
address or range of addresses is being banned from starting new chats.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin with
a letter, not include spaces, not end with an underscore, and not contain two
consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.


-----

```
FromIpAddress
Language
MasterLabel
ToIpAddress

```

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
The IP address of the user that you want to block, or the beginning of the range
of IP addresses you want to block. If you want to block a range of IP addresses,
indicate the end of the range in the `ToIpAddress` field. If you don’t indicate
an IP address in the ToIpAddress field, the only IP address that will be blocked
is the IP address in the `FromIpAddress` field.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort

**Description**
Label for the blocking rule.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
(Optional) The end of the range of IP addresses that you want to block. The range
begins with and includes the IP address in the `FromIpAddress` field, and it
ends with and includes the IP address in the `ToIpAddress field.`


-----

##### Usage

Use this object to query and manage rules for blocking customers from starting new chats with agents.
