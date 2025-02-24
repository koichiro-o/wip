#### Division

A logical segment of your organization's data. For example, if your company is organized into different business units, you could create
a division for each business unit, such as “North America,” “Healthcare,” or “Consulting.” Available only if the organization has the Division
permission enabled.

##### Supported Calls
```
create(), describeSObjects(), getDeleted(), getUpdated(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
**•** Divisions must be enabled for your organization to access this object. To discover whether divisions have been enabled for an
organization, inspect the User or Group object for the DefaultDivision field—if it is present, then divisions have been enabled,
and this field (the field is named Division in objects other than User and Group) will be available in all relevant objects.

**•** Customer Portal users can’t access this object.


-----

##### Fields

**Field**
```
IsActive
IsGlobalDivision
Name
SortOrder

##### Usage

```

**Type**
boolean

**Properties**
Create, Defaulted on create, Filter, Update

**Description**
Indicates whether the division is active (true) or not (false). Label is Active.

**Type**
boolean

**Properties**
Defaulted on createFilter

**Description**
Indicates whether the division is your organization’s global default division (true)
or not (false). Label is Global Division.

**Type**
string

**Properties**
Create, Filter, Update

**Description**
A descriptive name for the division. Limit: 80 characters.

**Type**
int

**Properties**
Create, Filter, Nillable, Update

**Description**
The order in which this division name appears in the Division picklist field when
creating or editing users in the Salesforce user interface.


The values available for that field are the global division ID for the organization, created when divisions are first enabled, and any other
division IDs that have been created. The division ID associated with a user is populated in the objects owned or created by the user.

You can use the division ID to make searches, reports, and list views run more quickly and return more relevant results if an organization
has very large data sets. For more information, see the Salesforce online help, in the Fields description for the object.

You can use WITH in SOSL to pre-filter results based on division. This is faster than specifying the division in a WHERE clause.


-----

Note: The User object has a Division field that is unrelated to this object. The Division field is a standard text field similar
to Company or Department that has no special properties. Do not confuse it with the `DefaultDivision` field, which does
relate to this object.

SEE ALSO:

Overview of Salesforce Objects and Fields
