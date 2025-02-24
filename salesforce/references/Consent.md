### Consent

Your users can store consent preferences in different locations and possibly inconsistently. You can locate your customers’ preferences
for consent across multiple records when using API version 44.0 and later. Tracking consent preferences helps you and your users respect
the most restrictive requests. You can use the Consent API with specific Data Cloud parameters with API version 50.0 and later.

#### Compile Consent Settings

Gets consent details based on a single action, like email or track, across specific consent management objects when the records have a
lookup relationship. This resource is available in REST API version 45.0 and later.

To call Consent API, you must have either the View All Data or the Allow User Access to Privacy Data user permission. Requiring a perm
ensures that the System Administrator gives explicit permission. This API accesses org-wide consent data, such as links between records
and the value of consent flags, not just records to which the user ordinarily has access.

Consent API gets consent details based on a single action, like email or track, across the Contact, Contact Point Type Consent, Data Use
Purpose, Individual, Lead, Person Account, and User objects when the records have a lookup relationship.

When you select email as the action, the API only aggregates consent for records that contain the same email address. If the record ID
specified in the URI is associated with a record that contains a different email address, the consent settings of the associated record aren’t
included in the API response. The Consent API can't locate records in which the email address field is protected by Platform Encryption.

Note: When the API compares consent settings across records, it doesn’t incorporate settings from converted leads.


-----

**Action** **Fields Consulted** **API Response** **Response Schema**


email
Contact.HasOptedOutOfEmail Within the time range {

if specified in

ContactPointTypeConsent.ContactPointType "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveFrom {
Returns TRUE if all

ContactPointTypeConsent.EffectiveTo "result" : "<Success/errormessage>",

consulted field values

ContactPointTypeConsent.PrivacyConsentStatus are 0. "proceed" : { "emailResult" : "<Success/errormessage>",

email : “<true/false>” }

DataUsePurpose.Name Returns FALSE if any
consulted field value is }
Lead.HasOptedOutOfEmail
1 or if no related
}
PersonAccount.HasOptedOutOfEmail Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


fax
Contact.HasOptedOutOfFax Returns TRUE if all {

consulted field values

DataUsePurpose.Name "<ID/Email>" :

are 0.

Lead.HasOptedOutOfFax {
Returns FALSE if any
PersonAccount.HasOptedOutOfFax "result" : "<Success/errormessage>",
consulted field value is


geotrack
DataUsePurpose.Name

Individual.HasOptedOutGeoTracking

mail
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


1 or if no related "proceed" : { "faxResult" : "<Success/errormessage>", fax
Contact, Lead, or : "<true/false>" }
Person Account object
}
exists.

}

Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is


1 or if no related "proceed" : { "geotrackResult" : "<Success/errormessage>",
Individual object exists. "geotrack" : "<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "mailingResult" : "<Success/errormessage>",

"mail" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related


-----

Contact, Contact Point }
Type Consent, Lead, or
Person Account object
exists.


phone
Contact.DoNotCall Within the time range {

if specified in

ContactPointTypeConsent.ContactPointType "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveFrom {
Returns TRUE if all

ContactPointTypeConsent.EffectiveTo "result" : "<Success/errormessage>",

consulted field values

ContactPointTypeConsent.PrivacyConsentStatus are 0. "proceed" : { "phoneResult" : "<Success/errormessage>",

"phone" : "<true/false>" }

DataUsePurpose.Name Returns FALSE if any
consulted field value is }
Lead.DoNotCall
1 or if no related
}
PersonAccount.DoNotCall
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


portability
DataUsePurpose.Name

Individual.SendIndividualData

process
DataUsePurpose.Name

Individual.HasOptedOutProcessing

profile
DataUsePurpose.Name

Individual.HasOptedOutProfiling


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

0 or if no related "proceed" : { "portabilityResult" :
Individual object exists. "<Success/errormessage>", "portability" : "<true/false>"
}

}

}


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "processResult" : "<Success/errormessage>",
Individual object exists. "process" : "<true/false>" }

}

}


-----

shouldforget
DataUsePurpose.Name

Individual.ShouldForget

social
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


1 or if no related "proceed" : { "profileResult" : "<Success/errormessage>",
Individual object exists. "profile" : "<true/false>" }

}

}

Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is


0 or if no related "proceed" : { "shouldForgetResult" :
Individual object exists. "<Success/errormessage>", "shouldforget" :
"<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "socialResult" : "<Success/errormessage>",

"social" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related
}
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


solicit
DataUsePurpose.Name

Individual.HasOptedOutSolicit

storepiielsewhere DataUsePurpose.Name

Individual.CanStorePiiElsewhere


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "solicitResult" : "<Success/errormessage>",
Individual object exists. "solicit" : "<true/false>" }

}

}


-----

Returns FALSE if the "result" : "<Success/errormessage>",
consulted field value is

"proceed" : { "storePIIElsewhereResult" :

0 or if no related

"<Success/errormessage>", "storepiielsewhere" :

Individual object exists.

"<true/false>" }

}

}


track
DataUsePurpose.Name

Individual.HasOptedOutTracking

web
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "trackResult" : "<Success/errormessage>",
Individual object exists. "track" : "<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "webResult" : "<Success/errormessage>",

"web" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related
}
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


##### Syntax

**URI**
```
  /services/data/vXX.X/consent/action/action?ids=listOfIds

```
**Formats**
JSON

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
```
  None

```

-----

**Request parameters**

**Parameter**
```
  action

```

Required. The proposed action.

If this parameter is used, `actions` can't be used.


`aggregatedConsent` Optional: true or false. `aggregatedConsent` is the same as
```
                 aggregatedConsent=true. If true, one result is returned indicating whether

```
to proceed or not, rather than a result for each ID. If any ID in the list returns false, the
aggregated result is false.

```
datetime

```

Optional. The timestamp for which consent is determined. The value is converted to
the UTC timezone and must be formatted as described in Valid Date and DateTime
Formats. If not specified, defaults to the current date and time.


`ids` Required. Comma-separated list of IDs. The ID can be the record ID or the email address
listed on the record.

```
policy

```

Optional. Use `policy=requireExplicitConsent` to specify in the API
response whether explicit consent was given for a contact point channel. The API
returns an infoNotFound response when consent isn’t specified.

This parameter is available in API version 49.0 and later.


`purpose` Optional. The reason for contacting a customer.

`verbose` Optional: true or false. verbose is the same as verbose=true. Verbose responses
are slower than non-verbose responses. See the examples for a verbose response.

##### Example

**Request for URI structure**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/consent/action/track?ids=003xx000004TxyY,00Qxx00000syyO,003zz000004zzZ
   -H "Authorization: Bearer token"

```
**Request for Email addresses as IDs, specified purpose and timespan, and a verbose response**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/consent/action/email?ids=j0t5t5b2@tkbxp5ia.com,4quxlswo@23wj7pwh.com&datetime=2018-12-12T00:00:00Z
   -H "Authorization: Bearer token"

```
**Response Body**


-----

#### Compile Multiple Types of Consent Settings

Gets consent details based on multiple actions, like email and track, across specific consent management objects when the records have
a lookup relationship. Available in API version 45.0 and later.

To call Consent API, you must have either the View All Data or the Allow User Access to Privacy Data user permission. Requiring a perm
ensures that the System Administrator gives explicit permission. This API accesses org-wide consent data, such as links between records
and the value of consent flags, not just records to which the user ordinarily has access.

Consent API gets consent details across the Contact, Contact Point Type Consent, Data Use Purpose, Individual, Lead, Person Account,
and User objects when the records have a lookup relationship.

The following table shows how the API responses are determined. If the consulted fields find conflicting consent preferences, the response
returns the least permissive preference. For example, if Contact.HasOptedOutOfEmail is false, but Lead.HasOptedOutOfEmail is true,
the response indicates that you can’t proceed with emailing the user.

When you select email as the action, the API only aggregates consent for records that contain the same email address. If the record ID
specified in the URI is associated with a record that contains a different email address, the consent settings of the associated record aren’t
included in the API response.

Note: When the API compares consent settings across records, it doesn’t incorporate settings from converted leads.

**Action** **Fields Consulted** **API Response** **Response Schema**


email
Contact.HasOptedOutOfEmail


Within the time range {
if specified in

"<ID/Email>" :

ContactPointTypeConsent:


-----

ContactPointTypeConsent.ContactPointType Returns TRUE if all {

consulted field values

ContactPointTypeConsent.EffectiveFrom "result" : "<Success/errormessage>",

are 0.

ContactPointTypeConsent.EffectiveTo "proceed" : { "emailResult" : "<Success/errormessage>",
Returns FALSE if any

email : “<true/false>” }

ContactPointTypeConsent.PrivacyConsentStatus
consulted field value is
}
DataUsePurpose.Name 1 or if no related
Contact, Contact Point }
Lead.HasOptedOutOfEmail
Type Consent, Lead, or

PersonAccount.HasOptedOutOfEmail Person Account object
exists.


fax
Contact.HasOptedOutOfFax Returns TRUE if all {

consulted field values

DataUsePurpose.Name "<ID/Email>" :

are 0.

Lead.HasOptedOutOfFax {
Returns FALSE if any
PersonAccount.HasOptedOutOfFax "result" : "<Success/errormessage>",
consulted field value is


geotrack
DataUsePurpose.Name

Individual.HasOptedOutGeoTracking

mail
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


1 or if no related "proceed" : { "faxResult" : "<Success/errormessage>", fax
Contact, Lead, or : "<true/false>" }
Person Account object
}
exists.

}

Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is


1 or if no related "proceed" : { "geotrackResult" : "<Success/errormessage>",
Individual object exists. "geotrack" : "<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "mailingResult" : "<Success/errormessage>",

"mail" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related
}
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


-----

phone
Contact.DoNotCall Within the time range {

if specified in

ContactPointTypeConsent.ContactPointType "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveFrom {
Returns TRUE if all

ContactPointTypeConsent.EffectiveTo "result" : "<Success/errormessage>",

consulted field values

ContactPointTypeConsent.PrivacyConsentStatus are 0. "proceed" : { "phoneResult" : "<Success/errormessage>",

"phone" : "<true/false>" }

DataUsePurpose.Name Returns FALSE if any
consulted field value is }
Lead.DoNotCall
1 or if no related
}
PersonAccount.DoNotCall
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


portability
DataUsePurpose.Name

Individual.SendIndividualData

process
DataUsePurpose.Name

Individual.HasOptedOutProcessing

profile
DataUsePurpose.Name

Individual.HasOptedOutProfiling


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "profileResult" : "<Success/errormessage>",
Individual object exists. "profile" : "<true/false>" }

}

}


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

0 or if no related "proceed" : { "portabilityResult" :
Individual object exists. "<Success/errormessage>", "portability" : "<true/false>"
}

}

}


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "processResult" : "<Success/errormessage>",
Individual object exists. "process" : "<true/false>" }

}

}


-----

shouldforget
DataUsePurpose.Name

Individual.ShouldForget

social
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

0 or if no related "proceed" : { "shouldForgetResult" :
Individual object exists. "<Success/errormessage>", "shouldforget" :
"<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "socialResult" : "<Success/errormessage>",

"social" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related
}
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


solicit
DataUsePurpose.Name

Individual.HasOptedOutSolicit

storepiielsewhere DataUsePurpose.Name

Individual.CanStorePiiElsewhere


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

1.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

0 or if no related "proceed" : { "storePIIElsewhereResult" :
Individual object exists. "<Success/errormessage>", "storepiielsewhere" :
"<true/false>" }

}


Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is

1 or if no related "proceed" : { "solicitResult" : "<Success/errormessage>",
Individual object exists. "solicit" : "<true/false>" }

}

}


-----

track
DataUsePurpose.Name

Individual.HasOptedOutTracking

web
ContactPointTypeConsent.ContactPointType

ContactPointTypeConsent.EffectiveFrom


}

Returns TRUE if the {
consulted field value is

"<ID/Email>" :

0.

{

Returns FALSE if the
"result" : "<Success/errormessage>",
consulted field value is


1 or if no related "proceed" : { "trackResult" : "<Success/errormessage>",
Individual object exists. "track" : "<true/false>" }

}

}


ContactPointTypeConsent.ContactPointType Within the time range {

if specified in

ContactPointTypeConsent.EffectiveFrom "<ID/Email>" :

ContactPointTypeConsent:

ContactPointTypeConsent.EffectiveTo {
Returns TRUE if all

ContactPointTypeConsent.PrivacyConsentStatus "result" : "<Success/errormessage>",

consulted field values

DataUsePurpose.Name are 0. "proceed" : { "webResult" : "<Success/errormessage>",

"web" : "<true/false>" }

Returns FALSE if any
consulted field value is }
1 or if no related
}
Contact, Contact Point
Type Consent, Lead, or
Person Account object
exists.


##### Syntax

**URI**
```
  /services/data/vXX.X/consent/multiaction?actions=listOfActions&ids=listOfIds

```
**Formats**
JSON

**HTTP methods**
GET

**Authentication**
```
  Authorization: Bearer token

```
**Request body**
```
  None

```
**Request parameters**

```
actions

```

Required. Comma-separated list of proposed actions.

If this parameter is used, `action` can't be used.


-----

`aggregatedConsent` Optional: true or false. `aggregatedConsent` is the same as
```
                 aggregatedConsent=true. If true, one result is returned indicating whether

```
to proceed or not, rather than a result for each ID. If any ID in the list returns false, the
aggregated result is false.

```
datetime

```

Optional. The timestamp for which consent is determined. The value is converted to
the UTC timezone and must be formatted as described in Valid Date and DateTime
Formats. If not specified, defaults to the current date and time.


`ids` Required. Comma-separated list of IDs. The ID can be the record ID or the email address
listed on the record.

```
policy

```

Optional. Use `policy=requireExplicitConsent` to specify in the API
response whether explicit consent was given for a contact point channel. The API
returns an infoNotFound response when consent isn’t specified.

This parameter is available in API version 49.0 and later.


`purpose` Optional. The reason for contacting a customer.

`verbose` Optional: true or false. verbose is the same as verbose=true. Verbose responses
are slower than non-verbose responses. See the examples for a verbose response.

##### Example

**Request for Multiaction URI structure**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/consent/multiaction?actions=track,geotrack,email&ids=003xx000008TiyY,00Qxx00000skwO,dek65@tf7h.com
   -H "Authorization: Bearer token"

```
**Request for email addresses as IDs, specified purpose and timespan, and a verbose response**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/consent/action/email?ids=j0t5t5b2@tkbxp5ia.com,4quxlswo@23wj7pwh.com&datetime=2018-12-12T00:00:00Z&purpose=billing&verbose=true
   -H "Authorization: Bearer token"

```
**Response Body**


-----

#### Use the Consent API with Data Cloud

The Consent API supports Data Cloud. Use the Consent API to read and write to the Data Cloud profile. Contact your Salesforce
Representative for consumer rights guidance within Data Cloud.

##### Required Permissions

To use Data Cloud parameters for Consent API, you must have either the ModifyAllData or the ConsentApiUpdate user permission.
Requiring a perm ensures that the Salesforce admin gives explicit permission. These parameters write org-wide consent data, such as
links between records and the value of consent flags, which are usually inaccessible to non-admin users.

##### Actions Supported by Consent API with Data Cloud

|Action|Description|
|---|---|
|Processing|This action is used to restrict processing of data in Data Cloud processes such as query and segmentation.|


-----

|Action|Description|
|---|---|
|Portability|This action is used to allow export of Data Cloud profile data.|
|ShouldForget|This action indicates the right to be forgotten, which means permanently deleting PII (Personally Identifiable Information) data and any related records. After a profile is processed, it can no longer be used again.|


##### Data Cloud Read Parameters

The Consent API allows you to gather information about the Data Cloud profile. Use the mode and `ids` Data Cloud parameters as
described below.

##### Syntax

**HTTP method**
GET

**Available since release:**
48.0

**URI**

Note: You can access the consent API using three different URIs based on the Action. The Actions supported are
```
    processing,portability, and shouldforget.
  /services/data/vXX.X/consent/action/processing?ids=<list_of_ids>&mode=<cdp>
  /services/data/vXX.X/consent/action/portability?ids=<list_of_ids>&mode=<cdp>
  /services/data/vXX.X/consent/action/shouldforget?ids=<list_of_ids>&mode=<cdp>

```
**Request parameters**

**Parameter** **Description**

`ids` Required. Comma-separated list of IDs. The ID provided must be present in a field
mapped to Individual.Individual Id.

`mode` Optional. Default is normal. Valid value to retrieve a Data Cloud profile is cdp.

##### Read Example

**URI**
```
  /services/data/v62.0/consent/action/portability?ids=00932I3SU92&mode=cdp

```
**Response**
```
  { "j00932I3SU92" : { "result" : "Success", "proceed" : { "portability" : "true"
  "portabilityResult" : "Success" } } }

##### Write Parameters

```
The Consent API also allows you to write information to the Data Cloud profile. Use the ids, mode, and status parameters as described
below.


-----

Note: You can update your consent information with the consent API using three different URIs. The URIs are based on the action
that is to be performed on the Data Cloud profile. The actions supported are `processing,` `portability, and`
```
  shouldforget.

##### Syntax

```
**HTTP method**
PATCH

**Available since release**
50.0

**URI when action is processing**
```
  /services/data/vXX.X/consent/action/processing?ids=list_of_ids&mode=cdp&status=optin
  or optout

```
**Request parameters when action is processing**

**Parameter** **Description**

`ids` Required. Comma-separated list of IDs. The ID provided must be present in a field
mapped to Individual.Individual Id.

`mode` Optional. Default is normal. Valid value to use for updating a Data Cloud profile is cdp.

`status` Required. Status of the consent. Allowed values are `optin` or `optout. However,`
when action is processing use status as `optout.`

**URI when action is shouldforget**
```
  /services/data/vXX.X/consent/action/shouldforget?ids=list_of_ids&mode=cdp&status=optin
  or optout

```
**Request parameters when action is shouldforget**

**Parameter** **Description**

`ids` Required. Comma-separated list of IDs. The ID provided must be present in a field
mapped to Individual.Individual Id.

`mode` Optional. Default is normal. Valid value to use for updating a Data CloudCDP profile is
```
                   cdp.

```
`status` Required. Status of the consent. Allowed values are `optin` or `optout. However,`
when action is shouldforget use status as `optin.`

**URI action is portability**
```
  /services/data/vXX.X/consent/action/portability?ids=list_of_ids&mode=cdp&status=optin
  or optout

```

-----

**Request parameters when action is portability**

**Parameter** **Description**

`ids` Required. Comma-separated list of IDs. The ID provided must be present in a field
mapped to Individual.Individual Id.

`mode` Optional. Default is normal. Valid value to use for updating a Data Cloud profile is cdp.

`status` Required. Status of the consent. Allowed values are optin or optout. When action
is portability use status as `optin.`

```
  aws_s3_bucket_id
  aws_access_key_id
  aws_secret_access_key
  aws_s3_folder
  aws_region

##### Write Example

```
**When action is processing**
```
  body: {}

```
**When action is portability**
```
    body:{
       }

```
**When action is shouldforget**


Required only when mode is 'cdp' and the action is 'portability'. This parameter must
be passed in as part of the PATCH request body. This parameter is used to pass the S3
bucket location for portability requests to Data Cloud.

Required only when mode is 'cdp' and the action is 'portability'. This parameter must
be passed in as part of the PATCH request body. This parameter is used to pass the S3
bucket access key for portability requests to Data Cloud.

Required only when mode is 'cdp' and the action is 'portability'. This parameter must
be passed in as part of the PATCH request body. This parameter is used to pass the S3
bucket secret access key for portability requests to Data Cloud.

Required only when mode is 'cdp' and the action is 'portability'. This parameter must
be passed in as part of the PATCH request body. This parameter is used to pass the S3
bucket folder for portability requests to Data Cloud.

Required only when mode is 'cdp' and the action is 'portability'. This parameter must
be passed in as part of the PATCH request body. This parameter is used to pass the S3
bucket's aws region for portability requests to Data Cloud.


-----
