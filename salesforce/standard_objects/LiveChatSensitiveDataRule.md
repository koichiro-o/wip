#### LiveChatSensitiveDataRule

Represents a rule for masking or deleting data of a specified pattern. Written as a regular expression (regex). This object is available in
API version 35.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), update(), retrieve()

 Special Access Rules

```
As of Summer ’20 and later, only authenticated internal and external users can access this object.

##### Fields

```
ActionType
Description

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

The action to take on the text (remove or replace) when the sensitive data rule
is triggered.

**Type**
textarea

**Properties**
Create, Nillable, Update


-----

```
DeveloperName
EnforceOn
IsEnabled

```

**Description**
The description of the sensitive data rule—for example, “Block social security
numbers.”

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores
and alphanumeric characters, and must be unique in your org. It must begin
with a letter, not include spaces, not end with an underscore, and not contain
two consecutive underscores. In managed packages, this field prevents naming
conflicts on package installations. With this field, a developer can change the
object’s name in a managed package and the changes are reflected in a
subscriber’s organization.

Note: When creating large sets of data, always specify a unique
`DeveloperName` for each record. If no `DeveloperName` is
specified, performance slows down while Salesforce generates one for
each record.

Note: Only users with View DeveloperName OR View Setup and
Configuration permission can view, group, sort, and filter this field.

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Determines the roles on which the rule is enforced. The value is determined
using bitwise OR operation. There are seven possible values:

**1. Rule enforced on Agent**

**2. Rule enforced on Visitor**

**3. Rule enforced on Agent and Visitor**

**4. Rule enforced on Supervisor**

**5. Rule enforced on Agent and Supervisor**

**6. Rule enforced on Visitor and Supervisor**

**7. Rule enforced on Agent, Visitor, and Supervisor**

**Type**
boolean


-----

```
Language
MasterLabel
NamespacePrefix
Pattern

```

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Specifies whether a sensitive data rule is active (true) or not (false). Default
value (if none is provided) is `false.`

**Type**
picklist

**Properties**
Create, Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The language of the sensitive data rule.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Label for the sensitive data rule.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition
org that creates a managed package has a unique namespace prefix. Limit: 15
characters. You can refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace
prefix of the org for all objects that support it, unless an object is in an
installed managed package. In that case, the object has the namespace prefix
of the installed managed package. This field’s value is the namespace prefix
of the Developer Edition org of the package developer.

**•** In orgs that are not Developer Edition orgs, `NamespacePrefix` is set
only for objects that are part of an installed managed package. All other
objects have no namespace prefix.

**Type**
textarea


-----

```
Priority
Replacement

##### Usage

```

**Properties**
Create, Update

**Description**
The pattern of text blocked by the rule. Written as a JavaScript regular expression
(regex).

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the priority level of a Chat.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The string of characters that replaces the blocked text (if `ActionType`
`Replace` is selected).


Use this object to mask or delete data of specified patterns, such as credit card, social security, phone and account numbers, or even
profanity.
