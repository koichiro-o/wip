#### RuleTerritory2Association

Represents a record-assignment rule and its association to an object, such as Account. Available if Sales Territories has been enabled.

##### Supported Calls
```
describeSObjects(), getDeleted(), getUpdated(), query(), retrieve()

 Special Access Rules

```
Standard users can access this object. If a territory model is in `Active` state, any standard user can view that model, including its
territories and assignment rules. For territories in an active model, any standard user can view assigned records and assigned users subject
to your Salesforce sharing settings. Users cannot view territory models in other states (such as `Planning` or `Archived).`

##### Fields

```
IsInherited

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort, Update


-----

```
RuleId
Territory2Id
