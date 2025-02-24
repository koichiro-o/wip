#### ContentWorkspaceDoc

Represents a link between a document and a public library in Salesforce CRM Content. This object is available in versions 17.0 and later.

Note: This object does not apply to documents and versions in a personal library.

##### Supported Calls
```
create(), delete(), describeSObjects()query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** Customer and Partner Portal users must have the “View Content in Portal” permission in order to query and obtain content in libraries
where they have access.

**•** Customer and Partner Portal users can only edit documents if they have a Salesforce CRM Content feature license.


-----

**•** To create a ContentWorkspaceDoc, you must be a member of the library with one of these library privileges enabled:

**–** “Add Content”

**–** “Add Content On Behalf of Others”

**–** “Manage Library”

**•** To query all library documents in a library, a user must be a member of that library, regardless of library permissions.

##### Fields

```
ContentDocumentId
ContentWorkspaceId
IsOwner

```

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library document.

This is a relationship field.

**Relationship Name**
ContentDocument

**Relationship Type**
Lookup

**Refers To**
ContentDocument

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
Read only. ID of the library.

This is a relationship field.

**Relationship Name**
ContentWorkspace

**Relationship Type**
Lookup

**Refers To**
ContentWorkspace

**Type**
boolean

**Properties**
Defaulted on create, Filter, Group, Sort


-----

**Description**
Read only. Indicates whether the library owns the document and determines
permissions for that document (true) or not (false). Documents can belong to
more than one library, but only one library owns the document and determines its
permissions.

##### Usage

**•** Use this object to link a document to one or more libraries.

**•** To share a document with additional libraries, create additional ContentWorkspaceDoc records which join the document to the
additional libraries.

**•** Inserting a ContentWorkspaceDoc triggers the publish process for public libraries.

**•** A document can be published into many public libraries, but it will always be owned by one library which controls the security of
the document.

**•** A document can only be published into the document owner's personal library. You can't publish into another user's personal library.
Personal libraries are not visible via the API.

**•** To publish a document into a personal library, you must specify your user ID as the first publish location ID. If you leave the first
publish location ID blank, it defaults to the current user's ID.

**•** A document can be published from a personal library into a public library, but once it has been published into the public library, it
can't be published into the personal library again.

**•** You can't publish a document from a personal library into a public library that has restricted content types.

**•** You can't update or delete a library document via the API.

SEE ALSO:

ContentWorkspace
