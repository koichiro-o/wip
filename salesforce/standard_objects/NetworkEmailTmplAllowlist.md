#### NetworkEmailTmplAllowlist

Represents an allowlist for the one-time password (OTP) email templates that are sent to end users during the Headless Registration
Flow, the Headless Passwordless Login Flow, and the Headless Forgot Password Flow. This object is available in API version 60.0 and
later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
EmailTemplateId
NetworkId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The IDs of the allowlisted email templates that can be sent to users during the headless
authorization flows for registration, passwordless login, and forgot password. You can list
multiple template IDs. When your app sends its initial request to Headless Registration API
or Headless Passwordless Login API, the `emailtemplate` parameter can include only
an email template ID from the allowlist. For Headless Forgot Password API, it works the same
way, but only if email template allowlisting is enabled.

This field is a relationship field.

**Relationship Name**
EmailTemplate

**Relationship Type**
Lookup

**Refers To**
EmailTemplate

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The ID of the Experience Cloud site for which the allowlist is being configured.

This field is a relationship field.

**Relationship Name**
Network

**Relationship Type**
Lookup

**Refers To**
Network

