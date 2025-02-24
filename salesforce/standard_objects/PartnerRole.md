#### PartnerRole

```

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The record being inserted or updated.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
An item is added to the Organization Sync Log if it failed to be replicated to the
linked organization. This picklist includes the following values:

**•** `Failed: The replication continued to fail after multiple retries, and won’t`
be retried further.

**•** `Resolved: The replication succeeded after retrying.`

**•** `Retrying: Salesforce is retrying the replication.`

This field is available in API version 35.0 and later.


Represents a role for an account Partner, such as consultant, supplier, and so on.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
ApiName

```

**Type**
string

**Properties**
Filter, Group, idLookup, Sort


-----

```
MasterLabel
ReverseRole
SortOrder

##### Usage

```

**Description**
Uniquely identifies a picklist value so it can be retrieved without using an id or master label.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Master label for this partner role value. This display value is the internal label that does not
get translated. Limit: 255 characters.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Sort

**Description**
Name of the reverse role that corresponds to this partner role. For example, if the role is
“subcontractor,” then the reverse role might be “general contractor.” In the user interface,
assigning a partner role to an account creates a reverse partner relationship so that both
accounts list the other as a partner.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
Number used to sort this value in the partner role picklist. These numbers are not guaranteed
to be sequential, as some previous partner role values might have been deleted.


This object represents a value in the partner role picklist. In the user interface, the partner role picklist provides additional information
about the role of a Partner, such as their corresponding reverse role. Query this object to retrieve the set of values in the partner role
picklist, and then use that information while processing PartnerRole records to determine more information about a given partner role.
For example, the application could determine the reverse role of a given Partner `Role` value and the value of the `ReverseRole`
property in the associated PartnerRole object.

SEE ALSO:

Overview of Salesforce Objects and Fields


-----
