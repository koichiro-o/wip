### Consent Write

Your users can store consent preferences in different locations. The Consent Write API can update and write consent across multiple
records through a single API call, helping you sync consent across records or populate the new Consent data model. This resource is
available in REST API version 48.0 and later.

Consent API writes consent values across the Contact, Contact Point Type Consent, Data Use Purpose, Individual, Lead, Person Account,
and User objects when the records have a lookup relationship or share an email address. This API can also write to the Data Cloud
Individual record. The Consent API can't locate records in which the email address field is protected by Platform Encryption.

Note: For the Spring ‘21 release, the API only takes in a single email address. Any record with a matching email address is updated
based on the parameters set in the API call.

All records with the email address listed are updated. If the Create Individual parameter is selected and no Individual record exists, the
API creates an Individual record. If warranted, the API also creates a Contact Point Type Consent and Contact Point Email record.

Only Data Cloud uses the request body. If not passing anything in the request body, pass in an empty object {}.

#### Syntax

**URI**
```
  /services/data/vXX.X/consent/action/action?ids=listOfIds

```
**Formats**
JSON

**HTTP methods**
PATCH

**Authentication**
```
  Authorization: Bearer token

```
**Request parameters**

```
blobParam

```

Optional. Use to pass information to Data Cloud, such as portability write location. Use
only for `mode=cdp. This parameter must be passed in as part of the PATCH request`
body.


`captureDate` Optional. The date and time when consent is captured. The default is the date and
time the API call is made.

`captureContactPointType` Optional. Describes how consent is captured (web, phone, email). Supported values
are:

**•** `email`

**•** `phone`

**•** `web` (default)

`captureSource` Optional. The source through which consent is captured. The default capture source
is Consent API. Max length 255 characters.


-----

```
consentName

```

Optional. Use to set the name for any new consent records. Default is: Individual
```
Name-Datetime (<Name> 2019-03-31T15:47:57). Max length is

```
255 characters.


`createIndividual` Optional. Boolean. If set to `true and the API call includes an email address that`
matches multiple records without an Individual object, then an Individual object is

created. Any consent records with an email address that match the email in the API
call are linked to the new Individual object. If multiple records are found, then any
records not linked to an Individual object is linked to the Individual object found in the
other records. If more than one Individual object is found on the matching records,
then the call is rejected.

`doubleOptIn` Optional. The date and time that the double opt-in is completed, formatted as described
in Valid Date and DateTime Formats.

`effectiveFrom` Optional. The date from which consent is effective, formatted as described in Valid
Date and DateTime Formats. The default is the date the API call is made.

`effectiveTo` Optional. The date through which consent is effective, formatted as described in Valid
Date and DateTime Formats.

```
ids
individualName

```

Required. The email address used to sync consent. The ID can be the record ID or the
email address listed on the record. When `mode=cdp, the ID value is a string equal`
to the Individual ID attribute.

Optional. The name of the person in an Individual record. If a name isn’t provided for
a new Individual record, then the local part of the passed-in email address is used. Max
length is 80 characters.


`mode` Optional. Default is `normal. The allowed modes are:` `normal` or `cdp. With`
```
                 mode=cdp, the request is passed to the Data Cloud platform to get or write consent.

```
The `mode=cdp` parameter only supports the `action,` `blobParam, and` `ids`
parameters.

```
  purposeName
  status

```
**Action**

Allowed values are:

**•** email

**•** fax

**•** geotrack

**•** mailing

**•** phone


Optional. The data use purpose for which consent is provided. Must use an existing
data use purpose that you previously created. If more than one purpose with the same
name exists, only one purpose is selected.

Required. Status of the consent (OptIn, OptOut, Seen, NotSeen.) If action exists
on an Individual object (for example, tracking or processing), the only valid values are
`OptIn` and `OptOut.`


-----

**•** portability

**•** process

**•** profile

**•** shouldForget

**•** social

**•** solicit

**•** storePiiElsewhere

**•** track

**•** web

#### Security

To call the Consent Write API, you must have either the ModifyAllData or the ConsentApiUpdate user permission. This API writes org-wide
consent data, such as links between records and the value of consent flags, and not just records to which the user ordinarily has access.
The ConsentApiUpdate user permission grants full write permission to the user during the Consent Write API call.

#### Example

**Example Request**
```
  curl -X PATCH
  https://MyDomainName.my.salesforce.com/services/data/v62.0/consent/action/<action>?ids=<email-OR-recordID>&status=<optout/optin/seen/notseen>&createIndividual=<true/false>
   -H "Content-Type: application/json" -d "@exampleRequestBody.json"

```
**Example Request Body**
```
  {}

```
**Example Response Body**
```
  {
   "<email-OR-recordID>" : {
    "result" : "Success",
    "edited" : [{
      "objectType" : "<Contact, Lead, User, etc.>",
      "field" : "<HasOptedOutofFax, DoNotCall,etc>",
      "valueOfField" : "<true/false>",
      "id" : "<recordID>"
    }],
   }
  }
