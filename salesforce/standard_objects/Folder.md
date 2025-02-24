#### Folder

Represents a repository for a Dashboard, Document, EmailTemplate, Macro, QuickText, or Report. Only one type of item can be contained
in a folder.

##### Supported Calls
```
create(), delete(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), search(),
update(), upsert()

 Special Access Rules

```
**•** You must have the “Modify All Data” permission to create, update, or delete document folders and email template folders.

**•** Guest and Customer Portal users can’t access this object.

**•** To query this object, no special permissions are needed.

**•** As of API version 35.0, when a folder is shared with a role, it is only visible to users in that role. Superior roles in the role hierarchy
don’t gain visibility.

**•** If analytics folder sharing is turned on, then users need these permissions to create and manage report folders and dashboard folders:

**–** “Create Dashboard Folders”

**–** “Create Report Folders”

**•** To use folders for macros and quick text, enable folders for these objects in Setup on the Macro Settings and Quick Text Settings
pages.

##### Fields

```
AccessType

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
DeveloperName
IsReadonly
Name

```

**Description**
Required. Indicates who can access the Folder. Available values include:

**•** `Hidden—Folder is hidden from everyone.`

**•** `Public—Folder is accessible by all users.`

**•** `Shared—Folder is accessible only by a User in a particular Group or UserRole. The API`
doesn’t allow you to view, insert, or update which group or Role the Folder is shared
with.

Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The unique name of the object in the API. This name can contain only underscores and
alphanumeric characters, and must be unique in your org. It must begin with a letter, not
include spaces, not end with an underscore, and not contain two consecutive underscores.
In managed packages, this field prevents naming conflicts on package installations. With
this field, a developer can change the object’s name in a managed package and the changes
are reflected in a subscriber’s organization. Label is Folder Unique Name.

Note: When creating large sets of data, always specify a unique DeveloperName
for each record. If no DeveloperName is specified, performance slows down while
Salesforce generates one for each record.

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Group, Sort, Update

**Description**
Indicates whether this Folder is read-only (true) or editable (false). Label is `Read`
```
  Only.

```
Note: If analytics folder sharing is turned on for your organization, then this field is
present but not used.

**Type**
string

**Properties**
Create, Filter, Group, idLookup, Sort, Update

**Description**
Label of the folder as it appears in the user interface. Label is Document Folder Label.


-----

```
NamespacePrefix
ParentId
Type

```

**Type**
string

**Properties**
Filter, Group, Nillable, Sort

**Description**
The namespace prefix that is associated with this object. Each Developer Edition org that
creates a managed package has a unique namespace prefix. Limit: 15 characters. You can
refer to a component in a managed package by using the
```
  namespacePrefix__componentName notation.

```
The namespace prefix can have one of the following values.

**•** In Developer Edition orgs, `NamespacePrefix` is set to the namespace prefix of the
org for all objects that support it, unless an object is in an installed managed package.
In that case, the object has the namespace prefix of the installed managed package. This
field’s value is the namespace prefix of the Developer Edition org of the package
developer.

**•** In orgs that are not Developer Edition orgs, NamespacePrefix is set only for objects
that are part of an installed managed package. All other objects have no namespace
prefix.

**Type**
reference

**Properties**
Create, Filter, Group, Nillable, Sort

**Description**
ID of the parent object, if any.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**
Required. Type of objects contained in the Folder. This field can’t be updated. Available values
include:

**•** `Dashboard`

**•** `Document`

**•** `Email` (for Salesforce Classic email templates)

**•** `EmailTemplate` (for Lightning email templates)

**•** `Macro`

**•** `QuickText`

**•** `Report`


-----

##### Usage

Only one type of item can be contained in a folder, either Dashboard, Document, EmailTemplate, Macro, QuickText, or Report.

SEE ALSO:

Overview of Salesforce Objects and Fields
