#### WorkAccessShare

Used to control Givers of WorkBadgeDefinition records.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Additional Considerations and Related Objects

```
[Related to WorkAccess Object. WorkAccess is the parent of WorkAccessShare.](https://docs.google.com/a/salesforce.com/document/d/11IkXSCNKBD_04YlyOPvWS94iyVeQ7zN98M03LdcW4eM/edit#bookmark=id.7idtv3rbjtcr)

##### Fields

The properties available for some fields depend on the default organization-wide sharing settings. The properties listed are true for the
default settings of such fields.

```
AccessLevel
ParentId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
CRUD Access Level (picklist values: Read Only, Read/Write, Owner).

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**
ID for WorkAccess record.

This is a relationship field.


-----

```
RowCause
UserOrGroupId
