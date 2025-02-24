#### ActionLinkTemplate

Action link templates let you reuse action link definitions and package and distribute action links. An action link is a button on a feed
element. Clicking an action link can take a user to another Web page, initiate a file download, or invoke an API call to an external server
or Salesforce. Use action links to integrate Salesforce and third-party services into the feed. This object is available in API version 33.0
and later.


-----

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
Only users with the “Customize Application” permission can modify or delete this object.

##### Fields

```
ActionLinkGroupTemplateId
ActionUrl

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID of the ActionLinkGroupTemplate with which this action link template is
associated.

This is a relationship field.

**Relationship Name**
ActionLinkGroupTemplate

**Relationship Type**
Lookup

**Refers To**
ActionLinkGroupTemplate

**Type**
textarea

**Properties**
Create, Update

**Description**
The action link URL. For example, a `Ui` action link URL is a Web page. A
`Download` action link URL is a link to the file to download. Ui and Download
action link URLs are provided to clients. An `Api` or ApiAsync action link URL
is a REST resource. `Api` and `ApiAsync` action link URLs aren’t provided to
clients. Links to Salesforce can be relative. All other links must be absolute and
start with `https://.`

Links to resources hosted on Salesforce servers can be relative, starting with a
```
  /. All other links must be absolute and start with https://. This field can

```
contain context variables and binding variables in the form
```
  {!Bindings.key}, for example,
  https://www.example.com/{!Bindings.itemId}. Set the binding

```
variable’s value when you instantiate the action link group from the template.


-----

```
Headers
IsConfirmationRequired
IsGroupDefault
Label

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP headers sent when corresponding action links are invoked.
This field can be used only for `Api` and `ApiAsync` action links. This field can
contain context variables and binding variables in the form
```
  {!Bindings.key}.

```
**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If `true, a confirmation dialog appears before the action is executed.`

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
If true, action links derived from this template are the default or primary action
in their action groups. There can be only one default action per action group.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
A custom label to display on the action link button. If none of the LabelKey
values make sense for an action link, use a custom label. Set the LabelKey
field to `None` and enter a label name in the `Label field.`

Action links have four states: new, pending, success, and failed. These strings are
appended to the label for each state:

**•** _Label_

**•** _Label Pending_

**•** _Label Success_

**•** _Label Failed_

For example, if the value of Label is “Call Home,” the values of the four action
link states are: Call Home, Call Home Pending, Call Home Success, and Call Home
Failed.


-----

```
LabelKey
LinkType
Method

```

If `LabelKey` has any value other than `None, the Label` field is empty.

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
Key for the set of labels to display for these action link states: new, pending,
success, failed. For example, the Approve set contains these labels: Approve,
[Pending, Approved, Failed. For a complete list of keys and labels, see Action Link](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)
[Labels in the Connect REST API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.chatterapi.meta/chatterapi/connect_appendices_action_links_labels.htm)

If none of the label key values make sense for an action link, set this field to None
and enter a custom label name in the Label field.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The type of action link. One of these values:

**•** `Api—The action link calls a synchronous API at the action URL. Salesforce`
sets the status to SuccessfulStatus or FailedStatus based on
the HTTP status code returned by your server.

**•** `ApiAsync—The action link calls an asynchronous API at the action URL.`
The action remains in a `PendingStatus` state until a third party makes
a request to /connect/action-links/actionLinkId to set the
status to `SuccessfulStatus` or `FailedStatus` when the
asynchronous operation is complete.

**•** `Download—The action link downloads a file from the action URL.`

**•** `Ui—The action link takes the user to a web page at the action URL.`

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
HTTP method for the action URL. One of these values:

**•** `HttpDelete—Returns HTTP 204 on success. Response body or output`
class is empty.

**•** `HttpGet—Returns HTTP 200 on success.`

**•** `HttpHead—Returns HTTP 200 on success. Response body or output class`
is empty.


-----

```
Position
RequestBody
UserAlias
UserVisibility

```


**•** `HttpPatch—Returns HTTP 200 on success or HTTP 204 if the response`
body or output class is empty.

**•** `HttpPost—Returns HTTP 201 on success or HTTP 204 if the response`
body or output class is empty. Exceptions are the batch posting resources
and methods, which return HTTP 200 on success.

**•** `HttpPut—Return HTTP 200 on success or HTTP 204 if the response body`
or output class is empty.

`Ui` and `Download` action links must use `HttpGet.`

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
An integer specifying the position of the action link template relative to other
action links in the group. 0 is the first position.

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Template for the HTTP request body sent when corresponding action links are
invoked. This field can be used only for `Api` and `ApiAsync` action links. This
field can contain context variables and binding variables in the form
```
  {!Bindings.key}.

```
**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
If you selected `CustomUser` or `CustomExcludedUser` for
```
  UserVisibility, this field is the alias for the custom user. Use the alias in

```
a template binding to specify the custom user when an action link group is
created using the template.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

**Description**
Who can see the action link. This value is set per action link, not per action link
group. One of these values:

**•** `Creator—Only the creator of the action link can see the action link.`

**•** `Everyone—Everyone can see the action link.`

**•** `EveryoneButCreator—Everyone but the creator of the action link`
can see the action link.

**•** `Manager—Only the manager of the creator of the action link can see the`
action link.

**•** `CustomUser—Only the custom user can see the action link.`

**•** `CustomExcludedUser—Everyone but the custom user can see the`
action link.

##### Usage

Create action link templates in Setup. Use Apex classes in the `ConnectApi` namespace or Connect REST API to instantiate action
links from templates and to post feed elements with the action links.

[For information about action links, see Working with Action Links in the Apex Developer Guide or the Connect REST API Developer Guide.](https://developer.salesforce.com/docs/atlas.en-us.254.0.apexcode.meta/pages/connectapi_features_action_links.htm?search_text=working%20with%20action%20links)
