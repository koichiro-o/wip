#### ForecastingShare

Represents forecasts shared between a forecast manager and a user. Available in API version 44.0 and later.

##### Supported Calls
```
create(), delete(), describeSObjects(), query(), retrieve(), update(), upsert()

 Special Access Rules

```
As of Spring ’20 and later, only standard users with the View All Forecasts or Allow Forecasting permission or delegated forecast manager
status can access this object.

##### Fields

```
AccessLevel
SharedForecastManagerRoleId

```

**Type**
picklist

**Properties**
Create, Filter, Group, Restricted picklist, Sort

**Description**

Whether the user you’re sharing your forecasts with can view and adjust the
forecasts or view only. This field is new since the pilot.

Picklist values:

**•** `ViewAndEdit`

**•** `ViewOnly`

**Type**
reference

**Properties**
Create, Filter, Group, Sort


-----

```
RoleType
UserOrGroupId

##### Usage

```

**Description**

The ID of either:

**•** The role of the manager whose forecasts you want to share.

**•** The territory whose forecasts you want to share.

**Type**
picklist

**Properties**
Filter, Group, Restricted picklist, Sort

**Description**

The type of hierarchy associated with the forecast share.

**•** `R`  - Role-based

**•** `T`  - Territory-based

**•** `Y`  - Territory2-based

**Type**
reference

**Properties**
Create, Filter, Group, Sort

**Description**

The ID of the user with whom the forecast is shared.


Use this object to let any stakeholder at your company view and adjust forecast managers’ forecasts.
