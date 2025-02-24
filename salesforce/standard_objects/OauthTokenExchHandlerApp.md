#### OauthTokenExchHandlerApp

Represents the enablement settings for a specific Salesforce connected app or external client app that’s enabled for the token exchange
handler. A handler can be enabled for multiple apps. This object is available in API version 60.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

 Fields

```
```
ApexExecutionUserId

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

```
ConnectedApplicationId
IsDefault
OauthTokenExchangeHandlerId

```

**Description**
The ID of the user who runs the Apex token exchange handler. We recommend that you use
an integration user.

This field is a relationship field.

**Relationship Name**
ApexExecutionUser

**Relationship Type**
Lookup

**Refers To**
User

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The connected app that’s being used to integrate with Salesforce.

This field is a relationship field.

**Relationship Name**
ConnectedApplication

**Relationship Type**
Lookup

**Refers To**
ConnectedApplication

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether the token exchange handler is the default handler for this app. During the
token exchange flow, in the token request, you can optionally include a token_handler
parameter with the name of a specific handler’s Apex class. If you don’t include this parameter,
Salesforce defaults to the default handler.

The default value is `false.`

**Type**
reference

**Properties**
Create, Filter, Group, Sort, Update


-----

**Description**
The `OauthTokenExchangeHandler` with which these enablement settings are
associated.

This field is a relationship field.

**Relationship Name**
OauthTokenExchangeHandler

**Relationship Type**
Lookup

**Refers To**
OauthTokenExchangeHandler
