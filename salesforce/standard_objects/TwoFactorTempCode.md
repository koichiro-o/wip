#### TwoFactorTempCode

Stores information about a user’s temporary verification code for confirming their identity when logging in. This object is available in
API version 37.0 and later.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Special Access Rules

```
You need the Manage Multi-Factor Authentication in API permission to access this object. (Note that multi-factor authentication was
formerly called two-factor authentication.)

##### Fields

```
Expiration
Identifier
TempCode
UserId

```

**Type**
dateTime

**Properties**
Filter, Sort

**Description**
The date and time when the temporary verification code expires. The code expires
in 1 to 24 hours after it’s generated. Salesforce admins and non-admin users with
the Manage Multi-Factor Authentication in User Interface permission set the
expiration time when generating the code.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The unique identifier for the temporary code. This is a required field that can take
any value.

**Type**
encryptedstring

**Description**
A request for this value always returns `null.`

**Type**
reference


-----

**Properties**
Filter, Group, Sort

**Description**
The ID for the user who’s associated with the temporary verification code.
