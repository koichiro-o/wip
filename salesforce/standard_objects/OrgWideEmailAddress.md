#### OrgWideEmailAddress

Represents an organization-wide email address for user profiles.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(),
upsert()

```

-----

##### Special Access Rules

Only authenticated users with the View Setup and Configuration permission can access this object.

##### Fields

```
Address
DisplayName
IsAllowAllProfiles
IsVerified

```

**Type**
email

**Properties**
Create, Filter, Sort, Update

**Description**
An email alias that can be used by users of your org.

**Type**
string

**Properties**
Create, Filter, Sort, Update

**Description**
The name used to identify the sender of the email.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, any user profile in your organization can use this object. If` `false, only specified`
user profiles can use this object when sending email. If you do not have the appropriate user
profile, you can’t use this object.

The default value is `false..`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the email address has been verified by its owner.

The default value is false.

This field is available in API version 58.0 and later.

**Purpose**
Picklist

Possible values are DefaultNoreply, UserSelection, UserSelectionAndDefaultNoReply


-----

```
Purpose

##### Usage

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Indicates how an email address can be used. `UserSelection` allows users with the
correct profile to select the address as the From address for an email.

Possible values are `DefaultNoreply,` `UserSelection,`
```
  UserSelectionAndDefaultNoReply.

```

This object represents an email alias to use as the From address for an email, which can be selected by users with a user profile. You can
pass in the OrgWideEmailAddress ID when calling `sendEmail()` for a SingleEmailMessage.
