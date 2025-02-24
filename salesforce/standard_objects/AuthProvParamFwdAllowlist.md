#### AuthProvParamFwdAllowlist

Represents an allowlisted URL parameter that can be forwarded from authentication provider client configuration URLs to the authorization
URL. Use this type to add custom functionality to authentication providers. For example, allowlist a `ui_locales` parameter and use
it to send a user's language preference from Salesforce to the third-party provider's login page. This object is available in API version
62..0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

```

-----

##### Fields

**Field**
```
AuthProviderId
Description
Param
