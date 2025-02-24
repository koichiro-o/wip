#### OrderShare

```

**Properties**
Create, Defaulted on create, Filter, Nillable, Sort, Update

**Description**
Summary of all the ReservedBalanceAmount for all the order payment summary references.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
Type of reference between the OrderSummary and the OrderPaymentSummary.

Possible values are:

**•** `Shared`


Represents a sharing entry on an Order. This object is available in API version 48.0 and later.

You can only create, edit, and delete sharing entries for standard objects whose `RowCause` field is set to `Manual. Sharing entries`
for standard objects with different `RowCause` values are created as a result of your Salesforce org’s sharing configuration and are
read-only. For some sharing mechanisms, such as sharing sets, sharing entries aren’t stored at all.

Note: While Salesforce currently maintains read-only sharing entries for multiple sharing mechanisms, it’s possible that we’ll stop
storing certain share records to improve performance. As a best practice, don’t create customizations that rely on the availability
of these sharing entries. Any changes to sharing behavior will be communicated before they occur.

##### Supported Calls
```
describeSObjects(), query(), retrieve()

 Fields

```
```
OrderAccessLevel

```

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**
Level of access that the user or group has to the order.

Possible values are:


-----

```
OrderId
RowCause
UserOrGroupId

```


**•** `All—Owner. This value isn’t valid when creating, updating, or deleting records.`

**•** `Edit—Read/Write`

**•** `Read—Read Only`

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the order associated with this sharing entry. This field can't be updated.

This is a relationship field.

**Relationship Name**
Order

**Relationship Type**
Lookup

**Refers To**
Order

**Type**
picklist

**Properties**
Filter, Group, Nillable, Restricted picklist, Sort

**Description**
Reason that this sharing entry exists. If you’re creating a sharing entry, the only permitted
value is Manual. If no value is specified, the field defaults to Manual. All other RowCause
values are read-only. After the sharing entry is created, this field can’t be edited.

**Type**
reference

**Properties**
Filter, Group, Sort

**Description**
ID of the user or group that has been given access to the order. This field can't be updated.

This is a polymorphic relationship field.

**Relationship Name**
UserOrGroup

**Relationship Type**
Lookup

**Refers To**
Group, User


-----

##### Usage

This object allows you to determine which users and groups can view or edit orders owned by other users.

If you attempt to create a record that matches an existing record, any modified fields are updated, the system returns the existing record.
