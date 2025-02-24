#### SetupAuditTrail

Represents changes you or other admins made in your org’s Setup area for at least the last 180 days. This object is available in API version
15.0 and later.

Note: SetupAuditTrail is not a supported standard controller. Using SetupAuditTrail as a standard controller in a Visualforce page
results in an error.

##### Supported Calls
```
query(), retrieve()

```
Note: Aggregate queries aren’t supported on this object. For example, `SELECT count() FROM SetupAuditTrail`
works but `SELECT count(Id) FROM SetupAuditTrail` fails.

##### Fields

```
Action
CreatedByContext
CreatedByIssuer

```

**Type**
string

**Properties**
Filter, Sort

**Description**
The category of the change made in Setup. For example, a value of `PermSetCreate`
indicates that an administrator created a permission set. The Display field contains more
specific information.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The context under which the Setup change was made. For example, if Einstein uses
cloud-to-cloud services to make a change in Setup, the value of this field is `Einstein.`
This field is available in API version 48.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DelegateUser
Display
Section

```

**Description**
Reserved for future use.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The Login-As user who executed the action in Setup. If a Login-As user didn’t perform the
action, this field is blank. This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Nillable, Sort

**Description**
The full description of changes made in Setup. For example, if the Action field has a value
of `PermSetCreate, the` `Display` field has a value like “Created permission set MAD:
with user license Salesforce.”

**Type**
string

**Properties**
Nillable, Sort

**Description**
The section in the Setup menu where the action occurred. For example, Manage Users or
Company Profile.


Note: You can use SOQL joins to get the information you need more quickly. For example, running SELECT CreatedBy.Name
```
  FROM SetupAuditTrail LIMIT 10 returns the first and last names of the last 10 people to make changes in Setup.
