#### UserTerritory2Association

Represents an association (by assignment) between a territory and a user record. Available only if Sales Territories has been enabled.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve()

 Special Access Rules

```
Standard and partner users can access this object. If a territory model is in `Active` state, any standard or partner user can view that
model, including its territories and assignment rules. For territories in an active model, any standard or partner user can view assigned
records and assigned users based on your Salesforce sharing settings. Users cannot view territory models in other states (such as
`Planning` or `Archived).`


-----

##### Fields

**Field Name**
```
IsActive
RoleInTerritory2
Territory2Id
UserId
