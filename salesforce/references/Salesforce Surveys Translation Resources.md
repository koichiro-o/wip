### Salesforce Surveys Translation Resources

```
Use REST APIs to translate survey fields, view, update, or delete translated survey fields. The translated values of surveys fields are stored
in Flow fields.

The following survey fields can be translated:

**•** Survey name

**•** Pause message

**•** Welcome message

**•** Questions

**•** Answer choices and ranking items

**•** Thank you message

IN THIS SECTION:

Add or Change the Translation of a Survey Field
If a survey field can be translated or is already translated into a particular language, you can add or change the translated value of
the survey field. This resource is available in REST API version 48.0 and later.

Add or Update the Translated Value of Multiple Survey Fields in One or More Languages
If one or more survey fields can be translated or are already translated, you can add or update the translated values of the survey
fields in the languages into which survey fields can be translated. This resource is available in REST API version 48.0 and later.

Delete the Translated Value of a Survey Field
After a survey field is translated into a particular language, you can delete the translated value of the survey field. This resource is
available in REST API version 48.0 and later.

Delete the Translated Value of Multiple Survey Fields in One or More Languages
After survey fields are translated into one or more languages, you can delete the translated values of multiple survey fields. This
resource is available in REST API version 48.0 and later.

Get Translated Value of a Survey Field
After a survey field is translated into a particular language, you can use this resource to get the translated value of the survey field.
This resource is available in REST API version 48.0 and later.

Get the Translated Values of Multiple Survey Fields in One or More Languages
After survey fields are translated into one or more languages, you can view the translated values of multiple survey fields in the
translated languages. This resource is available in REST API versions 48.0 and later.


-----

#### Add or Change the Translation of a Survey Field

If a survey field can be translated or is already translated into a particular language, you can add or change the translated value of the
survey field. This resource is available in REST API version 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/record/developerName/language

```
**Formats**
JSON

**HTTP methods**
POST

**Authentication**
```
  Authorization: Bearer token

```
**Request body JSON example**
```
  {
  "value": "China"
  }

```
**Request parameters**

**Parameter** **Description**

`developerName` Optional. Developer name of the flow field.

`language` Optional Translated language of the flow field.

`value` Required. Translated value of the flow field.

**Response parameters**

**Parameter** **Description**

`createdBy` ID of the user who translated the flow field.

`createdDate` Date and time the flow field was translated.

`developerName` Developer name of the flow field.

`language` Language into which the flow field was translated.

`value` Translated value of the flow field.

`isOutofDate` Indicates if the flow field is out of date.


-----

in One or More Languages

##### Example
```
{
  "createdBy": "005xxx",
  "createdDate": "2018-09-14T00:10:30Z",
  "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
  "language": "zh_CN",
  "value": "��",
  "isOutOfDate": true
}

#### Add or Update the Translated Value of Multiple Survey Fields in One or More Languages

```
If one or more survey fields can be translated or are already translated, you can add or update the translated values of the survey fields
in the languages into which survey fields can be translated. This resource is available in REST API version 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/records/upsert

```
**Formats**
JSON

**HTTP methods**
POST

**Request body JSON example**
```
  [
   {
    "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
    "language": "en_US",
    "value": "China"
   },
   {
    "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
    "language": "zh_CN",
    "value": "��"
   }
  ]

```
**Request parameters**

**Parameter** **Description**

`developerName` Required. Developer name of the flow field.

`language` Required. Language into which the flow field is translated.


-----

`value` Required. New or updated value of the flow field.

**Response parameters**

**Parameter** **Description**

`createdBy` ID of the user who translated the flow field.

`createdDate` Date and time the flow field was translated.

`developerName` Developer name of the flow field.

`language` Language into which the flow field was translated.

`value` Updated value of the flow field.

`isOutofDate` Indicates if the flow field is out of date.

##### Example
```
[
  {
   "createdBy": "005xxx",
   "createdDate": "2018-09-14T00:10:30Z",
   "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
   "language": "en_US",
   "value": "China",
   "isOutOfDate": false
  },
  {
   "createdBy": "005xxx",
   "createdDate": "2018-09-14T00:10:30Z",
   "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
   "language": "zh_CN",
   "value": "��",
   "isOutOfDate": false
  }
]

#### Delete the Translated Value of a Survey Field

```
After a survey field is translated into a particular language, you can delete the translated value of the survey field. This resource is available
in REST API version 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`


-----

or More Languages

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/record/developerName/language

```
**Formats**
JSON

**HTTP methods**
DELETE

**Request parameters**

**Parameter** **Description**

`developerName` The developer name of the flow field. For example,
```
                  Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel

```
`language` Language of the translated field. Possible values are:

**•** `da`

**•** `nl_NL`

**•** `fi`

**•** `fr`

**•** `de`

#### Delete the Translated Value of Multiple Survey Fields in One or More Languages

After survey fields are translated into one or more languages, you can delete the translated values of multiple survey fields. This resource
is available in REST API version 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/records/delete

```
**Formats**
JSON

**HTTP methods**
POST

**Request body JSON example**


-----

**Request parameters**

**Parameter** **Description**

`developerName` Required. Developer name of the flow field.

`language` Required. Language into which the flow field was translated.

#### Get Translated Value of a Survey Field

After a survey field is translated into a particular language, you can use this resource to get the translated value of the survey field. This
resource is available in REST API version 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/record/developerName/language

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
None

**Request parameters**

**Path Parameter** **Description**

`developerName` Required. The developer name of the flow field. For example,
```
                  Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel

```
`language` Required. Language of the translated field. Possible values are:

**•** `da`

**•** `nl_NL`

**•** `fi`

**•** `fr`

**•** `de`


-----

More Languages

**Response parameters**

**Parameter** **Description**

`createdBy` ID of the user who translated the flow field.

`createdDate` Date and time the flow field was translated.

`developerName` Developer name of the flow field.

`language` Language into which the flow field was translated.

`value` Translated value of the flow field.

`isOutofDate` Indicates if the flow field is out of date.

##### Example
```
{
  "createdBy": "005xxx",
  "createdDate": "2018-09-14T00:10:30Z",
  "developerName": "Flow.Flow.MyFlow.1.Choice.Choice_1_Master.InputLabel",
  "language": "zh_CN",
  "value": "��",
  "isOutOfDate": true
}

#### Get the Translated Values of Multiple Survey Fields in One or More Languages

```
After survey fields are translated into one or more languages, you can view the translated values of multiple survey fields in the translated
languages. This resource is available in REST API versions 48.0 and later.

Note: This URI can only be used for the flow process type `Survey.`

##### Syntax

**URI**
```
  /services/data/vXX.X/localizedvalue/records/get

```
**Formats**
JSON

**HTTP methods**
POST

**Request body JSON example**


-----

More Languages


**Request parameters**

**Parameter** **Description**

`developerName` Required. Developer name of the flow field.

`language` Required. Language into which the flow field was translated.

**Response parameters**

**Parameter** **Description**

`createdBy` ID of the user who translated the flow field.

`createdDate` Date and time the flow field was translated.

`developerName` Developer name of the flow field.

`language` Language into which the flow field was translated.

`value` Translated value of the flow field.

`isOutofDate` Indicates if the flow field is out of date.

##### Example


-----
