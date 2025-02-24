#### EmailRelay

Represents the configuration for sending an email relay. An email relay routes email sent from Salesforce through your company’s email
servers. This object is available in API version 43.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
You must have the Email Administration, Customize Application, and View Setup user permissions to use this object.


-----

##### Fields

**Field Name**
```
AuthType
Host
IsRequireAuth
Password

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted Picklist, Sort, Update

**Description**

Specifies which SASL mechanism Salesforce uses for SMTP authentication. This
field is available when Enable SMTP Auth is selected. Select an option:

**•** PLAIN- Salesforce uses PLAIN SASL mechanism for SMTP authentication.
Default.

**•** LOGIN- Salesforce uses LOGIN SASL mechanism for SMTP authentication

This field is available in API version 52.0 and later.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**

Indicates the host name or IP address of your company's SMTP server.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**

Indicates whether (true) or not (false) authentication is required. When setting
this field to true, the TlsSetting must be set to RequiredVerify. This
field is available in API version 44.0 and later.

**Type**
encryptedstring

**Properties**
Create, Nillable, Update

**Description**

Specifies the password for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.


-----

```
Port
TlsSetting
Username

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Indicates the port number of your company's SMTP server.

**•** 25

**•** 587

**•** 10025

**•** 11025

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**

Specifies whether Salesforce uses TLS for SMTP sessions.

**•** `Off: TLS is turned off. SMTP session continues through an insecure`
connection.

**•** `Preferred: If the remote server supports TLS, Salesforce upgrades the`
current SMTP session to use TLS. If TLS is unavailable, Salesforce continues
the session without TLS.

**•** `Required: Salesforce continues the session only if the remote server`
supports TLS. If TLS is unavailable, Salesforce terminates the session without
delivering the email.

**•** `PreferredVerify: If the remote server supports TLS, Salesforce upgrades`
the current SMTP session to use TLS. Before the session begins, Salesforce
verifies that the certificate is signed by a valid certificate authority, and that
the common name presented in the certificate matches the domain or mail
exchange of the current connection. If TLS is available but the certificate is
not signed or the common name does not match, Salesforce disconnects
the session and does not deliver the email. If TLS is unavailable, Salesforce
continues the session without TLS.

**•** `RequiredVerify: Salesforce continues the session only if the remote`
server supports TLS, the certificate is signed by a valid certificate authority,
and the common name presented in the certificate matches the domain or
mail exchange to which Salesforce is connected. If any of these criteria are
not met, Salesforce terminates the session without delivering the email.

**Type**
string


-----

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**

Specifies the username for relay host STMP authentication. When
`IsRequireAuth` is set to true, this field is required. This field is available in
API version 44.0 and later.

##### Usage

An email relay must be associated with an active email domain filter to take effect. If you set up multiple email relays in one org, they
are processed in the priority order of their email domain filters.

Tip: If you also plan to activate Bounce Management and Email Compliance Management, confirm with your email admin that
[your company allows relaying email sent from Salesforce. For more information on bounce management, see Configure Deliverability](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)
[Settings for Emails Sent from Salesforce.](https://help.salesforce.com/articleView?id=emailadmin_send_through_salesforce_configure_deliverability.htm&language=en_US)

SEE ALSO:

EmailServicesFunction

EmailDomainFilter
