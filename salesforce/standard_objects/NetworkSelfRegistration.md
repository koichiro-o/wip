#### NetworkSelfRegistration

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The name of the default page in the Experience Cloud site that you want to
override with a custom page.OverrideType can take the following values:

**•** `LoginRequired`

**•** `ChangePassword`

**•** `ForgotPassword`

**•** `SelfReg`

**•** `Home`


Represents the account that self-registering Experience Cloud users are associated with by default. Self-registering users in an Experience
Cloud site are required to be associated with an account, which the admin must specify while setting up self-registration for the site. If
an account isn’t specified, Salesforce creates person accounts (when enabled) for self-registering users. This object is available in API
version 34.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(),
undelete(), update(), upsert()

 Fields

```
```
AccountId
ApexHandlerId

```

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the account that self-registering users in the Experience Cloud site are
associated with.

**Type**
reference


-----

```
ExecuteApexHandlerAsId
NetworkId
OptionsDisableStandardRgstrComponent
OptionsIncludePassword

```

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the Apex handler created by Configurable Self-Reg registration page
type.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

The ID of the user who is executing the configurable self-registration handler.

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**

The ID of `NetworkId` is unique within your org.

You can use only one account per Experience Cloud site to assign self-registering
users.

**Type**
boolean

**Properties**
Create, Filter, Update

**Description**
Determines whether you can use standard Aura and Lightning Web Runtime
(LWR) components for self-registration. If this field is true, self-registration flows
that use these components don’t work.

For more control over self-registration, set this field to true if you’re not using
the standard self-registration component.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Include Password
field is selected.


-----

```
OptionsShowEmail
OptionsShowFirstName
OptionsShowLastName
OptionsShowMobilePhone
OptionsShowNickname

```

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on Configurable Self-Reg registration page. If true, the Email field appears
on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the First Name
field appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Last Name field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Mobile field
appears on the self-registration form.

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Nickname field
appears on the self-registration form.


-----

```
OptionsShowUsername
VerificationMethod

```

**Type**
Boolean

**Properties**
Create, Filter, Update

**Description**

Option on the Configurable Self-Reg registration page. If true, the Username field
appears on the self-registration form.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort, Update

**Description**
The type of verification method that a user must supply when registering, which
can be:

**•** `SyncEmail—User must supply an email address to verify identity.`

**•** `SMS—User must supply a phone number to verify identity.`

