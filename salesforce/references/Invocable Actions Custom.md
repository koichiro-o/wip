### Invocable Actions Custom

```
Represents custom invocable actions that can be statically invoked. You can also get basic information for each type of action.

IN THIS SECTION:

Deploy Data Kit Components by Using Deploy Data Kit Components Flow
Deploys data kit components sequentially in one call. The response body contains the Flow_InterviewGuid. This flow is available by
using the REST API version 61.0 and later.

Get Custom Invocable Actions
Gets the list of all custom invocable actions. Some actions require special access. This resource is available in REST API version 32.0
and later.

Return HTTP Headers for Custom Invocable Actions
Returns only the headers that are returned by sending a GET request to the custom invocable actions resource. This gives you a
chance to see returned header values of the GET request before retrieving the content. This resource is available in REST API version
32.0 and later.

SEE ALSO:

_[Apex Developer Guide : InvocableMethod Annotation](https://developer.salesforce.com/docs/atlas.en-us.252.0.apexcode.meta/apexcode/apex_classes_annotation_InvocableMethod.htm)_

#### Deploy Data Kit Components by Using Deploy Data Kit Components Flow

Deploys data kit components sequentially in one call. The response body contains the Flow_InterviewGuid. This flow is available by
using the REST API version 61.0 and later.

##### URI
```
/services/data/v61.0/actions/custom/flow/sfdatakit__DeployDataKitComponents

 Formats

```
JSON, XML

##### HTTP Methods

POST


-----

Components Flow

##### Authentication
```
Authorization: Bearer token

 Properties

```
Name Type Description

`dataKitComponentsInput` Array of Required. A collection of data kit
`sfdatakit__DeployComponentInput` components to deploy. The collection list

contains the payload details about the
components.

`dataKitNameInput` Text Required. The data kit name that contains
the components.

`dataKitDataSpaceInput` Text Optional. The name of the data space to
deploy the data kit. If a data space isn’t

defined, the system deploys the
components in the default data space.

##### Example

This example request triggers the Deployed Data Kit Components flow to deploy the data stream bundle, data lake objects, and data
transforms components from the MyTestDatakit data kit.

**Example Request**
```
  curl
  https://MyDomainName.my.salesforce.com/services/data/v62.0/actions/custom/flow/sfdatakit__DeployDataKitComponents

```
**Example Request Body**


-----

**Example Response Body**
```
  {
       "actionName": "sfdatakit__DeployDataKitComponents",
       "errors": null,
       "invocationId": null,
       "isSuccess": true,
       "outputValues": {
         "Flow__InterviewGuid": "43c0ccb801784ff02fa0c8a1919b1877f5-605b",
         "Flow__InterviewStatus": "Waiting"
       },
       "sortOrder": -1,
       "version": 1
    }

#### Get Custom Invocable Actions

```
Gets the list of all custom invocable actions. Some actions require special access. This resource is available in REST API version 32.0 and
later.

Sending email with the `emailAlert` [action counts against your daily email limit for workflows. For more information, see Daily](https://help.salesforce.com/apex/HTViewHelpDoc?id=workflow_limits_email.htm&language=en_US#workflow_limits_email)
[Allocations for Email Alerts in Salesforce Help.](https://help.salesforce.com/apex/HTViewHelpDoc?id=workflow_limits_email.htm&language=en_US#workflow_limits_email)

When invoking an Apex action using the POST method and supplying the inputs in the request, only the following primitive types are
supported as inputs:

**•** `Blob`


-----

**•** `Boolean`

**•** `Date`

**•** `Datetime`

**•** `Decimal`

**•** `Double`

**•** `ID`

**•** `Integer`

**•** `Long`

**•** `String`

**•** `Time`

Describe and invoke for an Apex action respect the profile access for the Apex class. If you don’t have access, an error is issued.

If you add an Apex action to a flow, and then remove the Invocable Method annotation from the Apex class, a runtime error in the flow
occurs.

When a flow user invokes an autolaunched flow, the active flow version runs. If there’s no active version, the latest version runs. When
a flow admin invokes a flow, the latest version always runs.

If any of these elements are used in a flow, packageable components that reference the elements aren’t automatically included in the
package.

**•** Apex action

**•** Email alerts

**•** Post to Chatter core action

**•** Quick Action core action

**•** Send Email core action

**•** Submit for Approval core action

For example, if you use an email alert, manually add the email template that’s used by that email alert. To deploy the package successfully,
manually add those referenced components to the package.

[For more information about actions, see the Actions Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.252.0.api_action.meta/api_action/)

##### Syntax

 URI
```
/services/data/vXX.X/actions/custom

 Formats

```
JSON, XML

##### HTTP Methods

\ GET


-----

##### Authentication
```
Authorization: Bearer token

 Request parameters

```
None required

##### Example

Example Request
```
curl https://MyDomainName.my.salesforce.com/services/data/v62.0/actions/custom -H
"Authorization: Bearer token"

```
Example Response Body
```
{
     "quickAction" : "/services/data/v62.0/actions/custom/quickAction",
     "apex" : "/services/data/v62.0/actions/custom/apex",
     "emailAlert" : "/services/data/v62.0/actions/custom/emailAlert",
     "flow" : "/services/data/v62.0/actions/custom/flow",
     "sendNotification" : "/services/data/v62.0/actions/custom/sendNotification",
     "generatePromptResponse" :
"/services/data/v60.0/actions/custom/generatePromptResponse"
     }

#### Return HTTP Headers for Custom Invocable Actions

```
Returns only the headers that are returned by sending a GET request to the custom invocable actions resource. This gives you a chance
to see returned header values of the GET request before retrieving the content. This resource is available in REST API version 32.0 and
later.

##### URI
```
/services/data/vXX.X/actions/custom

 Formats

```
JSON, XML

##### HTTP Methods

HEAD

##### Authentication
```
Authorization: Bearer token

```

-----

##### Request parameters

None required

##### Example

Example Request
```
curl -X HEAD --head
https://MyDomainName.my.salesforce.com/services/data/v62.0/actions/custom -H "Authorization:
 Bearer token"

```
Example Response Body
```
HTTP/1.1 200 OK
Date: Mon, 21 Nov 2022 22:56:26 GMT
