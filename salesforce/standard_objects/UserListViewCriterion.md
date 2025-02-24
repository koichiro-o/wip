#### UserListViewCriterion

Represents the criterion for a user’s customized list view. The criterion consists of the filters or sort order a user added to a list view for
the Salesforce Mobile app. This object is available in API version 32.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Fields

```
```
ColumnName
Operation
SortOrder
UserListViewId

```

**Type**
string

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The name of the column in the user list view.

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update

**Description**
The criteria to apply, such as “equals” or “starts with.”

**Type**
int

**Properties**
Create, Filter, Group, Sort, Update

**Description**
The order in which the list view is evaluated compared to other UserListViewCriterion objects
for the given UserListView.

**Type**
reference


-----

```
Value

```

**Properties**
Create, Filter, Group, Sort

**Description**
The ID of the user list view.

This is a relationship field.

**Relationship Name**
UserListView

**Relationship Type**
Lookup

**Refers To**
UserListView

**Type**
string

**Properties**
Create, Filter, Group, Nillable, Sort, Update

**Description**
The field values used to filter the list view. For example, a value of `94105` if the Field is
`Billing Zip/Postal Code` shows only rows that have a billing ZIP code of 94105.

