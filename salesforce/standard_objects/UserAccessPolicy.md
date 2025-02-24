#### UserAccessPolicy

```

**Type**
string

**Properties**
Filter, Group, idLookup, Nillable, Sort

**Description**
The source of the user access change. For example, `UserAccessPolicyId.`


Represents a user access policy. This object is available in API version 57.0 and later.

Important: Where possible, we changed noninclusive terms to align with our company value of Equality. We maintained certain
terms to avoid any effect on customer implementations.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
To create or modify user access policies, users must have the Manage User Access Policies permission.


-----

##### Fields

**Field**
```
BooleanFilter
Description
DeveloperName
Language
MasterLabel
NamespacePrefix

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The logic that determines how your user criteria filters are applied in the user access policy.

**Type**
textarea

**Properties**
Filter, Group, Nillable, Sort

**Description**
Description of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique name for the user access policy.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The language of the user access policy.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Label for the user access policy. In the UI, this field is Label.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
Order
Status

```

**Description**
The namespace prefix associated with this object. Each Developer Edition organization that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
`namespacePrefix__componentName` notation.

The namespace prefix can have one of the following values:

**•** In Developer Edition organizations, the namespace prefix is set to the namespace prefix
of the organization for all objects that support it. There is an exception if an object is in
an installed managed package. In that case, the object has the namespace prefix of the
installed managed package. This field’s value is the namespace prefix of the Developer
Edition organization of the package developer.

**•** In organizations that are not Developer Edition organizations, `NamespacePrefix`
is only set for objects that are part of an installed managed package. There is no
namespace prefix for all other objects.

**Type**
int

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Indicates the order for which active policy is applied when a user meets the criteria for
multiple policies. Must be an integer from 0 to 10,000. Only the active policy with the lowest
`Order` value is applied. This field is required only if the `Status` field is set to `Active.`

Available in API version 61.0 and later.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the user access policy.

Possible values are:

**•** `Active`

**•** `Completed`

**•** `Design`

**•** `Failed`

**•** `Migrate`

**•** `Testing`

**•** `Updating`

The default value is `Design.`


-----

```
TriggerType

##### Usage

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of user record trigger for which this user access policy runs.

Possible values are:

**•** `Create—The user access policy runs when a user who matches the policy criteria is`
created.

**•** `CreateAndUpdate—The user access policy runs when a user who matches the`
policy criteria is either created or updated.

**•** `Update—The user access policy runs when a user who matches the policy criteria is`
updated.


[For more information, see User Access Policies in Salesforce Help.](https://help.salesforce.com/s/articleView?id=sf.perm_user_access_policies.htm&language=en_US)
