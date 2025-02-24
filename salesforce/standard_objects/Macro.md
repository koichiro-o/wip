#### Macro

Represents a macro, which is a set of instructions that tells the system to perform one or more tasks. This object is available in API version
32.0 and later.

##### Supported Calls
```
create(), delete(), describeLayout(), describeSObjects(), getDeleted(), getUpdated(), query(),
retrieve(), search(), update(), upsert()

 Fields

```
```
Description
FolderId
FolderName
IsAlohaSupported

```

**Type**
textarea

**Properties**
Create, Nillable, Update

**Description**
Description of what this macro does.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
Returns the ID of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
string

**Properties**
Filter, Nillable, Sort

**Description**
Name of the folder that contains the macro. Available in API version 44.0 and later.

**Type**
boolean

**Properties**
Defaulted on create, Filter


-----

```
IsLightningSupported
LastReferencedDate
LastViewedDate
Name
OwnerId
StartingContext

```

**Description**
Specifies whether the macro is supported in Salesforce Classic.

**Type**
boolean

**Properties**
Defaulted on create, Filter

**Description**
Specifies whether the macro is supported in Lightning Experience.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last referenced.

**Type**
dateTime

**Properties**
Filter, Nillable, Sort

**Description**
The date and time that the macro record was last viewed.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Name of the macro.

**Type**
reference

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
ID of the owner of the session record.

**Type**
picklist

**Properties**
Create, Filter, Group, Nillable, Restricted picklist, Sort


-----

**Description**
The object the macro performs actions on. In Salesforce Classic, macros are supported on
objects with both feed-based layouts and quick actions. In Lightning Experience, macros are
supported on standard and custom objects that allow quick actions and have a customizable
page layout.

##### Usage

A macro definition consists of a Macro object and several associated MacroInstruction objects.

First, create a Macro object. Then, create MacroInstructions that specify objects, operations, conditions, and targets for the macro.

A macro contains an ordered list of macro instructions whose index field, `sortOrder, is 0-based. If there’s an incorrect sequence of`
macro instructions, the macro doesn’t execute.

If you update a macro definition or add or remove instructions from a macro, make sure that the `sortOrder` field that defines the
execution order is correct. To delete an entire macro definition, invoke the delete operation on the Macro object.

The table describes the supported macro instruction targets and how they relate to each other.

Note: Strings indicated by `<brackets>` are variables. The variable description describes the required type. For example,
`Tab.<EntityApiName>` requires the entity name. If your custom entity name is `MyCustomObject, your target API is`
```
  Tab.MyCustomObject__c.

```
If a macro instruction listed in the table supports an implicit operation, you can use that operation as a direct child instruction without
explicitly specifying a target. The hyphens used in the table illustrate the hierarchical relationship between targets. A target isn't available
if its parent isn’t.

|Table 1: Macro Instruction Target Grammar and Hierarchy|Col2|
|---|---|
|Target API Name|Supported Operations|
|Tab.<EntityApiName>|SELECT, CLOSE (implicit)|
|- QuickAction.<EntityApiName>.<QuickActionName>|SELECT, SUBMIT (implicit)|
|- - Field.<QATargetEntityApiName>.<FieldApiName>|SET|
|- - Field.<QATargetEntityApiName>.<MultilineTextFieldApiName>.cursor|INSERT|
|- - Field.<QATargetEntityApiName>.<SinglelineTextFieldApiName>.end|INSERT|
|- QuickAction.Case.Email|SELECT, SUBMIT (implicit)|
|- - Field.EmailMessage.<FieldApiName>|SET|
|- - Field.EmailMessage.<MultilineTextFieldApiName>.cursor|INSERT|
|- - Field.EmailMessage.<SinglelineTextFieldApiName>.end|INSERT|
|- - Field.EmailTemplate|SET|
|- SidebarCmp.Knowledge|SELECT|


-----

|Target API Name|Supported Operations|
|---|---|
|- - SearchAction.KnowledgeArticle|SELECT|
|- - - Field.SearchString|SET, INSERT|
|- - - Command.Search|SUBMIT|
|- - SearchResult.KnowledgeArticle.MostRecentItem|SELECT|
|- - - Command.AttachToRecord|SUBMIT|
|- - - Command.InsertToEmail|SUBMIT|
|- - - Command.AttachToEmailAsPDF|SUBMIT|


Example: This example describes a macro that opens a quick action, sets some fields in the quick action, and submits the quick
action.
```
   0. SELECT Tab.Case
   1. SELECT QuickAction.Case.Email
   2. SET Field.EmailMessage.Subject
   3. SET Field.EmailMessage.ToAddress
   4. INSERT Field.EmailMessage.HtmlBody.cursor
   5. SUBMIT

##### Associated Objects

```
This object has the following associated objects. If the API version isn’t specified, they’re available in the same API versions as this object.
Otherwise, they’re available in the specified API version and later.

**MacroChangeEvent (API version 48.0)**
Change events are available for the object.

**MacroHistory**

History is available for tracked fields of the object.

**MacroOwnerSharingRule**

Sharing rules are available for the object.

**MacroShare**

Sharing is available for the object.
