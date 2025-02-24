#### SelfServiceUser

Represents a Contact who has been enabled to use your organization’s Self-Service portal, where he or she can obtain online support.

Note: Starting with Spring ’12, the Self-Service portal isn’t available for new Salesforce orgs. Existing orgs continue to have access
to the Self-Service portal.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Customer Portal users can't access this object.

##### Fields

```
ContactId
Email
FirstName

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Required. All Self-Service users must be associated with a Contact. The contact’s email should
match the Self-Service user email. The contact must have a value in the `AccountId` field
or an error occurs.

**Type**
email

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Make this the same as the email address for the Contact associated with this
SelfServiceUser. Password resets and other system communication will be sent to this email
address.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
First name of the Self-Service user.


-----

```
IsActive
IsDeleted
LanguageLocaleKey
LastLoginDate
LastName
LocaleSidKey

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the Self-Service user is allowed to log in to the Self-Service portal (true)
or not (false). Note that there is no way to delete a Self-Service user. They can only be
marked as inactive.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Indicates whether the object has been moved to the Recycle Bin (true) or not (false).
Label is Deleted.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. It is the primary language for the user. All on-screen
text in the Self-Service portal is displayed in this language.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time when the Self-Service user last logged in.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. Last name of the Self-Service user.

**Type**
picklist


-----

```
Name
SuperUser
TimeZoneSidKey
Username

```

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. The value of this field affects the formatting and
parsing of values, especially numeric values, in the Self-Service portal. Values are two-letter
codes that indicate language and sometimes language and country. The codes are based
on ISO standards.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Concatenation of `FirstName` and `LastName. Limited to 203 characters, including`
whitespaces.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**

Indicates whether this Self-Service user is a super user with additional access on his or her
company's Self-Service portal (true) or not (false).

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Required. This is a restricted picklist field. The time zone of a affects the offset used when
displaying or entering times in the Self-Service portal.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Required. This contains the name that a Self-Service user enters to log into the Self-Service
portal. Value must be unique in your organization. If you try to create or update a user with
a duplicate value, the operation is rejected and an error is returned.


-----

##### Usage

For security reasons, you can’t query Self-Service user passwords via the API or the user interface. However, the API allows you to set and
reset Self-Service user passwords using the `setPassword()` and `resetPassword()` calls.

SelfServiceUser records created from the API don’t cause a notification email to be sent. If you want to notify the user, you must send
them an email after creating the user.

SEE ALSO:

Contact

User
