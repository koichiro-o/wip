#### LoginIp

```
SELECT UserId, LoginTime from LoginHistory
WHERE LoginTime > 2010-09-20T22:16:30.000Z
AND LoginTime < 2010-09-21T22:16:30.000Z;
SELECT name, issuer, samlVersion FROM
SamlSsoConfig WHERE Id =
'0LE###############'
SELECT Type, DeveloperName FROM
AuthProvider WHERE Id =
'0SO###############'

```

Represents a validated IP address. This object is available in version 28.0 and later.

##### Supported Calls
```
describeSObjects(), delete(), query(), retrieve()

 Fields

```
```
ChallengeMethod
ChallengeSentDate

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The challenge method used to confirm the user’s identity. Possible values include the
following.

**•** `Email`

**•** `SMS`

**•** `TOTP_CHOICE: The user chooses multi-factor authentication.`

**•** `TOTP_ONLY: The user is required to use multi-factor authentication.`

**Type**
dateTime


-----

```
IsAuthenticated
SourceIp
UsersId

##### Usage

```

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the user was authenticated.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
If `true, the user has already been authenticated.`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The IP address the user logged in from.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
The ID of the user associated with this item.

This is a relationship field.

**Relationship Name**
Users

**Relationship Type**
Lookup

**Refers To**
User


At every login, the IP address of the login request is checked against the validated IP addresses using LoginIp. A match means the login
IP address is a known IP address. If there’s no match, the address is unknown, and the user is asked to confirm their identity.


-----
