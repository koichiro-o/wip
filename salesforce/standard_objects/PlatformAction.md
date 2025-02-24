#### PlatformAction

PlatformAction is a virtual read-only object. It enables you to query for actions displayed in the UI, given a user, a context, device format,
and a record ID. Examples include standard and custom buttons, quick actions, and productivity actions.

##### Supported Calls
```
describeSObjects(), query()

 Fields

```
```
ActionListContext
ActionTarget

```

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Required. The list context this action applies to. Valid values are:

**•** `Assistant`

**•** `BannerPhoto`

**•** `Chatter`

**•** `Dockable`

**•** `FeedElement`

**•** `Flexipage`

**•** `Global`

**•** `ListView`

**•** `ListViewDefinition`

**•** `ListViewRecord`

**•** `Lookup`

**•** `MruList`

**•** `MruRow`

**•** `ObjectHomeChart`

**•** `Photo`

**•** `Record`

**•** `RecordEdit`

**•** `RelatedList`

**•** `RelatedListRecord`

**Type**
textarea


-----

```
ActionTargetType
ActionTargetUrl
Category
ConfirmationMessage

```

**Properties**
Nillable

**Description**
The URL to invoke or describe the action when the action is invoked. If the action is a standard
button overridden by a Visualforce page, the ActionTarget returns the URL of the Visualforce
page, such as `/apex/pagename.`

This field is available in API version 35.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The type of the target when this action is triggered. Valid values are:

**•** `Describe—applies to actions with a user interface, such as quick actions`

**•** `Invoke—applies to actions with no user interface, such as action links or invocable`
actions

**•** `Visualforce—applies to standard buttons overridden by a Visualforce page`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
URL to invoke or describe the action when the action is invoked. This field is deprecated in
API version 35.0 and later. Use `ActionTarget instead.`

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Applies only to action links. Denotes whether the action link shows up in the feed item list
of actions or the overflow list of actions. Valid values are:

**•** `Primary`

**•** `Overflow`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort


-----

```
DeviceFormat
ExternalId
GroupId
IconContentType
IconHeight

```

**Description**
Applies only to action links. The message to display before the action is invoked. Field is null
if no confirmation is required before invoking the action.

**Type**
picklist

**Properties**
Defaulted on create, Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Specifies which action icon the PlatformAction query returns. If this field isn’t specified, it
defaults to Phone. Valid values are:

**•** `Aloha`

**•** `Desktop`

**•** `Phone`

**•** `Tablet`

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID for the PlatformAction. If the action doesn’t have an ID, its API name is used.

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The unique ID of a group of action links.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The content type—such as .jpg, .gif, or .png—of the icon for this action. Applies to both
custom and standard icons assigned to actions.

**Type**
int


-----

```
IconUrl
IconWidth
InvocationStatus
InvokedByUserId

```

**Properties**
Filter, Group, Nillable, Sort

**Description**
The height of the icon for this action. Applies only to standard icons.

**Type**
url

**Properties**
Filter, Group, Nillable, Sort

**Description**
The URL of the icon for this action.

**Type**
int

**Properties**
Filter, Group, Nillable, Sort

**Description**
The width of the icon for this action. Applies only to standard icons.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The status of the action within the feed item. Applies to action links only. Valid values are:

**•** `Failed`

**•** `New`

**•** `Pending`

**•** `Successful`

**Type**
reference

**Properties**
Filter, Group, Nillable, Sort

**Description**
The ID of the user who most recently invoked this action within the current feed item. Applies
to action links only.

This is a relationship field.

**Relationship Name**
InvokedByUser


-----

```
IsGroupDefault
IsMassAction
Label
PrimaryColor
RelatedListRecordId

```

**Relationship Type**
Lookup

**Refers To**
User

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Denotes whether this action is the default in an action link group. False for other action types.
Applies to action links only.

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort

**Description**
Indicates whether the action can be performed on multiple records.

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
The label to display for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The primary color of the icon for this action.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
Represents the ID of a record in an object’s related list.


-----

```
RelatedSourceEntity
Section
SourceEntity
Subtype

```

This field is available in API version 38.0 and later.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
When the ActionListContext is RelatedList or RelatedListRecord, this field represents
the API name of the related list to which the action belongs.

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
The section of the user interface the action resides in. Applicable only to Lightning Experience.
Valid values are:

**•** ActivityComposer

**•** CollaborateComposer

**•** NotesComposer

**•** Page

**•** SingleActionLinks

This field is available in API version 35.0 and later.

**Type**
string

**Properties**
Filter, Group, Sort

**Description**
Required. The object or record with which this action is associated.

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The subtype of the action. For quick actions, the subtype is `QuickActionType. For`
custom buttons, the subtype is `WebLinkTypeEnum. For action links, subtypes are` `Api,`
```
  ApiAsync, Download, and Ui. Standard buttons and productivity actions have no

```
subtype.


-----

```
TargetObject
TargetUrl
Type

##### Usage

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The type of object record the action creates, such as a contact or opportunity.

This field is available in API version 41.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
The URL that a custom button or link points to.

This field is available in API version 41.0 and later.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
The type of the action. Valid values are:

**•** `ActionLink—An indicator on a feed element that targets an API, a web page, or a`
file, represented by a button in the Salesforce Chatter feed UI.

**•** `CustomButton—When clicked, opens a URL or a Visualforce page in a window or`
executes JavaScript.

**•** `InvocableAction`

**•** `ProductivityAction—Productivity actions are predefined and attached to a`
limited set of objects. Productivity actions include Send Email, Call, Map, View Website,
and Read News. Except for the Call action, you can’t edit productivity actions.

**•** `QuickAction—A global or object-specific action.`

**•** `StandardButton—A predefined Salesforce button such as New, Edit, and Delete.`


PlatformAction can be described using describeSObject().

You can directly query for PlatformAction. For example, this query returns all fields for actions associated with each of the records of the
listed objects:


-----

Note: To query PlatformAction, provide the `ActionListContext` and `SourceEntity. If you query for`
`ActionListContext` with a value of RelatedList, and don't specify a RelatedSourceEntity, the query returns
the API name of the related list. In API v43.0 and before, `SourceEntity = 'Object API Name' and`
`ActionListContext = 'ListView'` is an invalid combination to fetch quick actions in a SOQL query. Use
`SourceEntity = 'Object ID' and ActionListContext = 'ListView'` instead.

This query uses multiple `ActionListContext` values in its `WHERE` clause to return all actions in the Lightning Experience user
interface (DeviceFormat = 'Desktop') for the specified object:
```
SELECT ActionListContext, Label, Type, Subtype, Section, SourceEntity,
   RelatedSourceEntity, ActionTarget, ActionTargetType, ApiName, Category,
   ConfirmationMessage, DeviceFormat, ExternalId, GroupId, IconContentType,
   IconHeight, IconUrl, IconWidth, Id, InvocationStatus, InvokedByUserId,
   IsGroupDefault, LastModifiedDate, PrimaryColor
FROM PlatformAction
WHERE ActionListContext IN ('Record','Chatter','RelatedList') AND
    SourceEntity = '001xx000003DlvX' AND
    DeviceFormat = 'Desktop'
